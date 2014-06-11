echo Setup git for project "dev_setup"
echo First create new repository on github called dev_setup
T:
cd T:\user\dev\Github\dev_setup
git init
git add README.md
git add git_setup.bat
git add .\notepad_appdata\functionList.xml
git commit -m "initial commit with notepad++ function list for python"
git remote add origin https://github.com/acutesoftware/dev_setup.git
git push -u origin master