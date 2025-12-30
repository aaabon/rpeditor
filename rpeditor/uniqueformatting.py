
# CBlock, Code, Small, Header3, Header2, Big, Block
'''
EVERYTHING IN THIS FILE ASSUMES EACH FORMAT IS USED AT MOST, ONCE PER MESSAGE
'''

def addBrackets(string, name, symbol):
    # adds {{name| + }}\n to given string, replacing symbols
    newstring = string.replace(symbol, "")
    return "{{" + name + "|" + newstring.strip('\n') + "}}"

def addBracketsStart(string, name):
    # adds {{name| + }}\n to given string that only has symbols at the front
    newstring = string.strip('\n')
    return "{{" + name + "|" + newstring + "}}"

def cblock(string):
    #```text``` -> {{CBlock|text}}
    substr = "CBlock"
    
    if not string.find("```"):
        return addBrackets(string, substr, "```")
    else:
        return string
    
def code(string):
    # `text` -> {{Code|text}}
    substr = "Code"

    if string.find("`") != -1:
        return addBrackets(string, substr, "`")
    else: 
        return string
    
# swaps to addBracketsStart here
def small(string):
    # -# text -> {{Small|text}
    substr = "-# "
    if string.find(substr) != -1:
            newstring = string.replace(substr, "")
            return addBracketsStart(newstring, "Small")
    else:
        return string
    
def header3(string):
    # ### text -> {{Header3|text}}
    substr = "### "
    if string.find(substr) != -1:
            newstring = string.replace(substr, "")
            return addBracketsStart(newstring, "Header3")
    else:
        return string

def header2(string):
    # ## text -> {{Header2|text}}
    substr = "## "
    if string.find(substr) != -1:
            newstring = string.replace(substr, "")
            return addBracketsStart(newstring, "Header2")
    else:
        return string

def big(string):
    # # text -> {{Big|text}}
    substr = "# "
    if string.find(substr) != -1:
            newstring = string.replace(substr, "")
            return addBracketsStart(newstring, "Small")
    else:
        return string

def block(string):
    # adds a blockquote and returns a new string
    substr = "> "
    if string.find(substr) != -1:
            newstring = string.replace(substr, "")
            return addBracketsStart(newstring, "Block")
    else:
        return string

def applyunique(string):
    # applies all above functions in order
    output = ""
    
    output = cblock(string)
    output = code(output)
    output = small(output)    
    output = header3(output)
    output = header2(output)
    output = big(output)
    output = block(output)
    
    return output