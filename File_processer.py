import tkinter as tk
import tkinter.font as tkFont

import codecs

import time
import json
import sys

from functools import partial

const_conpitition_mid_element  = ("中年級男跳遠","中年級女跳遠","中年級男 60 公尺","中年級女 60 公尺")
const_conpitition_high_element = ("高年級男跳遠","高年級女跳遠","高年級男跳高","高年級女跳高","高年級男 100 公尺","高年級女 100 公尺")
const_team_conpitition_mid_element = ("大隊接力 A 隊","大隊接力 B 隊")
const_team_conpitition_high_element = ("大隊接力 A 隊","大隊接力 B 隊")

const_conpitition_junior_one = ("國一男跳遠","國一女跳遠","國一男跳高","國一女跳高","國一男藥球","國一女藥球","國一女 100 公尺","國一男 100 公尺","國一女 400 公尺","國一男 400 公尺","國一女 800 公尺","國一男 1500 公尺")
const_conpitition_junior_two = ("國二男跳遠","國二女跳遠","國二男跳高","國二女跳高","國二男藥球","國二女藥球","國二女 100 公尺","國二男 100 公尺","國二女 400 公尺","國二男 400 公尺","國二女 800 公尺","國二男 1500 公尺")
const_conpitition_junior_tre = ("國三男跳遠","國三女跳遠","國三男跳高","國三女跳高","國三男藥球","國三女藥球","國三女 100 公尺","國三男 100 公尺","國三女 400 公尺","國三男 400 公尺","國三女 800 公尺","國三男 1500 公尺")

const_team_conpitition_junior_one = ("國一男生 400 公尺接力","國一女生 400 公尺接力")
const_team_conpitition_junior_two = ("國二男生 400 公尺接力","國二女生 400 公尺接力")
const_team_conpitition_junior_tre = ("國三男生 400 公尺接力","國三女生 400 公尺接力")

const_conpitition_senior_one = ("高一男跳遠","高一女跳遠","高一男跳高","高一女跳高","高一男藥球","高一女藥球","高一女 100 公尺","高一男 100 公尺","高一女 400 公尺","高一男 400 公尺","高一女 800 公尺","高一男 1500 公尺")
const_conpitition_senior_two = ("高二男跳高","高二女跳高","高二男藥球","高二女藥球","高二男跳遠","高二女跳遠","高二女 100 公尺","高二男 100 公尺","高二女 400 公尺","高二男 400 公尺","高二女 800 公尺","高二男 1500 公尺")
const_conpitition_senior_tre = ("高三男跳遠","高三女跳遠","高三男跳高","高三女跳高","高三男藥球","高三女藥球","高三女 100 公尺","高三男 100 公尺","高三女 400 公尺","高三男 400 公尺","高三女 800 公尺","高三男 1500 公尺")

const_team_conpitition_senior_one = ("高一男生 400 公尺接力","高一女生 400 公尺接力")
const_team_conpitition_senior_two = ("高二男生 400 公尺接力","高二女生 400 公尺接力")
const_team_conpitition_senior_tre = ("高三男生 400 公尺接力","高三女生 400 公尺接力")

const_class = ("仁","義","禮","智","信","忠","孝","和")
const_Grade_senior = ("高一","高二","高三")
const_Grade_junior = ("國一","國二","國三")

Grade = 0
Class = 0

Names = []

result_personal = []
result_teamwork = []
def renew_constant():
    global Grade,Class,Names,result_personal,result_teamwork
    Grade = 0
    Class = 0
    Names = []
    result_personal = []
    result_teamwork = []


def push (var):
    global result_personal
    result_personal.append([i.get() for i in var])

def push_team(var):
    global result_teamwork
    result_teamwork.append([i.get() for i in var])

def Name_parser(name):
    global Names
    Names = name.strip().split("\n")
    return None


def Grade_select(num):
    global Grade
    Grade +=num
    return None

def Class_select(num):
    global Class
    Class +=num
    return None

def Destroy_all_child(window):
    for child in window.winfo_children():
        child.destroy()
    return None

def window_destroyer(window):
    window.destroy()

def Create_Grade_select(window):
    tk.Button(window,bg="gray",text = "高中",font =("Microsoft JhengHei",20,"bold"), height = 1, width = 20,command = lambda:[Grade_select(9),Destroy_all_child(window),Grade_select_Second(window)]).pack()
    tk.Button(window,bg="gray",text = "國中",font =("Microsoft JhengHei",20,"bold"), height = 1, width = 20,command = lambda:[Grade_select(6),Destroy_all_child(window),Grade_select_Second(window)]).pack()
    tk.Button(window,bg="gray",text = "國小",font =("Microsoft JhengHei",20,"bold"), height = 1, width = 20,command = lambda:[Grade_select(0),Destroy_all_child(window),Grade_select_Second(window)]).pack()
    return None

def Grade_select_Second(window):
    if Grade < 6 :
        tk.Button(window,bg="gray",text = "一年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(1),Destroy_all_child(window),Class_selector(window)]).pack()
        tk.Button(window,bg="gray",text = "二年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(2),Destroy_all_child(window),Class_selector(window)]).pack()
        tk.Button(window,bg="gray",text = "三年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(3),Destroy_all_child(window),Class_selector(window)]).pack()
        tk.Button(window,bg="gray",text = "四年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(4),Destroy_all_child(window),Class_selector(window)]).pack()
        tk.Button(window,bg="gray",text = "五年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(5),Destroy_all_child(window),Class_selector(window)]).pack()
        tk.Button(window,bg="gray",text = "六年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(6),Destroy_all_child(window),Class_selector(window)]).pack()

    if Grade >= 6 :
        tk.Button(window,bg="gray",text = "一年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(1),Destroy_all_child(window),Class_selector(window)]).pack()
        tk.Button(window,bg="gray",text = "二年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(2),Destroy_all_child(window),Class_selector(window)]).pack()
        tk.Button(window,bg="gray",text = "三年級",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Grade_select(3),Destroy_all_child(window),Class_selector(window)]).pack()

def Class_selector(window):
    if Grade <= 6:
        for i in const_class[0:1]:
            tk.Button(window,bg="gray",text = i ,font =("Microsoft JhengHei",20,"bold"),command = lambda i=i:[Class_select(const_class.index(i)+1),Destroy_all_child(window),get_name(window)]).pack()
    elif Grade > 6 and Grade <=9:
        for i in const_class[0:4]:
            tk.Button(window,bg="gray",text = i ,font =("Microsoft JhengHei",20,"bold"),command = lambda i=i:[Class_select(const_class.index(i)+1),Destroy_all_child(window),get_name(window)]).pack()
    elif Grade > 9:
        for i in const_class:
            tk.Button(window,bg="gray",text = i ,font =("Microsoft JhengHei",20,"bold"),command = lambda i=i:[Class_select(const_class.index(i)+1),Destroy_all_child(window),get_name(window)]).pack()
    return None

def get_name(window):
    tk.Label(window,bg="#1f1f1f",fg = '#6495ed',text = "Input Namelist" ,font =("Microsoft JhengHei",20,"bold")).pack()
    input_name = tk.Text(window,height=20)
    input_name.pack()
    OK_btn = tk.Button(window,bg="gray",text = "OK",font =("Microsoft JhengHei",20,"bold"),command = lambda:[Name_parser(input_name.get("1.0", "end")),Destroy_all_child(window),compitition_select(window)])
    OK_btn.pack()

def compitition_select(window):
    if Grade >=3 and Grade <= 4 :
        Creator(window,const_conpitition_mid_element,0,Names,Grade)
    elif Grade >=5 and Grade <=6 :
        Creator(window,const_conpitition_high_element,0,Names,Grade)
    elif Grade == 7:
        Creator(window,const_conpitition_junior_one,0,Names,Grade)
    elif Grade == 8:
        Creator(window,const_conpitition_junior_two,0,Names,Grade)
    elif Grade == 9:
        Creator(window,const_conpitition_junior_tre,0,Names,Grade)
    elif Grade == 10:
        Creator(window,const_conpitition_senior_one,0,Names,Grade)
    elif Grade == 11:
        Creator(window,const_conpitition_senior_two,0,Names,Grade)
    elif Grade == 12:
        Creator(window,const_conpitition_senior_tre,0,Names,Grade)
    
def Creator(window,const,num,names,Grade):
    if len(const)>num:
        tk.Label(window,bg="#1f1f1f",fg = '#6495ed',text = const[num] ,font =("Microsoft JhengHei",20,"bold")).grid(row=0,column=3)
        var = [tk.IntVar() for i in range(len(Names))]
        [tk.Checkbutton(window,bg="gray",text = name ,variable = var[Names.index(name)] ,font =("Microsoft JhengHei",20,"bold")).grid(row=(Names.index(name)//7+1),column=(Names.index(name)%7)) for name in Names]
        tk.Button(window,bg="gray",text = "OK",font =("Microsoft JhengHei",20,"bold"),command = lambda:[push(var),Destroy_all_child(window),Creator(window,const,num+1,Names,Grade)]).grid(row=(len(Names)//7+2),column=3)
    elif len(const)==num:
        if Grade >=3 and Grade <= 4 :
            Creator_team(window,const_team_conpitition_mid_element,0,Names)
        elif Grade >=5 and Grade <=6 :
            Creator_team(window,const_team_conpitition_high_element,0,Names)
        elif Grade == 7:
            Creator_team(window,const_team_conpitition_junior_one,0,Names)
        elif Grade == 8:
            Creator_team(window,const_team_conpitition_junior_two,0,Names)
        elif Grade == 9:
            Creator_team(window,const_team_conpitition_junior_tre,0,Names)
        elif Grade == 10:
            Creator_team(window,const_team_conpitition_senior_one,0,Names)
        elif Grade == 11:
            Creator_team(window,const_team_conpitition_senior_two,0,Names)
        elif Grade == 12:
            Creator_team(window,const_team_conpitition_senior_tre,0,Names)

def Creator_team(window,const,num,names):
    if len(const)>num:
        tk.Label(window,bg="#1f1f1f",fg = '#6495ed',text = const[num] ,font =("Microsoft JhengHei",20,"bold")).grid(row=0,column=3)
        var = [tk.IntVar() for i in range(len(Names))]
        [tk.Checkbutton(window,bg="gray",text = name ,variable = var[Names.index(name)] ,font =("Microsoft JhengHei",20,"bold")).grid(row=(Names.index(name)//7+1),column=(Names.index(name)%7)) for name in Names]
        tk.Button(window,bg="gray",text = "OK",font =("Microsoft JhengHei",20,"bold"),command = lambda:[push_team(var),Destroy_all_child(window),Creator_team(window,const,num+1,Names)]).grid(row=(len(Names)//7+2),column=3)
    elif len(const)==num:
        parser(const)

def parser(const):
    parsed_personal = []
    parsed_teamwork = []
    for i in result_personal:
        parsed = []
        for var in range(len(i)):
            if i[var]:
                parsed.append(Names[var])
        parsed_personal.append(parsed)
    for i in result_teamwork:
        parsed = []
        for var in range(len(i)):
            if i[var]:
                parsed.append(Names[var])
        parsed_teamwork.append(parsed)
    
    if Grade >=3 and Grade <= 4 :
        dic = dict(zip(const_conpitition_mid_element+const_team_conpitition_mid_element,parsed_personal+parsed_teamwork))
    elif Grade >=5 and Grade <=6 :
        dic = dict(zip(const_conpitition_high_element+const_team_conpitition_high_element,parsed_personal+parsed_teamwork))
    elif Grade == 7:
        dic = dict(zip(const_conpitition_junior_one+const_team_conpitition_junior_one,parsed_personal+parsed_teamwork))
    elif Grade == 8:
        dic = dict(zip(const_conpitition_junior_two+const_team_conpitition_junior_two,parsed_personal+parsed_teamwork))
    elif Grade == 9:
        dic = dict(zip(const_conpitition_junior_tre+const_team_conpitition_junior_tre,parsed_personal+parsed_teamwork))
    elif Grade == 10:
        dic = dict(zip(const_conpitition_senior_one+const_team_conpitition_senior_one,parsed_personal+parsed_teamwork))
    elif Grade == 11:
        dic = dict(zip(const_conpitition_senior_two+const_team_conpitition_senior_two,parsed_personal+parsed_teamwork))
    elif Grade == 12:
        dic = dict(zip(const_conpitition_senior_tre+const_team_conpitition_senior_tre,parsed_personal+parsed_teamwork))
    union = []
    for i in parsed_personal:
        union += i
    for i in parsed_teamwork:
        union += i
    union = list(set(union))
    dic.update([('union',union),('Grade',Grade),('Class',Class)])
    json_dat = json.dumps(dic, indent=4,ensure_ascii = False)

    with open(str(Grade)+"_"+str(Class)+".txt", "w",encoding='UTF-8') as file:
        file.write(json_dat)
        
    tk.Button(window,bg="gray",text = "建立下一份資料",font =("Microsoft JhengHei",20,"bold"),command = lambda:[renew_constant(),Destroy_all_child(window),Create_Grade_select(window)]).pack()
    tk.Button(window,bg="gray",text = "Exit",font =("Microsoft JhengHei",20,"bold"),command = lambda:[sys.exit(0)]).pack()


window = tk.Tk()
window.title("ASHS_Compitition_Pass")
window.config(background = "#1f1f1f")
window.minsize(width = 1200 , height = 600)
tk.Label(window,bg="#1f1f1f",fg = '#6495ed',text = "ASHS_Compitition_Pass" ,font =("Microsoft JhengHei",20,"bold")).pack()

Create_Grade_select(window)

window.mainloop()
