from django import forms

class DataForm(forms.Form):
    x_values = forms.CharField(label='X-axis values (comma-separated)', widget=forms.TextInput(attrs={'placeholder': 'e.g., 1, 2, 3, 4'}))
    y_values = forms.CharField(label='Y-axis values (comma-separated)', widget=forms.TextInput(attrs={'placeholder': 'e.g., 10, 15, 7, 10'}))
