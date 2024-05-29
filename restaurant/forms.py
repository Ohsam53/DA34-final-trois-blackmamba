from django import forms
from django.forms import inlineformset_factory
from restaurant.models import Restaurant, Menu

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['food_category', 'local_category','title','imgfile_1', 'imgfile_2','imgfile_3',
                  'image_link', 'open_day', 'close_day', 'open_time', 'close_time', 'break_time',
                  'isParking', 'isValet', 'isPet', 'isPackaging', 'address', 'phone', 'introduction',
                  'menu_url', 'latitude', 'longitude', 'parking_area']
        widgets = {
            'food_category': forms.TextInput(attrs={'class': 'form-control'}),
            'local_category': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image_link': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'open_day': forms.TextInput(attrs={'class': 'form-control'}),
            'close_day': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'menu_url': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
            'parking_area': forms.TextInput(attrs={'class': 'form-control'})
        }

