from django import forms

class CamersForm(forms.Form):
    types = forms.CharField(label='Тип камеры', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'dvn, grz, pes, pvn'}))
    name = forms.CharField(label='Имя камеры', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Имя камеры'}))
    address = forms.GenericIPAddressField(label='IP-адрес', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'IP-адрес'}))
    link = forms.CharField(label='RTSP-ссылка', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'RTSP-ссылка'}))
    guid = forms.CharField(label='GUID', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'GUID'}))