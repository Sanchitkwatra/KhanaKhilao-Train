from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm

from Hungry_No_More.models import User,NGO,FoodDetails, Vendor
from . import models

class VendorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( "name", "username", "password1", "password2")

    @transaction.atomic
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_vendor=True
        if commit:
            user.save()
        return user



class NGOSignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=("station","name","phone_no","username","password1","password2")


    @transaction.atomic
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_ngo=True
        if commit:
            user.save()

        return user


class VendorFoodSubmitForm(forms.ModelForm):

    class Meta:
        model=FoodDetails
        fields=("train","station","veg","nonveg")

    # def __init__(self,*args,**kwargs):
    #     user=kwargs.pop('current_user')
    #     super(VendorFoodSubmitForm, self).__init__(*args,**kwargs)
    #     self.fields['vendor'].queryset=Vendor.objects.filter(user=user)


