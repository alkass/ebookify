from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pyqrcode import create as create_qrcode
from PIL import Image, ImageDraw, ImageFont
from os.path import join

def get_qr_code_image(request, identification):
    qr_code_img = create_qrcode("%s/%s" % (settings.PUBLIC_HOST_ADDRESS, identification))
    qr_file_path = join(settings.STATICFILES_DIRS[0], "media", "temp", "%s.png" % identification)
    qr_code_img.png(qr_file_path, scale=11, module_color=(68, 50, 102), background=(243, 235, 246))
    return HttpResponse(file(qr_file_path, "rb").read(), {"Content-type":"img/png"})

def get_author_initials_image(request, full_name):
    tokenized_name = full_name.title().strip().split(" ")
    initials = ""
    if len(tokenized_name) == 1:
        initials = tokenized_name[0][0]
    else:
        initials = "%s.%s." % (tokenized_name[0][0], tokenized_name[-1][0])
    font = ImageFont.truetype(join(settings.STATICFILES_DIRS[0], "fonts", "Roboto-Light.ttf"), 150)
    if len(initials) == 1:
        img = Image.new("RGBA", (300, 300), (211, 47, 47))
        draw = ImageDraw.Draw(img)
        if initials in ["M"]:
            draw.text((90, 70), initials ,(255, 255, 255),font=font)
        elif initials in ["W"]:
            draw.text((85, 70), initials ,(255, 255, 255),font=font)
        else:
            draw.text((100, 70), initials ,(255, 255, 255),font=font)
    else:
        img=Image.new("RGBA", (450, 450), (211, 47, 47))
        draw = ImageDraw.Draw(img)
        if initials[0] in ["M"]:
            draw.text((90, 130), initials ,(255, 255, 255),font=font)
        elif initials[0] in ["W"]:
            draw.text((85, 130), initials ,(255, 255, 255),font=font)
        else:
            draw.text((100, 130), initials ,(255, 255, 255),font=font)
    draw = ImageDraw.Draw(img)
    initials_file_path = join(settings.STATICFILES_DIRS[0], "media", "temp", "%s.png" % initials)
    img.save(initials_file_path)
    return HttpResponse(file(initials_file_path, "rb").read(), {"Content-type":"img/png"})
