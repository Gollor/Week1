import os
import random
from shutil import copyfile


in_path = '/bstorage/lalafo2/files/'
out_path = '/bstorage/course/week1/classifieds/'

test_dir = out_path + 'test/'
if not os.path.isdir(test_dir):
    os.makedirs(test_dir)

nd = 0
tf = 0

test_total = []
dirs = os.listdir(in_path)
dirs.sort()

for d in dirs:
    files = os.listdir(in_path + d)

    if len(files) >= 600:
        new_dir = out_path + str(nd) + '_' + d + '/'
        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)

        random.shuffle(files)

        test_files = files[:100]
        train_files = files[100:1000]

        for fn in train_files:
            copyfile(in_path + d + '/' + fn, new_dir + str(tf) + '.jpg')
            tf += 1

        for fn in test_files:
            test_total.append({'c': str(nd) + '_' + d, 'fn': in_path + d + '/' + fn})

        print('%s %s' % (len(train_files), nd))

        nd += 1


random.shuffle(test_total)

with open(out_path + 'labels.txt', 'w') as f:
    for i, a in enumerate(test_total):
        copyfile(a['fn'], test_dir + str(i) + '.jpg')
        f.write('%s %s\n' % (i, a['c']))
