# -*- coding: utf-8 -*-


def get_attr_number(root) -> int:
    """
    >>> import xml.etree.ElementTree as etree
    >>> xml = "<feed xml:lang='en'>\\n\\t<title>HackerRank</title>\\n\\t"
    >>> xml += "<subtitle lang='en'>Programming challenges</subtitle>\\n\\t"
    >>> xml += "<link rel='alternate' type='text/html' href='http://hackerrank"
    >>> xml += ".com/'/>\\n\\t<updated>2013-12-25T12:00:00</updated>\\n</feed>"
    >>> tree = etree.ElementTree(etree.fromstring(xml))
    >>> root = tree.getroot()
    >>> get_attr_number(root)
    5
    """
    # return etree.tostring(root).count(b'=')
    return sum(len(child.attrib) for child in root.iter())
