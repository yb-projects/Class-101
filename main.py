import dropbox
f1 = "C:/Users/TayoYuva/Documents/Mine/Studies/White Hat JR/Class/C101/file.txt"
print(f1)
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            print("file opened")
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.Bpx0aNhb9oSs29JGILKtpm3ucBTLIdBKOzGDcNBUKsoz864ovhAb9hm-dPFm5q6Pi_L7Rk0oL7X-NgmxfGbgnbeLoHHrS63eFsjsEEHNfKVZzEzCo6CnOB-8CMF1fqRDDWRJ4t1m_F8jY9Ip75u6W-0"
    transferData = TransferData(access_token)

    file_from = f1
    file_to = input("Enter the file path to transfer to (in Dropbox):")

    transferData.upload_file(file_from, file_to)
    print("File has been sucessfully moved!")

if __name__ == '__main__':
    main()
