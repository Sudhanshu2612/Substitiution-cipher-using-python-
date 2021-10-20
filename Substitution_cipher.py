
import string

def  substitution_encode(alpha,key,str):
    #create list of aplhabet
    alpha_list=[]            
    #slicing to create the list of characters     
    alpha_list[:0] = alpha
    #create array counts to store the index of the characters in string to substitute them later
    counts = []
    #start filling index into counts array 
    for i in str:
        #detecting whitespaces in the string if any 
        #if whitespace is there just append * into list
        if i == " ":
            counts.append("*")
        for j in alpha_list:
            if i == j:
                 counts.append(int(alpha_list.index(j)))
            else:
                pass
    #Creating list of cipher text to store all the conversions one by one 
    cipher_text=[]
    for n in counts:
        #if * replace with white space
        if n == '*':
            cipher_text.append(" ")
        else:
            #substituing from the key
            cipher_text.append(key[n])
    #join the cipher text list as a one string
    cipher = ''.join(cipher_text)
    #return the final string
    return cipher


#decoding is very similar to the encoding instead of splliting the alpha array we will split the key array
def  substitution_decode(alpha,key,cipher):
    key_list=[]
    #exact same as above splliting with slice
    key_list[:0] = key
    counts = []
    #same as the process of encoding just vice-versa
    for i in cipher:
        if i == " ":
            counts.append("*")
        for j in key_list:
            if i == j:
                 counts.append(int(key_list.index(j)))
            else:
                pass 
    #original text list
    original_text=[]
    for n in counts:
        if n == '*':
            original_text.append(" ")
        else:
            original_text.append(alpha[n])
    #joining list to print it as a string
    original = ''.join(original_text)
    return original

#callig the functions and printing the outputs 
#Driver code
cipher_text = substitution_encode('abcdefghijklmnopqrstuvwxyz','bpzhgocvjdqswkimlutneryaxf','it was a  dark and stormy night')
print("Your cipher text is : {}".format(cipher_text))
original_message= substitution_decode('abcdefghijklmnopqrstuvwxyz','bpzhgocvjdqswkimlutneryaxf','jn ybt b hbuq bkh tniuwx kjcvn')
print("Original message is :{}".format(original_message))