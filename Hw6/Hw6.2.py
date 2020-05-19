# Paripon Thanthong
# Date : 05/15/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/nqJWP6wELnE

from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
from collections import Counter

class Collector(HTMLParser):
    'Collects Hyperlink URLs into a list'

    def __init__(self,url):
        'Initializes parser, the url, and a list'

        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.word_lst = []    # For extended HTMLParser
    def handle_starttag(self, tag, attrs):
        'Collects hyperlink URLs in their absolute format'

        # Extended from HTML Parser
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url , attr[1])
                    # Only Choose this Links specifically
                    if absolute[:86] == 'https://en.wikipedia.org/wiki/DePaul_University_College_of_Computing_and_Digital_Media':
                    #if absolute[:4] == 'http':        # For Crawling more than one website

                        self.links.append(absolute)

    def handle_data(self, data):
        """ Extended Function to overide HTML Parser Collect Word """
        # Extended from HTML Parser
        # Overied this function for collecting word from webpage and store in to a list

        words = data.split()
        for word in words:
            if word.isalpha() == True:      # This is for filtering only alphabet string.
                self.word_lst.append(word.lower())

    def getLinks(self):
        """Get List of Links"""

        return self.links

    def getdata(self):
        """Get List of word"""

        return self.word_lst

def frequency(lst):
    """ Count repeated Word (Frequency of Word) """

    count = dict()
    for word in lst:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

def analyze(url):
    """Analyze Function Calling Class Collector Extended from HTML Parser"""

    #Note : Using the function to count repeated words and sorted by value

    print('\n\nVisiting',url)
    print('The most 25 common word')
    print('\n{:30} {:6}\n'.format('Word','Count'))

    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()

    words_lst = collector.getdata()
    print(words_lst)
    # word_count = Counter(words_lst)  # use collection
    # most_25_common = word_count.most_common(25) #

    word_count = frequency(words_lst)
    sorted_word_count = sorted(word_count.items(), key = lambda x : x[1],reverse= True)

    for word,count in sorted_word_count[:25]:
        print ('{:30}{:5}'.format(word,count))

    #return word_count

    # for word,count in most_25_common:
    #     print('{:30} {:5}'.format(word,count))
    # return urls


### This won't work because I set the class to only read one page with specific len of str.
visited = set()
def crawl2(url):
    """Web Crawler"""

    global visited
    if len(visited) >30:
        return
    visited.add(url)

    links = analyze(url)

    for link in links:
        if link not in visited:
            try:
                crawl2(link)
            except:
                pass

def main():
    url = 'https://en.wikipedia.org/wiki/DePaul_University_College_of_Computing_and_Digital_Media'

    analyze(url)
    # print(crawl2(url))

if __name__ == '__main__':
    main()



