Import("env")
from datetime import datetime

# 1. Récupération des versions depuis platformio.ini
build_flags = env.ParseFlags(env.get("BUILD_FLAGS", ""))
defines = {item[0]: item[1] for item in build_flags.get("CPPDEFINES", []) if isinstance(item, list)}

major = defines.get("VERSION_MAJOR", "0")
minor = defines.get("VERSION_MINOR", "0")
patch = defines.get("VERSION_PATCH", "0")

# 2. Génération de l'horodatage
now = datetime.now()
# Pour le nom du fichier (ex: 20260225_07h45)
timestamp_file = now.strftime("%Y%m%d_%Hh%M")
# Pour le code C++ (ex: 25/02/2026 07:45)
timestamp_cpp = now.strftime("%d/%m/%Y %H:%M")

# 3. INJECTION DANS LE CODE C++
# On ajoute une macro BUILD_TIME que vous pourrez utiliser dans Arduino
env.Append(CPPDEFINES=[
    ("BUILD_TIME", f'\\"{timestamp_cpp}\\"')
])

# 4. RENOMMAGE DU FICHIER .HEX
env_name = env.get("PIOENV", "avr")
progname = f"firmware_v{major}.{minor}.{patch}_{env_name}_{timestamp_file}"

print(f"--- [INFO] Build Time injecté : {timestamp_cpp} ---")
print(f"--- [INFO] Nom du fichier : {progname}.hex ---")

env.Replace(PROGNAME=progname)
