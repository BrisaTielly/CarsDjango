
from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )

class CarAdmin(admin.ModelAdmin):
    #Campos que vão aparecer para o admin
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') 

    #Campos que vão servir de busca
    search_fields = ('model', 'brand', )

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)




