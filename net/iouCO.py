import keras.backend as K

def iou(y_true, y_pred):
    AofT = K.abs(K.transpose(y_true)[2] - K.transpose(y_true)[0] + 1) * K.abs(K.transpose(y_true)[3] - K.transpose(y_true)[1] + 1)
    
    AofP = K.abs(K.transpose(y_pred)[2] - K.transpose(y_pred)[0] + 1) * K.abs(K.transpose(y_pred)[3] - K.transpose(y_pred)[1] + 1)

    overlap_0 = K.maximum(K.transpose(y_true)[0], K.transpose(y_pred)[0])
    overlap_1 = K.maximum(K.transpose(y_true)[1], K.transpose(y_pred)[1])
    overlap_2 = K.minimum(K.transpose(y_true)[2], K.transpose(y_pred)[2])
    overlap_3 = K.minimum(K.transpose(y_true)[3], K.transpose(y_pred)[3])

    intersection = (overlap_2 - overlap_0 + 1) * (overlap_3 - overlap_1 + 1)

    union = AofT + AofP - intersection

    iou = intersection / union

    iou = K.clip(iou, 0.0 + K.epsilon(), 1.0 - K.epsilon())

    return iou 

def iou_metric(y_true, y_pred):
    return iou(y_true, y_pred)

def iou_loss(y_true, y_pred):
    return -K.log(iou(y_true, y_pred))