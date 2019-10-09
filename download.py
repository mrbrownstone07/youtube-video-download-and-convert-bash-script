def readAndDownload():
    import os
    f = open("download_links.txt", "r")
    for x in f:
        cmd = "~/mp3/mp3.sh "+x
        os.system(cmd)
    
def clearFile():
    fin = open('download_links.txt', "r")
    data = fin.read()
    fin.close()
    fout = open('download_history.txt', "a")
    fout.write(data)
    fout.close()            
    open('download_links.txt', 'w').close()
    open('links.txt', 'w').close()
readAndDownload()
clearFile()
