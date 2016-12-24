from html.parser import HTMLParser
import os

webpage_file = os.path.join('/Users/Zartre/Documents/GitHub/KMITL-ElectiveCourseScanner', '2559_y1_s2.html')

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            print("Encountered a start tag:", tag)
            return tag
    def handle_data(self, data):
        print("Encountered some data  :", data)
    def handle_endtag(self, tag):
        if tag == 'title':
            print("Encountered an end tag :", tag)
#    def handle_data(self, data):
#        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed(open(webpage_file, 'r'))
