import os,shutil

imgs_name_txt = '/home/bbt/data/img_100w/img_100w_2/imgs_name.txt'
imgs_dir = '/home/bbt/data/img_100w/img_100w_2/imgs/'
imgs_output_dir = '/home/bbt/data/img_100w/img_100w_2/imgs_split'
split_num = 34
for i in range(split_num):
    dir_name = 'imgs_' + str(i)
    imgs_output_dir_split = os.path.join(imgs_output_dir, dir_name)
    if not os.path.exists(imgs_output_dir_split):
        os.makedirs(imgs_output_dir_split)
f = open(imgs_name_txt)
counter = 0
line = f.readline()
while line:
    line = line.strip()
    img_path = os.path.join(imgs_dir, line)
    belong = counter % split_num
    dir_name = 'imgs_' + str(belong)
    imgs_output_dir_split = os.path.join(imgs_output_dir, dir_name)
    img_output_path = os.path.join(imgs_output_dir_split, line)
    shutil.move(img_path,img_output_path)
    if counter == split_num * 100:
        counter = 0
        print '100 loop'
    line = f.readline()
    counter += 1
f.close()