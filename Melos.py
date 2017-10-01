from janome.tokenizer import Tokenizer
import random

lines = []
with open('text.txt', 'r', encoding='UTF-8') as text:
    for line in text:
        lines.extend(line.split('。'))

t = Tokenizer()
my_dict = {}


for line in lines:
    words = t.tokenize(line, wakati=True)
    words_num = len(words)
    for i in range(words_num-1):
        key1 = words[i]
        key2 = words[i+1]
        if key1 not in my_dict:
            my_dict[key1] = {}
            if key2 not in my_dict[key1]:
                my_dict[key1][key2] = 1
            else:
                my_dict[key1][key2] += 1
        else:
            if key2 not in my_dict[key1]:
                my_dict[key1][key2] = 1
            else:
                my_dict[key1][key2] += 1


while True:
    input('Auto Melos?')
    keyword = random.choice(['メロス', 'セリヌンティウス', ])
    sentence = keyword
    for i in range(100):
        if keyword not in my_dict:
            break
        keyword = random.choice(sorted(my_dict[keyword].items(), key=lambda x: x[1])[0:3])[0]
        sentence += keyword
    print(sentence+'。')