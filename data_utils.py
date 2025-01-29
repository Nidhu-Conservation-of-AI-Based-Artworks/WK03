import json
import request

def object_from_json_url(url):
  with request.urlopen(url) as in_file:
    return json.load(in_file)
