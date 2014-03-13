import urllib
from bs4 import BeautifulSoup
import pprint

def GetSitemap():

    # Link sitemap
    muc_tieu = 'http://tratu.soha.vn/dict/vn_vn/Special:Allpages'

    # Doc source web muc_tieu
    source = urllib.urlopen(muc_tieu).read()

    # Chuyen vao TV BEAUTIFUL SOUP
    soup = BeautifulSoup(source)

    # Lay link trong source
    # link co dang: <a href="...."></a>
    # Ta can lay: ... trong "href"

    set_links = set()
    for link in soup.find_all('a'):
        set_links.add( link.get('href') )

    # Link phu hop la link xuat phat voi "/dict/vn_vn"
    set_links_vn = set()
    for link in set_links:
        if str(link).find('/dict/vn_vn') == 0:
            set_links_vn.add(link)



file_path = 'data/960.txt'

# Ghi link ra file text: 'link_vn.txt'
def GhiLinkRaFile(ten_file, set_link):
    with open(ten_file, 'a') as f:
        for link in set_link:
            f.write(link + '\n')

def LayLinkCon(link_goc):
    
    
    soup = BeautifulSoup( urllib.urlopen(link_goc).read() )
    set_link = set()
    for link in soup.find_all('a'):
        l = str(link.get('href'))
        if l.find('Allpages') == -1 and l.find('/dict/vn_vn') == 0:
            set_link.add(l)

    GhiLinkRaFile( file_path, set_link)

def LayLinkToanBo(link_file):
    with open(link_file) as f:
        lines = f.read().split('\n')
        for line in lines:
            print "--> Trang: ", line
            LayLinkCon(u'http://tratu.soha.vn' + line)


# Lay tu dong nghia tu mot link
def LayTuDongNghia(link):
    soup = 
