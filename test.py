#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import argparse


class CheckWinUpdates():

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", "-f",
                            help="Insert CSV file to parse lax-winupdate01 results",
                           )
        parser.parse_args()

    def get_file(self):
        details = {}
        details['pending'] = []
        details['needing_install'] = []
        details['error'] = []
 
        dictReader = csv.DictReader(open('winupdates.4.3.13.small.csv', 'rb'), 
                                     delimiter=',')

        return dictReader

    def parse_file(self):
        for row in dictReader:
            if row['Status'] == 'pending':
                details['pending'].append(row)

        print details



cwu = CheckWinUpdates()
cwu.get_file()
