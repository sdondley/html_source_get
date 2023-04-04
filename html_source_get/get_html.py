# get_html.py
import sys

from html_source_get import get_the_html

def main(url=None):
    return(get_the_html(url))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        main(url)
    else:
        main()