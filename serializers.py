from rest_framework.serializers import ModelSerializer
from .models import School


class AllInOneSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class ClassAvgGenderHeightSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ["_class", "gender", "height"]