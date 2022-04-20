from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml_converter.xml_parser import XmlParser
from xml_converter.serializers import FileSerializer
from rest_framework import status



class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            xml_parser_obj = XmlParser(serializer.validated_data['file'])
            my_dict = xml_parser_obj.convert_xml_file_into_dictionary()
            return Response(my_dict, status=status.HTTP_200_OK)

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
