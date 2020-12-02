from django import forms

class AddTaskForm(forms.Form):
    content = forms.CharField(
        label = 'Task Content',
        widget=forms.TextInput(),
        max_length=255)
