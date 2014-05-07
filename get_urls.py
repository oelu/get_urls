#!/usr/local/bin/python2.7
""" get_urls.py
shows embedded links in websites
Usage:
      get_urls.py (-u <url> | --url <url>)

"""
__author__ = 'olivier'
from docopt import docopt
import re
import requests
import pprint


def get_website_content(url):
    """
    gets content from website using requests
    """
    print "connecting to: " + url
    url = "http://" + url
    r = requests.get(url)
    content = r.text
    return content


def get_urls_in_content(content):
    """
    returns a dict of urls found in content
    """
    urls = re.findall('''http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|
                      [!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+''', content)
    return urls


def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    # assigns docopt argument to url
    url = arguments['<url>']

    content = "\n" + get_website_content(url)
    pprint.pprint(get_urls_in_content(content))

if __name__ == "__main__":
    main()
