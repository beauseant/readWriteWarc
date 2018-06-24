import urllib.request
import warc

if __name__ == '__main__':

    urls = ['https://elpais.com/', 'https://elpais.com/tag/gente/a', 'https://politica.elpais.com/', 'https://elpais.com/internacional/']
    

    f = warc.open("test.warc.gz", "w")

    for u in urls:
        fp = urllib.request.urlopen( u )

        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        
        fp.close()        

        header = h = warc.WARCHeader({"WARC-Type": "response"}, defaults=True)
        header['WARC-Target-URI:'] = u
        
        record = warc.WARCRecord(header, mybytes)
        f.write_record( record )

        

    f.close()


    for u in urls:
        f = warc.open("test_trozos.warc.gz", "a")
        fp = urllib.request.urlopen( u )

        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        
        fp.close()        

        header = h = warc.WARCHeader({"WARC-Type": "response"}, defaults=True)
        header['WARC-Target-URI:'] = u
        
        record = warc.WARCRecord(header, mybytes)
        f.write_record( record )

        f.close()
    
