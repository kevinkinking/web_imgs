import cv2
from PIL import Image
import numpy as np
import io
import urllib
http_adress = 'http://pic06.babytreeimg.com/'
imgs_path = 'imgs_path.txt'
save_dir = 'imgs/'

lines = []
with open(imgs_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip('\n')
    img_web_url = http_adress + line
    try:
        resp = urllib.urlopen(img_web_url)
        img_bytes = np.asarray(bytearray(resp.read()), dtype = 'uint8')
        img_data = io.BytesIO(img_bytes)
        img = Image.open(img_data)
    except Exception as e:
        print img_web_url + ' get failed'
        print e
    print img_web_url
    img_cv = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
    cv2.namedWindow("show",0);
    cv2.resizeWindow("show", 1280, 960);
    cv2.imshow('show', img_cv)
    val = cv2.waitKey(0)
    if val == 27:
        break
    save_path = save_dir + line + '.jpg'
    cv2.imwrite(save_path, img_cv)