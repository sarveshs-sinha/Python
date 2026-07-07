#String- is a data type where we use to store text or character in quotes.
#Written in- " " or ''

name = "Sarvesh"
print(type(name))

#Operations- 

#1.Concatenation- means joining two or more string together using (+)

first = "Hello"
second = "World!"
result = first + " " + second
print(result)

#2.Length of string- means total number of characters in string, we use ( len() ) keyword.

q = "Python"
print(len(q))

#3.Indexing- means accessing a specific character from a string using its position, each has a specific position called index.

word = "Python"
print(word[0]) #means it will print 0th index value
print(word[3]) #means it will print 3rd index value
print(word[-1]) #means it will print last index value as it supports negavtive indexing also

#4.Slicing- means getting part of a string by using index position, helps to extract group of character.
#syntax- string[ start : end : jump]
#start is start index begins
#end where slicing stops and we count one minus from given
#jump where we take gap

s = "Sarvesh"
print(s[0:3])
print(s[0:8:2])
print(s[-4:-1]) #negattive slicing

#5.Functions- are built-in method used to perform different operations.

w = "hello world"

#upper()- all letter in capital
print(w.upper())

#lower()- all letter in small
print(w.lower())

#title()- first letter capital
print(w.title())

#capitalize()- frist letter capital of sentence
print(w.capitalize())

#replace()- replaces a word with another
print(w.replace("world", "python"))
