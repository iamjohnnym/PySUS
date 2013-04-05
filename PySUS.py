#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import argparse
import sys

class CheckWinUpdates():
    
    def __init__(self):
        #self.file_name = self.parse_arguments()
        self.dict_from_file = self.get_file(self.parse_arguments())
        self.details = {}
        self.parse_file()

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", "-f",
                            help="Insert CSV file to parse lax-winupdate01 results",
                           )
        args = parser.parse_args()
        return args.file

    def get_file(self, file_name):
 
        try:
            dictReader = csv.DictReader(open(file_name, 'rb'), 
                                        delimiter=',')
        except IOError, e:
            print e
            sys.exit(1)

        return dictReader

    def parse_file(self):
        self.details['pending'] = []
        self.details['needing_install'] = []
        self.details['error'] = []

        for row in self.dict_from_file:
            if row['Status'] == 'pending':
                self.details['pending'].append(row)

    def get_pending(self):
        for cnt, name in enumerate(self.details['pending']):
            if name['Status'] == 'pending':
                print name['Host']



if __name__ == '__main__':
    import argparse
    cwu = CheckWinUpdates()
    cwu.get_pending()
