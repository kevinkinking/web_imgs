import cv2
from PIL import Image
import numpy as np
import io
import urllib
import os
http_adress = 'http://pic06.babytreeimg.com/'
save_dir = 'family/'
save_img_ext = '.jpg'
qiniu_fun = '?imageView2/2/h/1920'

txt_path_list = [
'txt_files/split/xct',
'txt_files/split/xcu',
'txt_files/split/xcv',
'txt_files/split/xcw',
'txt_files/split/xcx',
'txt_files/split/xcy',
'txt_files/split/xcz',]

for txt_path in txt_path_list:
    lines = []
    with open(txt_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        family_id, img_path = line.split(',')
        img_path = eval(img_path)
        family_id = eval(family_id)
        img_name = img_path.split('/')[-1] + save_img_ext
        img_web_url = http_adress + img_path + qiniu_fun
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
        save_dir_family = save_dir + family_id
        if not os.path.exists(save_dir_family):
            os.makedirs(save_dir_family)
        save_path = os.path.join(save_dir_family, img_name)
        print family_id
        print save_path
        cv2.imwrite(save_path, img_cv)
        # cv2.namedWindow("show",0);
        # cv2.resizeWindow("show", 1280, 960);
        # cv2.imshow('show', img_cv)
        # val = cv2.waitKey(5)
        # if val == 27:
        #     break
