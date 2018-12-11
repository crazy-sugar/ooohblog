from django.contrib.auth.models import User, Group
from rest_framework import serializers

from backweb.models import Article


class ArtSerializer(serializers.ModelSerializer):
    desc = serializers.CharField(min_length=2,max_length=100,
                                 error_messages={
                                     'required': '描述必填',
                                     'min_length': '描述不少于2字符',
                                     'max_length': '描述最多不超过100字符'
                                 })
    title = serializers.CharField(min_length=1,max_length=30,
                                  error_messages={
                                      'required':'标题必填',
                                      'min_length':'描述不少于1字符',
                                      'max_length': '描述最多不超过100字符'
                                  })
    content = serializers.CharField(min_length=1,
                                    error_messages={
                                        'required': '内容必填',
                                        'min_length': '描述不少于1字符'
                                    })
    image = serializers.ImageField(required=False)
    type = serializers.CharField(required=False)

    class Meta:
        model = Article
        fields = ['title','desc','content','image','type']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.type:
            data['type']= instance.type.t_name
        return data

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.content)
        instance.type = validated_data.get('type', instance.content)
        instance.save()
        return instance



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','group')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')
