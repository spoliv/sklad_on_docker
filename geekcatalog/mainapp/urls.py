from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.catalog_view, name='catalog'),
    path('add/', mainapp.add_prod, name='add_product'),

]
