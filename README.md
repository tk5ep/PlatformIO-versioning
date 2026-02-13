# PlatformIO-versioning
Add a compiling versioning to you PlatformIO project

Idea found here and corrected some bugs
(https://stackoverflow.com/questions/56923895/auto-increment-build-number-using-platformio)

1) Make the file src/version.h  
```#define VERSION "0.0.0+0"```
2) Put this in a source file  
```#include "version.h"```
3) Add the autoincrement.py file in the project root
4) In platformio.ini, add this to your device  
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
