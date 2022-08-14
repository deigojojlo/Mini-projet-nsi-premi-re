
import os

def find_files(filename, search_path):
   result = ""
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result = os.path.join(root, filename)
   return result


a = find_files("puissance 4 shell.py","C:")
name = "puissance 4 shell.py"
path = ""
for i in range(len(a)):
    if a[i:i+len(name)] == name :
        break
    elif a[i] == "\\":
        path += "/"
    else :
        path += a[i]
print(path)



