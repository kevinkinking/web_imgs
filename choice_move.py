import os,shutil

imgs_name_txt = '/home/bbt/data/img_100w/img_100w_1/imgs_split/9.txt'
imgs_dir = '/home/bbt/data/img_100w/img_100w_1/imgs_split/imgs_9'
imgs_output_dir = '/home/bbt/data/img_q7_1/imgs9/imgs'

f = open(imgs_name_txt)
counter = 0
line = f.readline()
while line:
    line = line.strip()
    img_path = os.path.join(imgs_dir, line)
    img_output_path = os.path.join(imgs_output_dir, line)
    shutil.copy(img_path,img_output_path)
    line = f.readline()
f.close()