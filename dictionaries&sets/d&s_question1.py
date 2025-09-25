#  Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dict={"kutta":"dog", "paani":"water","kitaab":"book"}

a=input("enter word u want the translation for: ")

print(dict.get(a))

