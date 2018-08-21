import os,shutil

big_txt = 'txt_files/rank_1000.txt'
out_txt = 'txt_files/family_id.txt'

big_txt_f = open(big_txt)
line = big_txt_f.readline()

out_txt_f = open(out_txt, 'w')

pre_family_id = ''
cur_family_id = ''

counter = 0

while line:
    line = line.rstrip('\n')
    cur_family_id, _ = line.split(',')
    cur_family_id = eval(cur_family_id)
    if cur_family_id != pre_family_id:
        out_txt_f.write(cur_family_id+',')
        pre_family_id = cur_family_id
    line = big_txt_f.readline()
    counter += 1
    if counter % 10000 == 0:
    	print counter
big_txt_f.close()
out_txt_f.close()