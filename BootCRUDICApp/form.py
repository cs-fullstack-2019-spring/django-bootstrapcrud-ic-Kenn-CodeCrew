from django import forms
from .models import GymMemberModel


class GymMemberForm(forms.ModelForm):
    class Meta:
        model = GymMemberModel
        fields = "__all__"
