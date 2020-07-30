from pypinyin import pinyin, lazy_pinyin, Style
words = '如果这世界上有任何能够令我不高兴的事情，那必然是因为天空是绿色的'
pinyinout = pinyin(words)

count1 = 0
while count1 < len(pinyinout):
    pinyinout[count1] = "".join(pinyinout[count1])
    count1 += 1

count2 = 0
m = False
nums = '1234'

while count2 < len(pinyinout):
    for letter in pinyinout[count2]:
        if letter == 'ā':
            pinyinout[count2] = pinyinout[count2].replace('ā', 'a')
            pinyinout[count2] = '1' + pinyinout[count2]
        elif letter == 'á':
            pinyinout[count2] = pinyinout[count2].replace('á', 'a')
            pinyinout[count2] = '2' + pinyinout[count2]
        elif letter == 'ǎ':
            pinyinout[count2] = pinyinout[count2].replace('ǎ', 'a')
            pinyinout[count2] = '3' + pinyinout[count2]
        elif letter == 'à':
            pinyinout[count2] = pinyinout[count2].replace('à', 'a')
            pinyinout[count2] = '4' + pinyinout[count2]
        elif letter == 'ē':
            pinyinout[count2] = pinyinout[count2].replace('ē', 'e')
            pinyinout[count2] = '1' + pinyinout[count2]
        elif letter == 'é':
            pinyinout[count2] = pinyinout[count2].replace('é', 'e')
            pinyinout[count2] = '2' + pinyinout[count2]
        elif letter == 'ě':
            pinyinout[count2] = pinyinout[count2].replace('ě', 'e')
            pinyinout[count2] = '3' + pinyinout[count2]
        elif letter == 'ě':
            pinyinout[count2] = pinyinout[count2].replace('ě', 'e')
            pinyinout[count2] = '3' + pinyinout[count2]
        elif letter == 'è':
            pinyinout[count2] = pinyinout[count2].replace('è', 'e')
            pinyinout[count2] = '4' + pinyinout[count2]
        elif letter == 'ū':
            pinyinout[count2] = pinyinout[count2].replace('ū', 'u')
            pinyinout[count2] = '1' + pinyinout[count2]
        elif letter == 'ú':
            pinyinout[count2] = pinyinout[count2].replace('ú', 'u')
            pinyinout[count2] = '2' + pinyinout[count2]
        elif letter == 'ǔ':
            pinyinout[count2] = pinyinout[count2].replace('ǔ', 'u')
            pinyinout[count2] = '3' + pinyinout[count2]
        elif letter == 'ù':
            pinyinout[count2] = pinyinout[count2].replace('ù', 'u')
            pinyinout[count2] = '4' + pinyinout[count2]
        elif letter == 'ō':
            pinyinout[count2] = pinyinout[count2].replace('ō', 'o')
            pinyinout[count2] = '1' + pinyinout[count2]
        elif letter == 'ó':
            pinyinout[count2] = pinyinout[count2].replace('ó', 'o')
            pinyinout[count2] = '2' + pinyinout[count2]
        elif letter == 'ǒ':
            pinyinout[count2] = pinyinout[count2].replace('ǒ', 'o')
            pinyinout[count2] = '3' + pinyinout[count2]
        elif letter == 'ò':
            pinyinout[count2] = pinyinout[count2].replace('ò', 'o')
            pinyinout[count2] = '4' + pinyinout[count2]
        elif letter == 'ī':
            pinyinout[count2] = pinyinout[count2].replace('ī', 'i')
            pinyinout[count2] = '1' + pinyinout[count2]
        elif letter == 'í':
            pinyinout[count2] = pinyinout[count2].replace('í', 'i')
            pinyinout[count2] = '2' + pinyinout[count2]
        elif letter == 'ǐ':
            pinyinout[count2] = pinyinout[count2].replace('ǐ', 'i')
            pinyinout[count2] = '3' + pinyinout[count2]
        elif letter == 'ì':
            pinyinout[count2] = pinyinout[count2].replace('ì', 'i')
            pinyinout[count2] = '4' + pinyinout[count2]
        elif letter == 'ǘ':
            pinyinout[count2] = pinyinout[count2].replace('ǘ', 'u')
            pinyinout[count2] = '2' + pinyinout[count2]
        elif letter == 'ǚ':
            pinyinout[count2] = pinyinout[count2].replace('ǚ', 'u')
            pinyinout[count2] = '3' + pinyinout[count2]
        elif letter == 'ǜ':
            pinyinout[count2] = pinyinout[count2].replace('ǜ', 'u')
            pinyinout[count2] = '4' + pinyinout[count2]
    for i in pinyinout[count2]:
        z = i in nums
        if z == True:
            m = True
    if m == False:
        pinyinout[count2] = '5' + pinyinout[count2]
    count2 += 1



print(pinyinout)