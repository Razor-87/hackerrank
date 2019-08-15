# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from typing import Tuple


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        self.print_attributes(attrs)

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        self.print_attributes(attrs)

    def print_attributes(self, attrs):
        for attr, val in attrs:
            print(f'-> {attr} > {val}')


def html_parser(html: Tuple[str, ...]) -> None:
    """
    >>> html_parser(("<html><head><title>HTML Parser - I</title></head>",
    ... "<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"))
    Start : html
    Start : head
    Start : title
    End   : title
    End   : head
    Start : body
    -> data-modal-target > None
    -> class > 1
    Start : h1
    End   : h1
    Empty : br
    End   : body
    End   : html
    """
    parser = MyHTMLParser()
    for row in html:
        parser.feed(row)


if __name__ == '__main__':
    html = tuple(input() for _ in range(int(input())))
    html_parser(html)
