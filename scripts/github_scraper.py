#!/usr/bin/python3

import sys
import getopt
import requests
from bs4 import BeautifulSoup
import re

longest = 0
current = 0
cleandata = []


def main(argv):
    username = ''
    try:
        opts, args = getopt.getopt(argv, "hu:", ["username"])
    except getopt.GetoptError:
        print('github_scraper.py -u <username>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('github_scraper.py -u <username>')
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
    url = 'https://github.com/' + username
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.findAll('rect')
    for i in data:
        c = re.split('"', str(i))
        c_array = [c[3], c[5], c[7]]
        cleandata.append(c_array)
    return_data()


def longest_streak(data):
    longest = 0
    count = 0
    for i in data:
        if int(i[0]) == 0:
            longest = max(count, longest)
            count = 0
        else:
            count += 1
    return longest


longest = longest_streak(cleandata)


def current_streak(data):
    streak = 0
    for i in range(len(data) - 2, -1, -1):
        if int(data[i][0]) == 0:
            return streak
        else:
            streak += 1
    return streak


current = current_streak(cleandata)


def get_longest():
    return longest


def get_current():
    return current


def get_cleandata():
    return cleandata


def return_data():
    print("Longest: " + longest + "\n" + "Current: " + current)
