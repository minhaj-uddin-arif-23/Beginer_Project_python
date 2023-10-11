
"""
------   হাতে কলমে শব্দের ডিকশনারি------
"""
# def dictionary():
#     word_dictionary = {
#         "good":"Assalamualaiku everyone,you are fine",
#         "color":"Black , white ,red , green , blue , yellow !!"
#     }
#     while True:
#         word = input("Enter the Word: ")
#         if word in word_dictionary:
#             print(word,":",word_dictionary[word])
#         if word not in word_dictionary:
#           print("you type wrong word! ")

# dictionary()

"""
প্রি ডিকশনারি অটোমেটিক ওয়ার্ড ডিকশনারি করে দেয়

"""
from PyDictionary import PyDictionary
# while True:
#     word = input("Enter your word: ")
dictionary = PyDictionary("blue","egg")
print(dictionary.printMeanings())


