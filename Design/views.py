from django.shortcuts import render, redirect

##
import mysql
import mysql.connector
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q, F
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages    
from django.core.exceptions import ValidationError
import datetime
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required



from . models import UserInfo,FoodItemMst,ShopMst,AreaMst,CityMst, QualficationMst, DietitionsMst

from . forms import UserForm,FoodItemsForm,CityForm,AreaForm,ShopForm,FoodItemShopForm,FoodItemShop, QualificatoinForm, DietitionForm


def IndexView(request):# INSERT METHOD
       return render(request,"index.html")

def UserTrans(request, id=0):
    if request.method=="GET" :
        if (id==0):
            form = UserForm()
        else:
            uid = UserInfo.objects.get(pk=id)
            form = UserForm(instance=uid)
        return render(request,"UserForm.html",{'form': form})
    else :
        if (id==0):
            form= UserForm(request.POST)
        else :
            cid = UserInfo.objects.get(pk=id)
            form = UserForm(request.POST, instance=cid) 
        if form.is_valid():
            form.save()
        return redirect('IndexView')

def UserList(request):
    context = {'UserList': UserInfo.objects.all()}
    return render(request, 'UserList.html', context)

def UserDelete(request, id):
    uid = UserInfo.objects.get(pk=id)
    uid.delete()

    return redirect('UserTrans')

def BmiChart(request):
    return render(request, "BMICHART.HTML")

def ContactUs(request):
    return render(request, "ContactUs.html")

def AboutUs(request):
    return render(request, "AboutUs.html")

def AdminDashboard(request):
    return render(request, "Admin/AdminDashboard.html")
def UserDashboard(request):
    user = request.session.get('user')
    return render(request, "UserDashboard.html",{"user":user})

def DietitionDashboard(request):
    user = request.session.get('Dietition')
    return render(request, "Dietition/DietitionDashboard.html",{"user":user})

def Login(request):
    flag = 0
    if request.method == 'POST' and flag ==0:
        username = request.POST['username']
        password = request.POST['password']
        userType = request.POST['userType']
        if username == 'Admin' and userType == 'admin' and password =='Admin':
            request.session['admin'] = username
            flag = 1
            return redirect('AdminDashboard')
        elif flag == 0 and userType == 'user' and (UserInfo.objects.filter(Q(UserName = username)& Q(PassWord=password)).exists()):
            request.session['user'] =username
            flag =1
            return redirect('UserDashboard')
        
        elif flag == 0 and userType == 'Dietition' and (DietitionsMst.objects.filter(Q(UserName = username)& Q(PassWord=password)).exists()):
            request.session['Dietition'] =username
            flag =1
            return redirect('DietitionDashboard')
                
        else:
            content = {"message":"Invalid Credentials"}
            return render(request,'Login.html',content)


    else:
        return render(request,'Login.html')

def ChangePassword(request):
    if request.method == "POST":
        username = request.POST['username']
        oldpassword = request.POST['oldpassword']
        newPassword= request.POST['newPassword']
        confirmPassword= request.POST['confirmPassword']

        if newPassword == confirmPassword:
            if UserInfo.objects.filter(Q(UserName=username) & Q(PassWord = oldpassword)).exists():
                member = UserInfo.objects.get(UserName = username)
                member.PassWord = newPassword
                member.save()
                content ={"message":"Password Changed Successfully"}
                return render(request, "ChangePassword.html",content)

            else:
                content ={"message":"Username or Password is incorrect"}
                return render(request, "ChangePassword.html",content) 

        else:
            content ={"message":"New Password and Confirm password are not same "}
            return render(request, "ChangePassword.html",content)   

        
    return render(request, "ChangePassword.html")  


def ChangePasswordD(request):
    if request.method == "POST":
        username = request.POST['username']
        oldpassword = request.POST['oldpassword']
        newPassword= request.POST['newPassword']
        confirmPassword= request.POST['confirmPassword']

        if newPassword == confirmPassword:
            if DietitionsMst.objects.filter(Q(UserName=username) & Q(PassWord = oldpassword)).exists():
                member = DietitionsMst.objects.get(UserName = username)
                member.PassWord = newPassword
                member.save()
                content ={"message":"Password Changed Successfully"}
                return render(request, "Dietition/ChangePassword.html",content)

            else:
                content ={"message":"Username or Password is incorrect"}
                return render(request, "Dietition/ChangePassword.html",content) 

        else:
            content ={"message":"New Password and Confirm password are not same "}
            return render(request, "Dietition/ChangePassword.html",content)   
        
    return render(request, "Dietition/ChangePassword.html")  

def Logout(request):
    if  'admin' in request.session:
        del request.session['admin']
        return redirect("Login")
    
    if  'user' in request.session:
        del request.session['user']
        return redirect("Login")
    
    if  'Dietition' in request.session:
        del request.session['Dietition']
        return redirect("Login")

    
def Bmr(request):
    user = request.session.get('user')
    if request.method == "POST":
        height = request.POST['height']
        weight = request.POST['weight']
        gender = request.POST['gender']
        age = request.POST['age']
        activity = request.POST['activity']
        height = int(height)
        weight = int(weight)
        age = int(age)
        if gender == 'M':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
            if activity == 'sedentary':
                bmr = bmr * 1.2
            elif activity == 'lightly':
                bmr = bmr * 1.375
            elif activity == 'moderately':
                bmr = bmr * 1.55
            elif activity == 'very':
                bmr = bmr * 1.725
            elif activity == 'extra':
                bmr = bmr * 1.9
            fooddata = FoodItemMst.objects.all()
            return render(request, "Diet.html", {'bmr': bmr,"fooddata":fooddata})

            # return redirect('Diet')
        else:
            if activity == 'sedentary':
                bmr = bmr * 1.2
            elif activity == 'lightly':
                bmr = bmr * 1.375
            elif activity == 'moderately':
                bmr = bmr * 1.55
            elif activity == 'very':
                bmr = bmr * 1.725
            elif activity == 'extra':
                bmr = bmr * 1.9
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
            fooddata = FoodItemMst.objects.all()
            print(fooddata)
            return render(request, "Diet.html", {'bmr': bmr,"food":fooddata})
            
            
    else:
        return render(request, "Bmr.html",{"user":user})

def Diet(request):
    fooddata = FoodItemMst.objects.all()
    print(fooddata)
    return render(request, "Diet.html")

def ItemFrom(request):
    form = FoodItemsForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    return render(request,'Admin/ItemsForm.html',{'form':form})

def CityTrans(request):
    form = CityForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'Admin/CityMst.html',{'form':form})

def CityList(request):
    context = {'CityList': CityMst.objects.all()}
    return render(request, 'Admin/CityList.html', context)


def AreaTrans(request): 
    form = AreaForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'Admin/AreaMst.html',{'form':form})

def AreaList(request):
    context = {'AreaList': AreaMst.objects.all()}
    return render(request, 'Admin/AreaList.html', context)


def ShopTrans(request):
    form = ShopForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'Admin/ShopMst.html',{'form':form})

def FoodItemShopTrans(request):
    form = FoodItemShopForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'Admin/FoodItemShop.html',{'form':form})



def ViewShop(request):
    user = request.session.get('user')
    areas = AreaMst.objects.all()
   
    return render(request, "ViewShop.html",{'areas':areas,"user":user})

def FindShop(request):
    user = request.session.get('user') 

    area = request.POST['area']
    areas = AreaMst.objects.all()

    shopdata = ShopMst.objects.filter(AreaName_id = area)
    print(shopdata)
    return render(request, "ViewShop.html",{'shopdata':shopdata,'areas':areas,"user":user})

def ShowShop(request):
    shop = request.POST['shop']
    user = request.session.get('user')
    areas = AreaMst.objects.all()
    shopdata = FoodItemShop.objects.filter(ShopName_id = shop)
    
    return render(request, "ViewShop.html",{'shopdata':shopdata,'shop':shop,'areas':areas,"user":user})   


def QualificationTrans(request):
    form = QualificatoinForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'Admin/QualificationForm.html',{'form':form})

def DietitionTrans(request, id=0):
    if request.method=="GET" :
        if (id==0):
            form = DietitionForm()
        else:
            uid = DietitionsMst.objects.get(pk=id)
            form = DietitionForm(instance=uid)
        return render(request,"DietitionForm.html",{'form': form})
    else :
        if (id==0):
            form= DietitionForm(request.POST)
        else :
            cid = DietitionsMst.objects.get(pk=id)
            form = DietitionForm(request.POST, instance=cid) 
        if form.is_valid():
            form.save()
        return redirect('IndexView')

def DList(request):
    context = {'DList': DietitionsMst.objects.all()}
    return render(request, 'DList.html', context)

 
 