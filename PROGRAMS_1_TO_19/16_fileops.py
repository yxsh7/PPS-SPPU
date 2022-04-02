"""
To  copy  contents  of  one  file  to  other.  While  copying
a)  all  full  stops  are  to  be  replaced with  commas  
b)  lower  case  are  to  be  replaced  with  upper  case  
c)  upper  case  are  to  be replaced with lower case.
"""
# IMPORTANT!!! SPECIFY YOUR TEXT FILE LOCATION OR PROGRAM WILL NOT WORK
filename = "C:\YASH\CODE\PYTHON\MMCOE\one16.txt"
try:
    # Open file in read mode
    first = open(filename,"r") 
    # Automatically creates new text file
    second = open("16_two.txt","w")

    for line in first:
        # Replaces fullstop with comma
        line  = line.replace(".",",")
        # Swaps uppercase to lowercase and vice versa
        line = line.swapcase()
        # Writes it to second.txt
        second.write(line)
        print("done")
except:
    ("Error")

# GITHUB: yxsh7
