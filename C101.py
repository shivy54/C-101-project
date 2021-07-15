import dropbox

class TransferData:
    def __init__(self,aT):
        self.aT = aT
    def uploadFiles(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.aT)
        f = open(fileFrom,"rb")
        dbx.files_upload(f.read(),fileTo)


def main():
    token = "-2IKFVNr_CIAAAAAAAAAAQ4ficO3IFw0gN4uA-_4mlRvRP6iWblMKzi8XH2OE4nB"
    transfer= TransferData(token)
    fileFrom="test.txt"
    fileTo="/dropbox/test.txt"
    transfer.uploadFiles(fileFrom,fileTo)
    print("upload complete")

main()
    