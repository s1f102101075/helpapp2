from django import forms
from allauth.account.forms import SignupForm

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='姓',max_length=30)
    last_name = forms.CharField(label='名', max_length=30)
    sex = forms.CharField(label='性別', max_length=30)
    height = forms.CharField(label='身長', max_length=30)
    weight = forms.CharField(label='体重', max_length=30)

class SignupUserForm(SignupForm):
    first_name = forms.CharField(label='姓',max_length=30)
    last_name = forms.CharField(label='名', max_length=30)
    sex = forms.CharField(label='性別', max_length=30)
    height = forms.CharField(label='身長', max_length=30)
    weight = forms.CharField(label='体重', max_length=30)
    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.sex = self.cleaned_data['sex']
        user.height = self.cleaned_data['height']
        user.weight = self.cleaned_data['weight']
        user.save()
        return user
