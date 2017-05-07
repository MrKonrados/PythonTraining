import re

pattern1 = r'i\s'
errors = 0

with open('input.txt', 'r', encoding='utf8') as fin:
    fout = open('output.txt', 'w', encoding='utf8')
    for line in fin:
        if re.search(pattern1, line):
            line = re.sub(pattern1, r'I ', line.rstrip()) + "\n"
            errors += 1
        fout.write(line)
    fout.close()
print('Errors cout: ',errors)