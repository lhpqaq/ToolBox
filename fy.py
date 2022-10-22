import requests
import random
import json
from hashlib import md5
import sys
import urllib.parse
# Set your own appid/appkey.
appid = ''
appkey = ''

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = 'en'
to_lang =  'zh'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

salt = random.randint(32768, 65536)

def fanyi(query):
    sign = make_md5(appid + query + str(salt) + appkey)
    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    try:
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        for dst in result['trans_result']:
            print(dst['dst'])
    except:
        print('Error')
    # Show response
    #print(type(json.dumps(result, indent=4, ensure_ascii=False)))


def get_cmd_args():
    text_list = sys.argv[1:]
    text_len = len(text_list)
    if text_len == 0:
        return (0, '')
    elif text_len == 1:
        return (1, text_list[0])
    else:
        text = text_list[0]
        for i in range(1, text_len):
            text += ' '+text_list[i]
        return (text_len, text)

if __name__ == '__main__':
    cmdargs = get_cmd_args()
    text = ''
    if cmdargs[0] == 0:
        try:
            while 1:
                src = input()
                fanyi(str(src))
        except KeyboardInterrupt:
            pass
        #print('empty')
    else:
        text = cmdargs[1]
        fanyi(text)