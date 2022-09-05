# -*- coding: utf-8 -*-
"""
1. In cryptography, a Caesar cipher is a very simple encryption” technique in 
    which each letter in the plain text is replaced by a letter some fixed number 
    of positions down the alphabet. For example, with a shift of 3, A would be 
    replaced by D, B would become E, and so on. The method is named after Julius 
    Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 
    places") is a widely used example of a Caesar cipher where the shift is 13. 
    In Python, the key for ROT-13 may be represented by means of the following 
    dictionary:
        Your task in this exercise is to implement an encoder/decoder of ROT-13. 
        Once you're done, you will be able to read the following secret message:
            Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
        In your answer, make sure to deal with non-alpha characters (punctuation, 
        numbers, etc.)
    crypto_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
           'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
           'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
           'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
           'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
           'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
           'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 
2. Create a script that takes a sentence as input, and creates a dictionary with 
    each unique character as a key. The value should be the number of times that 
    character occurs.
    For example, your final dictionary would be similar to this:
        {'W': 1, 'h': 2, 'e': 4, 'n': 2, ' ': 10, 'y': 1, 'o': 5, 'u': 1, 'c': 1, 
         'm': 1, 't': 4, 'a': 3, 'f': 1, 'r': 2, 'k': 2, 'i': 2, 'd': 1, ',': 1, '.': 1}
"""
import time

class AssignmentSix:
    #1 crypto dictionary
    crypto_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
           'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
           'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
           'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
           'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
           'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
           'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 
    secret = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
    message = ""
    for char in secret:
        if(char.isalpha()):
            message += crypto_dict[char]
        else:
            message += char
    print(secret)
    print("Decoding:")
    for x in range (3):
        print(".")
        time.sleep(1)
    print(message)
    
    #2 occurence dictionary
    occDic = {}
    sen = input("Please input a sentence to create an occurence dictionary:\n")
    for char in sen:
        char = char.capitalize()
        if char in occDic:
            occDic[char] += 1
        else:
            occDic[char] = 1
    print(occDic)
    
    input("Press enter to exit")
