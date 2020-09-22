from django.contrib import admin
from .models import *
# Register your models here.


class ProdukImageInline(admin.StackedInline):
  model = Outlet
  max_num=10
  extra=0

class ProjectAdmin(admin.ModelAdmin):
  inlines = [ProdukImageInline]


admin.site.register(Kota, ProjectAdmin)