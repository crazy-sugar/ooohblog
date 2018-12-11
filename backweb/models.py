from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class AType(models.Model):
    t_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'tb_atype'


class Article(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.ImageField(null=True,upload_to='tb_article')
    category = models.ForeignKey(AType,null=True)
    is_delete = models.BooleanField(default=0)
    keywords = models.CharField(max_length=20,null=True)

    class Meta:
        db_table = 'tb_article'


class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True)
    phone = models.CharField(max_length=20,null=True)
    birth = models.DateField(blank=True,null=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)