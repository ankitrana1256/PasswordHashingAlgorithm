import random
import os
import hashlib

store = []
jumbled = []
hashfile = []

def saltinghashing(x):
    a = list(word)
    random.sample(a,5)
    random.shuffle(a)
    final = ''.join(a)
    jumbled.append(final)
    hash_object = hashlib.md5(final.encode())
    final_hash = hash_object.hexdigest()
    hashfile.append(final_hash)
    
def save():
#To change directory
    os.chdir("D:\\Python")
    if not os.path.isdir("ENCODE-DECODE"):
        os.makedirs("ENCODE-DECODE")
        print("Folder Created")
    else:
        print("Folder Found")
    os.chdir("D:\\Python\\ENCODE-DECODE")
    with open('Data.txt', mode='a') as v:
        v.writelines(word + '-' + hashfile[0] + '\n')
        print("Saving Data...")
        print("Successful")
        

word = str(input("Enter the word :")).upper()
store.append(word)
saltinghashing(word)
save()
