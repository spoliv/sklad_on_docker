from django import forms
from mainapp.models import Product


class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       exclude = ('receipt_date',)

   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field_name, field in self.fields.items():
           field.widget.attrs['class'] = 'form-control'
