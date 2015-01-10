from django.contrib import admin
from groupal.apps.web.models import UserProfile
from groupal.apps.web.models import ContactGroup
from groupal.apps.web.models import UserContactGroup

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ContactGroup)
admin.site.register(UserContactGroup)
