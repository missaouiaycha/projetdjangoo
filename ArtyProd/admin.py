from django.contrib import admin
from .models import CustomUser
admin.site.register(CustomUser)
from .models import Projet
admin.site.register(Projet)
from .models import Service
admin.site.register(Service)
from .models import Detail
admin.site.register(Detail)
