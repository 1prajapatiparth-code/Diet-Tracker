from django.contrib import admin
from django.urls import path,include

from.import views
urlpatterns =[
    path('', views.IndexView, name="IndexView"),
    path('UserTrans', views.UserTrans, name="UserTrans"),
    path('UserTrans/<int:id>', views.UserTrans, name="UserTrans"),
    path('UserDelete/<int:id>', views.UserDelete, name="UserDelete"),
    path('UserList', views.UserList, name="UserList"),
    path('BmiChart', views.BmiChart, name="BmiChart"),
    path('ContactUs', views.ContactUs, name="ContactUs"),
    path('AboutUs', views.AboutUs, name="AboutUs"),
    path('AdminDashboard', views.AdminDashboard, name="AdminDashboard"),
    path('UserDashboard', views.UserDashboard, name="UserDashboard"),
    path('Bmr', views.Bmr, name="Bmr"),
    
    path('Login', views.Login, name="Login"),
    path('Logout', views.Logout, name="Logout"),
    path('ChangePassword', views.ChangePassword,name="ChangePassword"),
    path('ChangePasswordD', views.ChangePasswordD,name="ChangePasswordD"),

    path('Diet', views.Diet, name="Diet"),
    path('ItemFrom', views.ItemFrom, name="ItemFrom"),
    path('CityTrans', views.CityTrans, name="CityTrans"),
    path('AreaTrans', views.AreaTrans, name="AreaTrans"),
    path('ShopTrans', views.ShopTrans, name="ShopTrans"),
    path('FoodItemShopTrans', views.FoodItemShopTrans, name="FoodItemShopTrans"),
    path('ViewShop', views.ViewShop, name="ViewShop"),
    path('FindShop/<int:id>', views.FindShop, name="FindShop"),
    path('FindShop', views.FindShop, name='FindShop'),
    path('ShowShop', views.ShowShop, name='ShowShop'),
    path('CityList', views.CityList, name='CityList'),
    path('UserList/<int:id>',views.UserTrans, name="UserTrans"),
    path('AreaList',views.AreaList, name="AreaList"),
    path('QualificationTrans',views.QualificationTrans, name="QualificationTrans"),
    path('DietitionTrans',views.DietitionTrans, name="DietitionTrans"),
    path('DList',views.DList, name="DList"),
    path('DietitionDashboard',views.DietitionDashboard, name="DietitionDashboard"),

     
    
    
    
    
    
    
    
    
    
    

 
    
]









