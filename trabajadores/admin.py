from django.contrib import admin
from .models import Trabajador

# Register your models here.
class TrabajadorAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Trabajador, TrabajadorAdmin)
