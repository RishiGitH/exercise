from rest_framework import serializers
from xml_converter.validators import validate_file_extension


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(validators=[validate_file_extension])