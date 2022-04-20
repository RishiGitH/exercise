import xmltodict
from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.forms import UploadFileForm
from xml_converter.xml_parser import XmlParser


def upload_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # TODO: Convert the submitted XML file into a JSON object and return to the user.
            xml_parser_obj = XmlParser(request.FILES['file'])
            my_dict = xml_parser_obj.convert_xml_file_into_dictionary()
            return JsonResponse(my_dict)

    return render(request, "upload_page.html")
