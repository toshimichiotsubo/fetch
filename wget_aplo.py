# Batch download from:
# https://vlbi.gsfc.nasa.gov/services/aplo/aplo_eph/
# file name is like vsgd_2015_03.eph

import urllib.request
import urllib.error

y1 = 2010
y2 = 2018

d = "https://vlbi.gsfc.nasa.gov/services/aplo/aplo_eph/"
l = "/home/otsubo/tmp/aplo_eph/"

#
def urlexists(url):
    """Return True if the URL exists.
    Args:
        url: URL
    Returns:
        True if the URL exists.
    """
    ret = False
    try:
        r = urllib.request.urlopen(url)
        r.close()
        ret = True
    except urllib.error.URLError as e:
        ret = False
    except urllib.error.HTTPError as e:
        ret = False
    return ret

#
def main():
    for y in range(y1, y2+1):
        for m in range(1, 13):
            fn = "vsgd_" + "{0:4d}".format(y) + "_" + "{0:02d}".format(m) + ".eph"
            url = d + fn
            print (url, end="")
            if not urlexists: 
                print (" not found")
                continue
            #print (url+"\n")
            f = l + fn
            urllib.request.urlretrieve(url, f)
            print (" downloaded")

if __name__ == '__main__':
    main()
