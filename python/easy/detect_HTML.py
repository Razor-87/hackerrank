# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from typing import Tuple


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')


def detect_html(html: Tuple[str, ...]) -> None:
    """
    >>> detect_html(('<head>', '<title>HTML</title>', '</head>',
    ... '<object type="application/x-flash"', ' data="your-file.swf"',
    ... ' width="0" height="0">',
    ... ' <!-- <param name="movie" value="your-file.swf" /> -->',
    ... ' <param name="quality" value="high"/>', '</object>'))
    head
    title
    object
    -> type > application/x-flash
    -> data > your-file.swf
    -> width > 0
    -> height > 0
    param
    -> name > quality
    -> value > high
    """
    parser = MyHTMLParser()
    for row in html:
        parser.feed(row)


if __name__ == '__main__':
    html = tuple(input() for _ in range(int(input())))
    detect_html(html)
