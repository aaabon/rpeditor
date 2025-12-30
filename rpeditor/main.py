from standformatting import *
from uniqueformatting import *
from re import I
'''
THIS FILE RECORDS AND WRITES DOWN TUPPERS + MESSAGES
'''

class Message:
    def __init__(self):
        self.tupper = ""
        self.message = []
    def __len__(self):
        return len(self.message)
        
    def getTupper(self): return self.tupper
    
    def getMessage(self): return self.message
    
    def setTupper(self, name):
        self.tupper = "'''" + name.strip('\n') + ":'''\n"

    def setTupperEmpty(self):
        self.tupper = ""
        
    def setMessage(self, message):
        self.message = message
    
    def addMessage(self, new): 
        self.message.extend([new])
        
def writeMessage(f, message, ):
    # ITSSSS A FULL MESSAGE SO SEND IT IN --------------------------------------
    i = 0

    print("Message writing\n")
    f.write(message.getTupper())
    # INSERT IF/ELSE, CHECK IF FIRST MESSAGE HAS {{BLOCK| THEN SKIP ADDING NEW LINE
    f.write('\n')
                
    for line in message.getMessage(): 
        i += 1
        f.write(f"{line}\n")
        f.write('\n')
        f.write('\n')

    for z in range(2): f.write('\n')
                
    message.setTupperEmpty()
    message.setMessage([])

def main():
    # Get and open file

    message = Message()
    
    print("running main\n")
    # reading text file (in hindsight maybe i should make the text files variables)
    with open("source.txt", 'r') as f:
        data = [line for line in f]
    
    # Write into file with extra lines, new file to preserve original
    with open("rp.txt", 'w') as f:
        j = len(data)
        i = 0
    
        while i < j:
        #getting name of tupper -----------------------------
            if not message.getTupper():
                message.setTupper(data[i])

            elif not data[i].strip('\n'):
                writeMessage(f, message)
            else:
                # its a message so focus on message.setMessage

                # check for unique formatting: CBlock, Code, Small, Header3, Header2, Big, Block
                data[i] = applyunique(data[i])
                # check for standard formatting: italicize, bold, underline, strikethrough
                data[i] = applystandard(data[i])

                message.addMessage(data[i])
            i += 1
            
        writeMessage(f, message)

    print("writing finished")
    f.close()