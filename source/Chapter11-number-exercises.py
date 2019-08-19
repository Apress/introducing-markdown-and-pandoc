#!/usr/bin/env python3

import sys


from panflute import *

ex_dict = {}
no_exercise = 1

def collect_numbers(elem, doc):
    global no_exercise
    if type(elem) == Div and \
        "Exercise" in elem.classes:
        if elem.identifier:
            ex_dict[elem.identifier] = no_exercise
        no_exercise += 1

no_exercise2 = 1

def number_exercises(elem, doc):
    global no_exercise2
    if type(elem) == Div and \
        "Exercise" in elem.classes:

        meta = doc.get_metadata()

        if doc.format == "latex":
            exercise_env = "exercises"
            if "exercise_env" in meta:
                exercise_env = meta["exercise_env"]

            if elem.identifier:
                label = r"\label{" + elem.identifier + "}"
            else:
                label = ""

            block = [
                RawBlock(r"\begin{" + exercise_env + "}" +
                            label,
                         "latex"),
                elem,
                RawBlock(r"\end{" + exercise_env + "}",
                         "latex")
            ]
            return block

        level = 1
        if "exercise_header_level" in meta:
            level = int(meta["exercise_header_level"])

        title = [Str("Exercise"),
                 Space,
                 Str(str(no_exercise2))]
        no_exercise2 += 1
        return [Header(*title, level = level,
                classes = elem.classes), elem]

def handle_citations(elem, doc):
    if type(elem) == Cite:
        actual_cite = elem.citations[0]
        identifier = actual_cite.id
        if not identifier.startswith("ex:"):
            return elem

        prefix_text = actual_cite.prefix.list
        prefix_text.extend([Space, Str("exercise")])

        if doc.format == "latex":
            return actual_cite.prefix.list + [
                RawInline(r"~\ref{" + identifier + "}", "latex")
            ]

        if identifier in ex_dict:
            ex_num = ex_dict[identifier]
            prefix_text.extend([
                Space, Str(str(ex_num))
            ])
        return [
            Link(*actual_cite.prefix.list,
            url = "#" + identifier)
        ]

run_filters([
    collect_numbers,
    number_exercises,
    handle_citations
])

