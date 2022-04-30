'''
Created on Apr 29, 2022

@author: mathewacarter29

Cryptography Project 4

Group Members: Mathew Carter, Caeden Erickson, Emily Betson, Alyssa Lowe
'''

'''
This method uses the table hexToBin to convert a hexidecimal nibble to its bitwise representation
'''
def convertHexToBin(nibble):
    hexToBin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
            '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
            'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    
    return hexToBin[nibble]


'''
Converts an entire key to its binary representation
'''
def convertKeyToBits(key):
    result = ""
    for nibble in key:
        if nibble == ' ':
            continue
        else:
            result += convertHexToBin(nibble)
        
    #A correct key will have length 64
    assert(len(result) == 64)
    return result

'''
This method will permute the key based on the permutation array
'''
def permute(keyBits, permutationArray):
    result = ''
    for pos in permutationArray:
        result += keyBits[pos - 1]
        
    return result

'''
Prints a human friendly version of a series of bits
'''
def makeReadable(keyBits):
    result = ''
    for i in range(0, len(keyBits), 4):
        result += keyBits[i : i + 4] + ' '
        
    return result
    
'''
Function to loop a given key

loop(abcde, 2) --> cdeab
'''
def loop(key, loopAmount):
    return key[loopAmount:] + key[:loopAmount]


'''
Contains the main code for this program

This code generate three sets of round keys for the three given keys
'''
def main():
    
    #Three given keys
    k1 = '1F1F 1F1F 0E0E 0E0E'
    k2 = 'FE01 FE01 FE01 FE01'
    k3 = 'FAB9 D5B8 CAB7 CBA6'
    
    keys = [k1, k2, k3]
    
    #This value is from the slides -- used to test functions    
    #test = '0010010101100111110011011011001111111101110011100100000000101010'
    
    #Permutation for finding c(n)
    C = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 
         51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
    
    #Permutation for finding d(n)
    D = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61,
         53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    
    #The loop values for each round of the key schedule as given in the slides
    loopTable = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    #Permutation for permutation choice 2
    pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 
           16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33,
           48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    
    for i in range(len(keys)):
        key = keys[i]
        keyBits = convertKeyToBits(key)
        print('Key ', i + 1, ': ', makeReadable(keyBits), sep = '')
        
        c = permute(keyBits, C)
        print('c(0): ', makeReadable(c), sep = '')
    
        d = permute(keyBits, D)
        print('d(0): ', makeReadable(d), sep = '')
        
        for i in range(len(loopTable)):
            loopAmount = loopTable[i]
            c = loop(c, loopAmount)
            d = loop(d, loopAmount)
            
            combine = c + d
            roundKey = permute(combine, pc2)
            print('Round key ', i + 1, ': \t', makeReadable(roundKey), sep = '')
        print()

if __name__ == '__main__':
    main()