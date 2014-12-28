from django.contrib import admin
from lmstarts.models import HostGroup
from lmstarts.models import Computer

# Register your models here.
admin.site.register(Computer)
admin.site.register(HostGroup)