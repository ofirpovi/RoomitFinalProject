from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


# # Sign Up View
# class SignUpView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('signup')
#     template_name = 'roomit_app/HTML/signup.html'  # TODO :replace with react
