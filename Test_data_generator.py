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
const_conpitition_senior_two = ("高二男跳遠","高二女跳遠","高二男跳高","高二女跳高","高二男藥球","高二女藥球","高二女 100 公尺","高二男 100 公尺","高二女 400 公尺","高二男 400 公尺","高二女 800 公尺","高二男 1500 公尺")
const_conpitition_senior_tre = ("高三男跳遠","高三女跳遠","高三男跳高","高三女跳高","高三男藥球","高三女藥球","高三女 100 公尺","高三男 100 公尺","高三女 400 公尺","高三男 400 公尺","高三女 800 公尺","高三男 1500 公尺")

const_team_conpitition_senior_one = ("高一男生 400 公尺接力","高一女生 400 公尺接力")
const_team_conpitition_senior_two = ("高二男生 400 公尺接力","高二女生 400 公尺接力")
const_team_conpitition_senior_tre = ("高三男生 400 公尺接力","高三女生 400 公尺接力")

const_file_name_mid_element = ("3_1","4_1")
const_file_name_high_element = ("5_1","6_1")

const_file_name_junior_one = ("7_1","7_2","7_3","7_4")
const_file_name_junior_two = ("8_1","8_2","8_3","8_4")
const_file_name_junior_tre = ("9_1","9_2","9_3","9_4")

const_file_name_senior_one = ("10_1","10_2","10_3","10_4","10_5","10_6","10_7","10_8")
const_file_name_senior_two = ("11_1","11_2","11_3","11_4","11_5","11_6","11_7","11_8")
const_file_name_senior_tre = ("12_1","12_2","12_3","12_4","12_5","12_6","12_7","12_8")

const_class = ("仁","義","禮","智","信","忠","孝","和")

slice_data = [2,2,2,2,2,2,2,2,2,2,3,3,6,6
]
Json_dat = const_team_conpitition_senior_one

import json

for i in const_file_name_senior_one:
    Class = const_class[int(i[-1])-1]
    name = '高一'+ Class
    name_lis = [name+"%02d" % i for i in range(38)]
    slice = []
    for num in slice_data:
        slice.append(name_lis[:num])
        name_lis = name_lis[num:]
    dic = dict(zip(const_conpitition_senior_one+const_team_conpitition_senior_one,slice))
    
    union = [name+"%02d" % i for i in range(38)]
    dic.update([('union',union),('Grade',int(i[:2])),('Class',int(i[-1]))])
    json_dat = json.dumps(dic, indent=4,ensure_ascii = False)
    with open(i+".txt", "w",encoding='UTF-8') as file:
        file.write(json_dat)

for i in const_file_name_senior_two:
    Class = const_class[int(i[-1])-1]
    name = '高二'+ Class
    name_lis = [name+"%02d" % i for i in range(38)]
    slice = []
    for num in slice_data:
        slice.append(name_lis[:num])
        name_lis = name_lis[num:]
    dic = dict(zip(const_conpitition_senior_two+const_team_conpitition_senior_two,slice))

    union = [name+"%02d" % i for i in range(38)]
    dic.update([('union',union),('Grade',int(i[:2])),('Class',int(i[-1]))])
    json_dat = json.dumps(dic, indent=4,ensure_ascii = False)
    with open(i+".txt", "w",encoding='UTF-8') as file:
        file.write(json_dat)
    
for i in const_file_name_senior_tre:
    Class = const_class[int(i[-1])-1]
    name = '高三'+ Class 
    name_lis = [name+"%02d" % i for i in range(38)]
    slice = []
    for num in slice_data:
        slice.append(name_lis[:num])
        name_lis = name_lis[num:]
    dic = dict(zip(const_conpitition_senior_tre+const_team_conpitition_senior_tre,slice))
    
    union = [name+"%02d" % i for i in range(38)]
    dic.update([('union',union),('Grade',int(i[:2])),('Class',int(i[-1]))])
    json_dat = json.dumps(dic, indent=4,ensure_ascii = False)
    with open(i+".txt", "w",encoding='UTF-8') as file:
        file.write(json_dat)

for i in const_file_name_junior_one:
    Class = const_class[int(i[-1])-1]
    name = '國一'+ Class 
    name_lis = [name+"%02d" % i for i in range(38)]
    slice = []
    for num in slice_data:
        slice.append(name_lis[:num])
        name_lis = name_lis[num:]
    dic = dict(zip(const_conpitition_junior_one+const_team_conpitition_junior_one,slice))
    
    union = [name+"%02d" % i for i in range(38)]
    dic.update([('union',union),('Grade',int(i[:1])),('Class',int(i[-1]))])
    json_dat = json.dumps(dic, indent=4,ensure_ascii = False)
    with open(i+".txt", "w",encoding='UTF-8') as file:
        file.write(json_dat)

for i in const_file_name_junior_two:
    Class = const_class[int(i[-1])-1]
    name = '國二'+ Class 
    name_lis = [name+"%02d" % i for i in range(38)]
    slice = []
    for num in slice_data:
        slice.append(name_lis[:num])
        name_lis = name_lis[num:]
    dic = dict(zip(const_conpitition_junior_two+const_team_conpitition_junior_two,slice))
    
    union = [name+"%02d" % i for i in range(38)]
    dic.update([('union',union),('Grade',int(i[:1])),('Class',int(i[-1]))])
    json_dat = json.dumps(dic, indent=4,ensure_ascii = False)
    with open(i+".txt", "w",encoding='UTF-8') as file:
        file.write(json_dat)

for i in const_file_name_junior_tre:
    Class = const_class[int(i[-1])-1]
    name = '國三'+ Class 
    name_lis = [name+"%02d" % i for i in range(38)]
    slice = []
    for num in slice_data:
        slice.append(name_lis[:num])
        name_lis = name_lis[num:]
    dic = dict(zip(const_conpitition_junior_tre+const_team_conpitition_junior_tre,slice))
    
    union = [name+"%02d" % i for i in range(38)]
    dic.update([('union',union),('Grade',int(i[:1])),('Class',int(i[-1]))])
    json_dat = json.dumps(dic, indent=4,ensure_ascii = False)
    with open(i+".txt", "w",encoding='UTF-8') as file:
        file.write(json_dat)