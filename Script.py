#Rename files inside the running folder
import os
import re

def main():
    path = r'FILEPATH'
    os.chdir(path)
    for count, filename in enumerate(os.listdir('.')):
        src = path + '\\' + filename
        # newName = filename.replace("[ShaKaw]_","") #replace specific substring
        newName = re.sub("([\(\[]).*?([\)\]])",'',filename, flags=re.DOTALL)#replace string between () or []
        os.rename(src, newName)

if __name__ == '__main__':
    main()