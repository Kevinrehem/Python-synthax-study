def count_vowels_and_consonants(text_input):
    answer = [0,0]
    for i in range(len(text_input)):
        if text_input[i] >= 'a' and text_input[i] <= 'z':
            if(text_input[i] in 'aeiou'):
                answer[0]+=1
            else:
                answer[1]+=1
    return answer
        
text_input = input('Digite uma frase: ')
text_input=text_input.lower()
answer = count_vowels_and_consonants(text_input)
print(f'{answer[0]} vogais e {answer[1]} consoantes')