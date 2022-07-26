# program for convertion between words and Morse code
'''
Author:Guo Yingwei
Date  :2019/2/11
E-mail:guoyingwei6@gmail.com
'''

# dict of words2morse
dict1 = {'a':'.-'  ,'b':'-...','c':'-.-.','d':'-.'  ,'e':'.'   ,
         'f':'..-.','g':'--.' ,'h':'....','i':'..'  ,'j':'.---',
         'k':'-.-' ,'l':'.-..','m':'--'  ,'n':'-.'  ,'o':'---' ,
         'p':'.--.','q':'--.-','r':'.-.' ,'s':'...' ,'t':'-'   ,
         'u':'..-' ,'v':'...-','w':'.--' ,'x':'-..-','y':'-.--','z':'--..',
         '0':'-----' ,'1':'.----' ,'2':'..---' ,'3': '...--','4': '....-' ,
         '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.' }

# dict of morse2words
dict2 = dict(zip(dict1.values(),dict1.keys()))

def encode():
    
    words = input("Input a sentence you want to endoce,NO PUNCTUATION:").strip().lower()

    for letter in words:
        if letter == ' ':
            print('/',end=' ')
        else:
            print(dict1[letter], end=' ')
    print()

def decode():
    codes = input("Input Morse code you want to decode,ONLY MORSE CODE:").strip().split(" ")

    for sign in codes:
        if sign == '/':
            print(' ',end='')
        else:
            print(dict2[sign], end='')
    print()

    
def main():    
    while 1 == 1:
        choice = input("Encode(Words to Morse codes) or Decode(Morse codes to Words).Plase input [0/1]")

        if   choice == '0':
            encode()
        elif choice == '1':
            decode()
        else:
            break

if __name__=="__main__":
    main()
    
