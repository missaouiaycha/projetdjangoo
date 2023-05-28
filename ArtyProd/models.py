from django.db import models
from django.contrib.auth.models import User,Group

class CustomUser(User):
    telephone = models.CharField(max_length=20,null=True, blank=True)
    image=models.ImageField(upload_to='upload/photos/',null=True, blank=True)
    fichier_CV = models.FileField(upload_to='upload/documents/',null=True, blank=True)

class Projet(models.Model):
    TYPE_CHOICES=[('achevé','achevé'),('en cours','en cours'),('request','request')]
    libellai = models.CharField(max_length=50)
    description = models.TextField()
    date_debut = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='upload/photos/')
    date_fin = models.DateTimeField(null=True, blank=True)
    etat=models.CharField(max_length=50,choices=TYPE_CHOICES,default='request')
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    Group = models.OneToOneField(Group,on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.libellai

class Service(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()
    image=models.ImageField(upload_to='upload/photos/')
    def __str__(self):
        return self.type
        
class Detail(models.Model):
    nom=models.CharField(max_length=50,default='')
    fichier = models.FileField(upload_to='upload/documents/')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Contact(models.Model):
    nom=models.CharField(max_length=50,default='')
    prenom=models.CharField(max_length=50,default='')
    mail=models.CharField(max_length=50,default='')
    message=models.TextField()
    def __str__(self):
        return self.nom