# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s: str):
  if len(s) < 3:
    s
  elif not s.endswith('ing'):
  # elif s[-3:] != 'ing':
    s = s + 'ing'
  else:
    s = s + 'ly'
  return  s

# better solution
  # def verbing(s):
  #   if len(s) >= 3:
  #       if s[-3:] == 'ing':
  #           s += 'ly'
  #       else:
  #           s += 'ing'
  #   return s

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # 'not' in not_bad //return bool
  not_bad = s.find('not')
  bad = s.find('bad')
  exclamationMark = s.find('!')

  if not_bad != -1 and bad != -1 and bad > not_bad and exclamationMark != -1:
    s = s[:not_bad] + 'good' + '!'
  elif not_bad != -1 and bad != -1 and bad > not_bad:
      s = s[:not_bad] + 'good'
  return s
  

# a = ['fups','lol']
# for index, string in enumerate(a):
#   # index
#   string

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  def half_index(x):
      from math import ceil
      return ceil(len(x) / 2)
  halv_A = half_index(a)
  halv_B = half_index(b)
  return a[:halv_A] + b[:halv_B] + a[halv_A:] + b[halv_B:] 


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (prefix + ' got: ' + got + ' expected: ' + expected)


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

main()

# import asyncio
# async def async_demo():
#     print(10)


# asyncio.run(async_demo())
# print(5)
a = ['fups','lol']
for index, string in enumerate(a):
  print(index)
  print(string)

  b = ['fups','lol', 'col']
for  index, string in enumerate(b):
  print(string)