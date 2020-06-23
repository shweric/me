"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will generate a sentence by laying our a line of words under dictionaries
some_words = ['what', 'does', 'this', 'line', 'do', '?']

#for dictionary"word" in variable "some_words", print dictionary"word" = "some_words"
for word in some_words:
    print(word) #it did the same

#for dictionary"word" in variable "some_words", print dictionary"word" = "some_words"
for x in some_words:
    print(x) #it did the same

#for dictionary"word" in variable "some_words", print dictionary"word" = "some_words"
print(some_words) #printed the statement ['what', 'does', 'this', 'line', do, '?'] instead

#if the int of text in some_words is larger than 3, then print 'some_words contains more than 3 words'
if len(some_words) > 3:
    print('some_words contains more than 3 words') #it printed "some_words contains more than 3 words"

#define usefulFunction(), so when type in usefulFunction(), it prints platform.uname()
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction() #it prints error 
#Traceback (most recent call last):
 # File "<stdin>", line 1, in <module>
 # File "<stdin>", line 7, in usefulFunction
# NameError: name 'platform' is not defined
#>>> def usefulFunction():
#...  print(platform.uname())
#... usefulFunction()
#  File "<stdin>", line 3
#    usefulFunction()
#                 ^
#SyntaxError: invalid syntax
#>>> 
