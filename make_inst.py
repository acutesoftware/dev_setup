# make_inst.py  written by Duncan Murray 15/7/2014
# Script to show the steps to build a windows installer
# for a python program.

"""

Steps to setup environment for Windows installer
1. install Python 3.4

2. install NSIS
http://nsis.sourceforge.net/Download

3. install pynsist
http://pynsist.readthedocs.org/en/latest/
 > pip install pynsist

4. Edit the install sections below and run this script
At the end, a Windows explorer window and the NSIS program 
is launched - drag the installer.nsi into the NSISI program
and an installation file is built

"""

######################################
app_name = "Duncans SQL Generator"
ver = "0.9"
entry = "sql_gen:main"
packages = [] # ['bs4', 'requests']
ext_files = [] # ['LICENSE']
ico = "DJMAPP.ICO" 
license_string = "written by Duncan Murray 2014\nhttp://rem.mit-license.org/" 
######################################

import os
fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "build" + os.sep + "nsis")

def main():
    create_licence(license_string)  # comment out if one already exists
    create_my_script(app_name, ver, entry, packages, ext_files, ico)
    compile_install_script()
    print("Done")

def compile_install_script():
    os.system("python -m nsist installer.cfg")
    os.system("start " + fldr )
    os.system("E:\\apps\\nsis\\NSIS.exe")
    
def create_licence(txt):
    with open("LICENSE", "w") as f:
        f.write(txt + "\n")
    
def create_my_script(appName, ver, entry, packages, ext_files, ico):
    if '\'' in appName:
        print("STOP - you cant have single quotes in the title")
        exit(1)
    with open("installer.cfg", "w") as f:
        f.write("[Application]\n")
        f.write("name=" + appName + "\n")
        f.write("version=" + ver + "\n")
        f.write("# How to launch the app - this calls the 'main' function from the 'myapp' package:\n")
        f.write("entry_point=" + entry + "\n")
        if ico != '':
            f.write("icon=" + ico + "\n")
        f.write("\n")
        f.write("[Python]\n")
        f.write("version=3.4.0\n")
        f.write("\n")
        f.write("[Include]\n")
        f.write("# Importable packages that your application requires, one per line\n")
        if len(packages) > 0:
            f.write("packages = " + packages[0] + "\n")
        if len(packages) > 1:
            for p in packages[1:]:
                f.write("  " + p + "\n")
        f.write("\n")
        f.write("# Other files and folders that should be installed\n")
        if len(ext_files) > 0:
            f.write("files = " + ext_files[0] + "\n")
        if len(ext_files) > 1:
            for ex in ext_files[1:]:
                f.write("  " + ex + "\n")

def create_sample_script():
    with open("installer.cfg", "w") as f:
        f.write("[Application]\n")
        f.write("name=My App\n")
        f.write("version=1.0\n")
        f.write("# How to launch the app - this calls the 'main' function from the 'myapp' package:\n")
        f.write("entry_point=myapp:main\n")
        f.write("icon=myapp.ico\n")
        f.write("\n")
        f.write("[Python]\n")
        f.write("version=3.4.0\n")
        f.write("\n")
        f.write("[Include]\n")
        f.write("# Importable packages that your application requires, one per line\n")
        f.write("packages = requests\n")
        f.write("bs4\n")
        f.write("html5lib\n")
        f.write("\n")
        f.write("# Other files and folders that should be installed\n")
        f.write("files = LICENSE\n")
        f.write("data_files/\n")

main()







