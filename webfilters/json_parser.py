import json
from cytoolz import get_in


class JSONParser:

    @staticmethod
    def parse(raw_json, fields, referer_url=None):
        assert fields and raw_json, 'Missing args'
        data = raw_json
        result = {}
        for field in fields:
            selectors = field.get('selector', '').split(',')
            for selector in selectors:
                selector = selector.split('.')
                res = get_in(selector, data)
                if res is not None:
                    break
            result[field.get('name')] = res
        return result

class JSONLDParser:

    @staticmethod
    def parse(raw_message, fields, referer_url=None):
        assert fields and raw_message, 'Missing args'
        data = raw_message['json']
        json_data = json.loads(data)
        return JSONParser.parse(json_data, fields, referer_url)

