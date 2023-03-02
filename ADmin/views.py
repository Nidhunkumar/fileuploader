from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from user.models import User_files 
import pandas as pd
import re
import csv
import json
 
def ADmin_login(request):
    if request.method == "POST":
        username=request.POST["username"]
        raw_password=request.POST["password"]
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('admin_index')

        
    return render(request,"ADmin/Admin_login.html")

def ADmin_index(request):
    all_files=User_files.objects.all()
    
    return render(request,"ADmin/ADmin_index.html",{'all_files':all_files})
def logout_view(request):
    logout(request)
    return redirect('admin_login')



def csv_to_objects(request,id):
    csv_file=User_files.objects.get(id=id)
    if csv_file:
        file_name=csv_file.file
        if str(file_name).endswith('.csv'):
            df=pd.read_csv(csv_file.file)
            json_records = df.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context={"data":data}
            return render(request,"ADmin/ADmin_file_single_table.html",context)
        elif str(file_name).endswith('.xlsx'):
            df=pd.read_excel(csv_file.file)
            json_records = df.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            print(data)
            context={"data":data}
            return render(request,"ADmin/ADmin_file_single_table.html",context)
        


        
    