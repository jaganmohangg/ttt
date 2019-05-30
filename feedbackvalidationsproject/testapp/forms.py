from django import forms
from django.core import validators


class FeedBackForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re Enter Password',widget=forms.PasswordInput)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(20)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print('validating passwords match...')
        total_cleaned_data=super().clean()
        fpwd=total_cleaned_data['password']
        spwd=total_cleaned_data['rpassword']
        if fpwd != spwd:
            raise forms.ValidationError('Both passwords must be matched')
        bot_handler_value=total_cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Request from BOT...cannot be submitted!!!')
        email=total_cleaned_data['email']
        if email[-9:]!='gmail.com':
            raise forms.ValidationError('Must be gmail!!!')

    #  ExPLICIT VALIDATORS
    # def clean_name(self):
    #     print('clean_name is executing...')
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError('The minimum number of characters in the name should be 4')
    #     return inputname
    # def clean_rollno(self):
    #     inputrollno=self.cleaned_data['rollno']
    #     print('clean_rollno is executing..')
    #     return inputrollno
    # def clean_email(self):
    #     inputemail=self.cleaned_data['email']
    #     print('clean_email is executing..')
    #     return inputemail
    # def clean_feedback(self):
    #     inputfeedback=self.cleaned_data['feedback']
    #     print('clean_feedback is executing..')
    #     return inputfeedback
