from django import forms
from .models import Parfume, Parfume_volume


selection = (
    ('Есть','Есть'),
    ('Нет','Нет'),

)

cat_selection =  (
    ('Мужской','Мужской'),
    ('Женский','Женский'),
    ('Унисекс','Унисекс'),
)
 

class ParfumeForm(forms.ModelForm):

    brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'placeholder':"наименование бренда"}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'placeholder':"наименование"}))
    toilet_water = forms.CharField(widget=forms.Select(choices=selection, attrs={'class': 'form-control'}))
    category = forms.CharField(widget=forms.Select(choices=cat_selection, attrs={'class': 'form-control'}))
    img = forms.ImageField( widget=forms.FileInput())    

    class Meta:
        model = Parfume
        fields = ('brand',  
                  'toilet_water', 'name', 'category', 'img')
        



parfumes = Parfume.objects.all()

class ParfumeVolumeForm(forms.ModelForm):

    volum_ml = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number', 'placeholder':"12345"}))
    parfum = forms.ModelChoiceField(queryset=parfumes, widget=forms.Select(attrs={'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number', 'placeholder':"12345"}))



    class Meta:
        model = Parfume_volume
        fields = (
                'parfum',
                'volum_ml',
                'price',
                 ) 
        