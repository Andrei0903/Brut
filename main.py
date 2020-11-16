import random

def goot_password_generate(length = 10):
 

  letters = "abcdefgihjklmnopqrstuvwxyz"
  upper_letters = "abcdefgihjklmnopqrstuvwxyz"
  digits = "0123456789"
  symbol = "@#$%^Y&U*("
  alhabet = letters + upper_letters + digits + symbol

  password = ""

  for i in range(length):
    char = random.choice(alhabet)
    password += char

  return (password)


popular_password = """123456
password
12345678
qwerty
123456789
12345
1234
111111
"""
popular_password = popular_password.split('\n')
counter = 0



def bad_password_generator():
  global counter
  password = popular_password[counter]
  
  counter += 1
  if counter >= len(popular_password):
    counter = 0
  
  return password



for i in range(20):
  print (bad_password_generator())



#https://repl.it/@AndreiShantsev/JumboDefiniteBackticks#main.py
