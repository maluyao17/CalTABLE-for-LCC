import pandas as pd
import csv
import numpy as np
import os

# 项目库表
def read_ProjectLib():
    data = []
    if os.path.exists('Sheet_pro.csv') == 0:
        data_xls = pd.read_excel('项目库表.xlsx',index_col=0)
        data_xls.to_csv('Sheet_pro.csv', encoding='utf-8')
    
    with open('Sheet_pro.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:179]:
                per_data.append(i)
            data.append(per_data)
    data = data[5:][:]


    ass_line = np.array(np.zeros([len(data),7]),dtype=str)
    # ass_trans = [] 
    for i in range(0,len(data)):
        tmp_ass_line = []
        if data[i][7] != '0':
            tmp = set(data[i][7].split(","))
            k = 0
            for j in tmp:
                if j not in tmp_ass_line and j != '' and j!='0':
                    tmp_ass_line.append(j)
                    ass_line[i][k] = j
                    k += 1
            ass_line[i][6] = k

    ass_trans = np.array(np.zeros([len(data),4]),dtype=str)
    # ass_trans = [] 
    for i in range(0,len(data)):
        tmp_ass_trans = []
        if data[i][9] != '0':
            tmp = set(data[i][9].split(","))
            k = 0
            for j in tmp:
                if j not in tmp_ass_trans and j != '' and j!='0':
                    tmp_ass_trans.append(j)
                    ass_trans[i][k] = j
                    k += 1
            ass_trans[i][3] = k
    # print(ass_line[i])
    return data, ass_line, ass_trans

# 配变表
def read_DistributionTrans():
    data = []
    if os.path.exists('Sheet_trans.csv') == 0:
        data_xls = pd.read_excel('配变表.xlsx',index_col=0)
        data_xls.to_csv('Sheet_trans.csv', encoding='utf-8')
    with open('Sheet_trans.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:-1]:
                per_data.append(i)
            data.append(per_data)
    data = data[2:][:]
    return data

# 中压线路表
def read_MidVoltage():
    data = []
    if os.path.exists('Sheet_MidVoltage.csv') == 0:
        data_xls = pd.read_excel('中压线路表.xlsx',index_col=0)
        data_xls.to_csv('Sheet_MidVoltage.csv', encoding='utf-8')
    with open('Sheet_MidVoltage.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:-1]:
                per_data.append(i)
            data.append(per_data)
    data = data[2:][:]
    return data

# 存在低电压问题配变的表
def read_lowVtrans():
    data = []
    if os.path.exists('Sheet_lowVtrans.csv') == 0:
        data_xls = pd.read_excel('存在低电压问题的配变表.xlsx',index_col=0)
        data_xls.to_csv('Sheet_lowVtrans.csv', encoding='utf-8')
    with open('Sheet_lowVtrans.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:-1]:
                per_data.append(i)
            data.append(per_data)
    data = data[2:][:]
    return data
    print("")
    
def insert_corLineTrans(input, key, line, trans):
    if key == 'ProLib':
        k = 0
        for i in range(141, 147):
            input[:][i] = line[:,k]
            k = k+1
        k = 0
        for i in range(151, 153):
            input[:][i] = trans[:,k]
    if key == 'pro_list':
        input = np.array(input)
        input = np.concatenate((input, np.array(line)), axis=1)
        input = np.concatenate((input, np.array(trans)), axis=1)
        input = input.tolist()
    return input

def save_scv(csv_name, data):
    with open(csv_name, 'w', encoding='utf-8', newline='') as sheet_input:
        writer = csv.writer(sheet_input)
        writer.writerow(['序号','项目名称','项目类别','项目目的','初始投资成本','运行成本','维护成本','故障成本','退役成本','总LCC', \
                    '增供电量效益','可靠性提升效益','提前更换残旧设备收益',	'低电压效益','总效益','总利润','单位投资效益','供电分区'])
        for row in data:
            writer.writerow(row)
    df = pd.read_csv(csv_name)
    output_file = "计算结果.xlsx"
    writer = pd.ExcelWriter(output_file, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    writer.save()

def read_ProjectLib_f(fname):
    data = []
    if os.path.exists('Sheet_pro.csv') == 0:
        data_xls = pd.read_excel(fname, index_col=0)
        data_xls.to_csv('Sheet_pro.csv', encoding='utf-8')
    
    with open('Sheet_pro.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:179]:
                per_data.append(i)
            data.append(per_data)
    data = data[5:][:]


    ass_line = np.array(np.zeros([len(data),7]),dtype=str)
    # ass_trans = [] 
    for i in range(0,len(data)):
        tmp_ass_line = []
        if data[i][7] != '0':
            tmp = set(data[i][7].split(","))
            k = 0
            for j in tmp:
                if j not in tmp_ass_line and j != '' and j!='0':
                    tmp_ass_line.append(j)
                    ass_line[i][k] = j
                    k += 1
            ass_line[i][6] = k

    ass_trans = np.array(np.zeros([len(data),4]),dtype=str)
    # ass_trans = [] 
    for i in range(0,len(data)):
        tmp_ass_trans = []
        if data[i][9] != '0':
            tmp = set(data[i][9].split(","))
            k = 0
            for j in tmp:
                if j not in tmp_ass_trans and j != '' and j!='0':
                    tmp_ass_trans.append(j)
                    ass_trans[i][k] = j
                    k += 1
            ass_trans[i][3] = k
    # print(ass_line[i])
    return data, ass_line, ass_trans


# 配变表
def read_DistributionTrans_f(fname):
    data = []
    if os.path.exists('Sheet_trans.csv') == 0:
        data_xls = pd.read_excel(fname,index_col=0)
        data_xls.to_csv('Sheet_trans.csv', encoding='utf-8')
    with open('Sheet_trans.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:-1]:
                per_data.append(i)
            data.append(per_data)
    data = data[2:][:]
    return data

# 中压线路表
def read_MidVoltage_f(fname):
    data = []
    if os.path.exists('Sheet_MidVoltage.csv') == 0:
        data_xls = pd.read_excel(fname,index_col=0)
        data_xls.to_csv('Sheet_MidVoltage.csv', encoding='utf-8')
    with open('Sheet_MidVoltage.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:-1]:
                per_data.append(i)
            data.append(per_data)
    data = data[2:][:]
    return data

# 存在低电压问题配变的表
def read_lowVtrans_f(fname):
    data = []
    if os.path.exists('Sheet_lowVtrans.csv') == 0:
        data_xls = pd.read_excel(fname,index_col=0)
        data_xls.to_csv('Sheet_lowVtrans.csv', encoding='utf-8')
    with open('Sheet_lowVtrans.csv', encoding="utf-8") as file_obj:
        file = csv.reader(file_obj)
        for row in file:
            per_data = []
            for i in row[1:-1]:
                per_data.append(i)
            data.append(per_data)
    data = data[2:][:]
    return data

if __name__ == '__main__':
    read_ProjectLib()
    read_DistributionTrans()