import jwt
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from app.models import Application


class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        application_secret = request.GET.get('application_secret', '')
        if application_secret == "":
            return HttpResponse("application_secret not provided")

        form = AuthenticationForm()

        application = Application.objects.filter(application_secret=application_secret)
        if len(application) == 0:
            return HttpResponse("Application with that application_secret not found")

        application = application[0]

        return render(request, self.template_name, dict(form=form, application=application))

    def post(self, request):
        application_secret = request.GET.get('application_secret', '')

        application = Application.objects.filter(application_secret=application_secret)

        if len(application) == 0:
            return HttpResponse("Application with that application_secret not found")

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            encoded = jwt.encode({
                "username": user.username,
                "email": user.email
            }, 'secret', algorithm='HS256')

            return redirect(application[0].return_url + "?token=" + encoded.decode("utf-8"))

        return render(request, self.template_name, dict(form=form, application=application[0]))
