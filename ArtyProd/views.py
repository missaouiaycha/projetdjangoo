from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from ArtyProd.forms import UserRegistrationForm
from .models import *
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm
def acceuil(request):
    return render(request, 'ArtyProd/acceuil.html')
def navbar(request):
    return render(request, 'ArtyProd/navbar.html')
def about(request):
    return render(request, 'ArtyProd/about.html')

def listRequest(request):
    projets= Projet.objects.all()
    context={'projets':projets}
    return render(request,'ArtyProd/listRequest.html',context)
@login_required
def listdetail(request,libellai):
    if(Projet.objects.filter(libellai=libellai)):
        details=Detail.objects.filter(projet__libellai=libellai)
        projet_name=Projet.objects.filter(libellai=libellai).first()
        context={'details':details,'projet_name':projet_name}
        return render(request,'services/listdetail.html',context)
    else:
        messages.warning(request,"No such projet found")
        return redirect('ArtyProd/listprojet')
def contact(request):
    return render(request, 'ArtyProd/contact.html')

def Portfolio(request):
  projets=Projet.objects.all()
  context={'projets':projets}
  return render(request, 'ArtyProd/Portfolio.html',context)


def service(request):
  services=Service.objects.all()
  context={'services':services}
  return render(request, 'ArtyProd/service.html',context)

def ajouter_projet(request):
  return render(request, 'ArtyProd/ajouter_projet.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Bienvenue {username}, Votre compte a été créé avec succès !')
            return redirect('/login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})




def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '')
        prenom = request.POST.get('prenom', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(nom=nom, prenom=prenom, email=email, message=message)
        contact.save()
        
        html = render_to_string('ArtyProd/form.html', {
            'nom': nom,
            'prenom': prenom,
            'email': email,
            'message': message
        })
        
        send_mail(
            'Sujet du formulaire de contact',
            'Ceci est le message',
            'missaouiaycha2021@gmail.com',
            ['missaouimaycha2021@gmail.com'],
            html_message=html
        )
        
        return render(request, 'ArtyProd/acceuil.html')
    
    return render(request, 'ArtyProd/contact.html')

def navbar(request):
    return render(request, 'ArtyProd/navbar.html')


def ajouter_projet(request):
    if request.method == 'POST' and request.user.is_authenticated:
        nom = request.POST.get('libellai', '')
        date_fin = request.POST.get('date_fin', '')
        description = request.POST.get('description', '')
        if request.FILES.get('image', None):
                image = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
        image = request.POST.get('image', '')
        user=request.user
        projet = Projet(libellai=nom,date_fin=date_fin, description=description, image=fs.url(filename),user=user)
        projet.save()
        return render(request, 'ArtyProd/acceuil.html')
    return render(request, 'ArtyProd/ajouter_projet.html')



def listGroup(request):
    groups = Group.objects.all()
    users = CustomUser.objects.all()
    context = {
        'groups': groups,
        'users': users,
    }
    return render(request, 'ArtyProd/group.html', context)



@login_required
def ajoutDetail(request, projet_id):
    services = Service.objects.all()
    context = {'services': services}
    if request.method == 'POST' and request.user.is_authenticated:
        nom = request.POST.get('nom', '')
        fichier = request.FILES.get('ficher', None)
        service_id = request.POST.get('service', '')
        s = Service.objects.get(id=service_id)
        p = Projet.objects.get(id=projet_id)
        detail = Detail(nom=nom, fichier=fichier, service=s, projet=p)
        detail.save()
        return redirect('listdetail', libellai=p.libellai)
    return render(request, 'ArtyProd/ajoutdetail.html', context)
@login_required
def listdetail(request,libellai):
    if(Projet.objects.filter(libellai=libellai)):
        details=Detail.objects.filter(projet__libellai=libellai)
        projet_name=Projet.objects.filter(libellai=libellai).first()
        context={'details':details,'projet_name':projet_name}
        return render(request,'ArtyProd/listdetail.html',context)
    else:
        messages.warning(request,"No such projet found")
        return redirect('ArtyProd/listprojet')
