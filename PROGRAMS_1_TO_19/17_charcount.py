"""
To  count  total  characters  in  file,  total  words  in  file,  total  lines  in  file  and  frequency  of 
given word in file.
"""
#  IMPORTANT!!! SPECIFY YOUR TEXT FILE LOCATION OR PROGRAM WILL NOT WORK
filename = "C:\YASH\CODE\PYTHON\MMCOE/program17.txt"

# Declare 
num_of_char = 0
num_of_words = 0
num_of_lines = 0 

# COUNT 
with open (filename,"r") as file:
    for line in file:
        wordlist = line.split()
        num_of_lines += 1
        num_of_words += len(wordlist)
        data = line.replace(" ","") # REMOVING SPACES, SO THEY ARE NOT COUNTED AS CHARACTERS 
        num_of_char += len(data)

print("Number of characters are:", num_of_char - 2) # -2 FOR REMOVING \n being counted as characters 
print("Number of words are:", num_of_words)
print("Number of Lines are:", num_of_lines)

# GITHUB: yxsh7
         

     

    