import cv2
from PIL import Image
import numpy as np
import io
import urllib
import os

img_web_url = 'http://pic06.babytreeimg.com/2015/0605/FgmBhedh-1ZOitt5sAprpGdYkA-K'
try:
    resp = urllib.urlopen(img_web_url)
    img_bytes = np.asarray(bytearray(resp.read()), dtype = 'uint8')
    img_data = io.BytesIO(img_bytes)
    img = Image.open(img_data)
except Exception as e:
    print img_web_url + ' get failed'
print img_web_url
img_old = np.asarray(img)
print img_old.shape
img_cv = cv2.cvtColor(img_old,cv2.COLOR_RGB2BGR)
cv2.namedWindow("show",0);
cv2.resizeWindow("show", 1280, 960);
cv2.imshow('show', img_cv)
val = cv2.waitKey(0)