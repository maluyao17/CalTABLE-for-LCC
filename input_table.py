import re
import dataprocessing
import numpy as np
import pandas as pd
import math


def zip2list(A, B):
    C = np.vstack((A, B))
    return C

def cal_line(line, df, field, key):
    row = df[df['馈线名称']==line]
    if row.empty:
        value = 0.0
    else:
        if field in df.columns:
            if key == 'cal':
                value = np.float64(row[field].values[0])
            if key == 'find':
                value = row[field].values[0]
            if key == 'sum':
                value = row[field].sum()
        else:
            value = 0.0
    return value

def cal_trans(trans, df, field, key):
    row = df[df['配变名称']==trans]
    if row.empty:
        value = 0.0
    else:
        if field in df.columns:
            if key == 'cal':
                value = np.float64(row[field].values[0])
            if key == 'find':
                value = row[field].values[0]
            if key == 'sum':
                value = row[field].sum()
        else:
            value = 0.0
    return value

# def sum_line(line, df, field):
#     row = df[df['馈线名称']==line]
#     if row.empty:
#         value = 0.0
#     else:
#         if field in df.columns:
#             value = np.float16(row[field].values[0])
#         else:
#             value = 0.0
#     return value 

# def find_line(line, df, field):
#     row = df[df['馈线名称']==line]
#     if row.empty:
#         value = 0.0
#     else:
#         if field in df.columns:
#             # print(row['供电负荷性质'].values[0])
#             value = row[field].values[0]
#         else:
#             value = 0.0
#     return value

# def find_trans(trans, df, field):
#     row = df[df['变电站名称']==trans]
#     if row.empty:
#         value = 0.0
#     else:
#         if field in df.columns:
#             value = row[field].values[0]
#         else:
#             value = 0.0
#     return value

def find_distrans(trans, df, field, key):
    row = df[df['配变名称']==trans]
    if row.empty:
        value = 0.0
    else:
        if field in df.columns:
            if key == 'cal':
                value = row[field].values[0]
            if key == 'mean':
                value = row[field].mean()
        else:
            value = 0.0
    return value

# def low_Voltage(trans, df, )
class Input_table():
    def __init__(self, Pro_Lib, Ass_line, Ass_trans, Dis_Trans, mid_Volt, lowV_trans):
        # self.Pro_Lib, self.Ass_line, self.Ass_trans = dataprocessing.read_ProjectLib()
        # self.Dis_Trans = dataprocessing.read_DistributionTrans()
        # self.mid_Volt = dataprocessing.read_MidVoltage()
        # self.lowV_trans = dataprocessing.read_lowVtrans()

        self.Pro_Lib = Pro_Lib
        self.Ass_line = Ass_line
        self.Ass_trans = Ass_trans
        self.Dis_Trans = Dis_Trans
        self.mid_Volt = mid_Volt
        self.lowV_trans = lowV_trans
        self.Pro_Lib = dataprocessing.insert_corLineTrans(self.Pro_Lib, 'ProLib', self.Ass_line, self.Ass_trans)

        self.df_dt = pd.read_csv('Sheet_lowVtrans.csv')
        self.df_l = pd.read_csv('Sheet_MidVoltage.csv')
        self.dl_t = pd.read_csv('Sheet_trans.csv')
    def InputTable(self):

        # 项目名称
        self.pro_name = np.array([tmp[0] for tmp in self.Pro_Lib])

        # 项目初始投资
        self.pro_invest = [tmp[24] for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_name, self.pro_invest)

        # 10kV变压器
        self.trans10 = [tmp[48] for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.trans10)

        # 中压架空线
        self.medium_line = [(np.float16(tmp[38])+np.float16(tmp[40])) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.medium_line)
        

        # 中压电缆
        self.medium_cable = [tmp[36] for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.medium_cable)

        # 中压柜
        self.medium_switchgear = [tmp[42] for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.medium_switchgear)

        # 低压架空线
        self.low_line = [(tmp[51]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.low_line)

        # 低压电缆
        self.low_cable = [0] * len(self.Pro_Lib)
        self.pro_list = zip2list(self.pro_list, self.low_cable)

        # 低压柜
        self.low_switchgear = [tmp[52] for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.low_switchgear)

        # 关联馈线
        # cor_line = [(tmp[0]) for tmp in self.Ass_line]
        self.cor_line = [(tmp[7]).split(',')[0] for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.cor_line)

        # 关联配变
        self.cor_trans = [(tmp[9]).split(',')[0] for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.cor_trans)
        
        # 项目类别
        self.pro_class = [(tmp[18]) for tmp in self.Pro_Lib]
        # self.pro_list = zip2list(self.pro_list, pro_class)

        # 关联数目
        self.cor_amount = [0]*len(self.pro_class)
        for i in range(len(self.pro_class)):
            if self.pro_class[i] == '低压配电网项目':
                self.cor_amount[i] = self.Ass_trans[i][3]
                if self.pro_name[i] == '新增配变解决110kV里美变电站10kV龙美线10kV和平下厝高厝围仔公用台变配变预过载':
                     print('---------------------------------------')
                     print(self.Ass_trans[i][3])
            else:
                self.cor_amount[i] = self.Ass_line[i][6]
                if self.pro_name[i] == '新增配变解决110kV里美变电站10kV龙美线10kV和平下厝高厝围仔公用台变配变预过载':
                     print('---------------------------------------')
                     print(self.Ass_line[i][6])
        self.pro_list = zip2list(self.pro_list, self.cor_amount)
        self.pro_list = zip2list(self.pro_list, self.pro_class)

        # 供电分区
        self.supply_zone = [(tmp[15]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.supply_zone)

        # 问题编码
        self.error_code = [(tmp[108]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.error_code)
        # print('---------------------------------------------')
        # print(self.error_code)

        # 报装容量
        self.capacity = [0] * len(self.Pro_Lib)
        self.pro_list = zip2list(self.pro_list, self.capacity)

        # 关联馈线供电量计算
        self.power_line = np.zeros([len(self.Ass_line), 10])
        for i in range(len(self.Ass_line)):
            for j in range(0, 6):
                if self.Ass_line[i][j] != '0.0':
                    self.power_line[i][j] = cal_line(self.Ass_line[i][j], self.df_l, '年供电量(kWh)', 'cal')   # 计算馈线供电量

        # 关联台区供电量计算
        self.power_trans = np.zeros([len(self.Ass_trans), 10])

        for i in range(len(self.Ass_trans)):
            for j in range(0, 3):
                if self.Ass_trans[i][j] != '0.0':
                    self.power_trans[i][j] = cal_trans(self.Ass_trans[i][j], self.dl_t, '供电量(kWh)', 'cal') # 计算变电站供电量

        # 关联馈线/配变年供电量
        self.cor_powerSupply = [0]*len(self.pro_class)
        for i in range(len(self.pro_class)):
            if self.pro_class[i] == '低压配电网项目':
                self.cor_powerSupply[i] = 1.5*sum(self.power_trans[i,:])
            else:
                if self.cor_amount[i]!=0:
                    self.cor_powerSupply[i] = 1.5*sum(self.power_line[i,:])
            if self.pro_name[i] == '新增配变解决110kV铜盂变电站10kV溪西线溪西9#公用台变解决电压偏低':
                print("--------245245----------------")
                print(self.cor_powerSupply[i])
                print(self.power_trans[i,:])
                print(self.power_line[i,:])
                print("----------2452452-------------")
        self.pro_list = zip2list(self.pro_list, self.cor_powerSupply)


        # 关联馈线新增环网柜数
        self.ring_network = [np.int16((np.float16(tmp[56])/4.0+np.float16(tmp[58]))) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.ring_network)

        # 关联馈线柱上开关总数
        self.line_switch = [(tmp[57]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.line_switch)

        # 新增线路回数
        self.new_line = [(tmp[89]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.new_line)

        # 新增台区数
        self.new_trans = [(tmp[90]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.new_trans)

        # 退役配变容量
        self.retired_transCap = [tmp[124] if tmp[124]!='' else 0 for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.retired_transCap)

        # 新增配变容量
        self.new_transCap = [(tmp[49]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.new_transCap)

        # 项目目的
        self.pro_types = [(tmp[92]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.pro_types)

        # 所属供电分区
        self.power_partition = [str(0)]*len(self.pro_class)
        for i in range(len(self.pro_class)):
            if self.pro_class[i] == '低压配电网项目':
                self.power_partition[i] = cal_trans(self.cor_trans[i], self.dl_t, '负荷性质', 'find')    # 查询负荷性质
            else:
                self.power_partition[i] = cal_line(self.cor_line[i], self.df_l, '供电负荷性质', 'find')  # 查询供电负荷性质
        self.pro_list = zip2list(self.pro_list, self.power_partition)

        # 关联线路的中压用户数
        self.cor_mediumUser = [0]*len(self.pro_class)
        for i in range(len(self.pro_class)):
            if self.pro_class[i] == '低压配电网项目':
                self.cor_mediumUser[i] = 1
            else:
                # for j in range(len(self.Ass_line)):
                for k in range(6):
                    if self.Ass_line[i][k] != '0.0':
                        # print(medium_User(self.Ass_line[j][k], self.df_l))
                        self.cor_mediumUser[i] += cal_line(self.Ass_line[i][k], self.df_l, '装接配变总数', 'find')    # 查询装接配变总数
            if self.cor_mediumUser[i] == 0:  
                self.cor_mediumUser[i] = 20
        self.pro_list = zip2list(self.pro_list, self.cor_mediumUser)

        # 电压等级
        self.voltage_level = [(tmp[17]) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.voltage_level)

        # 过载时间
        self.overload_time = [0]*len(self.pro_types)
        for i in range(len(self.pro_types)):
            if self.pro_types[i] == '解决中压线路过载':
                self.overload_time[i] = cal_line(self.Pro_Lib[i][157], self.df_l, '过载累计持续时间(h)', 'find') # 查询过载累计持续时间(h)
            elif self.pro_types[i] == '解决配变过载':
                self.overload_time[i] = cal_trans(self.Pro_Lib[i][158], self.dl_t, '过载累计持续时间(min)', 'find') # 查询过载累计持续时间(min)
            if self.overload_time[i] == '':
                self.overload_time[i] = 0
        self.pro_list = zip2list(self.pro_list, self.overload_time)

        # 年最大安全电流
        self.annual_maxI = [0]*len(self.pro_types)
        for i in range(0, len(self.Pro_Lib)):
            self.annual_maxI[i] = cal_line(self.Pro_Lib[i][157], self.df_l, '年最大电流(A)', 'find') # 查询年最大电流(A)
        self.pro_list = zip2list(self.pro_list, self.annual_maxI)

        # 安全电流
        self.safe_I = self.annual_maxI
        self.pro_list = zip2list(self.pro_list, self.safe_I)

        # 额定容量
        self.Sn = [0]*len(self.pro_types)
        for i in range(0, len(self.Pro_Lib)):
            self.Sn[i] = find_distrans(self.Pro_Lib[i][158], self.dl_t, '额定容量(kVA)', 'cal') # 查询额定容量(kVA)
        self.pro_list = zip2list(self.pro_list, self.Sn)

        # 最大负载率
        self.max_loadRate = [0]*len(self.pro_types)
        for i in range(0, len(self.Pro_Lib)):
            self.max_loadRate[i] = find_distrans(self.Pro_Lib[i][158], self.dl_t, '年最高负载率(%)', 'cal') # 年最高负载率(%)
        self.pro_list = zip2list(self.pro_list, self.max_loadRate)

        # 新增自动化点
        self.new_automation = [np.int16(np.float16(tmp[56])/4.0+np.float16(tmp[57])+np.float16(tmp[58])) for tmp in self.Pro_Lib]
        self.pro_list = zip2list(self.pro_list, self.new_automation)

        # 配变末端电压
        self.trans_TerminalV = [0]*len(self.pro_types)

        for i in range(0, len(self.Pro_Lib)):
            if self.pro_class[i] == '低压配电网项目':
                self.trans_TerminalV[i] = find_distrans(self.Pro_Lib[i][158], self.dl_t, '末端电压最小值(V)', 'cal')
            else:
                tmp_sum = 0.0
                # self.trans_TerminalV[i] = 0.0
                for j in range(141, 146):
                    if self.Pro_Lib[i][j] == '0':
                        break
                    tmp_sum += cal_line(self.Pro_Lib[i][j], self.df_dt, '首端电压最小值(V)', 'sum')
                    # k += 1
                if self.cor_amount[i] != 0:
                    self.trans_TerminalV[i] = tmp_sum/np.float16(self.cor_amount[i])
                if math.isnan(self.trans_TerminalV[i]) :
                    self.trans_TerminalV[i] = 220



        # 低电压台区个数
        self.lowV_trans = [0]*len(self.pro_types)
        self.tmp_acount = [0]*len(self.pro_types)
        for i in range(0, len(self.Pro_Lib)):
            if self.pro_class[i] == '低压配电网项目':
                if self.trans_TerminalV[i] > 198:
                    self.lowV_trans[i] = 0
                else:
                    if self.Pro_Lib[i][158] == 0:
                        self.lowV_trans[i] = 0
                    else:
                        tmp = set(self.Pro_Lib[i][158].split(","))
                        if tmp != {'0'} and tmp !={''}:
                            self.lowV_trans[i] = len(tmp)
                        if self.pro_name[i] == '新增配变解决110kV东洋站10kV西新线10kV贵屿西美村4#公用台变电压偏低':
                             print('xiixixixixixiixixiiiiiiiiixiixixixixixixix')
                             print(tmp)
                                           
            else:
                for j in range(141, 146):
                    if self.Pro_Lib[i][j] == '0':
                        break
                    if ((self.df_dt[self.df_dt['馈线名称'] == self.Pro_Lib[i][j]]).empty)==False:
                        self.tmp_acount[i] += 1
                self.lowV_trans[i] = self.tmp_acount[i]
                
        self.pro_list = zip2list(self.pro_list, self.lowV_trans)
        self.pro_list = zip2list(self.pro_list, self.trans_TerminalV)
        self.pro_list = np.transpose(self.pro_list)
        self.pro_list = dataprocessing.insert_corLineTrans(self.pro_list, 'self.pro_list', self.Ass_line, self.Ass_trans)
        return self.Pro_Lib, self.Ass_line, self.Ass_trans, self.Dis_Trans, self.mid_Volt, self.lowV_trans, self.pro_list