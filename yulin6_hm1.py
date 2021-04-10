# -*- coding: utf-8 -*-

# PPHA 30535
# Spring 2021
# Homework 1

# yulin6
# Venessa-19

# Due date: Sunday April 11th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
birthday=[1,9,9,8,1,1,1,9]
for location in range(len(birthday)):
    print ('The value at position',location+1,'is',birthday[location])
#as the location is counted from 0, we should use location+1 to make the sentence readable


# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results.
forward=input("type in a work or phrase:")
forward_big=forward.upper()
#Inconsistencies in case can lead to errors in judgment. Uniform case

import re,string
punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{} '
forward_big_clear=re.sub(r"[%s]+" %punc, "",forward_big)
#the code used to remove the punctuations is cited from the following site.
#the original code can't remove the blank. So, I added blank into it.
#https://blog.csdn.net/haiziccc/article/details/101027675?utm_medium=
#distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearn
#Pai2%7Edefault-1.control&dist_request_id=1330144.8104.16180371869928785&depth_
#1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommend
#FromMachineLearnPai2%7Edefault-1.control

backword=reversed(list(forward_big_clear))
if list(forward_big_clear)==list(backword):
    print("It's a palindrome")
else:
    print("This isn't a palindrome")


# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')
choice_small=choice.lower()
if choice_small in available_vegetables:
    print("you can have the vegetable")
elif choice_small not in available_vegetables:
    print("You've made an invalid choice. Please pick again")


# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".
stood=['Lets','take','a','walk','babe','cuz','we','arent','getting','anysleep','tonight']
map_filter=[l.lower() for l in stood if l[0]=="a" or l[0]=="b"]
print(map_filter)


# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
#reverse double
start_list = [[3],[5],[7],[9],[11],[13]]
[[v*2 for v in sublist] for sublist in reversed(start_list)]


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
dictionary = dict(zip(short_names, long_names))
print (dictionary)