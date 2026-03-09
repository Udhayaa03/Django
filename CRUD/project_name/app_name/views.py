from django.shortcuts import render,redirect
from app_name.models import Register

# Create your views here.

def home(request):
    register_entries = Register.objects.all()
    return render(request, "home.html", {"register_entries": register_entries})

def register(request):
    #  print("Registered Successfully")

    register_entries = Register.objects.all() # display panna

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        role = request.POST.get("role")

        print(f"Name: {name}, Email: {email}, Age: {age}, Role: {role}")  
        register_entry = Register(name=name, email=email, age=age, role=role)
        register_entry.save()
        print("Registered Successfully ")

    return render(request,"home.html",{"register_entries": register_entries}) # ingaiyum home la kodutha mathriri kodutha than display aagum



# ipo update function ah create pannanum

def update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        role = request.POST.get("role")

        edit = Register.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.role = role
        edit.save()
        print("Updated Successfully")
    register_entry = Register.objects.get(id=id)
    return render(request, "update.html", {"register_entry": register_entry})



# ipo delete function ah create pannanum
def deletedata(request,id):
    register_entry = Register.objects.get(id=id)
    register_entry.delete() 
    return redirect("/")  # home page ku thirumbi poga delete pannittu