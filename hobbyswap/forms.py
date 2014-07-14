from django_messages.models import *
from hobbyswap.models import Condition, Item, Category, Renter


__author__ = 'Travis'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmailUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': '10 Character Max'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'your@gmail.com'}))
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': '415-555-1111'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "phone")

    def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',)


class PostItemForm(forms.Form):
    item = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Item name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Detailed Description of item'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    price = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Please enter price per day'}))
    deposit = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Enter deposit'}))
    condition = forms.ModelChoiceField(queryset=Condition.objects.all())
    beg_availability = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Please enter Beginning Date'}))
    end_availability = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Please enter End Date'}))
    image = forms.ImageField()


class SelectItemForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all())
    post_user = forms.ModelChoiceField(queryset=Item.objects.all())
    renter = forms.ModelChoiceField(queryset=Renter.objects.all())
    subject = forms.CharField()
    message = forms.CharField()
    email = forms.EmailField()
    beg_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Please enter rental Beginning Date'}))
    end_date = forms.DateTimeField(help_text='Please enter the rental end date')
    price = forms.FloatField()
    deposit = forms.FloatField()
    to_email = forms.EmailField()


class ReviewForm(forms.Form):
    subject = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'placeholder': 'Review Subject'}))
    text = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={'placeholder': 'Write your review here'}))


#
# class MyComposeForm():
#     item = forms.ModelChoiceField(queryset=Item.objects.all())
#     beg_date = forms.DateTimeField(help_text='Please enter the first day of the rental')
#     end_date = forms.DateTimeField(help_text='Please enter the rental end date')
#     price = forms.FloatField()
#     deposit = forms.FloatField()
#
#     class Meta:
#         model = Message
#         fields = ('item', 'beg_date', 'end_date', 'price', 'deposit')
