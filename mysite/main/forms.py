from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Type your message here...'}))
    
    class Meta:
        model = Message
        fields = ['content']
