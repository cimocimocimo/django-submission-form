from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=500)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
