from django.contrib import admin
from .models import Model_INCAR, POSCAR_Down

# Register your models here.
class Admin_INCAR(admin.ModelAdmin):
    list_display = ["parameter","value"]

class Admin_POSCAR(admin.ModelAdmin):
    list_display = ['title','file','add_time']

admin.site.register(Model_INCAR,Admin_INCAR )
admin.site.register(POSCAR_Down,Admin_POSCAR)