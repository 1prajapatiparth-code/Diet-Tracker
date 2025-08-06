
from django import forms
from . models import UserInfo,FoodItemMst,CityMst,AreaMst,ShopMst,FoodItemShop, DietitionsMst, QualficationMst
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
class UserForm(forms.ModelForm):
    PassWord = forms.CharField(widget=forms.PasswordInput)
    # gender = forms.ChoiceField(
    #     choices=GENDER_CHOICES,
    #     widget=forms.RadioSelect(),
    #     required=True
    # )
    BirthDate = forms.DateField(widget=DateInput)
    class Meta:
        model=UserInfo
        fields =('Name','EmailId','ContactNo','BirthDate','Age','BloodGroup','UserName','PassWord','Gender')
        labels ={'Name':'Name','EmailId':'EmailId','ContactNo':'ContactNo','BirthDate':'Birth Date','Age':'Age','BloodGroup':'BloodGroup','UserName':'UserName','PassWord':'PassWord'}

class FoodItemsForm(forms.ModelForm):
    class Meta:
        model = FoodItemMst
        fields = "__all__"

class CityForm(forms.ModelForm):
    class Meta:
        model = CityMst
        fields = "__all__"
class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaMst
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super(AreaForm,self).__init__(*args,**kwargs)
        self.fields["CityName"].empty_label = "--Select City--"

class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopMst
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super(ShopForm,self).__init__(*args,**kwargs)
        self.fields["AreaName"].empty_label = "--Select Area--"

class FoodItemShopForm(forms.ModelForm):
    class Meta:
        model = FoodItemShop
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super(FoodItemShopForm,self).__init__(*args,**kwargs)
        self.fields["ShopName"].empty_label = "--Select The Shop--"
        self.fields["FoodItemName"].empty_label = "--Select The Food Item--"
                 
class QualificatoinForm(forms.ModelForm):
    class Meta:
        model = QualficationMst
        fields = "__all__"


class DietitionForm(forms.ModelForm):
    PassWord = forms.CharField(widget=forms.PasswordInput)
    # gender = forms.ChoiceField(
    #     choices=GENDER_CHOICES,
    #     widget=forms.RadioSelect(),
    #     required=True
    # )
    
    class Meta:
        model=DietitionsMst
        fields =('Name','EmailId','ContactNo','AreaName','Qualification', 'UserName','PassWord','Gender')
        labels ={'Name':'Name','EmailId':'EmailId','ContactNo':'ContactNo','AreaName':'AreaName','Qualification':'Qualification', 'UserName':'UserName','PassWord':'PassWord'}
