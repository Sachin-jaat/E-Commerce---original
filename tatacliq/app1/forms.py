
from django import forms
from .models import Profile
from .models import Product

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image']  # Include 'stock'

from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

from django import forms

from django.contrib.auth.models import Group

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        role = self.cleaned_data['role']

        if commit:
            user.save()
            # Create a linked user profile
            UserProfile.objects.create(user=user, role=role)

            # Assign group based on role
            group, created = Group.objects.get_or_create(name=role.capitalize())
            user.groups.add(group)

        return user
