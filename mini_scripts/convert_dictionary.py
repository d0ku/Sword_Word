import string

name=input("")

allowed_chars=[]
allowed_chars+=string.ascii_lowercase
allowed_chars+=string.ascii_uppercase
allowed_chars+="\n"
with open(name,"r") as dictionary_read:
    with open("converted.txt","w") as dictionary_write:
        temp_string=dictionary_read.read()
        temp=temp_string.split("\n")
        copy=True
        for x in temp:
            for y in x:
                if y not in allowed_chars:
                    copy=False
                    break
            if copy:
                print(x)
                dictionary_write.write(x)
                dictionary_write.write("\n")
            copy=True

        