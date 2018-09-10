# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 20:15:12 2016

@author: zico
"""

number = 5

def func():
    global number
    print number
    number = 10
    print number
func()
print number
#==============================================================================
# import pickle
# mylist = ["This", "is", 4, 13327]
# # Open the file C:\\binary.dat for writing. The letter r before the
# # filename string is used to prevent backslash escaping.
# myfile = open("C:\\binary.dat", "w")
# pickle.dump(mylist, myfile)
# myfile.close()
# 
# 
# myfile = open("C:\\binary.dat")
# loadedlist = pickle.load(myfile)
# myfile.close()
# print loadedlist
#==============================================================================
#==============================================================================
# import random
# print random.randint(1,100)
#==============================================================================

#==============================================================================
# def passing_example(a_list, an_int=2, a_string="A default string"):
#     a_list.append("A new item")
#     an_int = 4
#     a_string = "abs"
#     return a_list, an_int, a_string
# 
# my_list = [1, 2, 3]
# my_int = 10
# my_string = "12s"
# print passing_example(my_list, my_int, my_string)
# print my_list
# print my_int
# print my_string
#==============================================================================

#sample = [1, ["another", "list"], ("a", "tuple")]
#for i in range(len(sample)):
 #print sample[i]
#print sample[-1]

#mylist = ["List item 1", 2, 3.14,1,5, 7,8]
#print mylist[:]
#print mylist[::2]

#print "This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"}
#print "This is a %(noun)s." % {"noun": "test"}
#==============================================================================
# rangelist = range(10)
# print rangelist
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in rangelist:
#     # Check if number is one of
#     # the numbers in the tuple.
#     print("number:=", number)
#     if number in (3, 4, 7, 9):
#         # "Break" terminates a for without
#         # executing the "else" clause.
#         break
#     else:
#         # "Continue" starts the next iteration
#         # of the loop. It's rather useless here,
#         # as it's the last statement of the loop.
#         continue
# else:
#     # The "else" clause is optional and is
#     # executed only if the loop didn't "break".
#     pass # Do nothing
#==============================================================================

