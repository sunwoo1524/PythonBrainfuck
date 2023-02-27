import sys
import brainfuck

MEMORY_SIZE = 32768

dir = sys.argv[1]
file = open(dir, "r", encoding="UTF8")
code = file.readlines()
temp = ""

for s in code:
    temp += s

code = temp

bf = brainfuck.Brainfuck(code, MEMORY_SIZE)
bf.run()
