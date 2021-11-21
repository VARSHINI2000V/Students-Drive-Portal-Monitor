from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import students,admin,companies,registeration,studentplaced,staff
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def login(request):
    return render(request,'login.html')

def logining(request):
    if request.method == 'POST':
        request.session['email']=request.POST['email']
        email=request.POST['email']
        password=request.POST['password']
        user = students.objects.all().filter(email=email,Password=password).first()
        context=students.objects.all().filter(email=email,Password=password,dept='')
        details = {'students':students.objects.filter(email=email,Password=password)}
        if(user!=None):
            if(context):
                return render(request,'profile.html',details)
            else:
                return redirect('/drives/')
        else:
            messages.error(request,"Username or Password Error")
            return redirect('/login/')

def register(request):
    return render(request,'register.html')

def registering(request):
    if request.method=='POST':
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        dob=request.POST['dob']
        email=request.POST['email']
        phone=request.POST['phone']
        if password==cpassword:
            user = students.objects.all().filter(email=email).first()
            values="PLEASE LOGIN HERE FOR MORE DETAILS - http://127.0.0.1:8000/login/\n"+"Login credentials \n"+"Email- "+email+"\n"+"Password- "+password
            if(user==None):
                send_mail(
                    subject='HI CANDIDATE YOU ARE BEING REGISTERED AS A STUDENT',
                    message = values,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.POST['email']],
                    fail_silently=False
                )
                students.objects.create(Password=password,dob=dob,email=email,contact=phone)
                return redirect('/register/')
            else:
                messages.error(request,"Already registered")
                return redirect('/register/')

def myprofile(request):
    details = {'students':students.objects.filter(email=request.session['email'])}
    return render(request,'profile.html',details)



def updateprofile(request):
    if request.method=='POST':
        name=request.POST['name']
        surname=request.POST['surname']
        rollno=request.POST['rollno']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        dept=request.POST['dept']
        year=request.POST['year']
        cgpa=request.POST['cgpa']
        backlogs=request.POST['backlog']
        students.objects.filter(email=request.session['email']).update(firstname=name,lastname=surname,rollno=rollno,Address=address,state=state,country=country,dept=dept,year=year,cgpa=cgpa,backlogs=backlogs)
        return redirect('/drives/')


def logout(request):
    del request.session['email']
    return redirect('/login/')

def viewdrives(request):
    studentss=students.objects.filter(email=request.session['email']).values('cgpa')
    for i in studentss:
        value=i['cgpa']
    if value==None:
        return redirect('/myprofile/')
    else:
        studentss=students.objects.filter(email=request.session['email']).values('cgpa','backlogs','dept')
        companiess=companies.objects.values('PG','programme','name')
        context=companies.objects.all()
        if context==None:
            return HttpResponse("BO")
        else:
            for i in studentss:
                        context={'companies':companies.objects.filter(PG__lte=i['cgpa'],programme=i['dept'])}
                        if(context!=None and i['backlogs']==0):
                            return render(request,'view.html',context)
                        else:
                            context={'companies':companies.objects.filter(PG__gte=i['cgpa'],programme=i['dept'])}
                            return render(request,'view.html',context)


   


def drives(request):
    return render(request,'drive.html')

def placed(request):
    context1=studentplaced.objects.filter(email=request.session['email']).first()
    if(context1!=None):
        context={'placed':studentplaced.objects.filter(email=request.session['email'])}
        return render(request,'placed1.html',context)
    else:
        return render(request,'placed.html')

def admins(request):
    return render(request,'adminlogin.html')

def adminlogining(request):
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        admins = admin.objects.all().filter(name=name,password=password).first()
        context={'admin':admin.objects.filter(name=name,password=password)}
        if(admins!=None):
            return render(request,'adminhome.html',context)
        else:
            messages.error(request,"Username or Password Error")
            return redirect('/adminlogin/')

def adminlogout(request):
    return redirect('/adminlogin/')

def admindrive(request):
    context={'registered':registeration.objects.all()}
    return render(request,'Adrive.html',context)

def adminplaced(request):
    context={'placed':studentplaced.objects.all()}
    return render(request,'Aplaced.html',context)

def  index(request):
    return render(request,'index.html')

def newcompany(request):
    return render(request,'ANewDrive.html')

def addcompanies(request):
    if request.method == "POST":
        company=request.POST['company']
        location=request.POST['location']
        bond=request.POST['bond']
        fte=request.POST['fte']
        intern=request.POST['intern']
        ftepack=request.POST['ftesalary']
        internpack=request.POST['internsalary']
        programme=request.POST['programme']
        pg=request.POST['PG']
        link=request.POST['link']
        role=request.POST['Role']
        companies.objects.create(name=company,location=location,bond=bond,fte=fte,intern=intern,ftepack=ftepack,internpack=internpack,PG=pg,programme=programme,link=link,role=role)
        return redirect('/admin/company/')

def registerationstatus(request,id):
    values=companies.objects.filter(id=id).values('name')
    for i in values:
        value=i['name']
    context={'companies':companies.objects.filter(id=id),'registered':registeration.objects.filter(companyname=value,email=request.session['email']),'students':students.objects.filter(email=request.session['email']),'studentsplaced':studentplaced.objects.filter(email=request.session['email'])}
    return render(request,'registeration.html',context)

def registerationcompany(request):
    if request.method == "POST":
        register=request.POST['registered']
        context=students.objects.filter(email=request.session['email']).values('rollno','dept')
        for i in context:
            value=i['rollno']
            value1=i['dept']
        if(register=="yes"):
            email=request.session['email']
            company=request.POST['company']
            registeration.objects.create(email=email,rollno=value,companyname=company,status="Registered",programme=value1)
            send_mail(
                    subject='You have been successfully registered',
                    message = 'Login to view - http://127.0.0.1:8000/drives/',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.session['email']],
                    fail_silently=False
                )
            return redirect('/drives/')
        else:
            email=request.session['email']
            company=request.POST['company']
            registeration.objects.create(email=email,rollno=value,companyname=company,status="Not Interested",programme=value1)
            return redirect('/drives/') 

def placedstatus(request):
    if request.method == "POST":
        company=request.POST['company']
        context=students.objects.filter(email=request.session['email']).values('dept','email','rollno')
        for i in context:
            value=i['dept']
            value2=i['rollno']
            value3=i['email']
        bond=request.POST['bond']
        package=request.POST['package']
        intern=request.POST['internship']
        fte=request.POST['fte']
        role=request.POST['Role']
        internpack=request.POST['internpackage']
        image=request.FILES['image']
        studentplaced.objects.create(name=company,programme=value,bond=bond,ftepackage=package,intern=intern,fulltime=fte,internpack=internpack,rollno=value2,email=value3,role=role,image=image)
        students.objects.filter(email=request.session['email']).update(placed="PLACED")
        return redirect('/placed/')

def existingcompanies(request):
    context={'companies':companies.objects.all()}
    return render(request,'companies.html',context)

def deletecompanies(request,id):
    companies.objects.filter(id=id).delete()
    return redirect('/admin/companies/')

def staffregister(request):
    return render(request,'staffregister.html')

def stafflogin(request):
    return render(request,'stafflogin.html')

def staffhome(request):
    context={'staff':staff.objects.filter(name=request.session['name'])}
    return render(request,'staffhome.html',context)

def stafflogining(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        password=request.POST['password']
        staff.objects.create(name=name,dept=dept,password=password)
        return redirect('/staff/login/')

def stafflogins(request):
    name=request.POST['email']
    request.session['name']=request.POST['email']
    password=request.POST['password']
    context=staff.objects.filter(name=name,password=password)
    if(context!=None):
        return redirect('/staff/home/')
    else:
        return HttpResponse("No")

def staffplaced(request):
    confirm=staff.objects.filter(name=request.session['name']).values('dept')
    for i in confirm:
        value=i['dept']
    context={'placed':studentplaced.objects.all().filter(programme=value)}
    return render(request,'splaced.html',context)

def staffdrives(request):
    confirm=staff.objects.filter(name=request.session['name']).values('dept')
    for i in confirm:
        value=i['dept']
    context={'registered':registeration.objects.filter(programme=value)}
    return render(request,'sdrive.html',context)

def stafflogout(request):
    del request.session['name']
    return redirect('/staff/login/')

def search(request):
    context={'companies':companies.objects.all().values('name').distinct()}
    return render(request,'search.html',context)

def searching(request):
    values=staff.objects.values('dept')
    for i in values:
        value=i['dept']
    if request.method == "POST":
        company=request.POST['companies']
        context={'students':studentplaced.objects.filter(programme=value,name=company),'companies':companies.objects.all().values('name').distinct(),'companies1':companies.objects.filter(name=company)}
        return render(request,'search1.html',context)
    
def adminsearch(request):
    context={'companies':companies.objects.all().values('name').distinct()}
    return render(request,'adminsearch.html',context)

def adminsearching(request):
    if request.method == "POST":
        company=request.POST['companies']
        context={'students':studentplaced.objects.filter(name=company),'companies':companies.objects.all().values('name').distinct(),'companies1':companies.objects.filter(name=company)}
        return render(request,'adminsearch1.html',context)

def about(request):
    return render(request,'about.html')





