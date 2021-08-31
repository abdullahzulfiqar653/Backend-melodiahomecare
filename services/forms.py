from.models import Blog
from ckeditor.fields import RichTextFormField
class BlogForm(forms.ModelForm):
    class Meta:
          model = Blog
          fields = ['content']
          widgets = {
             'content': RichTextFormField(),
          }