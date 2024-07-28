
f = open('filecut.txt', encoding="utf8")

text = f.read()

f = open('split.txt', encoding="utf8")

textTranslate = f.read()

f.close()

textArray = text.split("\n\n")

textTranslate = textTranslate.split("\n")


for i in range(len(textArray)):
    entry = textArray[i].split("\n")
    entry[2] = textTranslate[i].split('_')[1]
    textArray[i] = entry

with open('translated.srt', 'w', encoding="utf8") as f:
    for entry in textArray:
        f.write(entry[0] + "\n" + entry[1] + "\n" + entry[2].strip() + "\n\n")