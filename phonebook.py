#!/usr/bin/env python

import urllib2


#url = "http://pbot.spimageworks.com/pts/jsp/PhoneDirectory.jsp?photo=on&search=malmela&SUBMIT=Go&site=spi&client=spi&proxystylesheet=spi&output=xml_no_dtd"

#response = urllib2.urlopen(url)

#print response.read()


class SPIPhonebook():
    def __init__(self):
        pass

    def getUrl(self, query):
        url = "http://pbot.spimageworks.com/pts/jsp/PhoneDirectory.jsp?" \
                  "photo=off&search={0}" \
                  "&SUBMIT=Go&site=spi&client=spi" \
                  "&proxystylesheet=spi&output=xml_no_dtd".format(query)

        return url

    def getHtml(self, url):
        file_name = open(url, 'r')
        lines = file_name.readlines()
        file_name.close()
        return lines
        """
        response = urllib2.urlopen(url)
        return response.read()
        """

    def parseOptions(self, args):
        pass

    def parseHtml(self, html):
        fields = ['EMAIL:']
        for line in html:
            for field in fields:
                if field in line:
                    print line

    def getField(self, line, element):
        pass
        




pb = SPIPhonebook()
#b.open_url('FOOOOOOO')
pb.parseHtml(pb.getHtml('contact.txt'))
