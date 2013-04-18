# coding=UTF-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    taobao_id = models.IntegerField(null=True, blank=True)
    taobao_nick = models.CharField(max_length=20, null=True, blank=True)
    sessionkey = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField('date ordered', null=True, blank=True)
    end_date = models.DateField('date expired', null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.user_nick 
    
def create_user_profile(sender, instance, created=True, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)