import string
import sys

""" That module chooses from a 'dictionary' file, only the words, which meet 
    conditions specified below. You can choose input as a program argument, if
    you don't do that, program will ask you for a filename. Converted output
    will be saved to file named 'converted.txt'."""

# Right now, allowed characters are a-Z from English alphabet and digits (0-9) 

allowed_chars=[]
allowed_chars+=string.ascii_lowercase
allowed_chars+=string.ascii_uppercase
allowed_chars+=string.digits

if len(sys.argv)>2:
    print("Usage: python3 convert_dictionary.py file_name")
    sys.exit(1)
elif len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename=input("What is the filename? ")


with open(filename,"r") as dictionary_read:
    with open("converted.txt","w") as dictionary_write:
        file_content=dictionary_read.read()
        temp=file_content.split("\n")
        
        copy=True
        for x in temp:
            for y in x:
                # TODO: This could be done with regex
                if y not in allowed_chars:
                    copy=False
                    break
            if len(x)==0:
                copy=False

            if copy:
                print(x)
                dictionary_write.write(x)
                dictionary_write.write("\n")
            copy=True
