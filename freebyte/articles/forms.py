from django import forms

from freebyte.articles.models import Article


# TODO:how to set lable's attribute: for
class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='标题',
        max_length=255)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='内容',
        max_length=4000)
    tags = forms.Field(
        widget=forms.TextInput(),
        label='标签',
        help_text='英文逗号分隔的标签')

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'status']
