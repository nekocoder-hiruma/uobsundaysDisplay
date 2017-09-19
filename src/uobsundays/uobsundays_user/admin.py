from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from uobsundays_user.models import User, SocialMediaUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'nric', 'mobile')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'nric', 'mobile', 'is_active', 'is_admin')

        def clean_password(self):
            return self.initial["password"]


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'nric', 'mobile', 'is_admin')
    list_filter = ('is_admin',)
    readonly_fields = ('last_time_vote',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'nric', 'mobile')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('first_time_vote', {'fields': ('first_time_vote',)}),
        ('last_time_vote', {'fields': ('last_time_vote',)}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nric', 'mobile', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class SocialAdmin(admin.ModelAdmin):
    list_display = ('UID', 'email', 'username', 'last_name', 'first_name')


admin.site.register(User, UserAdmin)
admin.site.register(SocialMediaUser, SocialAdmin)
admin.site.unregister(Group)
