eng_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
massage = input().lower()
new_word = ''
step = int(input())

for i in massage:
    find_place = eng_alphabet.find(i) 
    new_place = find_place + step 
    if i in eng_alphabet:
        new_word +=eng_alphabet[new_place]
    else:
        new_word +=i
        
print(new_word)
