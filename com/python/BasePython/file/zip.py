import zipfile
z = zipfile.ZipFile("RStudio-0.99.893.zip", "r")
for filename in z.namelist():
    print 'File:', filename
    bytes = z.read(filename)
    print 'has', len(bytes), 'bytes'