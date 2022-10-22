import os
import sys
bing = 'start msedge https://cn.bing.com/search?q='
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
    text_list = sys.argv[1:]
    srh = ''
    for i in text_list:
        srh = srh+i+'+'
    srh = srh.strip('+')
    os.system(bing+srh)