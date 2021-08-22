from django import forms

from .models import Deal, SubDeal


class DealForm(forms.ModelForm):

    class Meta:
        model = Deal
        fields = ['group', 'title', 'text', 'image']


class SubDealForm(forms.ModelForm):

    class Meta:
        model = SubDeal
        fields = ['title', 'quantity']
