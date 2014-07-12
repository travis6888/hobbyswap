from hobbyswap.models import Condition, Item, Category, Renter

__author__ = 'Travis'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmailUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=12, help_text="Format should be: 650-111-2222")

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
    item = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    price = forms.FloatField()
    deposit = forms.FloatField()
    condition = forms.ModelChoiceField(queryset=Condition.objects.all())
    beg_availability = forms.DateTimeField(help_text='Please enter beginning availability date')
    end_availability = forms.DateTimeField(help_text='Please enter availability end date')
    image = forms.ImageField()


class SelectItemForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all())
    post_user = forms.ModelChoiceField(queryset=Item.objects.all())
    renter = forms.ModelChoiceField(queryset=Renter.objects.all())
    subject = forms.CharField()
    message = forms.CharField()
    email = forms.EmailField()
    beg_date = forms.DateTimeField(help_text='Please enter the first day of the rental')
    end_date = forms.DateTimeField(help_text='Please enter the rental end date')
    price = forms.FloatField()
    deposit = forms.FloatField()
    to_email = forms.EmailField()



