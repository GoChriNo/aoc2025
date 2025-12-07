from aoutils import *

lines = get_lines("problems.txt")
lines_splitted = get_lines_splitted("problems.txt")



class Equation:
    def __init__(self):
        self.values = []
        self.starts = []
        self.operator = "+"

    def add_value(self, value, start):
        self.values.append(value)
        self.starts.append(start)
    
    def set_operator(self, operator):
        self.operator = operator

    def calculate(self):
        if self.operator == "+":
            return self.add()
        elif self.operator == "*":
            return self.mul()
        else:
            raise ValueError(f"{self.operator} not supported")
        
    
    def alter_values(self):
        last_end = self.starts[0]
        first_start = self.starts[0]
        for value, start in zip(self.values, self.starts):
            end = start + len(str(value))
            if start < first_start:
                first_start = start
            if end > last_end:
                last_end = end

        altered_values = []

        for i in range(first_start, last_end):
            current_value = ""
            for value, start in zip(self.values, self.starts):
                current_start = start
                current_end = current_start + len(str(value)) - 1
                if i >= current_start and i <= current_end:
                    current_value += str(value)[i - current_start]
            altered_values.append(int(current_value))

        self.values = altered_values
        print("alt", self.values)


    def mul(self):
        final = self.values[0]
        for value in self.values[1:]:
            final *= value
        return final

    def add(self):
        final = 0
        for value in self.values:
            final += value
        return final
            



equations = [Equation() for _ in range(len(lines_splitted[0]))]

for line, lines_splitted in zip(lines, lines_splitted):
    line.append(" ")
    current_equation = 0
    if line[0] not in ["+", "*"]:
        current_number = ""
        current_start = 0
        for i, num in enumerate(line):
            if num in "1234567890" and current_number == "":
                current_start = i
                current_number = num
            elif num in "1234567890" and current_number != "":
                current_number += num
            elif current_number != "":
                equations[current_equation].add_value(int(current_number), current_start)
                current_equation += 1
                current_number = ""
    else:
        for i, op in enumerate(lines_splitted):
            print
            equations[i].set_operator(op)


count = 0
for eq in equations:
    eq.alter_values()
    count += eq.calculate()

print(count)