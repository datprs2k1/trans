

f = open('filecut.txt', encoding="utf8")

text = f.read()

f.close()

textArray = text.split("\n\n")

x = [textArray[i:i + 150] for i in range(0, len(textArray), 150)]  

for l in range(len(x)):
    textTranslate = ""
    with open('split_' + str(l) +'.txt', 'w', encoding="utf8") as f:
        for i in range(len(x[l])):
            entry = x[l][i].split("\n")
            f.write(entry[0] + '_' + entry[2].strip() + "\n")
