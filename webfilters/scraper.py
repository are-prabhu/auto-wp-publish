from html_parser import HTMLParser
import urllib.request
from itertools import filterfalse

import lxml.html

fields = [{'name': 'url',
         'selector': "meta[name='referrer']",
         'type': 'TAGSET'},
        {'name': 'description',
         'selector': 'meta[property="og:description"]',
         'type': 'TEXT'},
        {'name': 'description',
          'selector': 'meta[name:"title"]',
          'type': 'TEXT'},
        {'name': 'language',
         'selector': "meta[property='og:locale']",
         'type': 'TEXT'},
        {'name': 'url',
         'selector': 'meta[property="og:url"]',
         'type': 'TEXT'},
        {'name': 'resource-type',
         'selector': "meta[property='og:type']",
         'type': 'TAGSET'},
        {'name': 'thumbnail',
         'selector': 'meta[property="og:image"]',
         'type': 'TEXT'},
        {'name': 'category',
         'selector': 'meta[property="article:section"]',
         'type': 'TEXT'},
        {'name': 'title',
         'selector': 'meta[property="og:title"]',
         'transform': '(.*) \\| EXAME.com - Negócios, economia, tecnologia e carreira',
         'type': 'TEXT'},
        {'name': 'keywords',
         'selector': 'meta[name="keywords"]',
         'type': 'TAGSET'},
        {'name': 'link',
          'selector': '.storylink',
          'type': 'TEXT'},
        {'name':  'paragraphs',
          'selector': '.story-body__list-item',
           'type': 'TEXT'},
         ]


def ArticleURL(url):
    connection = urllib.request.urlopen(url).read()
    parser = HTMLParser()
    parsed = parser.parse(connection,fields)
    print(parsed)
    return parsed

ArticleURL("http://www.wpbeginner.com/wp-themes/how-to-remove-the-sidebar-in-wordpress/")

'''
excludes = ['youtube.com', 'facebook.com', 'linkedin.com','twitter.com','flipboard.com','google.com', 'stumbleupon.com','itunes.apple.com','oath.com','flipboard.com','privacy.aol.com','apps.microsoft.com','tumblr.com','jp.','pinterest.com']

includes = ['http://','.com','https://']

dom = lxml.html.fromstring(connection.read())
dom = dom.xpath('//a/@href')
validdoms=[]
invaliddoms=[]

for inc in includes:
    valid =[x for x in dom if str(inc) in str(x)]
    for val in valid:
        validdoms.append(val)

for exc in excludes:
    invalid=[y for y in dom if str(exc) in str(y)]
    for inv in invalid:
        invaliddoms.append(inv)

validdom=list(set(validdoms) - set(invaliddoms))

for allink in validdom:
    try:
        with urllib.request.urlopen(allink) as url:
            raw_html = url.read()
            parser = HTMLParser()
            parsed = parser.parse(raw_html,fields)
            print (parsed)      
    except urllib.error.HTTPError or urllib.error.URLError:
        pass

'''






