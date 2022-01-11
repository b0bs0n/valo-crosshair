import os
from PIL import Image
import winregistry
import vdf


def get_crosshair_path():
    lib_path = None
    lib = None
    steamid = '824270'
    val = 'InstallPath'
    path = r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Valve\Steam'
    with winregistry.WinRegistry() as client:
        steam = client.read_entry(path, val)
    d = vdf.load(open(steam.value + r'\steamapps\libraryfolders.vdf'))
    if 'libraryfolders' in d.keys():
        libs = [key for key in d['libraryfolders'].keys()]
        for lib in libs:
            try:
                if steamid in d['libraryfolders'][lib]['apps'].keys():
                    lib = lib
                    break
            except TypeError:
                pass
        lib_path = d['libraryfolders'][lib]['path']
    elif 'LibraryFolders' in d.keys():
        libs = []
        for key in d['LibraryFolders'].keys():
            try:
                int(key)
                libs.append(d['LibraryFolders'][key])
            except ValueError:
                pass
        for lib in libs:
            files = [f for f in os.listdir(lib) if f.endswith('.acf') and f.startswith('appmanifest')]
            if 'appmanifest_824270.acf' in files:
                lib_path = lib
    lib_path += r'\steamapps\common\FPSAimTrainer\FPSAimTrainer\crosshairs'
    return lib_path


def get_managed_crosshairs(dir_):
    files = [f for f in os.listdir(dir_) if f.endswith('.png')]
    chairs = []
    for file in files:
        path = dir_ + '\\' + file
        with Image.open(path) as png:
            try:
                if png.info['software'] == 'val_crosshair_tool':
                    chairs.append(file)
            except KeyError:
                pass
    return files, chairs


if __name__ == '__main__':
    path2 = get_crosshair_path()
    chs = get_managed_crosshairs(path2)
    print(chs)
