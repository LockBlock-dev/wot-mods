import py_compile
import os
import sys

hardCoded_path = ''
#./res_mods/X.X.X.X/mods/modules

if hardCoded_path:
    mods_path = hardCoded_path
else:
    versions = os.listdir('./res_mods/')
    max = [0, '']

    for v in versions:
        split = v.split('.')
        ver = [float(split[0] + '.' + split[1]), v]
        if ver[0] > max[0]:
            max = ver

    mods_path = './res_mods/%s/mods/modules' % (max[1])

mods = os.listdir(mods_path)

print '[Loader] Trying to load following mods:', mods

sys.path.insert(0, mods_path)

for mod in mods:
    path = '%s/%s' % (mods_path,mod)
    if not path.endswith('.pyc'):
        py_compile.compile(path)
        print '[Compiler]', mod, 'compiled!'
        os.remove(path)

for mod in mods:
    try:
        path = '%s/%s' % (mods_path,mod)
        __import__(mod.strip('.pyc'))
        print '[Loader]', mod, 'loaded '
    except Exception, e:
        print '[Loader] Failed to load', mod ,e
