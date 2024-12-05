from django.shortcuts import render
from django.http import HttpResponse
from home.models import Register
# Create your views here.
def index(request):
    return render(request,'register.html')

def submit_form(request):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Address = request.POST['Address']
        Phone_Number = request.POST['Phone']
        Email = request.POST['Email']
        Collage_Name = request.POST['Collage']
        Gender = request.POST['Gender']
        Area_Py= request.POST.get('Python','off')
        Area_Java= request.POST.get('Java','off')
        Area_PH= request.POST.get('PHP','off')
        Area_Javas= request.POST.get('Javascript','off')
        AOI = []
        if Area_Py == "Python":
            AOI.append(Area_Py)
        if Area_Java == "Java":
            AOI.append(Area_Java)
        if Area_PH == "PHP":
            AOI.append(Area_PH)
        if Area_Javas == "Javascript":
            AOI.append(Area_Javas)
        print(First_Name,Last_Name,Address,Phone_Number,Email,Collage_Name,Gender,*AOI)
        Register(First_Name= First_Name,Last_Name=Last_Name,Address=Address,
                 Phone_Number = Phone_Number,Email=Email,Collage_Name=Collage_Name,Gender=Gender,Area_Of_Intrest= AOI).save()
        msg = "Form Submitted Succefully"
        return render(request,'register.html',{'msg':msg})
    else:
        return HttpResponse("<h1>404 Not Found...</h1>")