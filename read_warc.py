import urllib.request
import warc

if __name__ == '__main__':

    f = warc.open("test.warc.gz")
    for record in f:
        print (record['WARC-Target-URI'], record['Content-Length'])
