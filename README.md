# PlatformIO-versioning
Add a compiling versioning to you PlatformIO project

Idea found here and corrected some bugs
(https://stackoverflow.com/questions/56923895/auto-increment-build-number-using-platformio)

1) Make the file src/version.h  
```#define VERSION "0.0.0+0```
2) Put this in a source file  
```#include "version.h"```
3) Add the autoincrement.py file in the project root
4) In platformio.ini, add this to your device  
```extra_scripts = post:autoincrement.py```

This will generate variables than can be recalled :  
#define VERSION "0.0.1+68"  
#define VERSION_MAJOR 0  
#define VERSION_MINOR 0  
#define VERSION_PATCH 1  
#define VERSION_BUILD 68  
#define VERSION_DATE "2022-11-27"  
#define VERSION_TIME "23:35"  
#define VERSION_FULL "0.0.1+68 2022-11-27 23:35"  

END
