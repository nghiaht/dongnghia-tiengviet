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




# Ghi link ra file text: 'link_vn.txt'
def GhiLinkRaFile(ten_file, set_link):
    with open(ten_file, 'wb+') as f:
        for link in set_link:
            f.write(link + '\n')

def LayLinkCon(link_goc):
    soup = BeautifulSoup( urllib.urlopen(link_goc).read() )
    set_link = set()
    for link in soup.find_all('a'):
        l = str(link.get('href'))
        if l.find('Allpages') == -1 and l.find('/dict/vn_vn') == 0:
            set_link.add(l)
    return set_link
