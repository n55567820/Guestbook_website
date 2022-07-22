from django import forms
from .models import Articles

class create_article_form(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    type = forms.CharField(required=True, widget=forms.Select(choices=(('', '請選擇'),) + Articles.Articles_CHOICES,
                                                              attrs={'class':'form-control'}))

class edit_article_form(forms.Form):
    def __init__(self,id):
        super().__init__()
        self.fields['title'].initial = Articles.objects.filter(id=id)[0].title
        self.fields['content'].initial = Articles.objects.filter(id=id)[0].content
        self.fields['type'].initial = Articles.objects.filter(id=id)[0].type
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    type = forms.CharField(required=True, widget=forms.Select(choices=(('', '請選擇'),) + Articles.Articles_CHOICES,
                                                             attrs={'class':'form-control'}))

class comment_form(forms.Form):
    comment_content = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))