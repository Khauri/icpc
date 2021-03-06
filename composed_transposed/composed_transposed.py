#!/usr/bin/env python3
import fileinput
#V2 - Now with much less cheese
def main():
    queue = []
    expectInt = False
    for line in fileinput.input():
        if line != "***":
            if expectInt == True: # if int discovered output transposition
                transposeAmnt = int(line)
                while len(queue) > 0:
                    note = queue.pop(0)
                    print(transpose(note, transposeAmnt, False), end=" ")
                print()
            else:
                queue = line.split()
        else:
            exit()
            # if we know every 2nd line is a number, then we can alternate checking and not checking for an integer
        expectInt = not expectInt

def transpose(note, amount, preserve = True):
    notemap = [["A"], ["A#","Bb"], ["B","Cb"], ["C","B#"], ["C#","Db"], ["D"], ["D#","Eb"], ["E","Fb"], ["F","E#"], ["F#","Gb"], ["G"], ["G#","Ab"]]
    for i in range(len(notemap)):
        if note in notemap[i]:
            newNote = notemap[(i+amount)%len(notemap)]
            return newNote[1] if "b" in note and len(newNote) > 1 and preserve is True else newNote[0]

if __name__ == "__main__":
    main()