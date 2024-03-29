#We want to make a row of bricks that is goal inches long. We have a number of small
#bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the
#goal by choosing from the given bricks. This is a little harder than it looks and can be done
#without any loops

def make_bricks(small, big, goal):
  if goal / 5 < big:
    big = goal / 5
  if small + big * 5 >= goal:
    return True
  return False

#Given 3 int values, a b c, return their sum. However, if one of the values is the same as
#another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  return a + b + c

#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does
#not count towards the sum and values to its right do not count. So for example, if b is 13,
#then both b and c do not count.

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  return a + b + c


#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the
#range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a
#teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that
#value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e.
#"decomposition"). Define the helper below and at the same indent level as the main
#no_teen_sum().

# not made

#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit
#is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10
#if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the
#sum of their rounded values. To avoid code repetition, write a separate helper "def
#round10(num):" and call it 3 times. Write the helper entirely below and at the same indent
#level as round_sum().

# not made

#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most
#1), while the other is "far", differing from both other values by 2 or more. Note: abs(num)
#computes the absolute value of a number.

def close_far(a, b, c):
  if(abs(b - a) <= 1 or abs(c - a) <= 1) and (abs(b - a) >= 2 or abs(c - a) >= 2):
    if(abs(b - a) >= 2 and abs(b - c) >= 2) or (abs(c - a) >= 2 and abs(c - b) >=2 ):
      return True
  return False

#We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and
#big bars (5 kilos each). Return the number of small bars to use, assuming we always use
#big bars before small bars. Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  if big > (goal / 5):
    big = (goal / 5)
  if big * 5 + small < goal:
    return -1
  goal = goal - big * 5
  return goal
