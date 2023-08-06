# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии 
# или из документации к языку.

text = "История России насчитывает более тысячи лет, начиная с переселения восточных славян\
         на Восточно-Европейскую равнину в VI—VII веках, впоследствии разделившихся на русских, \
        украинцев и белорусов. История страны разделяется примерно на семь периодов: древнейший \
        (догосударственный) (до конца IX века н. э.) период, период Киевской Руси (до середины XII века), \
        период раздробленности (до начала XVI века), период единого Русского государства (с 1547 года царства) \
        (конец XV века — 1721), период Российской империи (1721—1917), советский период (1917—1991) \
        и новейшая история (с 1991)."

dict_counts = {}
SHOW_LIMIT = 10
new_sorted_dictionary = {}
new_text = text.replace(',', ''). \
                replace('.', ''). \
                replace('!', ''). \
                replace('?', ''). \
                replace('"', ''). \
                replace('-', ''). \
                replace('(', ''). \
                replace(')', ''). \
                lower(). \
                strip()
words_list = new_text.split()
for word in words_list:
    counter = words_list.count(word)
    dict_counts[word] = counter
sorted_values = sorted(dict_counts.values())[::-1]

for i in sorted_values:
    for k in dict_counts.keys():
        if dict_counts[k] == i:
            new_sorted_dictionary[k] = dict_counts[k]

print(list(new_sorted_dictionary.items())[0: SHOW_LIMIT])