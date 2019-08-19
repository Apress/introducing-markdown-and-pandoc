from panflute import *

def solution(elem, doc):
    if type(elem) == Div:

        if 'SOLUTION' not in elem.classes:
            # Return None to leave the node as it is
            return None

        meta = doc.get_metadata()
        if "solutions" not in meta:
            return Null
        if meta["solutions"] != True:
            return Null

        return None

run_filter(solution)
