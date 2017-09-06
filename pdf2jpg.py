#!/usr/bin/python
import cv2
import os
from PIL import Image

pdf_files = []
pwd = os.getcwd()
list_src = os.listdir(pwd)
for files in list_src:
    if os.path.splitext(files)[1] == '.pdf':
        pdf_files.append(files)

for pdf in pdf_files:
    src_file = pdf
    dest_file = src_file[:-4]+'.jpg'
    cmd = 'convert -density 500 %s -quality 100 %s' %(src_file,dest_file)
    os.system(cmd)

    if dest_file:
        img = cv2.imread(dest_file)
        crop_img = img[321:394,728:874]
        cv2.imwrite(dest_file,crop_img)
        im = Image.open(dest_file)
        im = im.resize((80,40),Image.ANTIALIAS)
        im.save(dest_file)
        print 'Successed transform %s to %s.' %(src_file,dest_file)

