from django.shortcuts import render,redirect
from .models import Contact
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test,login_required
from LRS_App.forms import UserForm
from django.contrib import messages
from .models import UploadedFile,UserProfile
from .forms import FileUploadForm

# Create your views here.


def home(request):
     latest_uploads = UploadedFile.objects.order_by('-uploaded_datetime')[:5]
     context = {'latest_uploads' : latest_uploads}
     return render(request, 'home.html' , context)

def about(request):
     return render(request, 'about.html')

@login_required(login_url='/')
def logoutUser(request):
    logout(request)
    return redirect('home')

def contact(request):
     if request.method == 'POST':
          Name = request.POST.get('name')
          Mail = request.POST.get('mail')
          Address = request.POST.get('address')
          Message = request.POST.get('message')
          contacts = Contact(Name = Name, Mail= Mail, Address=Address, Message= Message)
          contacts.save()
          return redirect('home')
     return render(request, 'contact.html')

def plans(request):
     return render(request, 'plans.html')

@login_required(login_url='/')
def myplan(request):
    profile = UserProfile.objects.get(user = request.user)
    user_plan = profile.plan
    print(user_plan)
    return render(request, 'myplan.html',{'user_plan': user_plan})

def loginUser(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           
            login(request, user)
            return redirect('home')
       
        else :     
            return render(request, 'loginUser.html')
        
     return render(request, 'loginUser.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        form = UserForm(request.POST)
        if form.is_valid() :
            form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            profile = UserProfile(user = request.user)
            profile.save()
            return redirect('home')
        else:
            form = UserForm()

    context={'form': UserForm}
    return render(request, 'register.html',context )

@login_required(login_url='/')
def upload_files(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user  # Set the uploader to the current admin user
            new_file.save()
            return redirect('home')  # Redirect to the homepage after successful upload
    else:
        form = FileUploadForm()
    
    return render(request, 'upload_files.html', {'form': form})

@csrf_exempt
def standard(request):
    amount = 100
    order_currency = 'INR'
    client = razorpay.Client(auth=('rzp_test_KCDkoo7vMVdCce','FuShgmjDhFqq26Msjx4nCyd4'))
    payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture': '1'})
    return render(request, 'standard.html')

@csrf_exempt
def business(request):
     amount = 100
     order_currency = 'INR'
     client = razorpay.Client(auth=('rzp_test_KCDkoo7vMVdCce','FuShgmjDhFqq26Msjx4nCyd4'))
     payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture': '1'})
     return render(request, 'business.html')

@csrf_exempt
def premium(request):
     amount = 100
     order_currency = 'INR'
     client = razorpay.Client(auth=('rzp_test_KCDkoo7vMVdCce','FuShgmjDhFqq26Msjx4nCyd4'))
     payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture': '1'})
     return render(request, 'premium.html')

@csrf_exempt
def vip(request):
     amount = 100
     order_currency = 'INR'
     client = razorpay.Client(auth=('rzp_test_KCDkoo7vMVdCce','FuShgmjDhFqq26Msjx4nCyd4'))
     payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture': '1'})
     return render(request, 'vip.html')

