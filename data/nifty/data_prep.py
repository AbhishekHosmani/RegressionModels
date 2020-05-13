import os

files_list = os.listdir()
print(files_list)

for item in files_list:
    new_filename = item.replace(' ','_')
    os.rename(item, new_filename)
    print("Filename changed from {} to {}".format(item, new_filename))

print("File modification complete")

