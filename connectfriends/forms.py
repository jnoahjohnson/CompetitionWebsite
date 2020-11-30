from django import forms

class create_group(forms.Form):
    Groupname = forms.CharField(help_text="Enter a name for your group")