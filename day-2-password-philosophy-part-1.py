import re

lines = [re.split('[-\: ]', l.strip()) for l in open('day-2-input.txt','r')]
print(lines)