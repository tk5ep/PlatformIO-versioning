# PlatformIO-versioning
Purpose :  
Add a versioning number to your PlatformIO project.  
  
Use :  
At each compiling, the patch version increments by one.  
If the minor field is changed, the patch is reset to 0.  
If the major field is changed, the minor and patch version are reset to 0.  

The minor and major changes can be made by hand, editing the first line of the **version.h** file or by runing the script :   
Increment Patch (Bugs correction) :  
```python autoincrement.py```  
(Ex: 1.1.5 → 1.1.6)  

Increment Minor (New fonctionnality) :  
```python autoincrement.py --minor```  
(Ex: 1.1.5 → 1.2.0)  

Increment Major (Change major) :  
```python autoincrement.py --major```  
(Ex: 1.1.5 → 2.0.0)  

Install:  
1) In your /src folder, create a file **version.h** containing the following line (or copy the one in this repository).  
```#define VERSION "0.1.0"```
  
3) Put this in a source file  
```#include "version.h"```
  
4) Add the **autoincrement.py** file in the project root
     
5) In **platformio.ini**, add this to your device :  
```extra_scripts = post:autoincrement.py```  
  
Result : The file **version.h** will, at each compling, contain the following variables that can be recalled in your scripts.  
    
#define VERSION "0.0.0+4"  
#define VERSION_MAJOR 0  
#define VERSION_MINOR 0  
#define VERSION_PATCH 0  
#define VERSION_BUILD 4  
#define VERSION_DATE "2026-02-13"  
#define VERSION_TIME "11:28"  
#define VERSION_FULL "0.0.0+4 2026-02-13 11:28"  

You can manually edit this file and change the VERSION numbers, for example:  
#define VERSION_ MAJOR 1  

Idea found here  
(https://stackoverflow.com/questions/56923895/auto-increment-build-number-using-platformio)  
But severely reworked to have a versioning like MAJOR.MINOR.PATCH  
END
