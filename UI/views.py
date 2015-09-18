from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pyqrcode import create as create_qrcode

def get_qr_code_image(request, identification):
    qr_code_img = create_qrcode("%s/download/%s" % (settings.PUBLIC_HOST_ADDRESS, identification))
    qr_file_path = "%s.png" % identification
    qr_code_img.png(qr_file_path, scale=11, module_color=(68, 50, 102), background=(243, 235, 246))
    response = HttpResponse(file(qr_file_path, "rb").read())
    response["Content-Type"] = "image/png"
    return response

def get_author_initials_image(request, author_name):
    pass
