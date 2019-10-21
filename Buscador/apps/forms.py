from django import forms

class Formulario(forms.Form):
    consulta = forms.CharField(max_length = 50,label = 'consulta')


def busqueda(request):
    # print("hola")
    return 1;
   