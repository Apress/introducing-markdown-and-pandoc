from sys import stdin

def main():
	exec_env = {}
    incode = False
    codeblock = []
    for line in stdin:
        print(line, end='')
        if line.startswith("```python"):
            incode = True
            continue
        if incode:
            if line.startswith("```"):
                exec("".join(codeblock), exec_env)
                incode = False
                codeblock = []
                continue
            codeblock.append(line)

if __name__ == "__main__":
    main()
