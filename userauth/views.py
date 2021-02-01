from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User,auth
from userauth.models import WebUser
# Create your views here.
#messages Create ar jonno
from django.contrib import messages
class RegisterView(View):
      def get(self,request):
            return render(request,'myauth/register.html')

      def post(self,request):
            context={
                  'has_error':False
            }
            username = request.POST.get('username')
            email = request.POST.get('useremail')
            phone = request.POST.get('userphone')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')


            if len(password1) < 8:
                  messages.add_message(request,messages.ERROR,'password minimum 8 charaters long')
                  context['has_error']=True

            if password1 != password2:
                  messages.add_message(request,messages.ERROR,'password not matching')
                  context['has_error']=True
      
            
            if User.objects.filter(email=email).exists():
                  messages.add_message(request,messages.ERROR,'Email address all ready taken')
                  context['has_error']=True
            try:
                  if WebUser.objects.get(phone_number=phone):
                        messages.add_message(request,messages.ERROR,'Phone number all ready taken')
                        context['has_error']=True
            except Exception as identifier:
                  pass
            if context['has_error']:
                  return render(request,'myauth/register.html')

            else:
                  user = User.objects.create_user(username=username,email=email,password=password1)
                  user.is_active = True
                  user.save()
                  webuser = WebUser(user=user,phone_number=phone)
                  webuser.save()
                  messages.add_message(request,messages.SUCCESS,'Account create successfully')
                  return redirect('login')

class LogInView(View):
      def get(self,request):
            return render(request,'myauth/login.html')

      def post(self,request):
            context={
                  'has_error':False
            }
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username =='':
                  messages.add_message(request,messages.ERROR,'Please,select your user name')
                  context['has_error'] =True

            if password =='':
                  messages.add_message(request,messages.ERROR,'Please,select your password')
                  context['has_error'] =True
            

            excual_user = auth.authenticate(username=username,password=password)
            
            if excual_user is None and context['has_error'] is None:
                  messages.add_message(request,messages.ERROR,'Invalid account')
                  context['has_error'] =True
            if context['has_error']:
                  return render(request,'myauth/login.html',context )

            if excual_user:
                  auth.login(request,excual_user)
                  if excual_user.is_superuser:
                        return redirect('/admin')
                  if excual_user.is_active:
                        return redirect('home')

            else:
                  return HttpResponse('not match')

#class LogOutView(View):
#      def post(self,request):
#            auth.logout(request)
#           messages.add_message(request,messages.SUCCESS,'Log out success')
#           return redirect('home')
def logout(request):
      auth.logout(request)
      messages.add_message(request,messages.SUCCESS,'Log out success')
      return redirect('home')