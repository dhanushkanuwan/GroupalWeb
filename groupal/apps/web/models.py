from django.db import models
from django.contrib.auth.models import User
import uuid
import os
import sys
from PIL import Image


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=100)
    birthday = models.DateField()
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    content_modified = models.DateField()
    thumbnail_modified = models.DateField()
    image_modified = models.DateField()
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class ContactGroup(models.Model):

    def get_thumbnail_upload_path(self, filename):
        name = str(uuid.uuid4())
        ext = os.path.splitext(filename)[1]
        return 'images/group/%s%s' % (name, ext)

    name = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255, )
    description = models.CharField(max_length=1000)
    #created_by = models.ForeignKey(User)
    content_modified = models.DateField()
    thumbnail_modified = models.DateField()
    deleted = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    thumbnail = models.ImageField(upload_to=get_thumbnail_upload_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(ContactGroup, self).save(*args, **kwargs)
        try:
            size = (128, 128,)
            im = Image.open(self.thumbnail.path)
            im.thumbnail(size)
            os.remove(self.thumbnail.path)
            im.save(self.thumbnail.path)
        except IOError as io:
            error = 'io error occurred'
        except:
            error = sys.exc_info()[0]
            test = ''

    def __unicode__(self):
        return u'%' % self.title


class UserContactGroup(models.Model):
    user_profile = models.ForeignKey(User)
    contact_group = models.ForeignKey(ContactGroup)
    type = models.IntegerField()
    deleted = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)











