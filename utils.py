from keras import backend as K

"""
All miscellenous functions are included in here
"""

def PSNR(y_true, y_pred):
    """
    Peak Signal-to-Noise Ratio metric
    """
    max_pixel = 1.0
    return (10.0 * K.log((max_pixel ** 2) / (K.mean(K.square(y_pred - y_true), axis=-1)))) / 2.303