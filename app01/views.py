from django.shortcuts import render,redirect
from app01 import models
import os
import datetime
import shutil

def INCAR_list(request):
    """INCAR列表"""
    #便于重定向的变量
    global n
    n=1
    queryset = models.Model_INCAR.objects.all()
    return render(request,'INCAR_list.html',{"queryset":queryset})

def INCAR_add(request):
    """添加INCAR参数"""
    if request.method == "GET":
        return render(request,"INCAR_add.html")
    # 获取用户POST提交过来的数据（暂不包含title 输入为空）暂时默认输入合法
    parameter = request.POST.get("parameter")
    value = request.POST.get("value")
    #保存到数据库
    models.Model_INCAR.objects.create(parameter=parameter,value=value)
    #重定向回列表页面,用redirect
    return redirect("/INCAR/list/")

def INCAR_delete(request):
    """删除参数"""
    #获取ID
    nid = request.GET.get('nid')
    #删除
    models.Model_INCAR.objects.filter(id = nid).delete()
    #重定向回参数列表
    if n == 1:
        return redirect("/INCAR/list/")

def INCAR_edit(request, nid):
    """修改参数名/参数值"""
    queryset = models.Model_INCAR.objects.all()
    row_object = models.Model_INCAR.objects.filter(id=nid).first()
    if request.method == "GET":
        return render(request,'INCAR_edit.html',{"queryset":queryset,"row_object":row_object},nid)
    parameter = request.POST.get("parameter")
    value = request.POST.get("value")
    #更新到数据库
    models.Model_INCAR.objects.filter(id=nid).update(value=value,parameter=parameter)
    return redirect("/INCAR/list/")

def INCAR_download(request):
    """导出INCAR文件"""
    global str_month, str_day, str_hour, str_minute
    curr_time = datetime.datetime.now()  # 2019-07-06 14:55:56.873893 <class 'datetime.datetime'>
    year = str(curr_time.year)  #  <class 'int'>
    if (curr_time.month < 10):
        str_month = '0' + str(curr_time.month)  #  <class 'int'>
    else:str_month = str(curr_time.month)
    if (curr_time.day < 10):
        str_day = '0' + str(curr_time.day)  #  <class 'int'>
    else:str_day = str(curr_time.day)
    if (curr_time.hour < 10):
        str_hour = '0' + str(curr_time.hour)  #  <class 'int'>
    else:str_hour = str(curr_time.hour)
    if (curr_time.minute < 10):
        str_minute = '0' + str(curr_time.minute)  #  <class 'int'>
    else:str_minute = str(curr_time.minute)

    str_second = str(curr_time.second) #  <class 'int'>
    # curr_time.date() #  <class 'datetime.date'>
    file_time = year+str_month+str_day+str_hour+str_minute+'s'+str_second
    path = './output/'+file_time # 想要创建的文件路径
    #  如果想要递归创建文件，则使用
    if os.path.isdir(path) == False:
        os.makedirs(path)  # 如果不存在，就递归地创建，即先创建 test_data 文件夹， 再创建 test_data1 文件夹
    fpath = path+"/"+"INCAR.INCAR"
    f = open(fpath, 'w')
    queryset = models.Model_INCAR.objects.all()
    for obj in queryset:
        f.write(obj.parameter+' = '+obj.value+'\n')
    f.close()
    return redirect("/INCAR/list/")

def get_allfile(path):  # 获取POTCAR所有文件
    all_file = []
    for f in os.listdir(path):  #listdir返回文件中所有目录
        f_name = os.path.join(path, f)
        all_file.append(f_name)
    return all_file

def Curr_time(month,day,hour,minute):
    global str_month, str_day, str_hour, str_minute
    curr_time = datetime.datetime.now()  # 2019-07-06 14:55:56.873893 <class 'datetime.datetime'
    year = str(curr_time.year)  # <class 'int'>
    if (month < 10):
        str_month = '0' + str(month)  # <class 'int'>
    else:
        str_month = str(month)
    if (day < 10):
        str_day = '0' + str(day)  # <class 'int'>
    else:
        str_day = str(day)
    if (hour < 10):
        str_hour = '0' + str(hour)  # <class 'int'>
    else:
        str_hour = str(hour)
    if (minute < 10):
        str_minute = '0' + str(minute)  # <class 'int'>
    else:
        str_minute = str(minute)
    second = str(curr_time.second)
    return year+str_month+str_day+str_hour+str_minute+ 's' +second

def merge(file1, file2):
    f1 = open(file1, 'a+', encoding='utf-8')
    with open(file2, 'r', encoding='utf-8') as f2:
        f1.write('\n')
        for i in f2:
            f1.write(i)
    f1.close()
    f2.close()

def POSCAR_list(request):
    """POSCAR列表"""
    global POSCAR_ori
    if request.method == "GET":
        return render(request,'POSCAR_list.html')
    # POSCAR_file = request.FILES.get("POSCAR_file")  #获取传来的文件,单个文件获取方式
    POSCAR_files = request.FILES.getlist('POSCAR_files[]')
    n = 0
    eles = {}
    ele_name_bat = request.POST.get('ele_name_bat')  # 统一
    ele_new_bat01 = request.POST.get("ele_new_bat" + "0")  # 统一：这里获取到第一个要更改成的元素
    ele_new_bat02 = request.POST.get("ele_new_bat" + "1")
    ele_new_bat03 = request.POST.get("ele_new_bat" + "2")
    ele_new_bat04 = request.POST.get("ele_new_bat" + "3")
    for POSCAR_file in POSCAR_files:
        curr_time = datetime.datetime.now()  # 2019-07-06 14:55:56.873893 <class 'datetime.datetime'>
        file_time = Curr_time(curr_time.month,
                     curr_time.day,
                     curr_time.hour,
                     curr_time.minute)
        #这里是输出文件夹
        des = "./output/" + file_time + "_" + str(n)  # 目标文件夹
        if not os.path.exists(des):  # 如果不存在，创建此路径
            os.makedirs(des)

        #这里从前端获取数据（每单个文件）
        ele_name = request.POST.get('ele_name' + str(n))  # 这里获取到更改的物质化学式名称
        if(ele_name_bat):
            ele_name = ele_name_bat
        ele_new_01 = request.POST.get("ele_new" + str(n)+"0")   #这里获取到第一个要更改成的元素
        ele_new_02 = request.POST.get("ele_new" + str(n)+"1")
        ele_new_03 = request.POST.get("ele_new" + str(n)+"2")
        ele_new_04 = request.POST.get("ele_new" + str(n)+"3")

        ele_new01 = ''
        ele_new02 = ''
        ele_new03 = ''
        ele_new04 = ''

        if ele_new_bat01:
            ele_new01 = ele_new_bat01
        if (ele_new_bat02):
            ele_new02 = ele_new_bat02
        if (ele_new_bat03):
            ele_new03 = ele_new_bat03
        if (ele_new_bat04):
            ele_new04 = ele_new_bat04

        if ele_new_01:
            ele_new01 = ele_new_01
        if ele_new_02:
            ele_new02 = ele_new_02
        if ele_new_03:
            ele_new03 = ele_new_03
        if ele_new_04:
            ele_new04 = ele_new_04

        #这里读取并导出POSCAR
        position = os.path.join(des, "POSCAR.POSCAR")  # 这里拼接输出文件夹和文件
        storage = open(position, 'wb')    #创建并写入POSCAR
        for chunk in POSCAR_file.chunks():
            storage.write(chunk)
        storage.close()
        f = open(position, 'r',encoding = 'utf-8')
        POSCAR_ori = f.read()
        POSCAR_ori = POSCAR_ori.split('\n')
        #POSCAR_ori = list(dict.fromkeys(POSCAR_ori))  ## 这里是去重
        f.close()

        #这里开始导出POTCAR
        src = "./potpaw_PBE.52"  # POTCAR原文件夹路径
        for POTCAR_first_file in os.listdir(src):
            # 遍历原文件夹中的文件
            if POTCAR_first_file == ele_new01:  #找到要更改的元素
                file02 = os.path.join(POTCAR_first_file , "POTCAR")   #找到要更改的元素的对应POTCAR文件
                full_first_path = os.path.join(src, file02)  # 把文件的完整路径得到
                #if os.path.isfile(full_file_name):  # 用于判断某一对象(需提供绝对路径)是否为文件
                shutil.copy(full_first_path, des)  # shutil.copy函数放入原文件的路径文件全名  然后放入目标文件夹

        POTCAR_first = os.path.join(des, "POTCAR")
        for POTCAR_sec_file in os.listdir(src):
            if POTCAR_sec_file == ele_new02:
                file03 = os.path.join(POTCAR_sec_file, "POTCAR")  # 找到要更改的元素的对应POTCAR文件
                full_sec_path = os.path.join(src, file03)  # 把文件的完整路径得到
                merge(POTCAR_first, full_sec_path)

        POTCAR_second = os.path.join(des, "POTCAR")
        for POTCAR_thi_file in os.listdir(src):
            if POTCAR_thi_file == ele_new03:
                file04 = os.path.join(POTCAR_thi_file, "POTCAR")  # 找到要更改的元素的对应POTCAR文件
                full_thi_path = os.path.join(src, file04)  # 把文件的完整路径得到
                merge(POTCAR_second, full_thi_path)

        POTCAR_third = os.path.join(des, "POTCAR")
        for POTCAR_fou_file in os.listdir(src):
            if POTCAR_fou_file == ele_new04:
                file05 = os.path.join(POTCAR_fou_file, "POTCAR")  # 找到要更改的元素的对应POTCAR文件
                full_fou_path = os.path.join(src, file05)  # 把文件的完整路径得到
                merge(POTCAR_third, full_fou_path)

        #这里更改POSCAR中物质化学式
        if(ele_name):
            POSCAR_ori[0] = ele_name

        #这里更改元素
        if(ele_new01):
            POSCAR_ori[5] = " " + ele_new01 + "   " + ele_new02 + "   " + ele_new03 + "   " + ele_new04

        eles[n] = POSCAR_ori[5]
        POSCAR_new = open(position, 'w')
        for obj in POSCAR_ori:
            POSCAR_new.write(obj+"\n")
        POSCAR_new.close()

        #这里导出INCAR
        fpath = des+"/"+"INCAR.INCAR"
        f = open(fpath, 'w')
        queryset = models.Model_INCAR.objects.all()  #从数据库中提取INCAR
        for obj in queryset:
            f.write(obj.parameter+' = '+obj.value+'\n')
        f.close()

        n = n + 1 #做计数
        # #使更改完的POSCAR文件显示在网页

    return render(request,'POSCAR_list.html',
                  {
                      "elements":eles, #list:每个POSCAR中的元素，用来提示
                      "POSCAR_files":POSCAR_files, #list:每个POSCAR文件的名字，用来提示上传成功
                      "上传成功":"上传成功！",
                   }
                  )





