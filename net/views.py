from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy as np
from .bbox_util import *
from .data_aug import *
from .iouCO import *

def index(request):
    return render(request, 'index.html')

def detect(imagen):
    
    model = load_model("modelo3", custom_objects={'iou_loss': iou_loss, 'iou_metric': iou_metric})

    img = cv2.imread(imagen)[:,:,::-1]
    img_ = Resize(225)(img.copy(), np.zeros((4,4)))[0]

    predictions = model.predict(np.array([img_])/255.0)

    plotted_img = draw_rect(img_, np.array([predictions[0]])*225.0, color=[255, 0, 0])
    return plotted_img
