from django import forms 


class usuarioForm(forms.Form):
    nombre= forms.CharField(label="Nombre ", max_length=50)
    apellido= forms.CharField(label="Apellido ", max_length=50)
    