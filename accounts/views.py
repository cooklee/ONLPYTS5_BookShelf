from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from accounts.forms import LoginForm


# class LoginView(View):
#
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'form.html', {'form': form})
#
#     def post(self, request):
#         form = LoginForm(request.POST)
#         next_url = request.GET.get('next', '/')
#         if form.is_valid():
#             user = authenticate(request, **form.cleaned_data)
#             if user is not None:
#                 login(request, user)
#                 return redirect(next_url)
#             else:
#                 return HttpResponse("Błędne dane logowania")
#         return render(request, 'form.html', {'form': form})
#
#
# class LogoutView(View):
#
#     def get(self, request):
#         logout(request)
#         return redirect("index_view")