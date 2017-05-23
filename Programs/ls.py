import os, os.path ,sys
import time
if len(sys.argv) == 1:
    path = os.getcwd()
else:
    path = sys.argv[1]

try:
    listdirs = os.listdir(path)
except FileNotFoundError:
    print("Błąd! Plik lub katalog nie istnieje.")
    exit()

for filename in listdirs:
    pathname = os.path.join(path, filename)
    filestat = os.stat(pathname)
    date = time.strftime("%d.%m.%Y   %H:%M", time.localtime(filestat.st_mtime))

    if not os.path.isfile(pathname):
        dir = "<DIR>"
    else:
        dir = "     "
    # print(filestat.st_mtime)
    print("{}  {}  {:20}\t{}".format(date, dir, filestat.st_size, filename))