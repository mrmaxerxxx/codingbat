#Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  result = ""
  for i in str:
    result = result + 2 * i
  return result

#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  counter = 0
  for i in range(len(str) - 1):
    if str[i:i + 2] == "hi":
      counter += 1
  return counter

#Return True if the string "cat" and "dog" appear the same number of times in the given
#string.

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str) - 2):
    if str[i:i+3]=="cat":
      cat+=1
    elif str[i:i+3]=="dog":
      dog+=1
  if cat==dog:
    return True
  return False

#Return the number of times that the string "code" appears anywhere in the given string,
#except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  counter = 0
  for i in range(len(str) - 3):
    if str[i:i + 2] == "co" and str[i + 3] == "e":
      counter = counter + 1
  return counter

#Given two strings, return True if either of the strings appears at the very end of the other
#string, ignoring upper/lower case differences (in other words, the computation should not
#be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
  a=a.lower()
  b=b.lower()
  if (len(a) >= len(b) and a[len(a) - len(b):len(a)]) == b or (len(a) < len(b) and b[len(b) - len(a):len(b)]) == a:
    return True
  return False

#Return True if the given string contains an appearance of "xyz" where the xyz is not
#directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  if len(str) < 3:
    return False
  if str[0:3] == "xyz":
    return True
  for i in range(len(str) - 3):
    if not str[i] == "." and str[i + 1:i + 4] == "xyz":
      return True
  return False

