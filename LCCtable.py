import input_table
import numpy as np
import input_table

class LCCtable:
    def __init__(self, Pro_Lib, Ass_line, Ass_trans, Dis_Trans, mid_Volt, lowV_trans, pro_list, demoFactor):
        ## input tables
        self.Pro_Lib = Pro_Lib
        self.Ass_line = Ass_line
        self.Ass_trans = Ass_trans
        self.Dis_Trans = Dis_Trans
        self.mid_Volt = mid_Volt
        self.lowV_trans = lowV_trans
        self.input_Para = np.array(pro_list)
        self.demoFactor = demoFactor

        ## parameters
        ### cost para
        self.Pro_Lib = Pro_Lib
        self.Ass_line = Ass_line
        self.Ass_trans = Ass_trans
        self.Dis_Trans = Dis_Trans
        self.mid_Volt = mid_Volt
        self.lowV_trans = lowV_trans
        self.input_Para = np.array(pro_list)

        ## parameters
        ### cost para
        # demoFactor.repairCost_Mtrans = 0.5839
        # demoFactor.repairCost_Mline = 23.9692  
        # demoFactor.repairCost_Mcable = 2.586
        # demoFactor.repairCost_Munits = 0.4619
        # demoFactor.repairCost_Lline = 3.7077
        # demoFactor.repairCost_Lcable = 3.7077
        # demoFactor.repairCost_Lunits = 6.6825
        
        # demoFactor.faultCost_Mtrans = 0.0
        # demoFactor.faultCost_Mline = 0.0
        # demoFactor.faultCost_Mcable = 0.0
        # demoFactor.faultCost_Munits = 0.0
        # demoFactor.faultCost_Lline = 0.0
        # demoFactor.faultCost_Lcable = 0.0
        # demoFactor.faultCost_Lunits = 0.0

        # demoFactor.removalCost_Mtrans = 0.2806
        # demoFactor.removalCost_Mline = 0.1148 
        # demoFactor.removalCost_Mcable = 2.2081
        # demoFactor.removalCost_Munits = 0.5835
        # demoFactor.removalCost_Lline = 0.0907
        # demoFactor.removalCost_Lcable = 1.7300
        # demoFactor.removalCost_Lunits = 0.1085
        
        # demoFactor.purchase_price = 0.31
        # demoFactor.DisTran_lossRate = 0.025
        # demoFactor.linePerLen_lossRate = 0.003

        # ### reliability para
        # demoFactor.overload_line_factor = 0.6
        # demoFactor.overload_line_invest = 2013
        # demoFactor.overload_line_rely = self.demoFactor.overload_line_factor*self.demoFactor.overload_line_invest
        # reliable_investment = self.demoFactor.overload_line_rely

        # demoFactor.highload_line_factor = 0.5
        # demoFactor.highload_line_invest = 7953
        # demoFactor.highload_line_rely = self.demoFactor.highload_line_factor*self.demoFactor.highload_line_invest
        # reliable_investment += self.demoFactor.highload_line_rely

        # demoFactor.overload_trans_factor = 0.6
        # demoFactor.overload_trans_invest = 3165
        # demoFactor.overload_trans_rely = self.demoFactor.overload_trans_factor*self.demoFactor.overload_trans_invest
        # reliable_investment += self.demoFactor.overload_trans_rely

        # demoFactor.highload_trans_factor = 0.5
        # demoFactor.highload_trans_invest = 5100
        # demoFactor.highload_trans_rely = self.demoFactor.highload_trans_factor*self.demoFactor.highload_trans_invest
        # reliable_investment += self.demoFactor.highload_trans_rely

        # demoFactor.newload_line_factor = 0.3
        # demoFactor.newload_line_invest = 31486
        # demoFactor.newload_line_rely = self.demoFactor.newload_line_factor*self.demoFactor.newload_line_invest
        # reliable_investment += self.demoFactor.newload_line_rely

        # demoFactor.newload_trans_factor = 0.3
        # demoFactor.newload_trans_invest = 8541
        # demoFactor.newload_trans_rely = self.demoFactor.newload_trans_factor*self.demoFactor.newload_trans_invest
        # reliable_investment += self.demoFactor.newload_trans_rely

        # demoFactor.modify_trans_factor = 0.3
        # demoFactor.modify_trans_invest = 392
        # demoFactor.modify_trans_rely = self.demoFactor.modify_trans_factor*self.demoFactor.modify_trans_invest
        # reliable_investment += self.demoFactor.modify_trans_rely

        # demoFactor.safety_line_factor = 1
        # demoFactor.safety_line_invest = 0
        # demoFactor.safety_line_rely = self.demoFactor.safety_line_factor*self.demoFactor.safety_line_invest
        # reliable_investment += self.demoFactor.safety_line_rely

        # demoFactor.lowV_trans_factor = 0.3
        # demoFactor.lowV_trans_invest = 1293
        # demoFactor.lowV_trans_rely = self.demoFactor.lowV_trans_factor*self.demoFactor.lowV_trans_invest
        # reliable_investment += self.demoFactor.lowV_trans_rely

        # demoFactor.netRack_factor = 1
        # demoFactor.netRack_invest = 11975
        # demoFactor.netRack_rely = self.demoFactor.netRack_factor*self.demoFactor.netRack_invest
        # reliable_investment += self.demoFactor.netRack_rely

        # demoFactor.replace_factor = 1
        # demoFactor.replace_invest = 104
        # demoFactor.replace_rely = self.demoFactor.replace_factor*self.demoFactor.replace_invest
        # reliable_investment += self.demoFactor.replace_rely

        # demoFactor.auto_factor = 1
        # demoFactor.auto_invest = 7937
        # demoFactor.auto_rely = self.demoFactor.auto_factor*self.demoFactor.auto_invest
        # reliable_investment += self.demoFactor.auto_rely

        # demoFactor.outage_user_last = 0.2
        # demoFactor.amount_user_last = 29000

        # demoFactor.outage_user = 0
        # demoFactor.amount_user = 0

        # demoFactor.outage_user_reduce = 5800
        
        # demoFactor.reliable_investment = reliable_investment

        # demoFactor.could_reduce_users = self.demoFactor.outage_user_reduce/self.demoFactor.reliable_investment

        # demoFactor.middle_newAuto = 468
        # demoFactor.middle_project = 170
        # demoFactor.low_project = 334
        # demoFactor.ave_users = 20
        # demoFactor.ave_adjusted = 0.265277778

        # demoFactor.region_GDP = 3017
        # demoFactor.region_supply = 240
        # demoFactor.GDP_SUPPLY = self.demoFactor.region_GDP/self.demoFactor.region_supply

        # demoFactor.ave_middle_users = self.demoFactor.ave_users

        # demoFactor.discount_rate = 0.07
        # demoFactor.rely_discount_rate = [0]*30
        # demoFactor.rely_discount_rate[0] = 1
        # for i in range(2, 31):
        #     demoFactor.rely_discount_rate[i-1] = 1/(pow((1+demoFactor.discount_rate),(i-1)))
        
        # demoFactor.sum_rely_discount_rate = sum(demoFactor.rely_discount_rate)
        # demoFactor.overload_lackpower_factor = 1

        # demoFactor.punish_factor = [5, 3.5, 4, 11.25, 4.5, 5.75]

        # demoFactor.Guangzhou = [8.25, 3.75, 6.25, 16.25, 7.25, 7.5]
        # demoFactor.santou = [5, 3.5, 4, 11.25, 4.5, 5.75]

        # # Increase power supply
        # demoFactor.Add_line_aveLoad = 0.2
        # demoFactor.Add_trans_aveLoad = 0.3
        # demoFactor.max_supplyAbility = 8800

        # demoFactor.growth_rate = 0.05
        # demoFactor.sales_profit = 0.15
        # demoFactor.years_to_saturation = 20
        
        # demoFactor.scale_line_factor = 0.7
        # demoFactor.scale_trans_factor = 0.7

        # demoFactor.K_0 = 4

        # demoFactor.radius_low = [0.15, 0.15, 0.25, 0.4, 0.5]
        # demoFactor.radius_middle = [2.4, 2.4, 4, 4, 12]

        # demoFactor.aveLoad_line = [0.2, 0.2, 0.2, 0.2, 0.2]
        # demoFactor.aveLoad_trans = [0.3, 0.3, 0.3, 0.3, 0.3]

        # demoFactor.lowV_in_years = 0.01

        # demoFactor.unqualified = 0.008
    
    # 项目名称
    def get_name_B(self, INPUT):
        self.project_name_B = INPUT.pro_name

    # 项目类别
    def get_type_C(self, INPUT):
        self.project_type_C = INPUT.pro_types

    # 线损电量
    def get_loss_D(self, INPUT):
        self.project_loss_D = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_class[i] == '低压配电网项目':
                self.project_loss_D[i] = self.project_IPsum_AJ[i]*self.demoFactor.DisTran_lossRate
                
            else:
                self.project_loss_D[i] = (np.float16(INPUT.medium_line[i]) + np.float16(INPUT.medium_cable[i]))*self.demoFactor.linePerLen_lossRate*self.project_IPsum_AJ[i]
        
        

    # 平均负载率
    def get_aveload_G(self, INPUT):
        self.project_aveload_G = [0.0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_class[i] != '低压配电网项目':
                if INPUT.supply_zone[i] == 'A+':
                    self.project_aveload_G[i] = self.demoFactor.aveLoad_line[0]
                elif INPUT.supply_zone[i] == 'A':
                    self.project_aveload_G[i] = self.demoFactor.aveLoad_line[1]
                elif INPUT.supply_zone[i] == 'B':
                    self.project_aveload_G[i] = self.demoFactor.aveLoad_line[2]
                elif INPUT.supply_zone[i] == 'C':
                    self.project_aveload_G[i] = self.demoFactor.aveLoad_line[3]
                elif INPUT.supply_zone[i] == 'D':
                    self.project_aveload_G[i] = self.demoFactor.aveLoad_line[4]
            else:
                t = np.float16(INPUT.new_transCap[i]) - np.float16(INPUT.retired_transCap[i])
                if t > 0 :
                    if INPUT.supply_zone[i] == 'A+':
                        self.project_aveload_G[i] = self.demoFactor.aveLoad_trans[0]
                    elif INPUT.supply_zone[i] == 'A':
                        self.project_aveload_G[i] = self.demoFactor.aveLoad_trans[1]
                    elif INPUT.supply_zone[i] == 'B':
                        self.project_aveload_G[i] = self.demoFactor.aveLoad_trans[2]
                    elif INPUT.supply_zone[i] == 'C':
                        self.project_aveload_G[i] = self.demoFactor.aveLoad_trans[3]
                    elif INPUT.supply_zone[i] == 'D':
                        self.project_aveload_G[i] = self.demoFactor.aveLoad_trans[4]
                else:
                    self.project_aveload_G[i] = 0
        # print(self.project_aveload_G)

    
    # 新增最大供电能力或新增配变容量
    def get_ability_H(self, INPUT):
        self.project_ability_H = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_class[i] == '低压配电网项目':
                self.project_ability_H[i] = np.float16(INPUT.new_transCap[i]) - np.float16(INPUT.retired_transCap[i])
            else:
                if INPUT.new_line[i] != '0':
                    self.project_ability_H[i] = 8800
                else:
                    if INPUT.pro_types[i] == '完善中压网架':
                        self.project_ability_H[i] = 8800/4
                    else:
                        self.project_ability_H[i] = 0
    
    # 项目供电半径
    def get_radius_I(self, INPUT):
        self.project_radius_I = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_class[i] != '低压配电网项目':
                if INPUT.supply_zone[i] == 'A+':
                    self.project_radius_I[i] = self.demoFactor.radius_middle[0]
                elif INPUT.supply_zone[i] == 'A':
                    self.project_radius_I[i] = self.demoFactor.radius_middle[1]
                elif INPUT.supply_zone[i] == 'B':
                    self.project_radius_I[i] = self.demoFactor.radius_middle[2]
                elif INPUT.supply_zone[i] == 'C':
                    self.project_radius_I[i] = self.demoFactor.radius_middle[3]
                elif INPUT.supply_zone[i] == 'D':
                    self.project_radius_I[i] = self.demoFactor.radius_middle[4]
            else:
                if INPUT.supply_zone[i] == 'A+':
                    self.project_radius_I[i] = self.demoFactor.radius_low[0]
                elif INPUT.supply_zone[i] == 'A':
                    self.project_radius_I[i] = self.demoFactor.radius_low[1]
                elif INPUT.supply_zone[i] == 'B':
                    self.project_radius_I[i] = self.demoFactor.radius_low[2]
                elif INPUT.supply_zone[i] == 'C':
                    self.project_radius_I[i] = self.demoFactor.radius_low[3]
                elif INPUT.supply_zone[i] == 'D':
                    self.project_radius_I[i] = self.demoFactor.radius_low[4]

 
    # L/L0
    def get_LL0_J(self, INPUT):
        self.project_LL0_J = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if (np.float16(INPUT.medium_line[i])+np.float16(INPUT.medium_cable[i]))/np.float16(self.project_radius_I[i]) > 1:
                self.project_LL0_J[i] = 1
            else:
                self.project_LL0_J[i] = (np.float16(INPUT.medium_line[i])+np.float16(INPUT.medium_cable[i]))/np.float16(self.project_radius_I[i])

    # K/K0
    def get_KK0_K(self, INPUT):
        self.project_KK0_K = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if (np.float16(INPUT.ring_network[i])+np.float16(INPUT.line_switch[i]))/4 > 1:
                self.project_KK0_K[i] = 1
            else:
                self.project_KK0_K[i] = (np.float16(INPUT.ring_network[i])+np.float16(INPUT.line_switch[i]))/4
    
    # LLV/LLV0
    def get_LLV0_L(self, INPUT):
        self.project_LLV0_L = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if (np.float16(INPUT.low_line[i])+np.float16(INPUT.low_cable[i]))/np.float16(self.project_radius_I[i]) > 1:
                self.project_LLV0_L[i] = 1
            else:
                self.project_LLV0_L[i] = (np.float16(INPUT.low_line[i])+np.float16(INPUT.low_cable[i]))/np.float16(self.project_radius_I[i])

    # 受报装影响的Q0
    def get_Q0_M(self, INPUT):
        self.project_Q0_M = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_class[i] == '低压配电网项目':
                self.project_Q0_M[i] = self.project_aveload_G[i]*8760*INPUT.capacity[i]
            else:
                self.project_Q0_M[i] = self.project_aveload_G[i]*8760*INPUT.capacity[i]
            if INPUT.pro_name[i] == '110kV上堡站新出线调整110kV上堡站10kV大亨线负荷':
                print('========234\\\\==================')
                print(self.project_Q0_M[i])
                print(self.project_aveload_G[i],INPUT.capacity[i])
                print('=========234\\\\=================')
                    
    # 新增线路和配变的实际饱和年供电电量（Qmax)
    def get_Qmax_N(self, INPUT):
        self.project_Qmax_N = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_class[i] == '低压配电网项目':
                self.project_Qmax_N[i] = self.project_aveload_G[i]*8760*self.project_ability_H[i]*(self.demoFactor.scale_trans_factor+(1-self.demoFactor.scale_trans_factor)*self.project_LLV0_L[i])
            else:
                self.project_Qmax_N[i] = self.project_aveload_G[i]*self.project_ability_H[i]*8760*(self.project_LL0_J[i]*self.demoFactor.scale_line_factor+self.project_KK0_K[i]*(1-self.demoFactor.scale_line_factor))
        # print(self.project_Qmax_N)
            if INPUT.pro_name[i] == '新增配变解决110kV铜盂变电站10kV溪西线溪西9#公用台变解决电压偏低':
                print("------------------------")
                print(f'{self.project_aveload_G[i]}*8760*{self.project_ability_H[i]}*({self.demoFactor.scale_trans_factor}+(1-{self.demoFactor.scale_trans_factor})*{self.project_LLV0_L[i]})')
                print("-----------------------")
            

    # 新出线年供电量达到包和容量的年份
    def get_saturationYears_F(self, INPUT):
        self.project_satYears_F = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if np.float16(INPUT.cor_powerSupply[i]) == 0.0:
                self.project_satYears_F[i] = self.demoFactor.years_to_saturation
            else:
                self.project_satYears_F[i] = (self.project_Qmax_N[i] - self.project_Q0_M[i])/(INPUT.cor_powerSupply[i]*self.demoFactor.growth_rate)
            if INPUT.pro_name[i] == '110kV上堡站新出线调整110kV上堡站10kV大亨线负荷':
                print("------------------------")
                print(f'{self.project_satYears_F[i]} = ({self.project_Qmax_N[i]} - {self.project_Q0_M[i]})/({INPUT.cor_powerSupply[i]}*{self.demoFactor.growth_rate})')
                print("-----------------------")

            if self.project_satYears_F[i] >= self.demoFactor.years_to_saturation:
                self.project_satYears_F[i] = self.demoFactor.years_to_saturation
            else:
                self.project_satYears_F[i] = np.int8((self.project_Qmax_N[i] - self.project_Q0_M[i])/(INPUT.cor_powerSupply[i]*self.demoFactor.growth_rate))
        # print(self.project_satYears_F)
    
    # 增供电量1
    def get_increasePower1_O(self, INPUT):
        self.project_IP1_O = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 1:
                self.project_IP1_O[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[0]
            else:
                self.project_IP1_O[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*1/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[0]
        # print(self.project_IP1_O)
            if INPUT.pro_name[i] == '110kV上堡站新出线调整110kV上堡站10kV大亨线负荷':
                print('==========================')
                print(self.project_IP1_O[i])
                print(f'({self.project_Q0_M[i]}+({self.project_Qmax_N[i]}-{self.project_Q0_M[i]})*1/{self.project_satYears_F[i]})*{self.demoFactor.rely_discount_rate[0]}')
                print('==========================')

    # 增供电量2
    def get_increasePower2_P(self, INPUT):
        self.project_IP2_P = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 2:
                self.project_IP2_P[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[1]
            else:
                self.project_IP2_P[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*2/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[1]

    # 增供电量3
    def get_increasePower3_Q(self, INPUT):
        self.project_IP3_Q = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 3:
                self.project_IP3_Q[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[2]
            else:
                self.project_IP3_Q[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*3/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[2]

    # 增供电量4
    def get_increasePower4_R(self, INPUT):
        self.project_IP4_R = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 4:
                self.project_IP4_R[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[3]
            else:
                self.project_IP4_R[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*4/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[3]
    
    # 增供电量5
    def get_increasePower5_S(self, INPUT):
        self.project_IP5_S = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 5:
                self.project_IP5_S[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[4]
            else:
                self.project_IP5_S[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*5/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[4]

    # 增供电量6
    def get_increasePower6_T(self, INPUT):
        self.project_IP6_T = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 6:
                self.project_IP6_T[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[5]
            else:
                self.project_IP6_T[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*6/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[5]

    # 增供电量7
    def get_increasePower7_U(self, INPUT):
        self.project_IP7_U = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 7:
                self.project_IP7_U[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[6]
            else:
                self.project_IP7_U[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*7/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[6]

    # 增供电量8
    def get_increasePower8_V(self, INPUT):
        self.project_IP8_V = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 8:
                self.project_IP8_V[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[7]
            else:
                self.project_IP8_V[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*8/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[7]

    # 增供电量9
    def get_increasePower9_W(self, INPUT):
        self.project_IP9_W = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 9:
                self.project_IP9_W[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[8]
            else:
                self.project_IP9_W[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*9/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[8]

    # 增供电量10
    def get_increasePower10_X(self, INPUT):
        self.project_IP10_X = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 10:
                self.project_IP10_X[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[9]
            else:
                self.project_IP10_X[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*10/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[9]

    # 增供电量11
    def get_increasePower11_Y(self, INPUT):
        self.project_IP11_Y = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 11:
                self.project_IP11_Y[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[10]
            else:
                self.project_IP11_Y[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*11/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[10]

    # 增供电量12
    def get_increasePower12_Z(self, INPUT):
        self.project_IP12_Z = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 12:
                self.project_IP12_Z[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[11]
            else:
                self.project_IP12_Z[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*12/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[11]

    # 增供电量13
    def get_increasePower13_AA(self, INPUT):
        self.project_IP13_AA = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 13:
                self.project_IP13_AA[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[12]
            else:
                self.project_IP13_AA[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*13/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[12]

    # 增供电量14
    def get_increasePower14_AB(self, INPUT):
        self.project_IP14_AB = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 14:
                self.project_IP14_AB[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[13]
            else:
                self.project_IP14_AB[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*14/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[13]

    # 增供电量15
    def get_increasePower15_AC(self, INPUT):
        self.project_IP15_AC = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 15:
                self.project_IP15_AC[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[14]
            else:
                self.project_IP15_AC[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*15/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[14]

    # 增供电量16
    def get_increasePower16_AD(self, INPUT):
        self.project_IP16_AD = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 16:
                self.project_IP16_AD[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[15]
            else:
                self.project_IP16_AD[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*16/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[15]

    # 增供电量17
    def get_increasePower17_AE(self, INPUT):
        self.project_IP17_AE = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 17:
                self.project_IP17_AE[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[16]
            else:
                self.project_IP17_AE[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*17/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[16]

    # 增供电量18
    def get_increasePower18_AF(self, INPUT):
        self.project_IP18_AF = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 18:
                self.project_IP18_AF[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[17]
            else:
                self.project_IP18_AF[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*18/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[17]

    # 增供电量19
    def get_increasePower19_AG(self, INPUT):
        self.project_IP19_AG = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 19:
                self.project_IP19_AG[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[18]
            else:
                self.project_IP19_AG[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*19/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[18]

    # 增供电量20
    def get_increasePower20_AH(self, INPUT):
        self.project_IP20_AH = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if self.project_satYears_F[i] < 20:
                self.project_IP20_AH[i] = self.project_Qmax_N[i]*self.demoFactor.rely_discount_rate[19]
            else:
                self.project_IP20_AH[i] = (self.project_Q0_M[i]+(self.project_Qmax_N[i]-self.project_Q0_M[i])*20/self.project_satYears_F[i])*self.demoFactor.rely_discount_rate[19]

    # 增供电量21-30
    def get_increasePower2130_AI(self, INPUT):
        self.project_IP2130_AI = [0]*len(INPUT.pro_class)
        sum_rate = 0
        for i in range(20, 30):
            sum_rate += self.demoFactor.rely_discount_rate[i]
        for i in range(0, len(INPUT.pro_class)):
            self.project_IP2130_AI[i] = self.project_Qmax_N[i]*(sum_rate)
    
    # 增供电量累加值
    def get_sumincreasePower_AJ(self, INPUT):
        self.project_IPsum_AJ = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            self.project_IPsum_AJ[i] = self.project_IP1_O[i]+self.project_IP2_P[i]+self.project_IP3_Q[i]+self.project_IP4_R[i]+self.project_IP5_S[i] + \
                                        self.project_IP6_T[i]+self.project_IP7_U[i]+self.project_IP8_V[i]+self.project_IP9_W[i]+self.project_IP10_X[i]+ \
                                        self.project_IP11_Y[i]+self.project_IP12_Z[i]+self.project_IP13_AA[i]+self.project_IP14_AB[i]+self.project_IP15_AC[i]+ \
                                        self.project_IP16_AD[i]+self.project_IP17_AE[i]+self.project_IP18_AF[i]+self.project_IP19_AG[i]+self.project_IP20_AH[i]+ \
                                        self.project_IP2130_AI[i]
            if INPUT.pro_name[i] == '110kV上堡站新出线调整110kV上堡站10kV大亨线负荷':
                print("------------------------")
                print(f'{self.project_IP1_O[i]}+{self.project_IP2_P[i]}+{self.project_IP3_Q[i]}+{self.project_IP4_R[i]}+{self.project_IP5_S[i]} + \
                                        {self.project_IP6_T[i]}+{self.project_IP7_U[i]}+{self.project_IP8_V[i]}+{self.project_IP9_W[i]}+{self.project_IP10_X[i]}+ \
                                        {self.project_IP11_Y[i]}+{self.project_IP12_Z[i]}+{self.project_IP13_AA[i]}+{self.project_IP14_AB[i]}+{self.project_IP15_AC[i]}+ \
                                        {self.project_IP16_AD[i]}+{self.project_IP17_AE[i]}+{self.project_IP18_AF[i]}+{self.project_IP19_AG[i]}+{self.project_IP20_AH[i]}+ \
                                        {self.project_IP2130_AI[i]}')
                print("-----------------------")

    # 惩罚因子
    def get_punish_AM(self, INPUT):
        self.project_punish_AM = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.power_partition[i] == '工业':
                self.project_punish_AM[i] = self.demoFactor.punish_factor[0]
            elif INPUT.power_partition[i] == '农业':
                self.project_punish_AM[i] = self.demoFactor.punish_factor[1]
            elif INPUT.power_partition[i] == '居民':
                self.project_punish_AM[i] = self.demoFactor.punish_factor[2]
            elif INPUT.power_partition[i] == '商业':
                self.project_punish_AM[i] = self.demoFactor.punish_factor[3]
            elif INPUT.power_partition[i] == '工民混合':
                self.project_punish_AM[i] = self.demoFactor.punish_factor[4]
            else:
                self.project_punish_AM[i] = self.demoFactor.punish_factor[5]

    # 归算系数
    def get_reduction_AN(self, INPUT):
        self.project_reduction_AN = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_types[i] == '解决中压线路过载':
                self.project_reduction_AN[i] = self.demoFactor.overload_line_factor
            if INPUT.pro_types[i] == '解决中压线路重载':
                self.project_reduction_AN[i] = self.demoFactor.highload_line_factor
            if INPUT.pro_types[i] == '解决配变过载':
                self.project_reduction_AN[i] = self.demoFactor.overload_trans_factor
            if INPUT.pro_types[i] == '解决配变重载':
                self.project_reduction_AN[i] = self.demoFactor.overload_trans_factor
            if INPUT.pro_types[i] == '变电站新出线满足新增负荷供电':
                if 'XLGZ' in INPUT.error_code[i]:
                    self.project_reduction_AN[i] = self.demoFactor.overload_line_factor
                elif 'XLZZ' in INPUT.error_code[i]:
                    self.project_reduction_AN[i] = self.demoFactor.highload_line_factor
                else:
                    self.project_reduction_AN[i] = self.demoFactor.newload_line_factor
            if INPUT.pro_types[i] == '新建台区满足负荷需求':
                self.project_reduction_AN[i] = self.demoFactor.newload_trans_factor
            if INPUT.pro_types[i] == '改造台区满足新增负荷':
                self.project_reduction_AN[i] = self.demoFactor.modify_trans_factor
            if INPUT.pro_types[i] == '解决中低压线路存在的安全隐患问题':
                self.project_reduction_AN[i] = self.demoFactor.safety_line_factor
            if INPUT.pro_types[i] == '解决台区电压偏低问题':
                self.project_reduction_AN[i] = self.demoFactor.lowV_trans_factor
            if INPUT.pro_types[i] == '完善中压网架':
                if INPUT.new_line[i] == '0':
                    self.project_reduction_AN[i] = self.demoFactor.netRack_factor
                else:
                    self.project_reduction_AN[i] = self.demoFactor.newload_line_factor
            if INPUT.pro_types[i] == '更换残旧设备或线路':
                self.project_reduction_AN[i] = self.demoFactor.replace_factor
            if INPUT.pro_types[i] == '配电自动化项目' :
                if INPUT.new_line[i] == '0':
                    self.project_reduction_AN[i] = self.demoFactor.auto_factor
                else:
                    self.project_reduction_AN[i] = self.demoFactor.newload_line_factor
        # print(self.project_reduction_AN)

    # 预计减少的停电户数初值
    def get_reduceOutage_AO(self, INPUT):
        self.project_reduceOutrage_AO = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            self.project_reduceOutrage_AO[i] = self.demoFactor.could_reduce_users*self.project_reduction_AN[i]*np.float16(INPUT.pro_invest[i])
    # 调整系数初值
    def get_adjusted_AP(self, INPUT):
        self.project_adjuest_AP = [0.0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.new_automation[i] == 0:
                self.project_adjuest_AP[i] = 1/self.demoFactor.ave_users
            else:
                if INPUT.pro_types[i] == '解决中压线路过载' or INPUT.pro_types[i] == '解决中压线路重载':
                    self.project_adjuest_AP[i] = INPUT.new_automation[i]/4
                if INPUT.pro_types[i] == '解决配变过载' or INPUT.pro_types[i] == '解决配变重载':
                    self.project_adjuest_AP[i] = 1/self.demoFactor.ave_users
                if INPUT.pro_types[i] == '变电站新出线满足新增负荷供电':
                    self.project_adjuest_AP[i] = INPUT.new_automation[i]/4
                if INPUT.pro_types[i] == '新建台区满足负荷需求' or INPUT.pro_types[i] == '改造台区满足新增负荷' or INPUT.pro_types[i] == '解决台区电压偏低问题':
                    self.project_adjuest_AP[i] = 1/self.demoFactor.ave_users
                if INPUT.pro_types[i] == '完善中压网架':
                    self.project_adjuest_AP[i] = INPUT.new_automation[i]/4
                if INPUT.pro_types[i] == '解决中低压线路存在的安全隐患问题':
                    self.project_adjuest_AP[i] = INPUT.new_automation[i]/4
                if INPUT.pro_types[i] == '更换残旧设备或线路':
                    if INPUT.voltage_level[i] == '0.4kV':
                        self.project_adjuest_AP[i] = 1/self.demoFactor.ave_users
                    else:
                        self.project_adjuest_AP[i] = 0.25
                if INPUT.pro_types[i] == '配电自动化项目':
                    self.project_adjuest_AP[i] = INPUT.new_automation[i]/4
            if self.project_adjuest_AP[i] > 0.8:
                self.project_adjuest_AP[i] = 0.8

    # 调整后预计可减少的停电时户数
    def get_UserAfterAdjusted_AQ(self, INPUT):
        self.project_UserAfterAdjusted_AQ = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            self.project_UserAfterAdjusted_AQ[i] = self.project_adjuest_AP[i]*self.project_reduceOutrage_AO[i]

    # 修正后得到的停电时户数
    def get_UserAfterRevision_AR(self, INPUT):
        self.project_UserAfterRevision_AR = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            self.project_UserAfterRevision_AR[i] = self.project_UserAfterAdjusted_AQ[i]/self.demoFactor.ave_adjusted
# self.project_UserAfterRevision_AR[i] = self.project_UserAfterAdjusted_AQ[i]/self.demoFactor.ave_adjusted/np.float16(INPUT.pro_invest[i])
    
    # 过载时间
    def get_overLoadtime_AS(self, INPUT):
        self.project_overLoadtime_AS = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_types[i] == '解决中压线路过载' or INPUT.pro_types[i] == '解决配变过载':
                if INPUT.overload_time[i] > 60:
                    self.project_overLoadtime_AS[i] = 60
                elif INPUT.overload_time[i] < 30:
                    self.project_overLoadtime_AS[i] = 30
                else:
                    self.project_overLoadtime_AS[i] = INPUT.overload_time
    
    # 非计划缺供电量
    def get_lackPower_AT(self, INPUT):
        self.project_lackPower_AT = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_types[i] == '解决中压线路过载':
                if INPUT.annual_maxI[i]>INPUT.safe_I[i]:
                    self.project_lackPower_AT[i] = (INPUT.annual_maxI[i]-INPUT.safe_I[i])*1.732*10*self.project_overLoadtime_AS[i]
            if INPUT.pro_class[i] == '解决配变过载':
                if INPUT.max_loadRate[i]>100:
                    self.project_lackPower_AT[i] = (INPUT.max_loadRate[i]/100-1)*INPUT.Sn[i]*self.project_overLoadtime_AS[i]

    # 预计可减少的缺供电量
    def get_reuduceLackPower_AU(self, INPUT):
        self.project_reduceLackPower_AU = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.cor_powerSupply[i] == 0:
                if INPUT.pro_class[i] == '低压配电网项目':
                    self.project_reduceLackPower_AU[i] = self.project_UserAfterRevision_AR[i]*self.demoFactor.max_supplyAbility*self.demoFactor.Add_trans_aveLoad/(self.demoFactor.ave_middle_users*INPUT.cor_mediumUser[i])
                else:
                    self.project_reduceLackPower_AU[i] = self.project_UserAfterRevision_AR[i]*self.demoFactor.max_supplyAbility*self.demoFactor.Add_line_aveLoad/INPUT.cor_mediumUser[i]
            else:
                self.project_reduceLackPower_AU[i] = self.project_UserAfterRevision_AR[i]*INPUT.cor_powerSupply[i]/(8760*np.float16(INPUT.cor_amount[i])*INPUT.cor_mediumUser[i])
            if INPUT.pro_name[i] == '新增配变解决110kV和平变电站10kV新科线10kV和平中寨工业区公用台变重载':
                 print(self.project_UserAfterRevision_AR[i],INPUT.cor_powerSupply[i],np.float16(INPUT.cor_amount[i]),INPUT.cor_mediumUser[i])
              


    
    # 低电压用户比例
    def get_userLowU_AW(self, INPUT):
        self.project_userLowU_AW = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.trans_TerminalV[i]<=198:
                self.project_userLowU_AW[i] = 0.2+(198-INPUT.trans_TerminalV[i])*0.02/2.2
            else:
                self.project_userLowU_AW[i] = 0
    
    # 低电压供电量平均值
    def get_aveLowU_AX(self, INPUT):
        self.project_avelowU_AX = [0]*len(INPUT.pro_class)
        for i in range(0, len(INPUT.pro_class)):
            if INPUT.pro_class[i] == '低压配电网项目':
                self.project_avelowU_AX[i] = input_table.cal_trans(INPUT.Pro_Lib[i][158], INPUT.dl_t, '供电量(kWh)', 'cal')
            else:
                for k in range(0, 6):
                    if INPUT.Ass_line[i][k] != '0.0':
                        self.project_avelowU_AX[i] += input_table.find_distrans(INPUT.Ass_line[i][k], INPUT.df_dt, '供电量(kWh)', 'mean')


def main(Pro_Lib, Ass_line, Ass_trans, Dis_Trans, mid_Volt, lowV_trans, demoFactor):
    INPUT = input_table.Input_table(Pro_Lib, Ass_line, Ass_trans, Dis_Trans, mid_Volt, lowV_trans)

    INPUT.InputTable()
    LCCtable_ = LCCtable(INPUT.Pro_Lib, INPUT.Ass_line, INPUT.Ass_trans, INPUT.Dis_Trans, INPUT.mid_Volt, INPUT.lowV_trans, INPUT.pro_list, demoFactor)
    LCCtable_.get_aveload_G(INPUT)
    LCCtable_.get_ability_H(INPUT)
    LCCtable_.get_radius_I(INPUT)
    LCCtable_.get_LL0_J(INPUT)
    LCCtable_.get_KK0_K(INPUT)
    LCCtable_.get_LLV0_L(INPUT)

    LCCtable_.get_Qmax_N(INPUT)
    LCCtable_.get_Q0_M(INPUT)
    LCCtable_.get_saturationYears_F(INPUT)
    LCCtable_.get_increasePower1_O(INPUT)
    LCCtable_.get_increasePower2_P(INPUT)
    LCCtable_.get_increasePower3_Q(INPUT)
    LCCtable_.get_increasePower4_R(INPUT)
    LCCtable_.get_increasePower5_S(INPUT)
    LCCtable_.get_increasePower6_T(INPUT)
    LCCtable_.get_increasePower7_U(INPUT)
    LCCtable_.get_increasePower8_V(INPUT)
    LCCtable_.get_increasePower9_W(INPUT)
    LCCtable_.get_increasePower10_X(INPUT)
    LCCtable_.get_increasePower11_Y(INPUT)
    LCCtable_.get_increasePower12_Z(INPUT)
    LCCtable_.get_increasePower13_AA(INPUT)
    LCCtable_.get_increasePower14_AB(INPUT)
    LCCtable_.get_increasePower15_AC(INPUT)
    LCCtable_.get_increasePower16_AD(INPUT)
    LCCtable_.get_increasePower17_AE(INPUT)
    LCCtable_.get_increasePower18_AF(INPUT)
    LCCtable_.get_increasePower19_AG(INPUT)
    LCCtable_.get_increasePower20_AH(INPUT)
    LCCtable_.get_increasePower2130_AI(INPUT)
    # LCCtable.get_sumincreasePower_AI(INPUT)
    LCCtable_.get_sumincreasePower_AJ(INPUT)
    LCCtable_.get_loss_D(INPUT)
    LCCtable_.get_punish_AM(INPUT)
    LCCtable_.get_reduction_AN(INPUT)
    LCCtable_.get_reduceOutage_AO(INPUT)
    LCCtable_.get_adjusted_AP(INPUT)
    LCCtable_.get_UserAfterAdjusted_AQ(INPUT)
    LCCtable_.get_UserAfterRevision_AR(INPUT)
    LCCtable_.get_overLoadtime_AS(INPUT)
    LCCtable_.get_lackPower_AT(INPUT)
    LCCtable_.get_reuduceLackPower_AU(INPUT)
    LCCtable_.get_aveLowU_AX(INPUT)
    LCCtable_.get_userLowU_AW(INPUT)

    return INPUT, LCCtable_
