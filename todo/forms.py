from django import forms

class AddTaskForm(forms.Form):
    content = forms.CharField(
        label = 'Task Content',
        widget = forms.TextInput(),
        max_length = 255)

class EditTaskForm(forms.Form):
    content = forms.CharField(
        label = 'Task Content',
        widget = forms.TextInput(),
        max_length = 255)
    is_done = forms.BooleanField(
        label = 'Is Done',
        required = False,
        widget = forms.CheckboxInput())
