def convertLine(hex):
    result = ""
    temp = hex.split(" ")
    for char in temp:
        #char = codecs.decode(char, "hex").decode('1250')
        char = bytes.fromhex(char).decode("cp852")
        result += " "
        result += char
    return result

import codecs
save = open("output.txt", "w")

readfile = open("input.txt", "r")
line = readfile.readline()
print(line)
while line:
    print(convertLine(line))
    save.write(convertLine(line) + "\n")
    line = readfile.readline()