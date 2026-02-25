# Manual PlatformIO versioning 
### Purpose :  
Add a versioning number to your PlatformIO project, following the Semantic Versioning (SemVer) rules :  
MAJOR.MINOR.PATCH  
  
### Install:    
1) Add the **rename_firmware.py** file in the project root directory.  
     
2) In **platformio.ini**, add the following to your device :  
```
build_flags =   
    -D VERSION_MAJOR=0  
    -D VERSION_MINOR=1  
    -D VERSION_PATCH=0  
extra_scripts = pre:rename_firmware.py
```  

### Usage :  
When PlatformIO is compiling, the resulting HEX file is renamed with the version number.  
You have to change the version number in the platformIO.ini file.  

Increment Patch (Bugs correction) :  
(Ex: 1.1.5 → 1.1.6)  
Increment Minor (New functionality) :  
(Ex: 1.1.5 → 1.2.0)  
Increment Major (Major change) :  
(Ex: 1.1.5 → 2.0.0)
  
### Result :
At each compling, the build hex file will be renamed after the datas contained in platformIO.ini and timestamped.
The compiled hex file is renamed like this :  
**firmware_v1.1.1_pro8MHzatmega328_20260225_0731**

The version number and build time can be called inside a script :
Example :  
    // Display the version  
    Serial.print("Version : ");  
    Serial.print(VERSION_MAJOR);  
    Serial.print(".");  
    Serial.print(VERSION_MINOR);  
    Serial.print(".");  
    Serial.println(VERSION_PATCH);  

    // Display the build time
    Serial.print("Compiled the : ");  
    Serial.println(BUILD_TIME);

I hope this helps... Let me know.
