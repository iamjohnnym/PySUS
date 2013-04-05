#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2


class SPIPhonebook():
    def __init__(self):
        self.user_name = None
        self.results = {}
        self.html = []
        self.fields = {'EMAIL:': '<a href='}

    def getUrl(self, query):
        url = "http://pbot.spimageworks.com/pts/jsp/PhoneDirectory.jsp?" \
                  "photo=off&search={0}" \
                  "&SUBMIT=Go&site=spi&client=spi" \
                  "&proxystylesheet=spi&output=xml_no_dtd".format(query)

        return url

    def getHtml(self, url):
        """
        file_name = open(url, 'r')
        lines = file_name.readlines()
        file_name.close()
        return lines
        """
        response = urllib2.urlopen(url)
        for line in response.readlines():
            for field in self.fields:
                if field in line:
                    self.html.append(line)

    def parseHtml(self, html):
        """
        Parse Html for specific fields, eg: EMAIL: or WORK:, must correspond
        with correct tags, self.fields located in __init__.  Example:

        self.fields = {'EMAIL:': '<a href=', 'WORK:': '</span'}
        
        """
        for line in html:
            for field in self.fields:
                if field in line:
                    result = self.getField(line, field, self.fields[field])
                    if not self.results.has_key(field):
                        self.results[field] = result

    def getField(self, line, field, element):
        """
        so ugly, fix me
        """
        field_start = line.find(field)
        field_start = line[field_start:]
        start = field_start.find(element)
        start_line = field_start[start:]
        start_element = start_line.find('>')
        start_line = start_line[start_element:]
        end_element = start_line.find('<')

        return start_line[1:end_element].strip()
    
    def run(self, user_name):
        self.user_name = user_name
        self.getHtml(self.getUrl(user_name))
        self.parseHtml(self.html)
        return self.results


if __name__ == '__main__':
    pb = SPIPhonebook()
    print pb.run('jmartin')
