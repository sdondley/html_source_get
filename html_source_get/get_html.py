# get_html.py
import sys

from html_source_get.html_source_get import get_html

def main(url=None):
    return get_html(url)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        main(url)
    else:
        main()