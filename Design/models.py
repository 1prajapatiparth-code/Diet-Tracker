from django.db import models

class UserInfo(models.Model):
    Name = models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    EmailId = models.EmailField(max_length=30)
    ContactNo = models.CharField(max_length=20)
    BirthDate = models.DateField()
    Age= models.DecimalField(max_digits=6,decimal_places=2)
    BloodGroup=models.CharField(max_length=10)
    UserName= models.CharField(max_length=30)
    PassWord=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.BirthDate.strftime('%d/%m/%Y')
    
class FoodItemMst(models.Model):
    Img = models.ImageField()
    Name = models.CharField(max_length=20)
    Calories = models.DecimalField(max_digits=6,decimal_places=2)
    Protein = models.DecimalField(max_digits=6,decimal_places=2)
    Carbs = models.DecimalField(max_digits=6,decimal_places=2)
    Fat = models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self) -> str:
        return self.Name

class CityMst(models.Model):
    CityName = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.CityName
    
class AreaMst(models.Model):
    CityName = models.ForeignKey(CityMst, on_delete=models.CASCADE)
    AreaName = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.AreaName
    
class ShopMst(models.Model):
    AreaName = models.ForeignKey(AreaMst, on_delete=models.CASCADE)
    ShopName = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.ShopName


class FoodItemShop(models.Model):
    ShopName = models.ForeignKey(ShopMst, on_delete=models.CASCADE)
    FoodItemName = models.ForeignKey(FoodItemMst, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=6,decimal_places=2)
    

class QualficationMst(models.Model):
    Qualification = models.CharField(max_length=40)

    def __str__(self):
        return self.Qualification

class DietitionsMst(models.Model):
    Name = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    EmailId = models.EmailField(max_length=30)
    ContactNo = models.CharField(max_length=20)
    Qualification = models.ForeignKey(QualficationMst, on_delete=models.CASCADE)
    AreaName = models.ForeignKey(AreaMst, on_delete=models.CASCADE)

    UserName= models.CharField(max_length=30)
    PassWord=models.CharField(max_length=10)
