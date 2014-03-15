import urllib
from bs4 import BeautifulSoup
import re
import codecs
pattern1= ur"(Danh từ|Động từ|Đại từ|Trợ từ).+?(?:Đồng nghĩa:)(.*?$)"
pattern2= ur"(?:Đồng nghĩa:)(.*?$)"
p1 = re.compile(pattern1, re.UNICODE | re.DOTALL | re.MULTILINE)
p2 = re.compile(pattern2, re.UNICODE | re.DOTALL | re.MULTILINE)

# Lay tu dong nghia tu mot link
def LayTuDongNghia(link):
    soup = BeautifulSoup( urllib.urlopen(link).read() )

    # Tu goc
    # thuoc the <input id="search" value="..">
    the_input = soup.find('input', id='search')
    tu_goc = the_input.get('value')
    
    # Loai tu, tu dong nghia
    text = soup.get_text()
    result = p2.findall(text)
    
    if len(result) > 0:
        ds_dongnghia = []
        for e in result:
            ds_dongnghia = ds_dongnghia + e.split(',')
        ketqua = u"@{tugoc}\n{dongnghia}\n\n"
        dong_nghia = (','.join(ds_dongnghia)).strip().lower()
        return (tu_goc,ketqua.format(tugoc=tu_goc.lower(),dongnghia=dong_nghia))
    return None

def LayTatCaTuDongNghia(link_file):
    # Tao file du lieu: dongnghiavn.nghia
    with codecs.open('data/dongnghiavn.nghia',encoding='utf-8', mode='a+') as wf:
        # Mo file chua toan bo link
        with open(link_file) as f:
            i = 0
            # Doc tung link
            for line in f.readlines():
                # Tim xem co tu dong nghia trong link khong
                result = LayTuDongNghia(u'http://tratu.soha.vn' + line)
                if result:
                    i += 1
                    print "#",i, result[0]
                    # Neu co ghi vao file
                    wf.write(result[1])
    return True
                
###
### TEST
### 
s = u"""
Danh từ
chỗ, vị trí tạo thành.
Đồng nghĩa: thể, thiên chế
Động từ
đưa cái khác
Đồng nghĩa: thay
Đồng nghĩa: cầm, cố
"""


#mat = p.search(s)

#result = p2.findall(s)
