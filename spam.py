'''
This is like, a trash can of code i stashed here, if youre reading this it means i forgot to remove it OOPS
'''

while i < j:
        #for line in data: 

        #getting name of tupper -----------------------------
                
            if message.getTupper() == "empty":
                #print("Setting Tupper\n")
                message.setTupper(data[i])
                # print(message.getTupper().strip('\n') + " name got!\n")

            elif data[i].strip('\n'):
                # end of message so write message into file and 
                print("END OF MESSAGE\n")
                print("Tupper: ")
                print(message.getTupper())
                print("Message: ")
                print(message.getMessage())
                message.setTupper("empty")
                message.setMessage([])

            else:
                #print("Setting Message\n")
                # its a message so focus on message.setMessage
                
                # run bold/italicize/underline stuff on every line anyways
                data[i] = italicize(data[i])
                data[i] = bold(data[i])
                # check for formatting: CBlock, Code, Small, Header3, Header2, Big, Block
                print("Data: ")
                print(data[i])
                
                # contents.append(data[i])
                # print(contents)

            f.write(data[i])
            f.write("\n")
            i += 1
            

while True:
        pos = string.find(sub, pos)
        if pos == -1: break
        
        if not start: 
            print("starting\n")
            output = output + string[pos:] + "<u>"
            start = 1
        else: 
            output = output + string[pos:] + "</u>"
            
def bold(string):
    # bolds given string and returns new one
    #return replacesymbol(string, "**")

    start = 0
    newstring = ""
    # finding locations of '*' symbol, i is index and c tracks the chars
    for i,c in enumerate(string):
        if "*" == c: 
            if (start == 1): # a previous * was found and so its a **
                newstring += "'''"
                start = 0
            else: start = 1
        else:
            newstring += c
            start = 0
        
    return newstring

#f.write(data[i])
            #f.write("\n")
            #print("iteration: " + str(i) + "\n")