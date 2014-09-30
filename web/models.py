from django.db import models

class UserProfile(models.Model):
	user_id = models.IntegerField(primary_key=True)
	email = models.EmailField(max_length=100)
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
	thumnail_modified = models.DateField()
	image_modified = models.DateField()
	deleted = models.BooleanField(default=False)


class ContactGroup(models.Model):
	name = models.CharField(unique=True, max_length=255)
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=1000)
	deleted = models.BooleanField(default=False)
	created = models.DateField(auto_now_add=True)
	modified = models.DateField(auto_now=True)


class UserContactGroup(models.Model):
	user_profile = models.ForeignKey(UserProfile)
	contact_group = models.ForeignKey(ContactGroup)
	moderator = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)
	created = models.DateField(auto_now_add=True)
	modified = models.DateField(auto_now=True)



