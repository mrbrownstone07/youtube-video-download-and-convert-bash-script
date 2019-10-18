def readAndDownload():
    import os
    f = open("links.txt", "r")
    for x in f:
        if checkIfDownloaded(x) != -1:
            cmd = "~/mp3/mp3.sh "+x
            os.system(cmd)
            d = open("download_history.txt", 'a')
            d.write(x)
            d.close()
        else:
            print("the file is already downloaded!")
        
def checkIfDownloaded(link):
    download_history = open("download_history.txt", 'r')
    for d in download_history:
        if d == link:
            download_history.close()
            return -1
    download_history.close()
    return 0


def clearFile():
    open('links.txt', 'w').close()

def main():
    readAndDownload()
    clearFile()

if __name__ == "__main__":
    main()


