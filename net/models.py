from distutils.command.upload import upload
from django.db import models

class ImgPredict(models.Model):
    id = models.AutoField(primary_key=True)
    img_to_p = models.ImageField(null=False, blank=False, upload_to="images/")
    