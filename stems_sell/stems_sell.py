#!/usr/bin/env python3
import fileinput
import re


def match(p, s):
    rules = { 'C':'[^aeiou]', 'V':'[aeiou]', '*':r'\w+'}
    m = re.compile(r'([CV]\d)')
    #*C2ies -> \w+(^aeiou){2,2}ies
    #print(p, '\n', s, '\n')
    print("before: ", s)
    for pattern in p:
        pattern[0] = pattern[0].replace("*", rules["*"])
        x = re.compile(pattern[0])

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