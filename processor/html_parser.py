import bs4
import re
from url_normalize import url_normalize
from urllib.parse import urlsplit

class HTMLParser():

    @staticmethod
    def parse(raw_html, fields, referer_url=None):
        assert fields and raw_html, 'Missing args'
        html_soup = bs4.BeautifulSoup(raw_html, 'html.parser')
        result = {}
        for field in fields:
            transform = field.get('transform', None)
            if field['type'] in ['TAGSET']:
                elements = html_soup.select(field.get('selector'))
            else:
                elements = [html_soup.select_one(field.get('selector'))]
            elements = [e for e in elements if e] if elements else []
            parsed_values = set()
            for element in elements:
                # get content if the selector is meta tag, else get cleaned text
                # get content attribute if meta tag, else get text
                if element.name in ['meta']:
                    parsed_value = element.get('content')
                else:
                    parsed_value = element.get('content') if element.get('content') else element.text

                if parsed_value:
                    # cleanup the parsed value by removing whitespaces
                    parsed_value = ' '.join(parsed_value.split())
                    if transform is not None:
                        regex_pattern = re.compile(transform)
                        matches = regex_pattern.match(parsed_value)
                        try:
                            parsed_value = matches.group(1)
                        except:
                            pass
                    parsed_values.add(parsed_value)

            result[field.get('name')] = ', '.join(parsed_values) if parsed_values else None
            # Normalize the urls
            if field.get('name') == 'url' and result.get('url'):
                result['url'] = url_normalize(result['url'])
            # convert relative urls to urls with prototypes for thumbnails
            if field.get('name') == 'thumbnail' and result.get('thumbnail'):
                thumbnail = result['thumbnail']
                relative_pattern = re.compile('^\/.*')
                if relative_pattern.match(thumbnail):
                    scheme = urlsplit(referer_url).scheme
                    result['thumbnail'] = "{}:{}".format(scheme, thumbnail)

        return result

