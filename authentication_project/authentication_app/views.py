from django.shortcuts import render, redirect


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout        #for authenticate not use model




def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if password == confirm_password:
            User.objects.create_user(
                username = username,
                email = email ,
                first_name = f_name ,
                last_name = l_name ,
                password = password ,
    

            )


            return  redirect('login_page')
        else:
            print('password not match')

    return render(request, 'register.html')      



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard_page')
        else:
            print('Invalid Password or Username')

   
   
    return render(request, 'login.html')



def dashboard_page(request):

    return render(request, 'dashboard.html')



def logout_view(request):
    logout(request)
    return redirect('login_page')

