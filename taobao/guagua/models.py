# coding=UTF-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    taobao_id = models.IntegerField()
    taobao_nick = models.CharField(max_length=20)
    sessionkey = models.CharField(max_length=100)
    start_date = models.DateField('date ordered')
    end_date = models.DateField('date expired', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.user_nick 
    
