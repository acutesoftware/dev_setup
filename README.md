## Development Environment Backup
Backups of config files and other annoying to reproduce settings


### Install Notes (Windows)

Install anaconda with Python 3.6 64bit

Anaconda3-4.3.1-Windows-x86_64.exe
https://repo.continuum.io/archive/Anaconda3-4.3.1-Windows-x86_64.exe



To customise the anaconda command prompt, go to the folder
C:\Users\Duncan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)

Modify the properties of "Anaconda Prompt"
- start in = T:\user\dev\src\python\AIKIF
- buffer size = 140
- font = Lucida Console 12
- colors = blue bg, white fg, opacity85%

Then right click the icon "Anaconda Prompt" and choose Pin to Taskbar



####Notes
If you want to use cx_Oracle use the 32 bit version of Python 3.5 (compat in local env)


To install scipy on Windows use the following script

~~~~
pip install wheel
pip install numpy-1.12.1rc1+mkl-cp36-cp36m-win32.whl
pip install scipy-0.19.0-cp36-cp36m-win32.whl
~~~~

but it is easier to just install anaconda 


##List of Files
###notepad_appdata
####functionList.xml
Contains function list for Python
credit = http://sourceforge.net/p/notepad-plus/discussion/482781/thread/515001cd/

To edit file, press WindowsKey-R, paste "%APPDATA%\notepad++\" and press ENTER

Note - trying to get CSS selectors as a function list - not working so far, but functionList.xml
needs to be edited from the roamingFolder C:\Users\duncan\AppData\Roaming\Notepad++

code so far:
```xml
			<parser id="css_list" displayName="CSS" commentExpr="((/\*.*?\*)/|(//.**$))">
				<function
				    mainExpr="([^\r\n\#,{};]+)(,|\{)"
					displayMode="$functionName">
					<functionName>
						<nameExpr expr="([^\r\n\#,{};]+)(,|\{)"/>
					</functionName>
				</function>
			</parser>
```
