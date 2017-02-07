def main():
    input = "C# E Db G#\n1\nD E# D A\n-1\n***"
    
    spl = input.split()

    noteStack = []
    for item in spl:
        try:
            transposeAmnt = int(item)
            while len(noteStack) > 0:
                note = noteStack.pop(0)
                transpose(note, transposeAmnt)
            print()
        except ValueError:
            noteStack.append(item)

def transpose(key, amount):
    notemap = ["A", "A#/Bb", "B/Cb", "C/B#", "C#/Db", "D", "D#/Eb", "E/Fb", "F/E#", "F#/Gb", "G", "G#/Ab"]
    for i in range(len(notemap)):
        if key in notemap[i].split("/"):
            print(notemap[(i+amount)%len(notemap)].split("/")[0], end=" ")


main()