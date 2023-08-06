# 1. Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s 
# (кроме переменной из одной буквы s) на None. 
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

variables_dict = {'mas': 35,
                  'ops': 56,
                  'asd': 75,
                  'max': 567,
                  's': 13,
                  'sums': 324,
                  }

def replace_s(variables_dict):
    word = None
    word_with_s = []
    for key in variables_dict:
        word = list(key)
        if word[-1] == 's' and len(word) > 1:
            word_with_s.append(key)

    temp = None
    variables_dict_new = {}
    for key, value in variables_dict.items():
        for i in word_with_s:
            if key == i:
                temp = value
                variables_dict[key] = None
                variables_dict_new[i[:-1:]] = temp
    
    variables_dict_res = variables_dict | variables_dict_new
    return variables_dict_res
                
        
print(replace_s(variables_dict))