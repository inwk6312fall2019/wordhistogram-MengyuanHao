"""This is a program which read a wordlist and find all the rotate pairs. s is how many steps does the letter moves""" 
def rotate_word(letter, s):
 wordlist = open("War and Peace")
   for letter in wordlist:
      if letter.isupper():
         ans = ord('A')
      elif letter.islower():
         ans = ord('a')
      else:
         ans = ord('letter')
    new = ans + (ord('letter') - ans) + n) % 26
    return new
