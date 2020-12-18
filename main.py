# формирование словаря кода
def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter + 1
    return d

# кодируем слова в буквы   
def encode_val(word):
    list_code = []
    lent = len(word)
   
    d = form_dict() # получаем словарь кода
    
    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code
 
# компаратор 2-х списков
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0
    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
 
    return dic  
 
# finish full encode   
def full_encode(value, key):
 
    dic = comparator(value, key)
    print(f'Сравнение {dic}')
  
    lis = []
    d = form_dict()
 
    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis
 
 
    
##### Расшифровка
 
def full_decode(value, key):
 
    dic = comparator(value, key)
    
    print (f'Дешифровка = {dic}')
    d = form_dict() # получаем словарь кода
 
    lis =[]
    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis
    
 
def decode_val(list_in):
 
    list_code = []
    lent = len(list_in)
 
    d = form_dict() # получаем словарь кода
    
    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code
 
 
if __name__ == "__main__":
 
    word = 'python'
    key = 'hello'
    
    print (f'Шифруемое слово: {word}')
    print (f'Ключ: {key}')
    print (form_dict())
    # Закодировали буквы в цифры
    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
 
    print (f'Значение: {value_encoded}')
    print (f'Ключ: {key_encoded}')
 
    # сдвигаем
    shifre = full_encode(value_encoded, key_encoded)
    print (f"Шифр: {''.join(decode_val(shifre))}")
 
    decoded = full_decode(shifre, key_encoded)
    print (f'Список декодирования: {decoded}')
    decode_word_list = decode_val(decoded)
    print (f"Расшифрованное слово: {''.join(decode_word_list)}")