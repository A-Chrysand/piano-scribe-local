import urllib.request
import numpy as np
va = [7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95, 103, 111, 119, 127]
pa = np.arange(21, 109)

url = []
for v in va:
    for p in pa:
        url.append('https://storage.googleapis.com/magentadata/js/soundfonts/salamander/acoustic_grand_piano/p%s_v%s.mp3' % (p, v))
b = []

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17")]
urllib.request.install_opener(opener)

while True:
    for u in url:
        print (u)
        try:
        #if True:
            urllib.request.urlretrieve(u)
        except:
            b.append(u)
            print ('eee...')
            continue
    u = b