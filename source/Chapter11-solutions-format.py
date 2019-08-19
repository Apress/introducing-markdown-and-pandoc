from panflute import *

def format_include(elem, doc):

    if type(elem) == Span:
        if not "out" in elem.classes:
            return elem
        if doc.format not in elem.classes:
            return []
        else:
            return elem.content.list

    if type(elem) == Div:
        if not "out" in elem.classes:
            return elem
        if doc.format not in elem.classes:
            return Null
        else:
            return elem.content.list

run_filter(format_include)
