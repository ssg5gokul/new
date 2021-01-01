from queue import Queue, Empty
from threading import Thread

class SafeWriter:
    def __init__(self, *args):
        self.filewriter = open(*args)
        self.queue = Queue()
        self.finished = False
        Thread(name = "SafeWriter", target=self.internal_writer).start()  
    
    def write(self, data):
        self.queue.put(data)
    
    def internal_writer(self):
        while not self.finished:
            try:
                data = self.queue.get(True, 1)
            except Empty:
                continue    
            self.filewriter.write(data)
            self.queue.task_done()
    
    def close(self):
        self.queue.join()
        self.finished = True
        self.filewriter.close()

def create(pair,k,val):
    if(k in pair.keys()):
        print("Key already exists")
    else:
        pair[k] = val
    
def delete(pair,k):
    try:
        del pair[k]
    except:
        print("Match not found")

def read(pair,k):
    try:
        print(pair[k])
    except:
        print("Match not found")
    
    

key_value = dict()
x = 1
if(len(key_value) == 0):
    while(x == 1):
        try:
            x = 0
            a = str(input("Enter key :"))
        except:
            x = 1
            print("wrong data type")
        b = dict() 
        data = input('Enter value separated by ":" ') 
        temp = data.split(':') 
        b[temp[0]] = temp[1] 
        


    create(key_value,a,b)
    
    

options = input("Select options among Create/Delete/Read/Exit")
while(options != "Exit"):
    if(options == "Create"):
        a = input("Enter key :")
        b = input("Enter value :")
        create(key_value,a,b)
    elif(options == "Delete"):
        a = input("Enter key :")
        delete(key_value,a)
    elif(options == "Read"):
        a = input("Enter key :")
        read(key_value,a)
    else:
        print("Select the correct option")
    options = input("Select options among Create/Delete/Read/Exit")


path = input("Type your storage path : ")
n = 1
while(n != 0):
    n = 0
    try:
        file_open = SafeWriter(path,"w")
    except:
        print("Error")
        n = 1
key_value = str(key_value)      
file_open.write(key_value)
file_open.close()

    
