import cv2
from PIL import Image
import numpy as np
import io
import urllib
import os
http_adress = 'http://pic06.babytreeimg.com/'
#http_adress = ''
txt_path = 'txt_files/img_100w_2.txt'
save_dir = 'img_100w_2/'
save_img_ext = '.jpg'

lines = []
with open(txt_path, 'r') as f:
    lines = f.readlines()
saved_imgs = os.listdir(save_dir)
for line in lines:
    line = line.rstrip('\n')
    img_name = line.split('/')[-1] + save_img_ext
    if img_name in saved_imgs:
    	continue
    else:
        img_web_url = http_adress + line
        try:
            resp = urllib.urlopen(img_web_url)
            img_bytes = np.asarray(bytearray(resp.read()), dtype = 'uint8')
            img_data = io.BytesIO(img_bytes)
            img = Image.open(img_data)
            print img_web_url
            img_old = np.asarray(img)
            img_cv = cv2.cvtColor(img_old,cv2.COLOR_RGB2BGR)
        except Exception as e:
            print img_web_url + ' get failed'
            continue
    
    save_path = save_dir + img_name
    print save_path
    cv2.imwrite(save_path, img_cv)
    # cv2.namedWindow("show",0);
    # cv2.resizeWindow("show", 1280, 960);
    # cv2.imshow('show', img_cv)
    # val = cv2.waitKey(5)
    # if val == 27:
    #     break
