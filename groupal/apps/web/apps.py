from django.apps import AppConfig
from django.db.models.signals import post_delete
import sys
import os
from django.core.files.storage import default_storage
from django.db.models import FileField



def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.

    Usage:
    >>> from django.db.models.signals import post_delete
    >>> post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")
    """
    for fieldname in sender._meta.get_all_field_names():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
        if field and isinstance(field, FileField):
            inst = kwargs['instance']
            f = getattr(inst, fieldname)
            m = inst.__class__._default_manager
            if hasattr(f, 'path') and os.path.exists(f.path)\
            and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
            .exclude(pk=inst._get_pk_val()):
                try:
                    default_storage.delete(f.path)
                except:
                    pass


def group_file_cleanup(sender, **kwargs):
    try:
        instance = kwargs['instance']
        file_path = getattr(instance, 'thumbnail').path
        if os.path.exists(file_path):
            os.remove(file_path)
    except:
        error = sys.exc_info()[0]


class GroupalConfig(AppConfig):
    name = 'groupal.apps.web'
    verbose_name = 'Groupal Application'

    def ready(self):
        ContactGroup = self.get_model('ContactGroup')
        post_delete.connect(group_file_cleanup, sender=ContactGroup, dispatch_uid='group.image.cleanup')