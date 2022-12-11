from downloadFIlesFromS3 import downloadFile
import uploadFilesToS3
from doctest import master
from optparse import Option
import tkinter
from tkinter import filedialog
import config
import boto3
from tkinter import *

s3 = boto3.client("s3", aws_access_key_id=config.access_key,
                  aws_secret_access_key=config.secret_access_key)
top = tkinter.Tk()
top.geometry("750x500")

#Create a canvas object
canvas= tkinter.Canvas(top, width= 500, height= 200, bg="SpringGreen2")




def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        ".txt"),("PDF Files",".pdf"),
                                                       ("all files",
                                                        ".\*")))
    filename = filename.replace('/','\\')                                                    
    print(filename)                                                        

    uploadFilesToS3.upload_file(filename)  
    #exit() 


def downloadFiles():
    #text.insert(END, content)
    FileToDownload = text.get(1.0, END)
    FileToDownload = FileToDownload.strip()
    #print(len(FileToDownload))
    downloadFile(FileToDownload)
    #exit()


button=tkinter.Button(top,text='UPLOAD',command=browseFiles)
text = tkinter.Text(top, width=25, height=10)
button2=tkinter.Button(top,text='DOWNLOAD',command=downloadFiles)
files = ''
if 'Contents' in s3.list_objects(Bucket=config.bucket_name):
    for key in s3.list_objects(Bucket=config.bucket_name)['Contents']:
        files += key['Key'] + '\n'
else:
    files = "No Files in S3"        

#Add a text in Canvas
canvas.create_text(250, 150, text=files, fill="black", font=('Helvetica 15 bold'))
canvas.pack()

button.pack()
text.pack()
button2.pack()
top.mainloop()





