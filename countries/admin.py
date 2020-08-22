from django.contrib import admin
from .models import Countries, Task, Product

# Register your models here.
class CountriesAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'capital', 'id',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'status')

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'categories')

admin.site.register(Countries, CountriesAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Product,ProductAdmin)