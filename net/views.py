import os
from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy as np

from .utils import get_plot
from .bbox_util import *
from .data_aug import *
from .iouCO import *
from .forms import imgForm
from .models import ImgPredict

def detect(imagen):
    pwd = os.path.dirname(__file__)
    path_img = os.path.abspath(os.path.join(pwd,".."))
    nombre = path_img + f"{imagen}_prediction.jpg"
    model = load_model(pwd + "/modelo3", custom_objects={'iou_loss': iou_loss, 'iou_metric': iou_metric})
    img = cv2.imread(path_img + imagen)[:,:,::-1]
    img_ = Resize(225)(img.copy(), np.zeros((4,4)))[0]
    predictions = model.predict(np.array([img_])/255.0)
    plotted_img = draw_rect(img_, np.array([predictions[0]])*225.0, color=[255, 0, 0])
    return (plotted_img,nombre)

def image(request):
    if request.method == 'POST':
        form = imgForm(request.POST, request.FILES)
        if form.is_valid():
            image = ImgPredict(img_to_p=form.cleaned_data.get('img_to_p'))
            image.save()
            imgF = detect(image.img_to_p.url)
            imgF = get_plot(imgF[0])
            return render(request, 'img.html', {'form': form, 'img': imgF}) 
    else:
        form = imgForm()
    return render(request, 'img.html', {'form': form})
