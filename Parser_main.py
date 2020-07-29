const_conpitition_mid_element  = ("中年級男跳遠","中年級女跳遠","中年級男 60 公尺","中年級女 60 公尺")
const_conpitition_high_element = ("高年級男跳遠","高年級女跳遠","高年級男跳高","高年級女跳高","高年級男 100 公尺","高年級女 100 公尺")
const_team_conpitition_mid_element = ("大隊接力 A 隊","大隊接力 B 隊")
const_team_conpitition_high_element = ("大隊接力 A 隊","大隊接力 B 隊")

const_conpitition_track_junior_one = ("國一女 100 公尺","國一男 100 公尺","國一女 400 公尺","國一男 400 公尺","國一女 800 公尺","國一男 1500 公尺")
const_conpitition_track_junior_two = ("國二女 100 公尺","國二男 100 公尺","國二女 400 公尺","國二男 400 公尺","國二女 800 公尺","國二男 1500 公尺")
const_conpitition_track_junior_tre = ("國三女 100 公尺","國三男 100 公尺","國三女 400 公尺","國三男 400 公尺","國三女 800 公尺","國三男 1500 公尺")

const_conpitition_field_junior_one = ("國一男跳高","國一女跳高","國一男跳遠","國一女跳遠","國一男藥球","國一女藥球")
const_conpitition_field_junior_two = ("國二男跳高","國二女跳高","國二男跳遠","國二女跳遠","國二男藥球","國二女藥球")
const_conpitition_field_junior_tre = ("國三男跳高","國三女跳高","國三男跳遠","國三女跳遠","國三男藥球","國三女藥球")

const_team_conpitition_junior_one = ("國一男生 400 公尺接力","國一女生 400 公尺接力")
const_team_conpitition_junior_two = ("國二男生 400 公尺接力","國二女生 400 公尺接力")
const_team_conpitition_junior_tre = ("國三男生 400 公尺接力","國三女生 400 公尺接力")

const_conpitition_track_senior_one = ("高一女 100 公尺","高一男 100 公尺","高一女 400 公尺","高一男 400 公尺","高一女 800 公尺","高一男 1500 公尺")
const_conpitition_track_senior_two = ("高二女 100 公尺","高二男 100 公尺","高二女 400 公尺","高二男 400 公尺","高二女 800 公尺","高二男 1500 公尺")
const_conpitition_track_senior_tre = ("高三女 100 公尺","高三男 100 公尺","高三女 400 公尺","高三男 400 公尺","高三女 800 公尺","高三男 1500 公尺")

const_conpitition_field_senior_one = ("高一男跳高","高一女跳高","高一男跳遠","高一女跳遠","高一男藥球","高一女藥球")
const_conpitition_field_senior_two = ("高二男跳高","高二女跳高","高二男跳遠","高二女跳遠","高二男藥球","高二女藥球")
const_conpitition_field_senior_tre = ("高三男跳高","高三女跳高","高三男跳遠","高三女跳遠","高三男藥球","高三女藥球")

const_team_conpitition_senior_one = ("高一男生 400 公尺接力","高一女生 400 公尺接力")
const_team_conpitition_senior_two = ("高二男生 400 公尺接力","高二女生 400 公尺接力")
const_team_conpitition_senior_tre = ("高三男生 400 公尺接力","高三女生 400 公尺接力")

const_class = ("仁","義","禮","智","信","忠","孝","和")
const_Grade_senior = ("高一","高二","高三")
const_Grade_junior = ("國一","國二","國三")

const_file_name_mid_element = ("3_1","4_1")
const_file_name_high_element = ("5_1","6_1")

const_file_name_junior_one = ("7_1","7_2","7_3","7_4")
const_file_name_junior_two = ("8_1","8_2","8_3","8_4")
const_file_name_junior_tre = ("9_1","9_2","9_3","9_4")

const_file_name_senior_one = ("10_1","10_2","10_3","10_4","10_5","10_6","10_7","10_8")
const_file_name_senior_two = ("11_1","11_2","11_3","11_4","11_5","11_6","11_7","11_8")
const_file_name_senior_tre = ("12_1","12_2","12_3","12_4","12_5","12_6","12_7","12_8")


import json
import sys , os

def import_data(const_file_name_data):
    result = []
    for name in const_file_name_data:
        with open(name+".txt", "r",encoding="UTF-8-sig") as file:
            json_dat = json.loads(file.read())
        result.append(json_dat)
    return result

def import_num_data():
    with open("num.txt","r",encoding="UTF-8") as file:
        num = list(map(int,file.read().strip().split(" ")))
    return num 

def get_all_union(all_data):
    result = []
    for i in all_data:
        result+=i['union']
    return result

def num_giver(name_list,num_list):
    dic = dict(zip(name_list, num_list[:len(name_list)]))
    return dic

def Summary_creator(all_data):
    for i in all_data:
        if i['Grade']>9:
            grade = const_Grade_senior[i['Grade']-10]
        elif i['Grade']<=9 and i['Grade']>6:
            grade = const_Grade_junior[i['Grade']-7]
        Class = i["Class"]
        print(grade + const_class[Class-1] , str(len(i["union"])) + "人")
        print("")
        print("領隊：   指導：   管理：   隊長：")
        print("")
        for _ in range(len(i['union'])//7):
            print(sub_create(i["union"][7*_:7*_+7]))
        if len(i['union'])%7 !=0:
            times = len(i['union'])//7
            print(sub_create(i["union"][7*times:]))
        print("")

def sub_create(name_lis):
    result = ' '
    parsed = ["%03d" % num_dic[i] + i for i in name_lis]
    return result.join(parsed)

def Subject_generator(Grade_data,const_data):
    result = []
    for subject in const_data:
        Lis = []
        string = ''
        for data in Grade_data: 
            dat = data[subject]
            parsed = ["%03d" % num_dic[i]+" "+ i +'('+const_class[data['Class']-1]+')' for i in dat]
            Lis+=parsed
        string+=(subject+"(共"+str(len(Lis))+"人)"+"\n")
        for _ in range(len(Lis)//4):
            string+=(" ".join(Lis[4*_:4*_+4])+"\n")
        if len(Lis)%4 !=0:
            times = len(Lis)//4
            string += (" ".join(Lis[4*times:])+"\n")
        result.append(string)
    return result

def relay_subject_generator(Grade_data,const_data):
    result = []
    for relay_subject in const_data:
         string = relay_subject + "\n"
         for data in Grade_data:
            Class = const_class[data['Class']-1]
            name_lis = data[relay_subject]
            parsed = ["%03d" % num_dic[i]+" "+i for i in name_lis]
            string += "("+Class+") "
            string += " ".join(parsed)
            string +="\n"
         result.append(string)
    return result

num_list = import_num_data()


junior_one_data = import_data(const_file_name_junior_one)
junior_two_data = import_data(const_file_name_junior_two)
junior_tre_data = import_data(const_file_name_junior_tre)

senior_one_data = import_data(const_file_name_senior_one)
senior_two_data = import_data(const_file_name_senior_two)
senior_tre_data = import_data(const_file_name_senior_tre)

all_data = junior_one_data+junior_two_data+junior_tre_data+senior_one_data+senior_two_data+senior_tre_data
num_dic = num_giver(get_all_union(all_data),num_list)


original_stdout = sys.stdout 

dir = os.getcwd()
if not os.path.isdir(dir+'\\compititionpass_out'):
    os.mkdir(dir+'\\compititionpass_out')
dir = os.getcwd()+"\\compititionpass_out\\"

with open(dir+'Summery_Out'+".txt", "w",encoding='UTF-8') as file:
    sys.stdout = file
    Summary_creator(all_data)
    sys.stdout = original_stdout

with open(dir+'Junior_field'+".txt", "w",encoding='UTF-8') as file:
    sys.stdout = file
    junior_one_field = Subject_generator(junior_one_data,const_conpitition_field_junior_one)
    junior_two_field = Subject_generator(junior_two_data,const_conpitition_field_junior_two)
    junior_tre_field = Subject_generator(junior_tre_data,const_conpitition_field_junior_tre)
    Out = list(zip(junior_one_field,junior_two_field,junior_tre_field))
    for i in Out:
        print("".join(i),end = "")
    sys.stdout = original_stdout

with open(dir+'Senior_field'+".txt", "w",encoding='UTF-8') as file:
    sys.stdout = file
    senior_one_field = Subject_generator(senior_one_data,const_conpitition_field_senior_one)
    senior_two_field = Subject_generator(senior_two_data,const_conpitition_field_senior_two)
    senior_tre_field = Subject_generator(senior_tre_data,const_conpitition_field_senior_tre)
    Out = list(zip(senior_one_field,senior_two_field,senior_tre_field))
    for i in Out:
        print("".join(i),end = "")
    sys.stdout = original_stdout

with open(dir+'Junior_track'+".txt", "w",encoding='UTF-8') as file:
    sys.stdout = file
    junior_one_track = Subject_generator(junior_one_data,const_conpitition_track_junior_one)
    junior_two_track = Subject_generator(junior_two_data,const_conpitition_track_junior_two)
    junior_tre_track = Subject_generator(junior_tre_data,const_conpitition_track_junior_tre)
    Out = list(zip(junior_one_track,junior_two_track,junior_tre_track))
    for i in Out:
        print("".join(i),end = "")
    sys.stdout = original_stdout

with open(dir+'Senior_track'+".txt", "w",encoding='UTF-8') as file:
    sys.stdout = file
    senior_one_track = Subject_generator(senior_one_data,const_conpitition_track_senior_one)
    senior_two_track = Subject_generator(senior_two_data,const_conpitition_track_senior_two)
    senior_tre_track = Subject_generator(senior_tre_data,const_conpitition_track_senior_tre)
    Out = list(zip(senior_one_track,senior_two_track,senior_tre_track))
    for i in Out:
        print("".join(i),end = "")
    sys.stdout = original_stdout

with open(dir+'Junior_relay'+".txt", "w",encoding='UTF-8') as file:
    sys.stdout = file
    relay_junior_one = relay_subject_generator(junior_one_data,const_team_conpitition_junior_one)
    relay_junior_two = relay_subject_generator(junior_two_data,const_team_conpitition_junior_two)
    relay_junior_tre = relay_subject_generator(junior_tre_data,const_team_conpitition_junior_tre)
    for i in relay_junior_one+relay_junior_two+relay_junior_tre:
        print("".join(i))
    sys.stdout = original_stdout

with open(dir+'Senior_relay'+".txt", "w",encoding='UTF-8') as file:
    sys.stdout = file
    relay_senior_one = relay_subject_generator(senior_one_data,const_team_conpitition_senior_one)
    relay_senior_two = relay_subject_generator(senior_two_data,const_team_conpitition_senior_two)
    relay_senior_tre = relay_subject_generator(senior_tre_data,const_team_conpitition_senior_tre)
    for i in relay_senior_one+relay_senior_two+relay_senior_tre:
        print("".join(i))
    sys.stdout = original_stdout
 