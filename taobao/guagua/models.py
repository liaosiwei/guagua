# coding=UTF-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
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
    
def create_user_profile(sender, instance, created=True, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)