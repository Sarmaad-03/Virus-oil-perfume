from django import forms
from .models import UserAccount
from .models import Purchase, Gift

from parfume.models import Parfume, Parfume_volume

class CustomerCreationForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'placeholder':"введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'placeholder':"введите фамилию"}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number', 'placeholder':"введите номер"}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control date-picker', 'placeholder':"введите дату"}))

    class Meta:
        model = UserAccount
        fields = ('first_name', 
                  'last_name', 
                  'birthday', 
                  'number')


users = UserAccount.objects.all()
parfumes = Parfume_volume.objects.all()

class PurchaseCreationForm(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=users, widget=forms.Select(attrs={'class': 'form-control'}))
    parfume = forms.ModelChoiceField(queryset=parfumes, widget=forms.Select(attrs={'class': 'form-control'}))

    def get_parfume_id(self):
        return self.parfume

    class Meta:
        model = Purchase
        fields = (
            'user',
            'parfume',
        )


class GiftForm(forms.ModelForm):

    parfume = forms.ModelChoiceField(queryset=parfumes, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Gift
        fields = ('parfume', )
        

    