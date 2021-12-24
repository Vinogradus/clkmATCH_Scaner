import mmap   
import os

signatures = [b'\x25\x65\x63\x68\x6f\x20\x40\x65\x63\x68\x6f\x20\x6f\x66\x66\x3e\x3e\x25\x66\x69\x6c\x65\x25\x0d\x0a\x25\x6c\x25\x65\x63\x68\x6f',
              b'\x6d\x6b\x64\x69\x72\x20\x25\x77\x69\x6e\x64\x69\x72\x25',
              b'\x72\x65\x6e\x20\x25\x66\x69\x6c\x65\x25\x20\x2a\x2e\x62\x61\x74']

def main():  
    filename_array = [] 
    i=0
    
    for root, dirs, files in os.walk(os.getcwd()):
        for file_name in files:
            if file_name != 'scan.py':
                filename_array.append(file_name)
                i+=1
                #print(file_name)

    j=0
    print("Scanning started.") 
    while (j < i):
        with open(filename_array[j], 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:   
            if s.find(signatures[0]) != -1 or s.find(signatures[1]) != -1 or s.find(signatures[2]) != -1:  
                print('File', filename_array[j],"contains a virus!") 
            else:  
                print('File', filename_array[j],"is clear.") 
            j+=1 

main()






