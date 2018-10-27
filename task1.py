import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

file = open("allSentences.txt", 'w')
pluralNouns = open("pluralNouns", 'w')

verbCounter = 0
conjCounter = 0

for child in root.findall('text'):
    paragraphs = child.find('paragraphs')
    for paragraph in paragraphs:
        sentences = paragraph.findall('sentence')
        for sentence in sentences:
            if sentence.attrib['id'] == '1':
                text = sentence.find('source')
                tokens = sentence.find('tokens')
                for token in tokens:
                    if token.attrib['id'] == '1':
                        tokens.remove(token)
                new = ET.SubElement(tokens, 'token', {'id': '0', 'text': ''})
                new.text = 'token'
                new.attrib['id'] = "100500"
                new.attrib['text'] = "ura uroki otmenili!!!"
                tokens = sentence.find('tokens')
                for token in tokens:
                    print(token.attrib)

            text = sentence.find('source')
            file.write(text.text + "\n")

            tokens = sentence.find('tokens')
            for token in tokens:
                word = token.attrib['text']
                vs = token.findall('tfr')
                for v in vs:
                    ls = v.find('v')
                    for l in ls:
                        gs = l.findall('g')
                        if gs[0].attrib['v'] == 'NOUN' and gs[len(gs) - 2].attrib['v'] == 'plur':
                            pluralNouns.write(word + "\n")
                        if word == 'может':
                            if gs[0].attrib['v'] == 'CONJ':
                                conjCounter += 1
                            elif gs[0].attrib['v'] == 'VERB':
                                verbCounter += 1

print("as conj: ", conjCounter)
print("as verb: ", verbCounter)
