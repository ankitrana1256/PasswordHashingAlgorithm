import random
import os
import hashlib

jumbled = []
hashfile = []

class operate:
    def __init__(self,word):
        a = list(word)
        l = len(a)
        
        # Salting
        random.sample(a,l)
        random.shuffle(a)
        self.final = ''.join(a)
        jumbled.append(self.final)
        
        # Hashing
        hash_object = hashlib.md5(self.final.encode())
        final_hash = hash_object.hexdigest()
        hashfile.append(final_hash)
    
    def save(self):
        
        # Creating Path
        os.chdir("D:\\Python")
        if not os.path.isdir("ENCODE-DECODE"):
            os.makedirs("ENCODE-DECODE")
            print("Folder Created")
        else:
            print("Folder Found")
        os.chdir("D:\\Python\\ENCODE-DECODE")
        # End path
        
        with open('Data.txt', mode='a') as v:
            v.writelines(word + '-' + self.final + '-' + hashfile[0] + '\n')
            print("Saving Data...")
            print("Successful")
        

word = str(input("Enter the word :"))
obj = operate(word)
obj.save()