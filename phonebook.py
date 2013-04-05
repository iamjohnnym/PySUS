#!/usr/bin/env python

import urllib2


#url = "http://pbot.spimageworks.com/pts/jsp/PhoneDirectory.jsp?photo=on&search=malmela&SUBMIT=Go&site=spi&client=spi&proxystylesheet=spi&output=xml_no_dtd"

#response = urllib2.urlopen(url)

#print response.read()


class SPIPhonebook():
    def __init__(self):
        pass

    def open_url(self, query):
        #file_name = open(url, 'r')
        #lines = file_name.readlines()
        #file_name.close()
        #print lines
        raw_url = "http://pbot.spimageworks.com/pts/jsp/PhoneDirectory.jsp?" +
                  "photo=off&search={0}".format(query) +
                  "&SUBMIT=Go&site=spi&client=spi" +
                  "&proxystylesheet=spi&output=xml_no_dtd"

        print raw_url

    def parse_options(self, args):
        pass

    def parse_html(self, option, element)
        pass




pb = SPIPhonebook()
pb.open_url('FOOOOOOO')
