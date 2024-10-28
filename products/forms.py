from django import forms
from .models import Products


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="nombre")
    descripcion = forms.CharField(max_length=300, label="descripcion")
    price = forms.DecimalField(max_digits=10, label="precio")
    avalible = forms.BooleanField(initial=True, label="disponible")
    photo = forms.ImageField(label="foto", required=False)    # require si el usuario desea dejar el campo vacio, asi mismo esta en el modelo 



    def save(self):        # cuando un usuario guarda sus datos con esta funcion por medio del object create el usuario guarda los datos en la base de datos

        Products.objects.create(

            name = self.cleaned_data["name"],
            descripcion = self.cleaned_data["descripcion"],
            price = self.cleaned_data["price"],
            avalible = self.cleaned_data["avalible"],
            photo = self.cleaned_data["photo"],

        )