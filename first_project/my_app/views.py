from django.shortcuts import render,HttpResponse,redirect
from .models import Employee

# Create your views here.
def index(request):
    return HttpResponse("Hello all we learn Django")

def home(request):
    return HttpResponse("This is home page")

def about(request):
    return HttpResponse("<h3>This is about page</h3>")

#THIS IS ORM TECHNIQUE IN PYTHONIC WAY 
def showemp(request):
    emp_data = Employee.objects.all()    #select * from Employee 
    context = {'emp': emp_data }
    
    return render(request, 'show.html',context)

def addemp(request):
    if request.method == "POST":
        eno = request.POST["eno"]
        ename = request.POST["ename"]
        esal = request.POST["esal"]
        eadd = request.POST["eadd"]
        email = request.POST["email"]
        emp = Employee(eno=eno, ename=ename, esal=esal, eadd=eadd , email=email)
        # or    emp = Employee.objects.create(.....same as above.....)

        emp.save()
        return redirect("/show")
    return render(request, "addemp.html")

def delete_emp(request, id): 
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('employee_details') #urlname

def update_emp(request, id):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        emp.eno = request.POST["eno"]
        emp.ename = request.POST["ename"]
        emp.esal = request.POST["esal"]
        emp.eadd = request.POST["eadd"]
        emp.email = request.POST["email"]
        emp.save()
        return redirect('employee_details')
    else:
        context = { 'emp': emp }
    return render( request, "updateemp.html",context )

    

