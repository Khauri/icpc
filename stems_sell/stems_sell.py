#!/usr/bin/env python3
import fileinput
import re
# An exercise in regular expressions
def match(p, s):
    m = re.compile(r'([CV]\d)')
    for pattern in p:
        r = stemToRegex(pattern[0])
        #print(pattern[0], r)
        for match in r.finditer(s):
            #print(match.group(0))
            s = s[:match.start(0)] + "replacement" + s[match.end(0):]
            print(match.group(0))
        #print('\n')
    #print(s)

"""
Converts stem format to regex
"""
def stemToRegex(stem):
    stemsReg = re.compile(r'([C|V])(\d)')
    replacements = {"C" : "([^aeiou])\\", "V": "([aeiou])\\"}
    any = r'\w+'
    backref = 1
    for s in stemsReg.finditer(stem):
        repl = replacements[s.group(1)]
        track = "{"+str(int(s.group(2)) - 1)+"}"
        stem = stem[:s.start(0)]+ repl + str(backref) + track + stem[s.end(0):]
        backref += 1
    stem = stem.replace("*", any)
    return re.compile(stem)
    
def main():
    lineCount = 0
    patterns = []
    sentence  = ""
    expectPattern = True
    for line in fileinput.input(): 
        if line == '\n' or line == '***':
            expectPattern = not expectPattern
            if sentence != "":
                match(patterns, sentence)
                patterns = []
                sentence = ""
        elif expectPattern:
            line = line.strip().split(" => ")
            patterns.append(line)
        else:
            sentence += line

if __name__ == "__main__":
    main()