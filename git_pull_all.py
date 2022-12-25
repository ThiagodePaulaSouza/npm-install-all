import os

current_dir = os.getcwd()

dirs = []
ls_inside_dir = [] 
package_file = ''

ls = os.listdir(current_dir)

for i in ls:
    if(os.path.isdir(current_dir + '\\' + i)):
        dirs.append(i)

for j in dirs:
    os.chdir(current_dir + '\\' + j)
    package_file = os.getcwd() + '\\' + '.git'

    print("\nYou are in "+ os.getcwd())
    print(package_file, "é ele")

    if(os.path.isdir(package_file)):
        print("Running git pull")
        os.system('git pull')
    else:
        print("Cannot find .git in this directory...")
