import os
folders=input("The list of folders provided by the client is:").split()
print (folders)

for folder in folders:
    
    try:
        files=os.listdir(folder)
    except FileExistsError:
        print("Please provide the valid file which exists")
        continue
    except FileNotFoundError:
        print("Please provide the valid file because the folder ///  " + folder + "  ///does not exist")
        continue

    print("Below is the files present in the folder:" + folder)
    print(files)

    for file in files:
        print(file)
