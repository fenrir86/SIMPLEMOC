# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .mail import send_mail_template
from .models import Comment


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem',
                              widget=forms.Textarea)

    def send_mail(self, course):
        subject = '[%s] Contato' % course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        """
             message = f'Nome: {context["name"]} \n' \
                  f'Email: {context["email"] } \n' \
                  f'Mensagem: \n {context ["message"]}'
        message = f'{message}'
        send_mail(subject,message,settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
     
        """
        template_name = 'courses/contact_email.html'
        send_mail_template(subject,template_name,context,[settings.CONTACT_EMAIL])

class CommentForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields = ['comment']
