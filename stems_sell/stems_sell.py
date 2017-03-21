#!/usr/bin/env python3
import fileinput
import re
# An exercise in regular expressions
def match(patterns, s):
    m = re.compile(r'([CV]\d)')
    for pattern in patterns:
        p = stemToRegex(pattern[0])
        r = ruleToRegex(pattern[1])
        s = re.sub(p, r, s)
    return s

"""
Converts stem format to regex
"""
def stemToRegex(stem):
    stemsReg = re.compile(r'([C|V])(\d)')
    replacements = {"C" : "([^aeiou])\\", "V": "([aeiou])\\"}
    any = r'(\w+)'
    backref = 1
    if(stem.find('*') > -1):
        stem = stem.replace("*", any)
        backref += 1
    for s in stemsReg.finditer(stem):
        repl = replacements[s.group(1)]
        track = "{"+str(int(s.group(2)) - 1)+"}"
        stem = stem[:s.start(0)]+ repl + str(backref) + track + stem[s.end(0):]
        backref += 1
    return stem

def ruleToRegex(rule):
    return re.sub(r'(\d)', r'\\\1',rule)

def main():
    lineCount = 0
    patterns = []
    sentence  = ""
    expectPattern = True
    for line in fileinput.input(): 
        if line == '\n' or line == '***':
            expectPattern = not expectPattern
            if sentence != "":
                print(match(patterns, sentence), end="***\n")
                patterns = []
                sentence = ""
        elif expectPattern:
            line = line.strip().split(" => ")
            patterns.append(line)
        else:
            sentence += line

if __name__ == "__main__":
    main()