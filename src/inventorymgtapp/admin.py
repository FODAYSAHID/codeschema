from django.contrib import admin
from .models import Computer, Printer, Wireless_Connection
from .forms import ComputerForm

# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
   list_display = ["staff_or_office", "pc_model", "IP_address", "MAC_address"]
   form = ComputerForm
   list_filter = ["staff_or_office", "pc_model", "IP_address"]
   search_fields = ["staff_or_office", "pc_model", "IP_address"]


admin.site.register(Computer, ComputerAdmin)
admin.site.register(Printer)
admin.site.register(Wireless_Connection)
