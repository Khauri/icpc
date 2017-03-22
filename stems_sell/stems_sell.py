#!/usr/bin/env python3
# An exercise in regular expressions
import fileinput
import re

"""
Matches a list of pattern-repl lists and modifies a string s to match
"""
def match(patterns, s):
    m = re.compile(r'([CV]\d)')
    for pattern in patterns:
        p, r = stemToRegex(pattern[0], pattern[1])
        s = re.sub(p, r, s, flags=re.IGNORECASE)
    return s

"""
Converts stem format to regex
CONVERSION RULES:
  rule:
    *  => '(\w+)'
    Cn => '([^aeiou])\1{$n-1$}' ; 1 <= n <= 9
    Vn => '([aeiou])\1{$n-1$}' ; 1 <= n <= 9
  replacement:
    n  => '\n' ; 1 <= n <= 9 
"""
def stemToRegex(matchRule, replacement):
    stemsReg = re.compile(r'([C|V])(\d)')
    replacements = {"C" : "[^aeiou]", "V": "[aeiou]"}
    any = r'(\w+)'
    # convert replacement rule
    replacement = re.sub(r'(\d)', r'\\\1', replacement)
    # convert match rule
    backref = 1
    if(matchRule.find('*') > -1):
        matchRule = matchRule.replace("*", any)
        backref += 1
    for s in stemsReg.finditer(matchRule):
        a = "({0})\\{1}{{{2}}}".format(replacements[s.group(1)], str(backref), str(int(s.group(2)) - 1))
        matchRule = matchRule[:s.start(0)]+ a + matchRule[s.end(0):]
        backref += 1
    return [matchRule, replacement]

"""
Reads input from a file, performs matches, prints
"""
def main():
    patterns = []
    sentence  = ""
    expectPattern = True
    for line in fileinput.input(): # read input
        if line == '\n' or line == '***':
            expectPattern = not expectPattern
            if sentence != "":
                # run match algorithm
                print(match(patterns, sentence), end="***\n")
                # reset pattern list and sentence
                patterns = []
                sentence = ""
        elif expectPattern: # collect patterns into patterns list
            line = line.strip().split(" => ") # seperate pattern from replacement rule
            patterns.append(line)
        else:
            sentence += line # collect sentence/paragraph line by line

if __name__ == "__main__":
    main()