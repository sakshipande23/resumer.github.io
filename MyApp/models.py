from django.db import models

# Create your models here.

# class Stuprnno(models.Model):
#     stu_fname = models.CharField(max_length=100)
#     stu_lname = models.CharField(max_length=100)
#     prnno = models.CharField(max_length=100)
#     stu_email = models.EmailField(max_length=200,default="YourDefaultHere")

#     def __str__(self):
#         return self.stu_fname
    
# class Tpocred(models.Model):
#     tponame = models.CharField(max_length=100)
#     tpopassword = models.CharField(max_length=100)

#     def __str__(self):
#         return self.tponame 
    
class Resume(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    dob = models.CharField(max_length=100)
    degree = models.TextField(max_length=500)
    degins = models.TextField(max_length=500, default="YourDefaultHere")
    degyear = models.TextField(max_length=500, default="YourDefaultHere")
    degper = models.TextField(max_length=500, default="YourDefaultHere")
    hscdeg = models.TextField(max_length=500, default="YourDefaultHere")
    hscins = models.TextField(max_length=500, default="YourDefaultHere")
    hscyear = models.TextField(max_length=500, default="YourDefaultHere")
    hscper = models.TextField(max_length=500, default="YourDefaultHere")
    inter = models.TextField(max_length=500)
    highschool = models.TextField(max_length=500)
    sscyear = models.TextField(max_length=500, default="YourDefaultHere")
    sscper = models.TextField(max_length=500, default="YourDefaultHere")
    about_you = models.TextField(max_length=1000)
    proskills = models.TextField(max_length=1000, default="YourDefaultHere")
    famskills = models.TextField(max_length=1000, default="YourDefaultHere")
    protech = models.TextField(max_length=1000, default="YourDefaultHere")
    famtech = models.TextField(max_length=1000, default="YourDefaultHere")
    experience = models.TextField(max_length=1000)
    brief_description = models.TextField(max_length=1000, default="YourDefaultHere")
    project_title = models.CharField(max_length=100, default="YourDefaultHere")
    project_tech = models.CharField(max_length=100, default="YourDefaultHere")
    project_description = models.TextField(max_length=1000, default="YourDefaultHere")
    achivements = models.TextField(max_length=500, default="YourDefaultHere")
    
    # cv_img = models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.name

