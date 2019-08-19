import sys
from panflute import *

PYTHON_IO_FILE = "/tmp/eval-python-io"
real_stdout = sys.stdout

exec_env = {}
def execute_code(code):
    f = open(PYTHON_IO_FILE, "w")
    sys.stdout = f
    exec(code, exec_env)
    sys.stdout.close()
    sys.stdout = real_stdout
    f = open(PYTHON_IO_FILE, "r")
    return f.read()

def eval_python(elem, doc):
    if type(elem) == CodeBlock:
        classes = elem.classes
        code_body = elem.text
        if 'python' in classes and "eval" in classes:
            eval_res = execute_code(code_body)
            return [elem, CodeBlock(eval_res)]

run_filter(eval_python)