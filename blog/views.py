from django.shortcuts import render,redirect
from .models import article
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

def liste_article(request):
    articles = article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/liste_article.html', context)




def ajouter_article(request):
    if request.method == 'POST' and request.user.is_authenticated:
        nom = request.POST.get('nom', '')
        description = request.POST.get('discription', '')
        if request.FILES.get('image', None):
                image = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
        image = request.POST.get('image', '')
        user=request.user
        projet = article(title=nom, content=description, image=fs.url(filename),user=user)
        projet.save()
        return redirect('liste_article')
    return render(request, 'blog/ajouter_article.html')