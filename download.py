def readAndDownload():
    import os
    f = open("links.txt", "r")
    for x in f:
        cmd = "mp3.sh "+x
        os.system(cmd)
    
def clearFile():
    open('links.txt', 'w').close()
readAndDownload()
clearFile()