from django import forms
from .models import MainCarousel, Bottles, WorkerDesc, WorkPlace

class M_CarouselForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите имя"}))
    img = forms.ImageField( widget=forms.FileInput())
    
    class Meta:
        model = MainCarousel
        fields = ('name', 'img')


class BottlesForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите имя"}))
    img = forms.ImageField( widget=forms.FileInput())

    class Meta:
        model = Bottles
        fields = ('name', 'img')


class WorkersForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите имя"}))
    spec = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите специальность"}))
    img = forms.ImageField( widget=forms.FileInput())
    desc = forms.CharField( widget = forms.Textarea(attrs = {'class':'form-control','placeholder':"введите описание"}))

    class Meta:
        model = WorkerDesc
        fields = ('name',  'spec', 'img', 'desc')




class WorkPlaceForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите имя"}))
    desc = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите описание"}))
    img = forms.ImageField( widget=forms.FileInput())
    
    class Meta:
        model = WorkPlace
        fields = (
            'name',
            'desc',
            'img',
        ) 

