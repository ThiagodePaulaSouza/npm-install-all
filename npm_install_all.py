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
    package_file = os.getcwd() + '\\' + 'package.json'

    print("\nYou are in "+ os.getcwd())

    if(os.path.isfile(package_file)):
        print("Running npm install --force")
        os.system('npm install --force')
    else:
        print("Cannot find package.json in this directory...")
