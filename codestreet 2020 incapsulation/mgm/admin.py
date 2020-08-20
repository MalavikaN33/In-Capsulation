from django.contrib import admin
from .forms import StockCreateForm
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name','issue_by', 'quantity']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
admin.site.register(Userinfo)
admin.site.register(StockHistory)
admin.site.register(supplier)



