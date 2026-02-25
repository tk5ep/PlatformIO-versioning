import sys, re, datetime, os

# Tentative d'importation de l'environnement PlatformIO
try:
    Import("env")
except:
    env = None

PATH_VERSION = './src/version.h'
MAJOR_IDX, MINOR_IDX, PATCH_IDX = 0, 1, 2

# 1. Vérification / Création initiale
if not os.path.exists(PATH_VERSION):
    os.makedirs(os.path.dirname(PATH_VERSION), exist_ok=True)
    with open(PATH_VERSION, 'w') as f:
        f.write('#define VERSION "0.1.0"')

# 2. Lecture de la version actuelle
with open(PATH_VERSION, 'r') as reader:
    content = reader.read()
    match = re.search(r'#define VERSION "([^"]*)"', content)
    if not match:
        print("Erreur : #define VERSION introuvable.")
        sys.exit(1)
    
    version_str = match.group(1)
    v = [int(n) for n in re.split(r'\.', version_str)]
    while len(v) < 3: v.append(0)

# 3. Logique d'incrémentation
if "--major" in sys.argv:
    v[MAJOR_IDX] += 1
    v[MINOR_IDX], v[PATCH_IDX] = 0, 0
elif "--minor" in sys.argv:
    v[MINOR_IDX] += 1
    v[PATCH_IDX] = 0
elif "--patch" in sys.argv or env is not None:
    # Si env est présent, c'est PlatformIO qui tourne : on incrémente le patch
    v[PATCH_IDX] += 1
elif "--get" in sys.argv:
    print(f"Version : {v[0]}.{v[1]}.{v[2]}")
    sys.exit(0)
else:
    # Aide en cas de lancement manuel sans argument
    print("\nVersion Manager by TK5EP - Usage:")
    print("---------------------------")
    print("python script.py --get    : Display actual version")
    print("python script.py --patch  : Increments patch (0.1.0 -> 0.1.1)")
    print("python script.py --minor  : Increments minor (0.1.1 -> 0.2.0)")
    print("python script.py --major  : Increments major (0.2.0 -> 1.0.0)")
    sys.exit(0)

# 4. Préparation des données de sortie
version = f"{v[0]}.{v[1]}.{v[2]}"
now = datetime.datetime.now()
datestamp, timestamp = now.strftime('%Y-%m-%d'), now.strftime('%H:%M')
versionFull = f"{version} {datestamp} {timestamp}"

# 5. Écriture dans version.h
with open(PATH_VERSION, 'w') as writer:
    writer.writelines([
        f'#define VERSION "{version}"\n',
        f'#define VERSION_MAJOR {v[MAJOR_IDX]}\n',
        f'#define VERSION_MINOR {v[MINOR_IDX]}\n',
        f'#define VERSION_PATCH {v[PATCH_IDX]}\n',
        f'#define VERSION_DATE "{datestamp}"\n',
        f'#define VERSION_TIME "{timestamp}"\n',
        f'#define VERSION_FULL "{versionFull}"'
    ])

print(f"--- Version updated to: {version} ---")

# 6. Renommage dynamique du binaire PlatformIO
if env:
    # Récupère le nom de l'environnement (ex: pro8MHzatmega328)
    build_tag = env.get('PIOENV', 'release')
    
    # Définit le nom du fichier (ex: firmware_v1.2.3_pro8MHzatmega328)
    progname = f"firmware_v{version}_{build_tag}"
    
    # Applique le renommage au processus de build
    env.Replace(PROGNAME=progname)
    print(f"--- Output file: {progname} ---")
