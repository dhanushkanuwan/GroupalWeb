from django.contrib import admin
from web.models import UserProfile
from web.models import ContactGroup
from web.models import UserContactGroup

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ContactGroup)
admin.site.register(UserContactGroup)
