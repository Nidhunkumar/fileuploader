from django.shortcuts import render
from .models import User_files
from django.contrib import messages

# Create your views here.

def user_index(request):
    return render(request, 'user/user_index.html')

def user_csv_uploader(request):
    if request.method == "POST":
        file=request.FILES['files']
        files_model=User_files(file=file)
        files_model.save()
        msg_success = "File Uploaded"
        return render (request,"user/user_csv_uploader.html",{'msg_success':msg_success})
    else:
        return render (request,"user/user_csv_uploader.html")

    
def user_xlsx_uploader(request):
    if request.method == "POST":
        file=request.FILES['files']
        files_model=User_files(file=file)
        files_model.save()
        msg_success = "File Uploaded"
        return render (request,"user/user_xlsx_uploader.html",{'msg_success':msg_success})
    else:
        return render (request,"user/user_xlsx_uploader.html")


    

