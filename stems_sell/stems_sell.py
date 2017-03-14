#!/usr/bin/env python3
import fileinput

def match(p, s):
    print(p, '\n', s, '\n') 

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
            patterns.append(line)
        else:
            sentence += line



main()