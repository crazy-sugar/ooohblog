from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=1,required=True,
                            error_messages={
                                'required': '文章标题是必填项'
                            })
    desc = forms.CharField(min_length=4,required=True,
                           error_messages={
                               'required': '文章标题是必填项',
                               'min_length': '文章简短描述不能少于4字符'
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填'
                              })
    icon = forms.ImageField(required=False)
    keywords = forms.CharField(required=False)


class EditArtForm(forms.Form):
    title = forms.CharField(min_length=1,required=True,
                            error_messages={
                                'required': '文章标题是必填项'
                            })
    desc = forms.CharField(min_length=4,required=True,
                           error_messages={
                               'required': '文章标题是必填项',
                               'min_length': '文章简短描述不能少于4字符'
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填'
                              })
    icon = forms.ImageField(required=False)
    keywords = forms.CharField(required=False)
