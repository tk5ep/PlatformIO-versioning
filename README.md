# PlatformIO-versioning
Purpose : Add a versioning number to your PlatformIO project.   
  
Idea found here  
(https://stackoverflow.com/questions/56923895/auto-increment-build-number-using-platformio)  

I have corrected some bugs to make it work.  

How to use it :  
  
1) Create a file src/version.h containing or copy the one in this repository.
```#define VERSION "0.0.0+0"```
  
3) Put this in a source file  
```#include "version.h"```
  
4) Add the autoincrement.py file in the project root
     
5) In platformio.ini, add this to your device :  
```extra_scripts = post:autoincrement.py```  
  
The file **version.h** will, at each compling, contain the following variables that can be recalled in your scripts.  
You can manually edit the file and change the VERSION numbers.  
  
#define VERSION "0.0.0+4"  
#define VERSION_MAJOR 0  
#define VERSION_MINOR 0  
#define VERSION_PATCH 0  
#define VERSION_BUILD 4  
#define VERSION_DATE "2026-02-13"  
#define VERSION_TIME "11:28"  
#define VERSION_FULL "0.0.0+4 2026-02-13 11:28"  

END
