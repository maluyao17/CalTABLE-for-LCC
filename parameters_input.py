import pandas as pd
def fixed_input_shantou(paraClass):
    paraClass.repairCost_Mtrans = 0.5839
    paraClass.repairCost_Mline = 23.9692  
    paraClass.repairCost_Mcable = 2.586
    paraClass.repairCost_Munits = 0.4619
    paraClass.repairCost_Lline = 3.7077
    paraClass.repairCost_Lcable = 3.7077
    paraClass.repairCost_Lunits = 6.6825
    
    paraClass.faultCost_Mtrans = 0.0
    paraClass.faultCost_Mline = 0.0
    paraClass.faultCost_Mcable = 0.0
    paraClass.faultCost_Munits = 0.0
    paraClass.faultCost_Lline = 0.0
    paraClass.faultCost_Lcable = 0.0
    paraClass.faultCost_Lunits = 0.0

    paraClass.removalCost_Mtrans = 0.2806
    paraClass.removalCost_Mline = 0.1148 
    paraClass.removalCost_Mcable = 2.2081
    paraClass.removalCost_Munits = 0.5835
    paraClass.removalCost_Lline = 0.0907
    paraClass.removalCost_Lcable = 1.7300
    paraClass.removalCost_Lunits = 0.1085
    
    paraClass.purchase_price = 0.31
    paraClass.DisTran_lossRate = 0.025
    paraClass.linePerLen_lossRate = 0.003

    ### reliability para
    paraClass.overload_line_factor = 0.6
    paraClass.overload_line_invest = 2013
    paraClass.overload_line_rely = paraClass.overload_line_factor*paraClass.overload_line_invest
    reliable_investment = paraClass.overload_line_rely

    paraClass.highload_line_factor = 0.5
    paraClass.highload_line_invest = 7953
    paraClass.highload_line_rely = paraClass.highload_line_factor*paraClass.highload_line_invest
    reliable_investment += paraClass.highload_line_rely

    paraClass.overload_trans_factor = 0.6
    paraClass.overload_trans_invest = 3165
    paraClass.overload_trans_rely = paraClass.overload_trans_factor*paraClass.overload_trans_invest
    reliable_investment += paraClass.overload_trans_rely

    paraClass.highload_trans_factor = 0.5
    paraClass.highload_trans_invest = 5100
    paraClass.highload_trans_rely = paraClass.highload_trans_factor*paraClass.highload_trans_invest
    reliable_investment += paraClass.highload_trans_rely

    paraClass.newload_line_factor = 0.3
    paraClass.newload_line_invest = 31486
    paraClass.newload_line_rely = paraClass.newload_line_factor*paraClass.newload_line_invest
    reliable_investment += paraClass.newload_line_rely

    paraClass.newload_trans_factor = 0.3
    paraClass.newload_trans_invest = 8541
    paraClass.newload_trans_rely = paraClass.newload_trans_factor*paraClass.newload_trans_invest
    reliable_investment += paraClass.newload_trans_rely

    paraClass.modify_trans_factor = 0.3
    paraClass.modify_trans_invest = 392
    paraClass.modify_trans_rely = paraClass.modify_trans_factor*paraClass.modify_trans_invest
    reliable_investment += paraClass.modify_trans_rely

    paraClass.safety_line_factor = 1
    paraClass.safety_line_invest = 0
    paraClass.safety_line_rely = paraClass.safety_line_factor*paraClass.safety_line_invest
    reliable_investment += paraClass.safety_line_rely

    paraClass.lowV_trans_factor = 0.3
    paraClass.lowV_trans_invest = 1293
    paraClass.lowV_trans_rely = paraClass.lowV_trans_factor*paraClass.lowV_trans_invest
    reliable_investment += paraClass.lowV_trans_rely

    paraClass.netRack_factor = 1
    paraClass.netRack_invest = 11975
    paraClass.netRack_rely = paraClass.netRack_factor*paraClass.netRack_invest
    reliable_investment += paraClass.netRack_rely

    paraClass.replace_factor = 1
    paraClass.replace_invest = 104
    paraClass.replace_rely = paraClass.replace_factor*paraClass.replace_invest
    reliable_investment += paraClass.replace_rely

    paraClass.auto_factor = 1
    paraClass.auto_invest = 7937
    paraClass.auto_rely = paraClass.auto_factor*paraClass.auto_invest
    reliable_investment += paraClass.auto_rely

    paraClass.outage_user_last = 0.2
    paraClass.amount_user_last = 29000

    paraClass.outage_user = None
    paraClass.amount_user = None

    paraClass.outage_user_reduce = 5800
    
    paraClass.reliable_investment = reliable_investment

    paraClass.could_reduce_users = paraClass.outage_user_reduce/paraClass.reliable_investment

    paraClass.middle_newAuto = 468
    paraClass.middle_project = 170
    paraClass.low_project = 334
    paraClass.ave_users = 20
    paraClass.ave_proInvest = 1
    paraClass.ave_adjusted = (paraClass.middle_newAuto/4+paraClass.middle_project/paraClass.ave_users)/(paraClass.middle_project+paraClass.low_project)/paraClass.ave_proInvest

    paraClass.region_GDP = 3017
    paraClass.region_supply = 240
    paraClass.GDP_SUPPLY = paraClass.region_GDP/paraClass.region_supply

    paraClass.ave_middle_users = paraClass.ave_users

    paraClass.discount_rate = 0.07
    paraClass.rely_discount_rate = [0]*30
    paraClass.rely_discount_rate[0] = 1
    for i in range(2, 31):
        paraClass.rely_discount_rate[i-1] = 1/(pow((1+paraClass.discount_rate),(i-1)))
    
    paraClass.sum_rely_discount_rate = sum(paraClass.rely_discount_rate)
    paraClass.overload_lackpower_factor = 1

    paraClass.punish_factor = [5, 3.5, 4, 11.25, 4.5, 5.75]

    paraClass.Guangzhou = [8.25, 3.75, 6.25, 16.25, 7.25, 7.5]
    paraClass.santou = [5, 3.5, 4, 11.25, 4.5, 5.75]
    paraClass.Foshan = [8.25, 3.75, 6, 15, 7.25, 7.5]
    paraClass.region = paraClass.santou
    # Increase power supply
    paraClass.Add_line_aveLoad = 0.2
    paraClass.Add_trans_aveLoad = 0.3
    paraClass.max_supplyAbility = 8800

    paraClass.growth_rate = 0.05
    paraClass.sales_profit = 0.15
    paraClass.years_to_saturation = 20
    
    paraClass.scale_line_factor = 0.7
    paraClass.scale_trans_factor = 0.7

    paraClass.K_0 = 4

    paraClass.radius_low = [0.15, 0.15, 0.25, 0.4, 0.5]
    paraClass.radius_middle = [2.4, 2.4, 4, 4, 12]

    paraClass.aveLoad_line = [0.2, 0.2, 0.2, 0.2, 0.2]
    paraClass.aveLoad_trans = [0.3, 0.3, 0.3, 0.3, 0.3]

    paraClass.lowV_in_years = 0.01

    paraClass.unqualified = 0.008

def fixed_input_foshan(paraClass):
    paraClass.repairCost_Mtrans = 0.968
    paraClass.repairCost_Mline = 28.539  
    paraClass.repairCost_Mcable = 2.2248
    paraClass.repairCost_Munits = 0.0606
    paraClass.repairCost_Lline = 26.3059
    paraClass.repairCost_Lcable = 26.3059
    paraClass.repairCost_Lunits = 0.3546
    
    paraClass.faultCost_Mtrans = 0.0
    paraClass.faultCost_Mline = 0.0
    paraClass.faultCost_Mcable = 0.0
    paraClass.faultCost_Munits = 0.0
    paraClass.faultCost_Lline = 0.0
    paraClass.faultCost_Lcable = 0.0
    paraClass.faultCost_Lunits = 0.0

    paraClass.removalCost_Mtrans = 0.2806
    paraClass.removalCost_Mline = 0.1148 
    paraClass.removalCost_Mcable = 2.2081
    paraClass.removalCost_Munits = 0.5835
    paraClass.removalCost_Lline = 0.0907
    paraClass.removalCost_Lcable = 1.7300
    paraClass.removalCost_Lunits = 0.1085
    
    paraClass.purchase_price = 0.43
    paraClass.DisTran_lossRate = 0.025
    paraClass.linePerLen_lossRate = 0.003

    ### reliability para
    paraClass.overload_line_factor = 0.6
    paraClass.overload_line_invest = 4333.6
    paraClass.overload_line_rely = paraClass.overload_line_factor*paraClass.overload_line_invest
    reliable_investment = paraClass.overload_line_rely

    paraClass.highload_line_factor = 0.5
    paraClass.highload_line_invest = 7781.38
    paraClass.highload_line_rely = paraClass.highload_line_factor*paraClass.highload_line_invest
    reliable_investment += paraClass.highload_line_rely

    paraClass.overload_trans_factor = 0.6
    paraClass.overload_trans_invest = 4797.41
    paraClass.overload_trans_rely = paraClass.overload_trans_factor*paraClass.overload_trans_invest
    reliable_investment += paraClass.overload_trans_rely

    paraClass.highload_trans_factor = 0.5
    paraClass.highload_trans_invest = 13346.19
    paraClass.highload_trans_rely = paraClass.highload_trans_factor*paraClass.highload_trans_invest
    reliable_investment += paraClass.highload_trans_rely

    paraClass.newload_line_factor = 0.3
    paraClass.newload_line_invest = 26525.75
    paraClass.newload_line_rely = paraClass.newload_line_factor*paraClass.newload_line_invest
    reliable_investment += paraClass.newload_line_rely

    paraClass.newload_trans_factor = 0.3
    paraClass.newload_trans_invest = 29193.64
    paraClass.newload_trans_rely = paraClass.newload_trans_factor*paraClass.newload_trans_invest
    reliable_investment += paraClass.newload_trans_rely

    paraClass.modify_trans_factor = 0.3
    paraClass.modify_trans_invest = 964.97
    paraClass.modify_trans_rely = paraClass.modify_trans_factor*paraClass.modify_trans_invest
    reliable_investment += paraClass.modify_trans_rely

    paraClass.safety_line_factor = 1
    paraClass.safety_line_invest = 1074.73
    paraClass.safety_line_rely = paraClass.safety_line_factor*paraClass.safety_line_invest
    reliable_investment += paraClass.safety_line_rely

    paraClass.lowV_trans_factor = 0.3
    paraClass.lowV_trans_invest = 7038.63
    paraClass.lowV_trans_rely = paraClass.lowV_trans_factor*paraClass.lowV_trans_invest
    reliable_investment += paraClass.lowV_trans_rely

    paraClass.netRack_factor = 1
    paraClass.netRack_invest = 76742.31
    paraClass.netRack_rely = paraClass.netRack_factor*paraClass.netRack_invest
    reliable_investment += paraClass.netRack_rely

    paraClass.replace_factor = 1
    paraClass.replace_invest = 2212.71
    paraClass.replace_rely = paraClass.replace_factor*paraClass.replace_invest
    reliable_investment += paraClass.replace_rely

    paraClass.auto_factor = 1
    paraClass.auto_invest = 14988.68
    paraClass.auto_rely = paraClass.auto_factor*paraClass.auto_invest
    reliable_investment += paraClass.auto_rely

    paraClass.outage_user_last = 0.25
    paraClass.amount_user_last = 60386

    paraClass.outage_user = None
    paraClass.amount_user = None

    paraClass.outage_user_reduce = 15096.5
    
    paraClass.reliable_investment = reliable_investment

    paraClass.could_reduce_users = paraClass.outage_user_reduce/paraClass.reliable_investment

    paraClass.middle_newAuto = 292
    paraClass.middle_project = 206
    paraClass.low_project = 354
    paraClass.ave_users = 20
    paraClass.ave_proInvest = 1
    paraClass.ave_adjusted = 0.3632

    paraClass.region_GDP = 12698.39
    paraClass.region_supply = 768
    paraClass.GDP_SUPPLY = paraClass.region_GDP/paraClass.region_supply

    paraClass.ave_middle_users = paraClass.ave_users

    paraClass.discount_rate = 0.07
    paraClass.rely_discount_rate = [0]*30
    paraClass.rely_discount_rate[0] = 1
    for i in range(2, 31):
        paraClass.rely_discount_rate[i-1] = 1/(pow((1+paraClass.discount_rate),(i-1)))
    
    paraClass.sum_rely_discount_rate = sum(paraClass.rely_discount_rate)
    paraClass.overload_lackpower_factor = 1

    paraClass.punish_factor = [8.25, 3.75, 6, 15, 7.25, 7.5]

    paraClass.Guangzhou = [8.25, 3.75, 6.25, 16.25, 7.25, 7.5]
    paraClass.Foshan = [8.25, 3.75, 6, 15, 7.25, 7.5]
    paraClass.region = paraClass.Foshan
    # Increase power supply
    paraClass.Add_line_aveLoad = 0.2
    paraClass.Add_trans_aveLoad = 0.3
    paraClass.max_supplyAbility = 8417.76

    paraClass.growth_rate = 0.05
    paraClass.sales_profit = 0.18
    paraClass.years_to_saturation = 20
    
    paraClass.scale_line_factor = 0.7
    paraClass.scale_trans_factor = 0.7

    paraClass.K_0 = 4

    paraClass.radius_low = [0.15, 0.15, 0.25, 0.4, 0.5]
    paraClass.radius_middle = [2.4, 2.4, 4, 4, 12]

    paraClass.aveLoad_line = [0.2, 0.2, 0.2, 0.2, 0.2]
    paraClass.aveLoad_trans = [0.3, 0.3, 0.3, 0.3, 0.3]

    paraClass.lowV_in_years = 0.01

    paraClass.unqualified = 0.02

def auto_input(paraClass):
    df = pd.read_excel('固定参数.xlsx')
    paraClass.repairCost_Mtrans = df.iloc[4, 9]
    paraClass.repairCost_Mline = df.iloc[4, 10]
    paraClass.repairCost_Mcable = df.iloc[4, 11]
    paraClass.repairCost_Munits = df.iloc[4, 12]
    paraClass.repairCost_Lline = df.iloc[4, 13]
    paraClass.repairCost_Lcable = df.iloc[4, 14]
    paraClass.repairCost_Lunits = df.iloc[4, 15]


    paraClass.faultCost_Mtrans = df.iloc[5, 9]
    paraClass.faultCost_Mline = df.iloc[5, 10]
    paraClass.faultCost_Mcable = df.iloc[5, 11]
    paraClass.faultCost_Munits = df.iloc[5, 12]
    paraClass.faultCost_Lline = df.iloc[5, 13]
    paraClass.faultCost_Lcable = df.iloc[5, 14]
    paraClass.faultCost_Lunits = df.iloc[5, 15]

    paraClass.removalCost_Mtrans = df.iloc[6, 9]
    paraClass.removalCost_Mline = df.iloc[6, 10]
    paraClass.removalCost_Mcable = df.iloc[6, 11]
    paraClass.removalCost_Munits = df.iloc[6, 12]
    paraClass.removalCost_Lline = df.iloc[6, 13]
    paraClass.removalCost_Lcable = df.iloc[6, 14]
    paraClass.removalCost_Lunits = df.iloc[6, 15]

    paraClass.purchase_price = df.iloc[10, 8]
    paraClass.DisTran_lossRate = df.iloc[10, 9]
    paraClass.linePerLen_lossRate = df.iloc[10, 10]

    ### reliability para
    paraClass.overload_line_factor = df.iloc[19, 9]
    paraClass.overload_line_invest = df.iloc[19, 10]
    paraClass.overload_line_rely = paraClass.overload_line_factor*paraClass.overload_line_invest
    reliable_investment = paraClass.overload_line_rely

    paraClass.highload_line_factor = df.iloc[20, 9]
    paraClass.highload_line_invest = df.iloc[20, 10]
    paraClass.highload_line_rely = paraClass.highload_line_factor*paraClass.highload_line_invest
    reliable_investment += paraClass.highload_line_rely

    paraClass.overload_trans_factor = df.iloc[21, 9]
    paraClass.overload_trans_invest = df.iloc[21, 10]
    paraClass.overload_trans_rely = paraClass.overload_trans_factor*paraClass.overload_trans_invest
    reliable_investment += paraClass.overload_trans_rely

    paraClass.highload_trans_factor = df.iloc[22, 9]
    paraClass.highload_trans_invest = df.iloc[22, 10]
    paraClass.highload_trans_rely = paraClass.highload_trans_factor*paraClass.highload_trans_invest
    reliable_investment += paraClass.highload_trans_rely

    paraClass.newload_line_factor = df.iloc[23, 9]
    paraClass.newload_line_invest = df.iloc[23, 10]
    paraClass.newload_line_rely = paraClass.newload_line_factor*paraClass.newload_line_invest
    reliable_investment += paraClass.newload_line_rely

    paraClass.newload_trans_factor = df.iloc[24, 9]
    paraClass.newload_trans_invest = df.iloc[24, 10]
    paraClass.newload_trans_rely = paraClass.newload_trans_factor*paraClass.newload_trans_invest
    reliable_investment += paraClass.newload_trans_rely

    paraClass.modify_trans_factor = df.iloc[25, 9]
    paraClass.modify_trans_invest = df.iloc[25, 10]
    paraClass.modify_trans_rely = paraClass.modify_trans_factor*paraClass.modify_trans_invest
    reliable_investment += paraClass.modify_trans_rely

    paraClass.safety_line_factor = df.iloc[26, 9]
    paraClass.safety_line_invest = df.iloc[26, 10]
    paraClass.safety_line_rely = paraClass.safety_line_factor*paraClass.safety_line_invest
    reliable_investment += paraClass.safety_line_rely

    paraClass.lowV_trans_factor = df.iloc[27, 9]
    paraClass.lowV_trans_invest = df.iloc[27, 10]
    paraClass.lowV_trans_rely = paraClass.lowV_trans_factor*paraClass.lowV_trans_invest
    reliable_investment += paraClass.lowV_trans_rely

    paraClass.netRack_factor = df.iloc[28, 9]
    paraClass.netRack_invest = df.iloc[28, 10]
    paraClass.netRack_rely = paraClass.netRack_factor*paraClass.netRack_invest
    reliable_investment += paraClass.netRack_rely

    paraClass.replace_factor = df.iloc[29, 9]
    paraClass.replace_invest = df.iloc[29, 10]
    paraClass.replace_rely = paraClass.replace_factor*paraClass.replace_invest
    reliable_investment += paraClass.replace_rely

    paraClass.auto_factor = df.iloc[30, 9]
    paraClass.auto_invest = df.iloc[30, 10]
    paraClass.auto_rely = paraClass.auto_factor*paraClass.auto_invest
    reliable_investment += paraClass.auto_rely

    paraClass.outage_user_last = df.iloc[18, 15]
    paraClass.amount_user_last = df.iloc[18, 16]

    paraClass.outage_user = df.iloc[18, 17]
    paraClass.amount_user = df.iloc[18, 18]

    paraClass.outage_user_reduce = df.iloc[18, 19]
    
    paraClass.reliable_investment = reliable_investment

    paraClass.could_reduce_users = paraClass.outage_user_reduce/paraClass.reliable_investment

    paraClass.middle_newAuto = df.iloc[18, 23]
    paraClass.middle_project = df.iloc[18, 24]
    paraClass.low_project = df.iloc[18, 25]
    paraClass.ave_users = df.iloc[18, 26]
    paraClass.ave_proInvest = df.iloc[18, 27]
    paraClass.ave_adjusted = df.iloc[18, 28]

    paraClass.region_GDP = df.iloc[21, 15]
    paraClass.region_supply = df.iloc[21, 16]
    paraClass.GDP_SUPPLY = paraClass.region_GDP/paraClass.region_supply

    paraClass.ave_middle_users = paraClass.ave_users

    paraClass.discount_rate = df.iloc[3,2]
    paraClass.rely_discount_rate = [0]*30
    paraClass.rely_discount_rate[0] = 1
    for i in range(2, 31):
        paraClass.rely_discount_rate[i-1] = 1/(pow((1+paraClass.discount_rate),(i-1)))
    
    paraClass.sum_rely_discount_rate = sum(paraClass.rely_discount_rate)
    paraClass.overload_lackpower_factor = df.iloc[21, 23]

    paraClass.punish_factor = [df.iloc[25, 16], df.iloc[26, 16], df.iloc[27, 16], df.iloc[28, 16], df.iloc[29, 16],
                            df.iloc[30, 16]]

    paraClass.Guangzhou = [df.iloc[25, 21], df.iloc[26, 21], df.iloc[27, 21], df.iloc[28, 21], df.iloc[29, 21],
                        df.iloc[30, 21]]
    paraClass.Foshan = [df.iloc[25, 23], df.iloc[26, 23], df.iloc[27, 23], df.iloc[28, 23], df.iloc[29, 23],
                    df.iloc[30, 23]]
    paraClass.region = paraClass.Foshan
    # Increase power supply
    paraClass.Add_line_aveLoad = df.iloc[40, 7]
    paraClass.Add_trans_aveLoad = df.iloc[40, 8]
    paraClass.max_supplyAbility = df.iloc[40, 9]

    paraClass.growth_rate = df.iloc[40, 10]
    paraClass.sales_profit = df.iloc[40, 11]
    paraClass.years_to_saturation = df.iloc[40, 12]

    paraClass.scale_line_factor = df.iloc[40, 13]
    paraClass.scale_trans_factor = df.iloc[40, 14]

    paraClass.K_0 = df.iloc[40, 15]

    paraClass.radius_low = [df.iloc[40, 17], df.iloc[40, 18], df.iloc[40, 19], df.iloc[40, 20], df.iloc[40, 21]]
    paraClass.radius_middle = [df.iloc[41, 17], df.iloc[41, 18], df.iloc[41, 19], df.iloc[41, 20], df.iloc[41, 21]]

    paraClass.aveLoad_line = [df.iloc[40, 24], df.iloc[40, 25], df.iloc[40, 26], df.iloc[40, 27], df.iloc[40, 28]]
    paraClass.aveLoad_trans = [df.iloc[41, 24], df.iloc[41, 25], df.iloc[41, 26], df.iloc[41, 27], df.iloc[41, 28]]

    paraClass.lowV_in_years = df.iloc[47, 7]

    paraClass.unqualified = df.iloc[58, 8]