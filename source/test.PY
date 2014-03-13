# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

test = ""
sub = u"Đồng nghĩa"
alo = ""
with open('an.htm') as f:
    doc = BeautifulSoup(f.read())
    s = doc.getText()
    vitri_batdau = s.find(sub)
    vitri_xuonghang = s.find("\n\n",vitri_batdau)
    chuoi_kq = s[vitri_batdau:vitri_xuonghang]
    print chuoi_kq



#s = s.decode('utf-8')
#print type(s)
#print type(sub)

#vitri = s.find(sub)
#print vitri

