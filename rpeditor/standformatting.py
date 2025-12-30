import re

# Strikethrough, underline, bold, italicize
'''
THESE FUNCTIONS REPLACE DISCORD FORMATTING WITH WIKI ONES
'''

def replacechar(string, sub, char):
    # replaces given substring (sub) with char in wiki format (so like <char></char>)
    output = ""
    openbracket = '<' + char + '>'
    closebracket = '</' + char + '>'
    
    output = string.replace(sub, openbracket, 1) #this is to start things off
    output = output.replace(sub, closebracket, 1)
    while True:
        # this is to catch any other chars in message
        loopbreak = output.find(sub)
        if loopbreak == -1: break
        output = output.replace(sub, openbracket, 1)
        output = output.replace(sub, closebracket, 1)
    return output

# THESE ARE "STUPID" METHODS SINCE THEY DON'T ACCOUNT FOR SINGULAR SYMBOLS
def strikethrough(string):
    # replace ~~word~~ with <s>word</s>
    return replacechar(string, "~~", 's').strip('\n')

def underline(string):
    # replace __word__ with <u>word</u>
    return replacechar(string, "__", 'u').strip('\n')

def bold(string):
    # bolds given string and returns new one
    #return replacesymbol(string, "**")
        
    return string.replace("**", "'''").strip('\n')

def italicize(string):
    # italicizes given string and returns new one
        
    return string.replace("*", "''").strip('\n')

def applystandard(string):
    # applies all above functions in correct order
    output = ""
    output = bold(string)
    output = italicize(output)
    output = underline(output)
    output = strikethrough(output)
    return output