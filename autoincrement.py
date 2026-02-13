import sys, re, datetime, os

PATH_VERSION = './src/version.h'
MAJOR_IDX, MINOR_IDX, PATCH_IDX = 0, 1, 2

# 1. Vérification et Création si absent
if not os.path.exists(PATH_VERSION):
    print(f"File {PATH_VERSION} not found. Creating  initial version 0.1.0...")
    with open(PATH_VERSION, 'w') as f:
        f.write('#define VERSION "0.1.0"')

# 2. Lecture du fichier
with open(PATH_VERSION, 'r') as reader:
    content = reader.read()
    match = re.search(r'#define VERSION "([^"]*)"', content)

    if not match:
        print("Error: Macro #define VERSION not found in existing file version.h.")
        sys.exit(1)

    line = match.group(1)
    # Extraction des chiffres actuels [Major, Minor, Patch]
    try:
        v = [int(n) for n in re.split('\.', line)]
        # Sécurité au cas où le fichier contient moins de 3 segments
        while len(v) < 3: v.append(0)
    except ValueError:
        print("Error: Wrong version format.")
        sys.exit(1)

# 3. Gestion de l'option --get (Lecture seule)
if "--get" in sys.argv:
    print(f"{v[0]}.{v[1]}.{v[2]}")
    sys.exit(0)

# 4. Logique d'incrémentation
if "--major" in sys.argv:
    v[MAJOR_IDX] += 1
    v[MINOR_IDX] = 0
    v[PATCH_IDX] = 0
elif "--minor" in sys.argv:
    v[MINOR_IDX] += 1
    v[PATCH_IDX] = 0
else:
    # Par défaut (patch)
    v[PATCH_IDX] += 1

# 5. Écriture des modifications
with open(PATH_VERSION, 'w') as writer:
    now = datetime.datetime.now()
    datestamp = now.strftime('%Y-%m-%d')
    timestamp = now.strftime('%H:%M')
    
    version = f"{v[MAJOR_IDX]}.{v[MINOR_IDX]}.{v[PATCH_IDX]}"
    versionFull = f"{version} {datestamp} {timestamp}"

    writer.writelines([
        f'#define VERSION "{version}"\n',
        f'#define VERSION_MAJOR {v[MAJOR_IDX]}\n',
        f'#define VERSION_MINOR {v[MINOR_IDX]}\n',
        f'#define VERSION_PATCH {v[PATCH_IDX]}\n',
        f'#define VERSION_DATE "{datestamp}"\n',
        f'#define VERSION_TIME "{timestamp}"\n',
        f'#define VERSION_FULL "{versionFull}"'
    ])

print(f"Version : {version}")
