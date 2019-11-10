# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from typing import Tuple


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment ', data, sep='\n')
        else:
            print('>>> Single-line Comment ', data, sep='\n')

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data ', data, sep='\n')


def html_parser(html: Tuple[str, ...]) -> None:
    parser = MyHTMLParser()
    for row in html:
        parser.feed(row)


if __name__ == '__main__':
    html = tuple(input() for _ in range(int(input())))
    html_parser(html)
