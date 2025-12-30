
# CBlock, Code, Small, Header3, Header2, Big, Block

def block(string):
    # adds a blockquote and returns a new string
    return "{{Block|" + string[1:] + "}}"

def applyunique(string):
    # applies all above functions in order
    output = ""
    
    output = block(string)
    
    return output