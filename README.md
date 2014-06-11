## Development Environment Backup
Backups of config files and other annoying to reproduce settings


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
				    mainExpr="(?<=#)(?={)"
					displayMode="$functionName">
					<functionName>
						<nameExpr expr="(?<=#)(?={)"/>
					</functionName>
				</function>
			</parser>
```
