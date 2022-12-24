#Author - jayspray
#Team - Dillusioners
#Word - same
#Info - This program checks how many times the same character or a group of characters appear in a file
import os
#User Display
print("###########################################################################################################################")
print(" This program is based on data analysis to check how many words include the same character or group of characters in a txt file ")
print("###########################################################################################################################")
#Function wordCount to calculate the answer
def wordCount(word,path):
    #Opening the file
    data = open(path,'r')
    #Initialising counter
    count = 0
    #Setting up a clean array
    clean_array = []
    #Reading all lines and storing them in lines[]
    lines = data.readlines()
    #Going through the list lines[] and cleaning each element up
    for i in range(len(lines)):
        wrd = lines[i]
        clean_array = wrd.split()
        #Then appending cleaned elements in this array
        for j in range(len(clean_array)):
            if word in clean_array[j]:
                count += 1
    #Printing answer
    print("Number of times that word appears in the file is : ",count)

#Loggers for checking for filepath
try:
    location = input("Enter the file name or directory in which the file exists : ")
    #Checking if filepath exists
    if(os.path.exists(location)):
        print("Ok found location!")
        w = input("Enter the word you want to search for : ")
        #Checking if location is a file to avoid error of permission
        isFile = os.path.isfile(location)
        if isFile:
            wordCount(w,location)
        else:
            location = input("Enter the file name with the directory now for verification: ")
            #Checking if filepath exists
            if(os.path.exists(location)):
                #Checking if location is a file to avoid error of permission
                isFile = os.path.isfile(location)
                if isFile:
                    wordCount(w,location)
                else:
                    print("Ok you don't know english as you again added a folder.")
    else:
        print("Directory doesnt exist")
#Just in case some error appears
except Exception as e:
    print("Something went wrong :)\nError is",e)
#Program ends :)