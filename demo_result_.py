import LCCtable
import numpy as np
import dataprocessing


class DEMO_Result():
    def LCC_invest(self):
        return np.float64(self.INPUT.pro_invest)

    def LCC_operatingCost(self):
        return [a*self.LCCtable_.purchase_price/10000 for a in self.LCCtable_.project_loss_D]

    def LCC_maintenanceCost(self):
        return [a*self.LCCtable_.repairCost_Mtrans + c*self.LCCtable_.repairCost_Mline+e*self.LCCtable_.repairCost_Mcable+g*self.LCCtable_.repairCost_Munits+i*self.LCCtable_.repairCost_Lline+k*self.LCCtable_.repairCost_Lcable+m*self.LCCtable_.repairCost_Lunits \
                for a,c,e,g,i,k,m in zip(np.float64(self.INPUT.trans10), np.float64(self.INPUT.medium_line)  \
                , np.float64(self.INPUT.medium_cable), np.float64(self.INPUT.medium_switchgear), np.float64(self.INPUT.low_line), np.float64(self.INPUT.low_cable), np.float64(self.INPUT.low_switchgear))]

    def LCC_faultCost(self):
        return [a*self.LCCtable_.faultCost_Mtrans + c*self.LCCtable_.faultCost_Mline+e*self.LCCtable_.faultCost_Mcable+g*self.LCCtable_.faultCost_Munits+i*self.LCCtable_.faultCost_Lline+k*self.LCCtable_.faultCost_Lcable+m*self.LCCtable_.faultCost_Lunits \
                for a,c,e,g,i,k,m in zip(np.float64(self.INPUT.trans10), np.float64(self.INPUT.medium_line)  \
                , np.float64(self.INPUT.medium_cable), np.float64(self.INPUT.medium_switchgear), np.float64(self.INPUT.low_line), np.float64(self.INPUT.low_cable), np.float64(self.INPUT.low_switchgear))]

    def LCC_removalCost(self):
        return [(a*self.LCCtable_.removalCost_Mtrans + c*self.LCCtable_.removalCost_Mline+e*self.LCCtable_.removalCost_Mcable+g*self.LCCtable_.removalCost_Munits+i*self.LCCtable_.removalCost_Lline+k*self.LCCtable_.removalCost_Lcable+m*self.LCCtable_.removalCost_Lunits-o*0.05)*self.LCCtable_.rely_discount_rate[29] \
                for a,c,e,g,i,k,m,o in zip(np.float64(self.INPUT.trans10), np.float64(self.INPUT.medium_line)  \
                , np.float64(self.INPUT.medium_cable), np.float64(self.INPUT.medium_switchgear), np.float64(self.INPUT.low_line), np.float64(self.INPUT.low_cable), np.float64(self.INPUT.low_switchgear),np.float64(self.INPUT.pro_invest))]

    def LCC_all(self):
        return [a + b + c + d + e for a, b, c, d, e in zip(self.LCC_invest(), self.LCC_operatingCost(),self.LCC_maintenanceCost(),self.LCC_faultCost(),self.LCC_removalCost())]

    def LCC_increasePowerBenefits(self):
        return [a*self.LCCtable_.sales_profit/10000 for a in self.LCCtable_.project_IPsum_AJ]

    def LCC_increaseReliableBenefits(self):
        i=0
        for a,b,c in zip(np.float64(self.LCCtable_.project_punish_AM),np.float64(self.LCCtable_.project_reduceLackPower_AU),np.float64(self.LCCtable_.project_lackPower_AT)):
            if self.INPUT.pro_name[i] == '110kV铜盂站10kV河陇线等线路自动化有效覆盖改造':
                print(a, b, c)
            i += 1
        return [(a*b+c*self.LCCtable_.overload_lackpower_factor)*self.LCCtable_.GDP_SUPPLY*self.LCCtable_.sum_rely_discount_rate/10000 for a,b,c in zip(np.float64(self.LCCtable_.project_punish_AM),np.float64(self.LCCtable_.project_reduceLackPower_AU),np.float64(self.LCCtable_.project_lackPower_AT))]

    # def LCC_preremoveBenefits():
    #     return [(0.023 - 0.0074) * self.LCCtable_.unqualified * a * fixed_parameters['I63' if self.input_parameters['N476'] == '低压配网网项目' else 'J63'] * fixed_parameters['R23'] * fixed_parameters['V23'] / 8760 / 10000
    def LCC_lowUCost(self):
        i=0
        for a,b,c in zip(self.LCCtable_.project_avelowU_AX, np.float64(self.INPUT.lowV_trans), self.LCCtable_.project_userLowU_AW):
            if self.INPUT.pro_name[i] == '新增配变解决110kV东洋站10kV西新线10kV贵屿西美村4#公用台变电压偏低':
                print(a,b,c)
            i += 1
        return [a*b*c*self.LCCtable_.unqualified*self.LCCtable_.sum_rely_discount_rate*self.LCCtable_.GDP_SUPPLY/10000 for a,b,c in zip(self.LCCtable_.project_avelowU_AX, np.float64(self.INPUT.lowV_trans), self.LCCtable_.project_userLowU_AW)]

    def LCC_investment_efficiency(self):
        return [a / b for a, b in zip(self.LCC_allCost(), self.LCC_all())]

    def LCC_allCost(self):
        return [a + b + c for a, b, c in zip(self.LCC_increasePowerBenefits(),self.LCC_increaseReliableBenefits(),self.LCC_lowUCost())]

    def LCC_allProfit(self):
        return [a - b for a, b in zip(self.LCC_allCost(), self.LCC_all())]

    def LCC_perInEFF(self):
        return [a/b for a, b in zip(self.LCC_allCost(), self.LCC_all())]

    def demo1(self, Pro_Lib, Ass_line, Ass_trans, Dis_Trans, mid_Volt, lowV_trans, demoFactor):
        self.INPUT, self.LCCtable_ = LCCtable.main(Pro_Lib, Ass_line, Ass_trans, Dis_Trans, mid_Volt, lowV_trans, demoFactor)


    def demo2(self):
        table = list(range(1, len(self.INPUT.Pro_Lib)+1))
        table = np.vstack((table, self.INPUT.pro_name))
        table = np.vstack((table, self.INPUT.pro_types))
        table = np.vstack((table, self.LCC_invest()))
        table = np.vstack((table, self.LCC_operatingCost()))
        table = np.vstack((table, self.LCC_maintenanceCost()))
        table = np.vstack((table, self.LCC_faultCost()))
        table = np.vstack((table, self.LCC_removalCost()))
        table = np.vstack((table, self.LCC_all()))
        table = np.vstack((table, self.LCC_increasePowerBenefits()))
        table = np.vstack((table, self.LCC_increaseReliableBenefits()))
        # table = np.vstack((table, [0 for i in range(table.shape[1])]))
        table = np.vstack((table, self.LCC_investment_efficiency()))

        table = np.vstack((table, self.LCC_lowUCost()))
        table = np.vstack((table, self.LCC_allCost()))
        table = np.vstack((table, self.LCC_allProfit()))
        table = np.vstack((table, self.LCC_perInEFF()))
        table = np.vstack((table, self.INPUT.supply_zone))
        dataprocessing.save_scv('result.csv', np.transpose(table))

