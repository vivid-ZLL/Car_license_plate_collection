#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/3 23:50
# @Author  : vivid-ZLL
# @File    : car_card.py

import urllib,urllib2
import random
import os
import sys
import string

reload(sys)
sys.setdefaultencoding('utf8')

start_page_url = 'http://minicarmuseum.com/platecreate.php?#mihon'
second_page_1_url = 'http://minicarmuseum.com/pdfoutput.php?plt=w&scn=43&dlc=IZ9PCJUF&frm=0'
second_page_2_url = 'http://minicarmuseum.com/pdfoutput.php?plt=g&scn=43&dlc=IZ9PCJUF&frm=0'
second_page_3_url = 'http://minicarmuseum.com/pdfoutput.php?plt=y&scn=43&dlc=IZ9PCJUF&frm=0'
second_page_4_url = 'http://minicarmuseum.com/pdfoutput.php?plt=b&scn=43&dlc=IZ9PCJUF&frm=0'

form_data = {
    'plate': 'white',
    'plate_clr': 'tokyo_oly1',
    'letter_clr': 'green',
    'gaikigo': 0,
    'fuin': 0,
    'bolt': 0,
    'hoken': 0,
    'romaji': 'SP',
    'bunrui1': 9,
    'bunrui2': 0,
    'bunrui3': 3,
    'hiragana': 'き',
    'number1': 2,
    'number2': 0,
    'number3': 1,
    'number4': 7,
    'number5':'+',
    'text_data2':'',
    'letter_clr2':'black',
    'frame':0,
    'text_data': '八戸',
    'scaleorg':43,
    'action':'ダウンロード',
    'chiikiname':'asahikawa',
}

def Career_B(url1,url2,form):
    career_auto_car = ['あ', 'い', 'う', 'え', 'か', 'き', 'く', 'け', 'こ', 'を']

    for j in range(len(career_auto_car)):
        for i in range(10):
            form['plate'] = 'green'
            num3_string = str(random.randint(0, 1000)).zfill(3)
            num4_string = str(random.randint(0,10000)).zfill(4)
            location_string = form['text_data']
            area_string = career_auto_car[j]
            form['hiragana'] = area_string
            form['bunrui1'] = num3_string[0]
            form['bunrui2'] = num3_string[1]
            form['bunrui3'] = num3_string[2]

            number = string.atoi(num4_string)
            if number == 0:
                form['number1'] = '･'
                form['number2'] = '･'
                form['number3'] = '･'
                form['number4'] = '･'
            elif number > 0 and number < 10:
                form['number1'] = '･'
                form['number2'] = '･'
                form['number3'] = '･'
                form['number4'] = num4_string[3]
            elif number >= 10 and number < 100:
                form['number1'] = '･'
                form['number2'] = '･'
                form['number3'] = num4_string[2]
                form['number4'] = num4_string[3]
            elif number >= 100 and number < 1000:
                form['number1'] = '･'
                form['number2'] = num4_string[1]
                form['number3'] = num4_string[2]
                form['number4'] = num4_string[3]
            else:
                form['number1'] = num4_string[0]
                form['number2'] = num4_string[1]
                form['number3'] = num4_string[2]
                form['number4'] = num4_string[3]


            data = urllib.urlencode(form)
            req = urllib2.Request(url1, data)
            response = urllib2.urlopen(req)
            page = response.read()
            pdf_page = urllib2.urlopen(url2,timeout=300)
            pdf_data = pdf_page.read()
            pwd = os.getcwd()
            folder = os.path.join(pwd,'case4')
            number = str(number).zfill(4)
            filename = '%s-%s-%s-%s.pdf' %(location_string,num3_string,area_string,number)
            filename = os.path.join(folder, filename)
            print filename
            with open(filename, 'wb') as f:
                f.write(pdf_data)
            print 'file saved!'

Career_B(start_page_url,second_page_2_url,form_data)
