from django import forms
from .models import Computer
 
class ComputerForm(forms.ModelForm):
   class Meta:
      model = Computer
      fields = ['staff_or_office', 'location', 'pc_model', 'IP_address', 'MAC_address','serial_number','ups', 'condition', 'network_connection', 'no_of_network_field']
