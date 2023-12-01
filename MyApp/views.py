from io import SEEK_CUR
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Resume
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# # Create your views here.
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
# from django.core.urlresolvers import resolve

from django.contrib.auth.decorators import login_required



# def index(request):
#     return render(request,"index.html")

# def loginb(request):
#     return render(request,"loginb.html")

# def logint(request):
#     # return render(request,"logint.html")
#     if request.method == "POST":
#         tponame = request.POST.get("tponame")
#         tpopassword = request.POST.get("tpopassword")
        
#         try:
#             # user = Tpocred.objects.get(tponame= tponame)
#             # user = Tpocred.objects.get(tpopassword=tpopassword)
            
#             user = Tpocred.objects.get(tponame=tponame, tpopassword=tpopassword)
            
#         except Tpocred.DoesNotExist:
#             user = None

#         if user and user.tponame == tponame and user.tpopassword == tpopassword:
#             # Retrieve stu_fname and stu_lname
#             tponame = user.tponame
#             tpopassword = user.tpopassword
            
#             request.session['tponame'] = tponame

#             # Pass them as context variables
#             context = {
#                 'tponame': tponame,
#                 'tpopassword': tpopassword,
#             }
#             return render(request, "dasht.html", context)
#         else:
#             messages.info(request, 'User Admin not found')

#     return render(request, "logint.html")



# def login(request):
#     if request.method == "POST":
#         prnno = request.POST.get("prnno")
#         password = request.POST.get("password")
        
#         try:
#             user = Stuprnno.objects.get(prnno=prnno)
            
#         except Stuprnno.DoesNotExist:
#             user = None


#         default_password = "Nmims%2021"
#         if user and user.prnno == prnno and password == default_password:
#             # Retrieve stu_fname and stu_lname
#             stu_fname = user.stu_fname
#             stu_lname = user.stu_lname
            
#             request.session['stu_fname'] = stu_fname

#             # Pass them as context variables
#             context = {
#                 'stu_fname': stu_fname,
#                 'stu_lname': stu_lname,
#             }
#             return render(request, "dash.html", context)
#         else:
#             messages.info(request, 'PRN number not found')

#     return render(request, "login.html")



# def logout(request):
#     auth.logout(request)
#     return redirect("/")

# def dash(request):
#     return render(request,"dash.html")
    
# def dasht(request):
#     return render(request,"dasht.html")
        
   
# # def tpo_add_student(request):
# #     if request.method == "POST":
# #         prnno = request.POST.get("prnno")
# #         confirm_prnno = request.POST.get("confirm_prnno")
# #         stu_fname = request.POST.get("stu_fname")
# #         stu_lname = request.POST.get("stu_lname")

# #         # Check if PRN numbers match
# #         if prnno == confirm_prnno:
# #             # Create a new student in the database
# #             student = Stuprnno(stu_fname=stu_fname, stu_lname=stu_lname, prnno=prnno)
# #             student.save()

# #             # Set a flag to indicate successful student addition
# #             student_added = True
# #         else:
# #             # Set a flag to indicate PRN mismatch
# #             student_added = False

# #         return render(request, "tpo_add_stu.html", {"student_added": student_added})
# #     else:
# #         return render(request, "tpo_add_stu.html")
    

# def viewstudents(request):
#     # students = Stuprnno.objects.all()
#     # return render(request, "viewstudents.html", {"students": students})    
#     students = Stuprnno.objects.all()
#     resume_info_dict = {}  # Create a dictionary to store resume information
#     for student in students:
#         try:
#             resume = Resume.objects.get(name=f"{student.stu_fname} {student.stu_lname}")
#             resume_info_dict[f"{student.stu_fname} {student.stu_lname}"] = resume
#         except Resume.DoesNotExist:
#             resume_info_dict[f"{student.stu_fname} {student.stu_lname}"] = None

#     return render(request, "viewstudents.html", {"students": students, "resume_info_dict": resume_info_dict})
  
# def view_stu_resume(request, student_name):
#     # return render(request,"view_stu_resume.html")
#     try:
#         resume = Resume.objects.get(name=student_name)
#     except Resume.DoesNotExist:
#         resume = None

#     return render(request, "view_stu_resume.html", {"resume_info": resume})
            
    
# # @login_required(login_url="/login/")

# def template(request):
#     return render(request,"index.html")








def create_resume(request):
    current_url = request.resolver_match.url_name
    current_url+=".html"
    
    if request.method=="POST":
        username=request.user.username 
        if request.POST.get("fname",""):

            obj,Resume_info = Resume.objects.get_or_create(username=username)
            obj.name =request.POST.get("fname","")+" " +request.POST.get("lname","")
            obj.cv_img=request.POST.get("myFile")
            obj.email=request.POST.get("email")
            obj.phone=request.POST.get("phone")
            # address=request.POST.get("address")
            # # +" " +request.POST.get("address2")
            # if request.POST["city"] or request.POST["state"]:
            #     address+=", " +request.POST.get("city")+" " +request.POST.get("state","")
            # obj.address=address    
            obj.dob=request.POST.get("dob","")
            # obj.=request.POST.get("degree","")
            # obj.degree=request.POST.get("degree","")
            obj.degree=request.POST.get("degree","")
            obj.degins =request.POST.get("degins","")
            obj.degyear =request.POST.get("degyear","")
            obj.degper =request.POST.get("degper","")
            obj.hscdeg =request.POST.get("hscdeg","")
            obj.hscins =request.POST.get("hscins","")
            obj.hscyear =request.POST.get("hscyear","")
            obj.hscper =request.POST.get("hscper","")
            obj.sscyear =request.POST.get("sscyear","")
            obj.sscper =request.POST.get("sscper","")
            obj.inter=request.POST.get("inter","")
            obj.highschool=request.POST.get("highschool","")
            obj.about_you=request.POST.get("about_you","")
            obj.experience=request.POST.get("experience","")
            obj.brief_description=request.POST.get("brief_description","")
            obj.project_title=request.POST.get("project_title","")
            obj.project_tech=request.POST.get("project_tech","")
            obj.project_description=request.POST.get("project_description","")
            obj.achivements=request.POST.get("achivements","")
            obj.proskills=request.POST.get("proskills","")
            obj.famskills=request.POST.get("famskills","")
            obj.protech=request.POST.get("protech","")
            obj.famtech=request.POST.get("famtech","")
            # name=full_name,phone=phone,email=email,address=address,degree=degree,inter=intermediate,highschool=highSchool,about_you=about_you,skills=skills,experience=experience,cv_img=cv_img)
            
            obj.save()
            # generate resume
            try:
                resume_info = Resume.objects.all()
                for resume_info in resume_info:
                    context={"resume_info":resume_info}
                return render(request,current_url,context)
            except:
                return render(request,current_url)
            # return redirect("MyApp:template")
            # messages.info(request, 'Resume Info Added Successfully. Download Resume Now')
        else:
            messages.info(request,"Invalid Details")
            return redirect("MyApp:create_resume")

    else:
        return render(request,"create_resume.html")

