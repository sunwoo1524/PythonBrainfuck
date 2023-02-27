from time import sleep

class Brainfuck:
    def __init__(self, code, memory_size):
        self.code = code
        self.memory = [0] * memory_size
        self.pointer = 0
        self.brackets = {}
    
    def getBracketsPos(self):
        count = 0
        stack = []

        while count < len(self.code):
            chr = self.code[count]

            if chr == "[":
                stack.append(count)
            elif chr == "]":
                if len(stack) == 0:
                    print(f"예상치 못한 토큰 ']' 줄 {count}")
                    return True
                else:
                    front_bracket = stack.pop()
                    self.brackets[front_bracket] = count
            
            count += 1
        
        if len(stack) != 0:
            print(f"예상치 못한 토큰 '[' 줄 {stack[0]}")
            return True
    
    def run(self):
        if self.getBracketsPos():
            return

        count = 0

        while count < len(self.code):
            c = self.code[count]

            if c == ">":
                self.pointer += 1

                if self.pointer >= len(self.memory):
                    print(f"메모리를 벗어났습니다. 줄 {count}")
                    return

            elif c == "<":
                self.pointer -= 1

                if self.pointer < 0:
                    print(f"메모리를 벗어났습니다. 줄 {count}")
                    return

            elif c == "+":
                self.memory[self.pointer] += 1

            elif c == "-":
                self.memory[self.pointer] -= 1

            elif c == ".":
                print(chr(self.memory[self.pointer]), end="")

            elif c == ",":
                self.memory[self.pointer] = ord(input())

            elif c == "[":
                if self.memory[self.pointer] == 0:
                    count = self.brackets[count] - 1

            elif c == "]":
                if self.memory[self.pointer] != 0:
                    for key, value in self.brackets.items():
                        if value == count:
                            count = key - 1
                            break
            
            count += 1#;print(count);print(self.memory[0], self.memory[1], self.memory[2])
