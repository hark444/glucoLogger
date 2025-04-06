from django.contrib.auth.forms import UserChangeForm


class UserProfileUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ["email", "first_name", "last_name"]
