from rest_framework.serializers import ModelSerializer
from groupal.apps.data.models import TestModel


class TestModelSerializer(ModelSerializer):
    class Meta:
        model = TestModel
