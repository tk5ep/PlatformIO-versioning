# PlatformIO-versioning
### Purpose :  
Add a versioning number to your PlatformIO project, following the Semantic Versioning (SemVer) rules :  
MAJOR.MINOR.PATCH  
  
### Usage :  
At each compiling, the patch version increments by one.  

If the minor field is changed, the patch is reset to 0.  
If the major field is changed, the minor and patch versions are reset to 0.  
The minor and major changed can be made by hand, editing the first line of the **version.h** file or by running the script:   

Increment Patch (Bugs correction) :  
```python autoincrement.py```  
(Ex: 1.1.5 → 1.1.6)  

Increment Minor (New functionality) :  
```python autoincrement.py --minor```  
(Ex: 1.1.5 → 1.2.0)  

Increment Major (Major change) :  
```python autoincrement.py --major```  
(Ex: 1.1.5 → 2.0.0) 

Displaying the version is done by running the script with --get parameter :  
```python autoincrement.py --get```  

### Install:    
1) In your /src folder, create a file **version.h** containing the following line (or copy the one in this repository).  
```#define VERSION "0.1.0"```  
Or if you have already started your project without a versioning, write your actual version guess, like 1.0.0 for example.  
Or simply, the script automatically generates an initial version (0.1.0) if no file is found in /src during the first compilation.  
  
3) Put this line in the head of your source file :   
```#include "version.h"```
  
4) Add the **autoincrement.py** file in the project root.  
     
5) In **platformio.ini**, add this to your device :  
```extra_scripts = post:autoincrement.py```  
  
### Result :
The file **version.h** will, at each compling, contain the following variables that can be recalled in your scripts.  
    
#define VERSION "0.1.0"  
#define VERSION_MAJOR 0  
#define VERSION_MINOR 0  
#define VERSION_PATCH 0  
#define VERSION_DATE "2026-02-13"  
#define VERSION_TIME "11:28"  
#define VERSION_FULL "0.1.0 2026-02-13 11:28"  

Ex:   Serial.println("Project version: " + String(VERSION_FULL));  
I hope this helps... Let me know.
