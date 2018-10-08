import re
import json


def match(string):
    pattern = re.compile(".*({.*})")
    raw_data = pattern.search(string).group(1)
    data = json.loads(raw_data)
    return data
