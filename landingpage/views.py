from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        try:
            tech_list = ['Python', 'C#', 'Java', 'AWS', 'Docker', 'MySQL']
            tech = []
            python = request.POST.get('Python')
            dotnet = request.POST.get('C#')
            java = request.POST.get('Java')
            aws = request.POST.get('AWS')
            docker = request.POST.get('Docker')
            mySQL = request.POST.get('MySQL')

            for tech_needed in tech_list:
                if request.POST.get(tech_needed) != None: tech.append(tech_needed)
        
        except Exception as e:
            print(f"error: {e}")
        """ 
        if "Python" in request.POST:
            print("Python")
        if "C#" in request.POST:
            print("C#")
        if "Java" in request.POST:
            print("Java")
        if "AWS" in request.POST:
            print("AWS")
        if "Docker" in request.POST:
            print("Docker")
        if "MySQL" in request.POST:
            print("MySQL")
        """
        send_mail(
            f"{name} contacted you through your landingpage", # subject
            f"{message}\nTechnologies: {tech}", # message
            email, # from e-mail
            ['example@email.com'] # to e-mail
        )

        help_contact = f"Thanks {name} for your request!"
        return render(request, 'andreas_template/index.html', {'help_contact': help_contact, 'name': name, 'email': email})
    else:
       help_contact = "I'll help you with"
       return render(request, 'andreas_template/index.html', {'help_contact': help_contact})