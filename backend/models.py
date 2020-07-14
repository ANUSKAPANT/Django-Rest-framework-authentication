from django.db import models
from django.contrib.auth.models import User,Group


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
@receiver(post_save, sender = User)
def create_auth_token(sender, instance = None, created = False, **kwargs):
	if created :
		group = Group.objects.get(name='user')
		instance.groups.add(group)
		Token.objects.create(user = instance)