from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QGridLayout, QProgressBar, QTableWidget, QTableWidgetItem, QHBoxLayout, QComboBox, QSlider, QLabel, QMessageBox
import dataprocessing
import sys
import LCCtable_
import demo_result
import pandas as pd
# from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QRect
from PyQt5.QtCore import Qt
import parameters_input
from PyQt5 import QtCore
import Analysis_excel

tmp_value = 0
class demoFactor():
    def __init__(self) -> None:
        parameters_input.fixed_input_foshan(demoFactor)
        pass

DEMO = demoFactor()

class FileDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(1000, 800)
        # self.setGeometry(-400, 0, 400, 600)
        self.initUI()

    def initUI(self):
        # layout = QGridLayout()
        self.setGeometry(600, 100, 600, 400)
        self.setWindowTitle('LCC 计算平台')


############################################################################3333
        # layout.addWidget(self.progress_lowU_sheet)
############################################# EXCEL表显示按钮+布局 ##########################################
        layout_table = QHBoxLayout()
        layout_other = QHBoxLayout()
        layout_another = QHBoxLayout()

        self.table = QTableWidget(self)
        self.table.setFixedSize(1000,500)
        # self.setCentralWidget(self.table)
        self.btn_table = QPushButton("选择Excel文件", self)
        self.btn_table.setFixedSize(500, 50)
        # self.btn_table.clicked.connect(self.loadExcelData)


        self.btn_cal = QPushButton('计算')
        self.btn_cal.setFixedSize(500, 50)

        self.text_cal = QLineEdit(self)
        self.text_cal.setReadOnly(True)
        self.text_cal.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.text_cal.setFixedSize(100,20)
        self.progress_cal = QProgressBar(self)

        self.progress_cal.setFixedSize(700,20)
#############################################################################
        

############################################ 副窗口1 #######################################
        self.btn_sub = QPushButton("导入资源", self)
        self.btn_sub.setFixedSize(200, 40)
        self.sub_window = SubWindow_input(self)
        self.sub_window.hide()
        self.btn_sub.clicked.connect(self.toggle_sub_window_input)

        # layout_.addWidget(self.btn_cal)
        # layout_.addWidget(self.progress_cal)
        # layout_.addWidget(self.text_cal)
        layout_table.addWidget(self.table)

        layout_other.addWidget(self.btn_table)
        layout_other.addWidget(self.btn_cal)
        layout_another.addWidget(self.text_cal)
        layout_another.addWidget(self.progress_cal)
############################################ 副窗口2 #########################################
#####################################################################################################
        self.btn_sub_para = QPushButton("修改参数", self)
        self.btn_sub_para.setFixedSize(200, 40)
        self.sub_window_para = SubWindow_para(self)
        self.sub_window_para.hide()
        self.btn_sub_para.clicked.connect(self.toggle_sub_window_para)

        self.btn_auto_para = QPushButton("从参数表导入参数", self)
        self.btn_auto_para.setFixedSize(200, 40)
        self.btn_auto_para.clicked.connect(self.auto_para_call)

        self.btn_fixed_para = QPushButton("导入内置参数", self)
        self.btn_fixed_para.setFixedSize(200, 40)
        self.btn_fixed_para.clicked.connect(self.fixed_para_call)

        self.btn_analysis = QPushButton("统计分析优化", self)
        self.btn_analysis.setFixedSize(200,40)
        self.sub_window_analysis = SubWindow_analysis(self)
        self.sub_analysis = SubWindow_analysis(self)
        self.btn_analysis.clicked.connect(self.toggle_sub_window_analysis)


        layout_subpara = QHBoxLayout()
        layout_subpara.addWidget(self.btn_sub)
        layout_subpara.addWidget(self.btn_sub_para)
        layout_subpara.addWidget(self.btn_auto_para)
        layout_subpara.addWidget(self.btn_fixed_para)
        layout_subpara.addWidget(self.btn_analysis)





####################### 主布局 ########################################################
        main_hbox = QVBoxLayout()
        # main_hbox.addLayout(layout)
        main_hbox.addLayout(layout_table)
        main_hbox.addLayout(layout_other)
        main_hbox.addLayout(layout_another)
        main_hbox.addLayout(layout_subpara)

        self.setLayout(main_hbox)
######################################################################################
####################### 事件 #######################################################

        self.btn_cal.clicked.connect(self.calculation)
        self.btn_table.clicked.connect(self.loadExcelData)


    def toggle_sub_window_input(self):   # 副窗口1
        if self.sub_window.isVisible():

            parent_global_pos = self.mapToGlobal(QPoint(0, 0))
            x = parent_global_pos.x() - self.sub_window.width() 
            y = parent_global_pos.y()
            self.sub_window.setGeometry(x, y, 300, 600)
            self.sub_window.hide()
        else:

            parent_global_pos = self.mapToGlobal(QPoint(0, 0))
            x = parent_global_pos.x() - self.sub_window.width() 
            y = parent_global_pos.y()
            self.sub_window.setGeometry(x, y, 300 ,600)
            self.sub_window.show()
    
    def toggle_sub_window_para(self):   # 副窗口2
        if self.sub_window_para.isVisible():

            parent_global_pos = self.mapToGlobal(QPoint(0, 0))
            x = parent_global_pos.x() - self.sub_window.width()  
            y = parent_global_pos.y()
            self.sub_window_para.setGeometry(x, y, 800, 600)
            self.sub_window_para.hide()
        else:

            parent_global_pos = self.mapToGlobal(QPoint(0, 0))
            x = parent_global_pos.x() - self.sub_window.width()
            y = parent_global_pos.y()
            self.sub_window_para.setGeometry(x, y, 800 ,600)
            self.sub_window_para.show()

    def toggle_sub_window_analysis(self):   # 副窗口3
        if self.sub_analysis.isVisible():
            parent_global_pos = self.mapToGlobal(QPoint(0, 0))
            x = parent_global_pos.x() - self.sub_window.width()  
            y = parent_global_pos.y()
            self.sub_analysis.setGeometry(x, y, 800, 600)
            self.sub_analysis.hide()
        else:

            parent_global_pos = self.mapToGlobal(QPoint(0, 0))
            x = parent_global_pos.x() - self.sub_window.width()
            y = parent_global_pos.y()
            self.sub_analysis.setGeometry(x, y, 800 ,600)
            self.sub_analysis.show()
    
    
    def auto_para_call(self):
        parameters_input.auto_input(DEMO)
    
    def fixed_para_call(self):
        parameters_input.fixed_input_shantou(DEMO)

    def loadExcelData(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择Excel文件", "", "Excel Files (*.xlsx *.xls)")
        if file_name:
            df = pd.read_excel(file_name)
            self.table.setRowCount(df.shape[0])
            self.table.setColumnCount(df.shape[1])
            self.table.setHorizontalHeaderLabels(df.columns)
            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iat[row, col]))
                    self.table.setItem(row, col, item)

    def calculation(self):
        demo = demo_result.DEMO_Result()
        if hasattr(self.sub_window, 'Pro_Lib')==False or hasattr(self.sub_window, 'Ass_line') == False or hasattr(self.sub_window, 'Ass_trans') == False or hasattr(self.sub_window, 'Dis_Trans') == False or hasattr(self.sub_window,'mid_Volt') == False or hasattr(self.sub_window, 'lowV_trans') == False:
            QMessageBox.about(self,"错误","未完全导入数据")
        else:
            for i in range(1001):
                k = i/10
                self.progress_cal.setValue(k)
                self.text_cal.setText('LCC计算中')
                QApplication.processEvents()
                if i == 50:
                    demo.demo1(self.sub_window.Pro_Lib, self.sub_window.Ass_line, self.sub_window.Ass_trans, self.sub_window.Dis_Trans, self.sub_window.mid_Volt, self.sub_window.lowV_trans, DEMO)
                    print('LCC计算')
                if i == 100:
                    demo.demo2()
                    self.text_cal.setText('LCC结果导出中')
                    print('结果导出')
            self.text_cal.setText('计算结束')

############# 子窗口2 ###################
class SubWindow_para(QWidget):
    def __init__(self, parent):
        super().__init__()
######################### LCC修理成本 #########################
        self.comboBox1 = QComboBox()
        self.Lablel1 = QLabel('全生命周期修理成本')
        self.Lablel1.setFixedSize(250,20)
        self.comboBox1.addItems(["全生命周期修理成本", "20kV变压器全生命周期修理成本", "中压架空线全生命周期修理成本", "中压电缆全生命周期修理成本", "中压柜全生命周期修理成本","低压架空线全生命周期修理成本", "低压电缆全生命周期修理成本","低压柜全生命周期修理成本"])   
        self.comboBox1.activated.connect(self.showSubsubWindow_repairPara)
##############################################################
######################## LCC故障成本 #########################
        self.comboBox2 = QComboBox()
        self.Lablel2 = QLabel('全生命周期故障成本')
        self.Lablel2.setFixedSize(250,20)
        self.comboBox2.addItems(["全生命周期故障成本", "20kV变压器全生命周期故障成本", "中压架空线全生命周期故障成本", "中压电缆全生命周期故障成本", "中压柜全生命周期故障成本","低压架空线全生命周期故障成本", "低压电缆全生命周期故障成本","低压柜全生命周期故障成本"])
        self.comboBox2.activated.connect(self.showSubsubWindow_faultPara)
##############################################################
######################## LCC拆除费用 #########################
        self.comboBox3 = QComboBox()
        self.Lablel3 = QLabel('拆除费用')
        self.Lablel3.setFixedSize(250,20)
        self.comboBox3.addItems(["拆除费用", "20kV变压器拆除费用", "中压架空线拆除费用", "中压电缆拆除费用", "中压柜拆除费用","低压架空线拆除费用", "低压电缆拆除费用","低压柜拆除费用"])
        self.comboBox3.activated.connect(self.showSubsubWindow_removalPara)
##############################################################
####################### 电价与线损 ##########################
        self.comboBox4 = QComboBox()
        self.Lablel4 = QLabel('购电电价与损耗')
        self.Lablel4.setFixedSize(250,20)
        self.comboBox4.addItems(["购电电价与损耗", "电网公司购电电价", "配变损耗率", "中压线路单位长度线损率"])
        self.comboBox4.activated.connect(self.showSubsubWindow_pricelossPara)
##############################################################

################## 可靠性计算系数-解决中压线路过载 #############
        self.comboBox5 = QComboBox()
        self.Lablel5 = QLabel('解决中压线路过载')
        self.Lablel5.setFixedSize(250,20)
        self.comboBox5.addItems(["解决中压线路过载", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox5.activated.connect(self.showSubsubWindow_overloadlinePara)
##############################################################
################## 可靠性计算系数-解决中压线路重载 #############
        self.comboBox6 = QComboBox()
        self.Lablel6 = QLabel('解决中压线路重载')
        self.Lablel6.setFixedSize(250,20)
        self.comboBox6.addItems(["解决中压线路重载", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox6.activated.connect(self.showSubsubWindow_highloadlinePara)
##############################################################
################## 可靠性计算系数-解决配变过载 #############
        self.comboBox7 = QComboBox()
        self.Lablel7 = QLabel('解决配变过载')
        self.Lablel7.setFixedSize(250,20)
        self.comboBox7.addItems(["解决配变过载", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox7.activated.connect(self.showSubsubWindow_overloadtransPara)
##############################################################
################## 可靠性计算系数-解决配变重载 #############
        self.comboBox8 = QComboBox()
        self.Lablel8 = QLabel('解决配变重载')
        self.Lablel8.setFixedSize(250,20)
        self.comboBox8.addItems(["解决配变重载", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox8.activated.connect(self.showSubsubWindow_highloadtransPara)
##############################################################
################## 可靠性计算系数-变电站新出线满足新增负荷供电 #############
        self.comboBox9 = QComboBox()
        self.Lablel9 = QLabel('变电站新出线满足新增负荷供电')
        self.Lablel9.setFixedSize(250,20)
        self.comboBox9.addItems(["变电站新出线满足新增负荷供电", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox9.activated.connect(self.showSubsubWindow_newloadlinePara)
##############################################################
################## 可靠性计算系数-新建台区满足负荷需求 #############
        self.comboBox10 = QComboBox()
        self.Lablel10 = QLabel('新建台区满足负荷需求')
        self.Lablel10.setFixedSize(250,20)
        self.comboBox10.addItems(["新建台区满足负荷需求", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox10.activated.connect(self.showSubsubWindow_newloadtransPara)
##############################################################
################## 可靠性计算系数-改造台区满足新增负荷 #############
        self.comboBox11 = QComboBox()
        self.Lablel11 = QLabel('改造台区满足新增负荷')
        self.Lablel11.setFixedSize(250,20)
        self.comboBox11.addItems(["改造台区满足新增负荷", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox11.activated.connect(self.showSubsubWindow_modifytransPara)
##############################################################
################## 可靠性计算系数-中低压线路存在的安全隐患问题 #############
        self.comboBox12 = QComboBox()
        self.Lablel12 = QLabel('中低压线路存在的安全隐患问题')
        self.Lablel12.setFixedSize(250,20)
        self.comboBox12.addItems(["中低压线路存在的安全隐患问题", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox12.activated.connect(self.showSubsubWindow_safetylinePara)
##############################################################
################## 可靠性计算系数-解决台区电压偏低问题 #############
        self.comboBox13 = QComboBox()
        self.Lablel13 = QLabel('解决台区电压偏低问题')
        self.Lablel13.setFixedSize(250,20)
        self.comboBox13.addItems(["解决台区电压偏低问题", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox13.activated.connect(self.showSubsubWindow_lowVtransPara)
##############################################################
################## 可靠性计算系数-完善中压网架 #############
        self.comboBox14 = QComboBox()
        self.Lablel14 = QLabel('完善中压网架')
        self.Lablel14.setFixedSize(250,20)
        self.comboBox14.addItems(["完善中压网架", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox14.activated.connect(self.showSubsubWindow_netRackPara)
##############################################################
################## 可靠性计算系数-更换残旧设备或线路 #############
        self.comboBox15 = QComboBox()
        self.Lablel15 = QLabel('更换残旧设备或线路')
        self.Lablel15.setFixedSize(250,20)
        self.comboBox15.addItems(["更换残旧设备或线路", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox15.activated.connect(self.showSubsubWindow_replacePara)
##############################################################
################## 可靠性计算系数-配电自动化项目 #############
        self.comboBox16 = QComboBox()
        self.Lablel16 = QLabel('配电自动化项目')
        self.Lablel16.setFixedSize(250,20)
        self.comboBox16.addItems(["配电自动化项目", "归算系数", "上一年度的投资额（元）", "可靠性相关的投资额"])
        self.comboBox16.activated.connect(self.showSubsubWindow_autoPara)
##############################################################
################## 可靠性计算系数-停电相关参数 #############
        self.comboBox17 = QComboBox()
        self.Lablel17 = QLabel('停电相关参数')
        self.Lablel17.setFixedSize(250,20)
        self.comboBox17.addItems(["停电相关参数", "上一年度的用户平均停电时间", "上一年度中压用户数", "本年度的用户平均停电时间","本年度的中压用户数", "本年度减少的停电时户数", "可靠性相关的投资额", "单位投资可减少的停电时户数"])
        self.comboBox17.activated.connect(self.showSubsubWindow_outagePara)
##############################################################
################## 可靠性计算系数-项目相关参数 #############
        self.comboBox18 = QComboBox()
        self.Lablel18 = QLabel('项目相关参数')
        self.Lablel18.setFixedSize(250,20)
        self.comboBox18.addItems(["项目相关参数", "中压项目的新增自动化点个数", "中压项目个数", "低压项目个数","线路平均用户数", "平均项目投资", "平均调整系数"])
        self.comboBox18.activated.connect(self.showSubsubWindow_projectPara)
##############################################################
################## 可靠性计算系数-产电参数 #############
        self.comboBox19 = QComboBox()
        self.Lablel19 = QLabel('产电参数')
        self.Lablel19.setFixedSize(250,20)
        self.comboBox19.addItems(["产电参数", "地区年GDP产值", "地区年供电量", "产电比"])
        self.comboBox19.activated.connect(self.showSubsubWindow_GDPsupplyPara)
##############################################################
################## 可靠性计算系数-负荷惩罚系数 #############
        self.comboBox20 = QComboBox()
        self.Lablel20 = QLabel('负荷惩罚系数')
        self.Lablel20.setFixedSize(250,20)
        self.comboBox20.addItems(["负荷惩罚系数", "工业惩罚系数", "农业惩罚系数", "居民惩罚系数", "商业惩罚系数", "工民混合惩罚系数", "其他惩罚系数"])
        self.comboBox20.activated.connect(self.showSubsubWindow_punishPara)
##############################################################
################## 可靠性计算系数-负荷地区系数 #############
        self.comboBox21 = QComboBox()
        self.Lablel21 = QLabel('负荷地区系数')
        self.Lablel21.setFixedSize(250,20)
        self.comboBox21.addItems(["负荷地区系数", "工业地区系数", "农业地区系数", "居民地区系数", "商业地区系数", "工民混合惩罚系数", "其他惩罚系数"])
        self.comboBox21.activated.connect(self.showSubsubWindow_regionPara)
##############################################################
################## 可靠性计算系数-其他系数 #############
        self.comboBox22 = QComboBox()
        self.Lablel22 = QLabel('其他系数')
        self.Lablel22.setFixedSize(250,20)
        self.comboBox22.addItems(["其他系数", "平均每条线路的中压用户数", "可靠性折现系数", "过载项目缺供电量调整系数"])
        self.comboBox22.activated.connect(self.showSubsubWindow_otherfactorPara)
##############################################################

################## 增供电量计算系数-增供电量系数 #############
        self.comboBox23 = QComboBox()
        self.Lablel23 = QLabel('供电半径')
        self.Lablel23.setFixedSize(250,20)
        self.comboBox23.addItems(["增供电量系数", "新增馈线饱和容量年平均负载率", "新增变压器饱和容量年平均负载率", "新增线路最大供电能力(KW)", "负荷增长率", "单位售电净利润", "新增设备n年可增长至饱和容量", "计算新增线路实际饱和年供电电量的比例系数", "计算新增配变的实际饱和年供电电量的比例系数", "K0"])
        self.comboBox23.activated.connect(self.showSubsubWindow_increasepowerPara)
##############################################################
################## 增供电量计算系数-低压供电半径系数 #############
        self.comboBox24 = QComboBox()
        self.Lablel24 = QLabel('低压供电半径')
        self.Lablel24.setFixedSize(250,20)
        self.comboBox24.addItems(["低压供电半径", "A+", "A", "B", "C", "D"])
        self.comboBox24.activated.connect(self.showSubsubWindow_radiuslowPara)
##############################################################
################## 增供电量计算系数-中压供电半径系数 #############
        self.comboBox25 = QComboBox()
        self.Lablel25 = QLabel('中压供电半径')
        self.Lablel25.setFixedSize(250,20)
        self.comboBox25.addItems(["中压供电半径", "A+", "A", "B", "C", "D"])
        self.comboBox25.activated.connect(self.showSubsubWindow_radiusmiddlePara)
##############################################################
################## 增供电量计算系数-新增馈线饱和容量年平均负载率 #############
        self.comboBox26 = QComboBox()
        self.Lablel26 = QLabel('新增馈线饱和容量年平均负载率')
        self.Lablel26.setFixedSize(250,20)
        self.comboBox26.addItems(["新增馈线饱和容量年平均负载率", "A+", "A", "B", "C", "D"])
        self.comboBox26.activated.connect(self.showSubsubWindow_aveloadlinePara)
##############################################################
################## 增供电量计算系数-新增变压器饱和容量年平均负载率 #############
        self.comboBox27 = QComboBox()
        self.Lablel27 = QLabel('新增变压器饱和容量年平均负载率')
        self.Lablel27.setFixedSize(250,20)
        self.comboBox27.addItems(["新增变压器饱和容量年平均负载率", "A+", "A", "B", "C", "D"])
        self.comboBox27.activated.connect(self.showSubsubWindow_aveloadtransPara)
##############################################################

################## 低电压计算系数-低电压时间在全年的占比 #############
        self.comboBox28 = QComboBox()
        self.Lablel28 = QLabel('低电压时间')
        self.Lablel28.setFixedSize(250,20)
        self.comboBox28.addItems(["低电压时间", "低电压时间在全年的占比"])
        self.comboBox28.activated.connect(self.showSubsubWindow_lowVPara)
##############################################################

################## 残旧设备更换系数-低电压不合格的占比 #############
        self.comboBox29 = QComboBox()
        self.Lablel29 = QLabel('低电压不合格')
        self.Lablel29.setFixedSize(250,20)
        self.comboBox29.addItems(["低电压不合格", "低电压不合格的时间的占比"])
        self.comboBox29.activated.connect(self.showSubsubWindow_unqualifiedPara)
##############################################################
        layout_box_all = QHBoxLayout()

        layout_box1 = QHBoxLayout()
        layout_box1.addWidget(self.comboBox1)
        layout_box1.addWidget(self.Lablel1)

        layout_box2 = QHBoxLayout()
        layout_box2.addWidget(self.comboBox2)
        layout_box2.addWidget(self.Lablel2)

        layout_box3 = QHBoxLayout()
        layout_box3.addWidget(self.comboBox3)
        layout_box3.addWidget(self.Lablel3)

        layout_box4 = QHBoxLayout()
        layout_box4.addWidget(self.comboBox4)
        layout_box4.addWidget(self.Lablel4)

        layout_box5 = QHBoxLayout()
        layout_box5.addWidget(self.comboBox5)
        layout_box5.addWidget(self.Lablel5)

        layout_box6 = QHBoxLayout()
        layout_box6.addWidget(self.comboBox6)
        layout_box6.addWidget(self.Lablel6)

        layout_box7 = QHBoxLayout()
        layout_box7.addWidget(self.comboBox7)
        layout_box7.addWidget(self.Lablel7)

        layout_box8 = QHBoxLayout()
        layout_box8.addWidget(self.comboBox8)
        layout_box8.addWidget(self.Lablel8)

        layout_box9 = QHBoxLayout()
        layout_box9.addWidget(self.comboBox9)
        layout_box9.addWidget(self.Lablel9)

        layout_box10 = QHBoxLayout()
        layout_box10.addWidget(self.comboBox10)
        layout_box10.addWidget(self.Lablel10)

        layout_box11 = QHBoxLayout()
        layout_box11.addWidget(self.comboBox11)
        layout_box11.addWidget(self.Lablel11)

        layout_box12 = QHBoxLayout()
        layout_box12.addWidget(self.comboBox12)
        layout_box12.addWidget(self.Lablel12)

        layout_box13 = QHBoxLayout()
        layout_box13.addWidget(self.comboBox13)
        layout_box13.addWidget(self.Lablel13)

        layout_box14 = QHBoxLayout()
        layout_box14.addWidget(self.comboBox14)
        layout_box14.addWidget(self.Lablel14)

        layout_box15 = QHBoxLayout()
        layout_box15.addWidget(self.comboBox15)
        layout_box15.addWidget(self.Lablel15)

        layout_box16 = QHBoxLayout()
        layout_box16.addWidget(self.comboBox16)
        layout_box16.addWidget(self.Lablel16)

        layout_box17 = QHBoxLayout()
        layout_box17.addWidget(self.comboBox17)
        layout_box17.addWidget(self.Lablel17)

        layout_box18 = QHBoxLayout()
        layout_box18.addWidget(self.comboBox18)
        layout_box18.addWidget(self.Lablel18)

        layout_box19 = QHBoxLayout()
        layout_box19.addWidget(self.comboBox19)
        layout_box19.addWidget(self.Lablel19)

        layout_box20 = QHBoxLayout()
        layout_box20.addWidget(self.comboBox20)
        layout_box20.addWidget(self.Lablel20)

        layout_box21 = QHBoxLayout()
        layout_box21.addWidget(self.comboBox21)
        layout_box21.addWidget(self.Lablel21)

        layout_box22 = QHBoxLayout()
        layout_box22.addWidget(self.comboBox22)
        layout_box22.addWidget(self.Lablel22)

        layout_box23 = QHBoxLayout()
        layout_box23.addWidget(self.comboBox23)
        layout_box23.addWidget(self.Lablel23)

        layout_box24 = QHBoxLayout()
        layout_box24.addWidget(self.comboBox24)
        layout_box24.addWidget(self.Lablel24)

        layout_box25 = QHBoxLayout()
        layout_box25.addWidget(self.comboBox25)
        layout_box25.addWidget(self.Lablel25)

        layout_box26 = QHBoxLayout()
        layout_box26.addWidget(self.comboBox26)
        layout_box26.addWidget(self.Lablel26)

        layout_box27 = QHBoxLayout()
        layout_box27.addWidget(self.comboBox27)
        layout_box27.addWidget(self.Lablel27)

        layout_box28 = QHBoxLayout()
        layout_box28.addWidget(self.comboBox28)
        layout_box28.addWidget(self.Lablel28)

        layout_box29 = QHBoxLayout()
        layout_box29.addWidget(self.comboBox29)
        layout_box29.addWidget(self.Lablel29)

        layout_box1234 = QVBoxLayout()
        layout_box1234.addLayout(layout_box1)
        layout_box1234.addLayout(layout_box2)
        layout_box1234.addLayout(layout_box3)
        layout_box1234.addLayout(layout_box4)

        layout_box516 = QVBoxLayout()
        layout_box1722 = QVBoxLayout()
        layout_box2327 = QVBoxLayout()

        layout_box2327.addLayout(layout_box23)
        layout_box2327.addLayout(layout_box24)
        layout_box2327.addLayout(layout_box25)
        layout_box2327.addLayout(layout_box26)
        layout_box2327.addLayout(layout_box27)

        layout_box1234_2325 = QVBoxLayout()
        layout_box1234_2325.addLayout(layout_box1234)
        layout_box1234_2325.addLayout(layout_box2327)

        layout_box28_ = QVBoxLayout()
        layout_box28_.addLayout(layout_box28)

        layout_box516.addLayout(layout_box5)
        layout_box516.addLayout(layout_box6)
        layout_box516.addLayout(layout_box7)
        layout_box516.addLayout(layout_box8)
        layout_box516.addLayout(layout_box9)
        layout_box516.addLayout(layout_box10)
        layout_box516.addLayout(layout_box11)
        layout_box516.addLayout(layout_box12)
        layout_box516.addLayout(layout_box13)
        layout_box516.addLayout(layout_box14)
        layout_box516.addLayout(layout_box15)
        layout_box516.addLayout(layout_box16)

        layout_box516_28 = QVBoxLayout()
        layout_box516_28.addLayout(layout_box516)
        layout_box516_28.addLayout(layout_box28_)

        layout_box1722.addLayout(layout_box17)
        layout_box1722.addLayout(layout_box18)
        layout_box1722.addLayout(layout_box19)
        layout_box1722.addLayout(layout_box20)
        layout_box1722.addLayout(layout_box21)
        layout_box1722.addLayout(layout_box22)

        layout_box29_ = QVBoxLayout()
        layout_box29_.addLayout(layout_box29)
        layout_box1722_29 = QVBoxLayout()
        layout_box1722_29.addLayout(layout_box1722)
        layout_box1722_29.addLayout(layout_box29_)

        layout_box_all.addLayout(layout_box1234_2325)
        layout_box_all.addLayout(layout_box516_28)
        layout_box_all.addLayout(layout_box1722_29)
        self.setLayout(layout_box_all)
        
        self.setWindowTitle("参数子窗口")
        parent_global_pos = parent.mapToGlobal(QPoint(0, 0))
        x = parent_global_pos.x()
        y = parent_global_pos.y() - parent.height()
        self.hide()
        self.setGeometry(x, y, 600, 600)
        self.tmp_para = 0
        self.fig = 0
    def receive_(self,data):
        # print(data)
        self.tmp_para = data
        # print(self.tmp_para)
############################## LCC修理成本选项 ##################################
    def showSubsubWindow_repairPara(self, index):
        if index == 1: 
            print(self.tmp_para)

            if self.tmp_para !=  DEMO.repairCost_Mtrans and self.tmp_para != 0 and self.fig == 1:
                DEMO.repairCost_Mtrans = self.tmp_para
                self.tmp_para = 0
            self.fig = 1
            self.customWidget = SubsubWindow_Para(DEMO.repairCost_Mtrans*1000, "全寿命周期修理成本 20kV变压器")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.repairCost_Mline and self.tmp_para != 0 and self.fig == 2:
                DEMO.repairCost_Mline = self.tmp_para
                self.tmp_para = 0
            self.fig = 2
            self.customWidget = SubsubWindow_Para(DEMO.repairCost_Mline*1000, "全寿命周期修理成本 中压架空线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.repairCost_Mcable and self.tmp_para != 0 and self.fig == 3:
                DEMO.repairCost_Mcable = self.tmp_para
                self.tmp_para = 0
            self.fig = 3
            self.customWidget = SubsubWindow_Para(DEMO.repairCost_Mcable*1000, "全寿命周期修理成本 中压电缆线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.repairCost_Munits and self.tmp_para != 0 and self.fig == 4:
                DEMO.repairCost_Munits = self.tmp_para
                self.tmp_para = 0
            self.fig = 4
            self.customWidget = SubsubWindow_Para(DEMO.repairCost_Munits*1000, "全寿命周期修理成本 中压柜")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.repairCost_Lline and self.tmp_para != 0 and self.fig == 5:
                DEMO.repairCost_Lline = self.tmp_para
                self.tmp_para = 0
            self.fig = 5
            self.customWidget = SubsubWindow_Para(DEMO.repairCost_Lline*1000, "全寿命周期修理成本 低压架空线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 6:
            if self.tmp_para !=  DEMO.repairCost_Lcable and self.tmp_para != 0 and self.fig == 6:
                DEMO.repairCost_Lcable = self.tmp_para
                self.tmp_para = 0
            self.fig = 6
            self.customWidget = SubsubWindow_Para(DEMO.repairCost_Lcable*1000, "全寿命周期修理成本 低压电缆")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 7:
            if self.tmp_para !=  DEMO.repairCost_Lunits and self.tmp_para != 0 and self.fig == 7:
                DEMO.repairCost_Lunits = self.tmp_para
                self.tmp_para = 0
            self.fig = 7
            self.customWidget = SubsubWindow_Para(DEMO.repairCost_Lunits*1000, "全寿命周期修理成本 低压柜")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
################################################################################
############################## LCC故障成本选项 ##################################
    def showSubsubWindow_faultPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.faultCost_Mtrans and self.tmp_para != 0 and self.fig == 8:
                DEMO.faultCost_Mtrans = self.tmp_para
                self.tmp_para = 0
            self.fig = 8
            self.customWidget = SubsubWindow_Para(DEMO.faultCost_Mtrans*1000, "全寿命周期故障成本 20kV变压器")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.faultCost_Mline and self.tmp_para != 0 and self.fig == 9:
                DEMO.faultCost_Mline = self.tmp_para
                self.tmp_para = 0
            self.fig = 9
            self.customWidget = SubsubWindow_Para(DEMO.faultCost_Mline*1000, "全寿命周期故障成本 中压架空线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.faultCost_Mcable and self.tmp_para != 0 and self.fig == 10:
                DEMO.faultCost_Mcable = self.tmp_para
                self.tmp_para = 0
            self.fig = 10
            self.customWidget = SubsubWindow_Para(DEMO.faultCost_Mcable*1000, "全寿命周期故障成本 中压电缆线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.faultCost_Munits and self.tmp_para != 0 and self.fig == 11:
                DEMO.faultCost_Munits = self.tmp_para
                self.tmp_para = 0
            self.fig = 11
            self.customWidget = SubsubWindow_Para(DEMO.faultCost_Munits*1000, "全寿命周期故障成本 中压柜")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.faultCost_Lline and self.tmp_para != 0 and self.fig == 12:
                DEMO.faultCost_Lline = self.tmp_para
                self.tmp_para = 0
            self.fig = 12
            self.customWidget = SubsubWindow_Para(DEMO.faultCost_Lline*1000, "全寿命周期故障成本 低压架空线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 6:
            if self.tmp_para !=  DEMO.faultCost_Lcable and self.tmp_para != 0 and self.fig == 13:
                DEMO.faultCost_Lcable = self.tmp_para
                self.tmp_para = 0
            self.fig = 13
            self.customWidget = SubsubWindow_Para(DEMO.faultCost_Lcable*1000, "全寿命周期故障成本 低压电缆")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 7:
            if self.tmp_para !=  DEMO.faultCost_Lunits and self.tmp_para != 0 and self.fig == 14:
                DEMO.faultCost_Lunits = self.tmp_para
                self.tmp_para = 0
            self.fig = 14
            self.customWidget = SubsubWindow_Para(DEMO.faultCost_Lunits*1000, "全寿命周期故障成本 低压柜")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
##############################################################################
############################## LCC拆除费用选项 ##################################
    def showSubsubWindow_removalPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.removalCost_Mtrans and self.tmp_para != 0 and self.fig == 15:
                DEMO.removalCost_Mtrans = self.tmp_para
                self.tmp_para = 0
            self.fig = 15
            self.customWidget = SubsubWindow_Para(DEMO.removalCost_Mtrans*1000, "拆除费用 20kV变压器")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.removalCost_Mline and self.tmp_para != 0 and self.fig == 16:
                DEMO.removalCost_Mline = self.tmp_para
                self.tmp_para = 0
            self.fig = 16
            self.customWidget = SubsubWindow_Para(DEMO.removalCost_Mline*1000, "拆除费用 中压架空线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.removalCost_Mcable and self.tmp_para != 0 and self.fig == 17:
                DEMO.removalCost_Mcable = self.tmp_para
                self.tmp_para = 0
            self.fig = 17
            self.customWidget = SubsubWindow_Para(DEMO.removalCost_Mcable*1000, "拆除费用 中压电缆线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.removalCost_Munits and self.tmp_para != 0 and self.fig == 18:
                DEMO.removalCost_Munits = self.tmp_para
                self.tmp_para = 0
            self.fig = 18
            self.customWidget = SubsubWindow_Para(DEMO.removalCost_Munits*1000, "拆除费用 中压柜")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.removalCost_Lline and self.tmp_para != 0 and self.fig == 19:
                DEMO.removalCost_Lline = self.tmp_para
                self.tmp_para = 0
            self.fig = 19
            self.customWidget = SubsubWindow_Para(DEMO.removalCost_Lline*1000, "拆除费用 低压架空线")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
            
        elif index == 6:
            if self.tmp_para !=  DEMO.removalCost_Lcable and self.tmp_para != 0 and self.fig == 20:
                DEMO.removalCost_Lcable = self.tmp_para
                self.tmp_para = 0
            self.fig = 20
            self.customWidget = SubsubWindow_Para(DEMO.removalCost_Lcable*1000, "拆除费用 低压电缆")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 7:
            if self.tmp_para !=  DEMO.removalCost_Lunits and self.tmp_para != 0 and self.fig == 21:
                DEMO.removalCost_Lunits = self.tmp_para
                self.tmp_para = 0
            self.fig = 21
            self.customWidget = SubsubWindow_Para(DEMO.removalCost_Lunits*1000, "拆除费用 低压柜")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
##############################################################################
############################## LCC电价与损耗选项 ##################################
    def showSubsubWindow_pricelossPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.purchase_price and self.tmp_para != 0 and self.fig == 22:
                DEMO.purchase_price = self.tmp_para
                self.tmp_para = 0
            self.fig = 22
            self.customWidget = SubsubWindow_Para(DEMO.purchase_price*1000, "电网公司 购电电价")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.DisTran_lossRate and self.tmp_para != 0 and self.fig == 23:
                DEMO.DisTran_lossRate = self.tmp_para
                self.tmp_para = 0
            self.fig = 23
            self.customWidget = SubsubWindow_Para(DEMO.DisTran_lossRate*1000, "配变损耗率")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.linePerLen_lossRate and self.tmp_para != 0 and self.fig == 24:
                DEMO.linePerLen_lossRate = self.tmp_para
                self.tmp_para = 0
            self.fig = 24
            self.customWidget = SubsubWindow_Para(DEMO.linePerLen_lossRate*1000, "中压线路单位长度线损率")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
##############################################################################
############################## 中压线路过载 ##################################
    def showSubsubWindow_overloadlinePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.overload_line_factor and self.tmp_para != 0 and self.fig == 25:
                DEMO.overload_line_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 25
            self.customWidget = SubsubWindow_Para(DEMO.overload_line_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.overload_line_invest and self.tmp_para != 0 and self.fig == 26:
                DEMO.overload_line_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 26
            self.customWidget = SubsubWindow_Para(DEMO.overload_line_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.overload_line_rely and self.tmp_para != 0 and self.fig == 27:
                DEMO.overload_line_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 27
            self.customWidget = SubsubWindow_Para(DEMO.overload_line_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 中压线路重载 ##################################
    def showSubsubWindow_highloadlinePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.highload_line_factor and self.tmp_para != 0 and self.fig == 28:
                DEMO.highload_line_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 28
            self.customWidget = SubsubWindow_Para(DEMO.highload_line_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.highload_line_invest and self.tmp_para != 0 and self.fig == 29:
                DEMO.highload_line_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 29
            self.customWidget = SubsubWindow_Para(DEMO.highload_line_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.highload_line_rely and self.tmp_para != 0 and self.fig == 30:
                DEMO.highload_line_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 30
            self.customWidget = SubsubWindow_Para(DEMO.highload_line_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 配变过载 ##################################
    def showSubsubWindow_overloadtransPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.overload_trans_factor and self.tmp_para != 0 and self.fig == 31:
                DEMO.overload_trans_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 31
            self.customWidget = SubsubWindow_Para(DEMO.overload_trans_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.overload_trans_invest and self.tmp_para != 0 and self.fig == 32:
                DEMO.overload_trans_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 32
            self.customWidget = SubsubWindow_Para(DEMO.overload_trans_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.overload_trans_rely and self.tmp_para != 0 and self.fig == 33:
                DEMO.overload_trans_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 33
            self.customWidget = SubsubWindow_Para(DEMO.overload_trans_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 配变重载 ##################################
    def showSubsubWindow_highloadtransPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.highload_trans_factor and self.tmp_para != 0 and self.fig == 34:
                DEMO.highload_trans_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 34
            self.customWidget = SubsubWindow_Para(DEMO.highload_trans_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.highload_trans_invest and self.tmp_para != 0 and self.fig == 35:
                DEMO.highload_trans_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 35
            self.customWidget = SubsubWindow_Para(DEMO.highload_trans_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.highload_trans_rely and self.tmp_para != 0 and self.fig == 36:
                DEMO.highload_trans_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 36
            self.customWidget = SubsubWindow_Para(DEMO.highload_trans_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 变电站新出线满足新增负荷供电 ##################################
    def showSubsubWindow_newloadlinePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.newload_line_factor and self.tmp_para != 0 and self.fig == 37:
                DEMO.newload_line_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 37
            self.customWidget = SubsubWindow_Para(DEMO.newload_line_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.newload_line_invest and self.tmp_para != 0 and self.fig == 38:
                DEMO.newload_line_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 38
            self.customWidget = SubsubWindow_Para(DEMO.newload_line_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.newload_line_rely and self.tmp_para != 0 and self.fig == 39:
                DEMO.newload_line_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 39
            self.customWidget = SubsubWindow_Para(DEMO.newload_line_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 新建台区满足负荷需求 ##################################
    def showSubsubWindow_newloadtransPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.newload_trans_factor and self.tmp_para != 0 and self.fig == 40:
                DEMO.newload_trans_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 40
            self.customWidget = SubsubWindow_Para(DEMO.newload_trans_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.newload_trans_invest and self.tmp_para != 0 and self.fig == 41:
                DEMO.newload_trans_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 41
            self.customWidget = SubsubWindow_Para(DEMO.newload_trans_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.newload_trans_rely and self.tmp_para != 0 and self.fig == 42:
                DEMO.newload_trans_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 42
            self.customWidget = SubsubWindow_Para(DEMO.newload_trans_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 改造台区满足新增负荷 ##################################
    def showSubsubWindow_modifytransPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.modify_trans_factor and self.tmp_para != 0 and self.fig == 43:
                DEMO.modify_trans_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 43
            self.customWidget = SubsubWindow_Para(DEMO.modify_trans_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.modify_trans_invest and self.tmp_para != 0 and self.fig == 44:
                DEMO.modify_trans_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 44
            self.customWidget = SubsubWindow_Para(DEMO.modify_trans_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.modify_trans_rely and self.tmp_para != 0 and self.fig == 45:
                DEMO.modify_trans_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 45
            self.customWidget = SubsubWindow_Para(DEMO.modify_trans_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 解决中低压线路存在的安全隐患问题 ##################################
    def showSubsubWindow_safetylinePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.safety_line_factor and self.tmp_para != 0 and self.fig == 46:
                DEMO.safety_line_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 46
            self.customWidget = SubsubWindow_Para(DEMO.safety_line_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.safety_line_invest and self.tmp_para != 0 and self.fig == 47:
                DEMO.safety_line_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 47
            self.customWidget = SubsubWindow_Para(DEMO.safety_line_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.safety_line_rely and self.tmp_para != 0 and self.fig == 48:
                DEMO.safety_line_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 48
            self.customWidget = SubsubWindow_Para(DEMO.safety_line_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 解决台区电压偏低问题 ##################################
    def showSubsubWindow_lowVtransPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.lowV_trans_factor and self.tmp_para != 0 and self.fig == 49:
                DEMO.lowV_trans_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 49
            self.customWidget = SubsubWindow_Para(DEMO.lowV_trans_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.lowV_trans_invest and self.tmp_para != 0 and self.fig == 50:
                DEMO.lowV_trans_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 50
            self.customWidget = SubsubWindow_Para(DEMO.lowV_trans_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.lowV_trans_rely and self.tmp_para != 0 and self.fig == 51:
                DEMO.lowV_trans_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 51
            self.customWidget = SubsubWindow_Para(DEMO.lowV_trans_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
######################################################################### 
############################## 完善中压网架 ##################################
    def showSubsubWindow_netRackPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.netRack_factor and self.tmp_para != 0 and self.fig == 52:
                DEMO.netRack_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 52
            self.customWidget = SubsubWindow_Para(DEMO.netRack_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.netRack_invest and self.tmp_para != 0 and self.fig == 53:
                DEMO.netRack_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 53
            self.customWidget = SubsubWindow_Para(DEMO.netRack_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.netRack_rely and self.tmp_para != 0 and self.fig == 54:
                DEMO.netRack_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 54
            self.customWidget = SubsubWindow_Para(DEMO.netRack_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 更换残旧设备或线路 ##################################
    def showSubsubWindow_replacePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.repalce_factor and self.tmp_para != 0 and self.fig == 55:
                DEMO.replace_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 55
            self.customWidget = SubsubWindow_Para(DEMO.replace_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.replace_invest and self.tmp_para != 0 and self.fig == 56:
                DEMO.replace_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 56
            self.customWidget = SubsubWindow_Para(DEMO.replace_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.replace_rely and self.tmp_para != 0 and self.fig == 57:
                DEMO.replace_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 57
            self.customWidget = SubsubWindow_Para(DEMO.replace_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 配电自动化项目 ##################################
    def showSubsubWindow_autoPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.auto_factor and self.tmp_para != 0 and self.fig == 58:
                DEMO.auto_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 58
            self.customWidget = SubsubWindow_Para(DEMO.auto_factor*1000,"归算系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.auto_invest and self.tmp_para != 0 and self.fig == 59:
                DEMO.auto_invest = self.tmp_para
                self.tmp_para = 0
            self.fig = 59
            self.customWidget = SubsubWindow_Para(DEMO.auto_invest*1000, "上一年度的投资额（万元）")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.auto_rely and self.tmp_para != 0 and self.fig == 60:
                DEMO.auto_rely = self.tmp_para
                self.tmp_para = 0
            self.fig = 60
            self.customWidget = SubsubWindow_Para(DEMO.auto_rely*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 停电相关参数 ##################################
    def showSubsubWindow_outagePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.outage_user_last and self.tmp_para != 0 and self.fig == 61:
                DEMO.outage_user_last = self.tmp_para
                self.tmp_para = 0
            self.fig = 61
            self.customWidget = SubsubWindow_Para(DEMO.outage_user_last*1000, "上一年度的用户平均停电时间")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.amount_user_last and self.tmp_para != 0 and self.fig == 62:
                DEMO.amount_user_last = self.tmp_para
                self.tmp_para = 0
            self.fig = 62
            self.customWidget = SubsubWindow_Para(DEMO.amount_user_last*1000, "上一年度中压用户数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.outage_user and self.tmp_para != 0 and self.fig == 63:
                DEMO.outage_user = self.tmp_para
                self.tmp_para = 0
            self.fig = 63
            self.customWidget = SubsubWindow_Para(DEMO.outage_user*1000, "本年度的用户平均停电时间")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.amount_user and self.tmp_para != 0 and self.fig == 64:
                DEMO.amount_user = self.tmp_para
                self.tmp_para = 0
            self.fig = 64
            self.customWidget = SubsubWindow_Para(DEMO.amount_user*1000, "本年度的中压用户数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.outage_user_reduce and self.tmp_para != 0 and self.fig == 65:
                DEMO.outage_user_reduce = self.tmp_para
                self.tmp_para = 0
            self.fig = 65
            self.customWidget = SubsubWindow_Para(DEMO.outage_user_reduce*1000, "本年度减少的停电时户数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
            
        elif index == 6:
            if self.tmp_para !=  DEMO.reliable_investment and self.tmp_para != 0 and self.fig == 66:
                DEMO.reliable_investment = self.tmp_para
                self.tmp_para = 0
            self.fig = 66
            self.customWidget = SubsubWindow_Para(DEMO.reliable_investment*1000, "可靠性相关的投资额")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 7:
            if self.tmp_para !=  DEMO.could_reduce_users and self.tmp_para != 0 and self.fig == 67:
                DEMO.could_reduce_users = self.tmp_para
                self.tmp_para = 0
            self.fig = 67
            self.customWidget = SubsubWindow_Para(DEMO.could_reduce_users*1000, "单位投资可减少的停电时户数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
##############################################################################
############################## 项目相关参数 ##################################
    def showSubsubWindow_projectPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.middle_newAuto and self.tmp_para != 0 and self.fig == 68:
                DEMO.middle_newAuto = self.tmp_para
                self.tmp_para = 0
            self.fig = 68
            self.customWidget = SubsubWindow_Para(DEMO.middle_newAuto*1000, "中压项目的新增自动化点个数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.middle_project and self.tmp_para != 0 and self.fig == 69:
                DEMO.middle_project = self.tmp_para
                self.tmp_para = 0
            self.fig = 69
            self.customWidget = SubsubWindow_Para(DEMO.middle_project*1000, "中压项目个数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.low_project and self.tmp_para != 0 and self.fig == 70:
                DEMO.low_project = self.tmp_para
                self.tmp_para = 0
            self.fig = 70
            self.customWidget = SubsubWindow_Para(DEMO.low_project*1000, "低压项目个数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.ave_users and self.tmp_para != 0 and self.fig == 71:
                DEMO.ave_users = self.tmp_para
                self.tmp_para = 0
            self.fig = 71
            self.customWidget = SubsubWindow_Para(DEMO.ave_users*1000, "线路平均用户数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.ave_proInvest and self.tmp_para != 0 and self.fig == 72:
                DEMO.ave_proInvest = self.tmp_para
                self.tmp_para = 0
            self.fig = 72
            self.customWidget = SubsubWindow_Para(DEMO.ave_proInvest*1000, "平均项目投资")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
            
        elif index == 6:
            if self.tmp_para !=  DEMO.ave_adjusted and self.tmp_para != 0 and self.fig == 73:
                DEMO.ave_adjusted = self.tmp_para
                self.tmp_para = 0
            self.fig = 73
            self.customWidget = SubsubWindow_Para(DEMO.ave_adjusted*1000, "平均调整系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        else:
            QMessageBox.about(self,"错误","不合法操作")
##############################################################################
############################## 配电自动化项目 ##################################
    def showSubsubWindow_GDPsupplyPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.region_GDP and self.tmp_para != 0 and self.fig == 74:
                DEMO.region_GDP = self.tmp_para
                self.tmp_para = 0
            self.fig = 74
            self.customWidget = SubsubWindow_Para(DEMO.region_GDP*1000,"地区GDP产值")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.region_supply and self.tmp_para != 0 and self.fig == 75:
                DEMO.region_supply = self.tmp_para
                self.tmp_para = 0
            self.fig = 75
            self.customWidget = SubsubWindow_Para(DEMO.region_supply*1000,"地区年供电量")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.GDP_SUPPLY and self.tmp_para != 0 and self.fig == 76:
                DEMO.GDP_SUPPLY = self.tmp_para
                self.tmp_para = 0
            self.fig = 76
            self.customWidget = SubsubWindow_Para(DEMO.GDP_SUPPLY*1000, "产电比")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 负荷惩罚系数 ##################################
    def showSubsubWindow_punishPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.punish_factor[0] and self.tmp_para != 0 and self.fig == 77:
                DEMO.punish_factor[0] = self.tmp_para
                self.tmp_para = 0
            self.fig = 77
            self.customWidget = SubsubWindow_Para(DEMO.punish_factor[0]*1000, "工业惩罚系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.punish_factor[1] and self.tmp_para != 0 and self.fig == 78:
                DEMO.punish_factor[1] = self.tmp_para
                self.tmp_para = 0
            self.fig = 78
            self.customWidget = SubsubWindow_Para(DEMO.punish_factor[2]*1000, "农业惩罚系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.punish_factor[2] and self.tmp_para != 0 and self.fig == 79:
                DEMO.punish_factor[2] = self.tmp_para
                self.tmp_para = 0
            self.fig = 79
            self.customWidget = SubsubWindow_Para(DEMO.punish_factor[2]*1000, "居民惩罚系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.punish_factor[3] and self.tmp_para != 0 and self.fig == 80:
                DEMO.punish_factor[3] = self.tmp_para
                self.tmp_para = 0
            self.fig = 80
            self.customWidget = SubsubWindow_Para(DEMO.punish_factor[3]*1000, "商业惩罚系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.punish_factor[4] and self.tmp_para != 0 and self.fig == 81:
                DEMO.punish_factor[4] = self.tmp_para
                self.tmp_para = 0
            self.fig = 81
            self.customWidget = SubsubWindow_Para(DEMO.punish_factor[4]*1000, "工民混合惩罚系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
            
        elif index == 6:
            if self.tmp_para !=  DEMO.punish_factor[5] and self.tmp_para != 0 and self.fig == 82:
                DEMO.punish_factor[5] = self.tmp_para
                self.tmp_para = 0
            self.fig = 82
            self.customWidget = SubsubWindow_Para(DEMO.punish_factor[5]*1000, "其他惩罚系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        else:
            QMessageBox.about(self,"错误","不合法操作")
##############################################################################
############################## 负荷系数 ##################################
    def showSubsubWindow_regionPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.region[0] and self.tmp_para != 0 and self.fig == 83:
                DEMO.region[0] = self.tmp_para
                self.tmp_para = 0
            self.fig = 83
            self.customWidget = SubsubWindow_Para(DEMO.region[0]*1000, "工业地区系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.region[1] and self.tmp_para != 0 and self.fig == 84:
                DEMO.region[1] = self.tmp_para
                self.tmp_para = 0
            self.fig = 84
            self.customWidget = SubsubWindow_Para(DEMO.region[2]*1000, "农业地区系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.region[2] and self.tmp_para != 0 and self.fig == 85:
                DEMO.region[2] = self.tmp_para
                self.tmp_para = 0
            self.fig = 85
            self.customWidget = SubsubWindow_Para(DEMO.region[2]*1000, "居民地区系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.region[3] and self.tmp_para != 0 and self.fig == 86:
                DEMO.region[3] = self.tmp_para
                self.tmp_para = 0
            self.fig = 86
            self.customWidget = SubsubWindow_Para(DEMO.region[3]*1000, "商业地区系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.region[4] and self.tmp_para != 0 and self.fig == 87:
                DEMO.region[4] = self.tmp_para
                self.tmp_para = 0
            self.fig = 87
            self.customWidget = SubsubWindow_Para(DEMO.region[4]*1000, "工民混合地区系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
            
        elif index == 6:
            if self.tmp_para !=  DEMO.region[5] and self.tmp_para != 0 and self.fig == 88:
                DEMO.region[5] = self.tmp_para
                self.tmp_para = 0
            self.fig = 88
            self.customWidget = SubsubWindow_Para(DEMO.region[5]*1000, "其他地区系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 7:
            if self.tmp_para !=  DEMO.region and self.tmp_para != 0 and self.fig == 89:
                DEMO.region = self.tmp_para
                self.tmp_para = 0
            self.fig = 89
            self.customWidget = SubsubWindow_Para(DEMO.region*1000, "单位投资可地区的停电时户数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
############################## 其他系数 ##################################
    def showSubsubWindow_otherfactorPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.ave_middle_users and self.tmp_para != 0 and self.fig == 90:
                DEMO.ave_middle_users = self.tmp_para
                self.tmp_para = 0
            self.fig = 90
            self.customWidget = SubsubWindow_Para(DEMO.ave_middle_users*1000,"平均每条线路的中压用户数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.sum_rely_discount_rate and self.tmp_para != 0 and self.fig == 91:
                DEMO.sum_rely_discount_rate = self.tmp_para
                self.tmp_para = 0
            self.fig = 91
            self.customWidget = SubsubWindow_Para(DEMO.sum_rely_discount_rate*1000,"可靠性折现系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
    
        elif index == 3:
            if self.tmp_para !=  DEMO.overload_lackpower_factor and self.tmp_para != 0 and self.fig == 92:
                DEMO.overload_lackpower_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 92
            self.customWidget = SubsubWindow_Para(DEMO.overload_lackpower_factor*1000, "过载项目缺供电量调整系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.discount_rate and self.tmp_para != 0 and self.fig == 93:
                DEMO.discount_rate = self.tmp_para
                DEMO.rely_discount_rate = [0]*30
                DEMO.rely_discount_rate[0] = 1
                for i in range(2, 31):
                    DEMO.rely_discount_rate[i-1] = 1/(pow((1+DEMO.discount_rate),(i-1)))                
                DEMO.sum_rely_discount_rate = sum(DEMO.rely_discount_rate)
                self.tmp_para = 0
            self.fig = 93
            self.customWidget = SubsubWindow_Para(DEMO.discount_rate*1000, "折现率")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
#########################################################################
############################## 增供电量系数 ##################################
    def showSubsubWindow_increasepowerPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.Add_line_aveLoad and self.tmp_para != 0 and self.fig == 94:
                DEMO.Add_line_aveLoad = self.tmp_para
                self.tmp_para = 0
            self.fig = 94
            self.customWidget = SubsubWindow_Para(DEMO.Add_line_aveLoad*1000, "新增馈线饱和容量年平均负载率")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.Add_trans_aveLoad and self.tmp_para != 0 and self.fig == 95:
                DEMO.Add_trans_aveLoad = self.tmp_para
                self.tmp_para = 0
            self.fig = 95
            self.customWidget = SubsubWindow_Para(DEMO.Add_trans_aveLoad*1000, "新增变压器饱和容量年平均负载率")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.max_supplyAbility and self.tmp_para != 0 and self.fig == 96:
                DEMO.max_supplyAbility = self.tmp_para
                self.tmp_para = 0
            self.fig = 96
            self.customWidget = SubsubWindow_Para(DEMO.max_supplyAbility*1000, "新增线路最大供电能力(KW)")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.growth_rate and self.tmp_para != 0 and self.fig == 97:
                DEMO.growth_rate = self.tmp_para
                self.tmp_para = 0
            self.fig = 97
            self.customWidget = SubsubWindow_Para(DEMO.growth_rate*1000, "负荷增长率")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.sales_profit and self.tmp_para != 0 and self.fig == 98:
                DEMO.sales_profit = self.tmp_para
                self.tmp_para = 0
            self.fig = 98
            self.customWidget = SubsubWindow_Para(DEMO.sales_profit*1000, "单位售电净利润")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
            
        elif index == 6:
            if self.tmp_para !=  DEMO.years_to_saturation and self.tmp_para != 0 and self.fig == 99:
                DEMO.years_to_saturation = self.tmp_para
                self.tmp_para = 0
            self.fig = 99
            self.customWidget = SubsubWindow_Para(DEMO.years_to_saturation*1000, "新增设备n年可增长至饱和容量")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 7:
            if self.tmp_para !=  DEMO.scale_line_factor and self.tmp_para != 0 and self.fig == 100:
                DEMO.scale_line_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 100
            self.customWidget = SubsubWindow_Para(DEMO.scale_line_factor*1000, "计算新增线路实际饱和年供电电量的比例系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 8:
            if self.tmp_para !=  DEMO.scale_trans_factor and self.tmp_para != 0 and self.fig == 101:
                DEMO.scale_trans_factor = self.tmp_para
                self.tmp_para = 0
            self.fig = 101
            self.customWidget = SubsubWindow_Para(DEMO.scale_trans_factor*1000, "计算新增配变的实际饱和年供电电量的比例系数")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        
        elif index == 9:
            if self.tmp_para !=  DEMO.K_0 and self.tmp_para != 0 and self.fig == 102:
                DEMO.K_0 = self.tmp_para
                self.tmp_para = 0
            self.fig = 102
            self.customWidget = SubsubWindow_Para(DEMO.K_0*1000, "K0")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
############################## 低压供电半径 ##################################
    def showSubsubWindow_radiuslowPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.radius_low[0] and self.tmp_para != 0 and self.fig == 103:
                DEMO.radius_low[0] = self.tmp_para
                self.tmp_para = 0
            self.fig = 103
            self.customWidget = SubsubWindow_Para(DEMO.radius_low[0]*1000, "A+")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.radius_low[1] and self.tmp_para != 0 and self.fig == 104:
                DEMO.radius_low[1] = self.tmp_para
                self.tmp_para = 0
            self.fig = 104
            self.customWidget = SubsubWindow_Para(DEMO.radius_low[1]*1000, "A")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.radius_low[2] and self.tmp_para != 0 and self.fig == 105:
                DEMO.radius_low[2] = self.tmp_para
                self.tmp_para = 0
            self.fig = 105
            self.customWidget = SubsubWindow_Para(DEMO.radius_low[2]*1000, "B")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.radius_low[3] and self.tmp_para != 0 and self.fig == 106:
                DEMO.radius_low[3] = self.tmp_para
                self.tmp_para = 0
            self.fig = 106
            self.customWidget = SubsubWindow_Para(DEMO.radius_low[3]*1000, "C")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.radius_low[4] and self.tmp_para != 0 and self.fig == 107:
                DEMO.radius_low[4] = self.tmp_para
                self.tmp_para = 0
            self.fig = 107
            self.customWidget = SubsubWindow_Para(DEMO.radius_low[4]*1000, "D")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
############################## 中压供电半径 ##################################
    def showSubsubWindow_radiusmiddlePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.radius_middle[0] and self.tmp_para != 0 and self.fig == 108:
                DEMO.radius_middle[0] = self.tmp_para
                self.tmp_para = 0
            self.fig = 108
            self.customWidget = SubsubWindow_Para(DEMO.radius_middle[0]*1000, "A+")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.radius_middle[1] and self.tmp_para != 0 and self.fig == 109:
                DEMO.radius_middle[1] = self.tmp_para
                self.tmp_para = 0
            self.fig = 109
            self.customWidget = SubsubWindow_Para(DEMO.radius_middle[1]*1000, "A")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.radius_middle[2] and self.tmp_para != 0 and self.fig == 110:
                DEMO.radius_middle[2] = self.tmp_para
                self.tmp_para = 0
            self.fig = 110
            self.customWidget = SubsubWindow_Para(DEMO.radius_middle[2]*1000, "B")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.radius_middle[3] and self.tmp_para != 0 and self.fig == 111:
                DEMO.radius_middle[3] = self.tmp_para
                self.tmp_para = 0
            self.fig = 111
            self.customWidget = SubsubWindow_Para(DEMO.radius_middle[3]*1000, "C")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.radius_middle[4] and self.tmp_para != 0 and self.fig == 112:
                DEMO.radius_middle[4] = self.tmp_para
                self.tmp_para = 0
            self.fig = 112
            self.customWidget = SubsubWindow_Para(DEMO.radius_middle[4]*1000, "D")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
############################## 新增馈线饱和容量年平均负载率 ##################################
    def showSubsubWindow_aveloadlinePara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.aveLoad_line[0] and self.tmp_para != 0 and self.fig == 113:
                DEMO.aveLoad_line[0] = self.tmp_para
                self.tmp_para = 0
            self.fig = 113
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_line[0]*1000, "A+")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.aveLoad_line[1] and self.tmp_para != 0 and self.fig == 114:
                DEMO.aveLoad_line[1] = self.tmp_para
                self.tmp_para = 0
            self.fig = 114
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_line[1]*1000, "A")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.aveLoad_line[2] and self.tmp_para != 0 and self.fig == 115:
                DEMO.aveLoad_line[2] = self.tmp_para
                self.tmp_para = 0
            self.fig = 115
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_line[2]*1000, "B")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.aveLoad_line[3] and self.tmp_para != 0 and self.fig == 116:
                DEMO.aveLoad_line[3] = self.tmp_para
                self.tmp_para = 0
            self.fig = 116
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_line[3]*1000, "C")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.aveLoad_line[4] and self.tmp_para != 0 and self.fig == 117:
                DEMO.aveLoad_line[4] = self.tmp_para
                self.tmp_para = 0
            self.fig = 117
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_line[4]*1000, "D")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
############################## 新增馈线饱和容量年平均负载率 ##################################
    def showSubsubWindow_aveloadtransPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.aveLoad_trans[0] and self.tmp_para != 0 and self.fig == 118:
                DEMO.aveLoad_trans[0] = self.tmp_para
                self.tmp_para = 0
            self.fig = 118
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_trans[0]*1000, "A+")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 2:
            if self.tmp_para !=  DEMO.aveLoad_trans[1] and self.tmp_para != 0 and self.fig == 119:
                DEMO.aveLoad_trans[1] = self.tmp_para
                self.tmp_para = 0
            self.fig = 119
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_trans[1]*1000, "A")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 3:
            if self.tmp_para !=  DEMO.aveLoad_trans[2] and self.tmp_para != 0 and self.fig == 120:
                DEMO.aveLoad_trans[2] = self.tmp_para
                self.tmp_para = 0
            self.fig = 120
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_trans[2]*1000, "B")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 4:
            if self.tmp_para !=  DEMO.aveLoad_trans[3] and self.tmp_para != 0 and self.fig == 121:
                DEMO.aveLoad_trans[3] = self.tmp_para
                self.tmp_para = 0
            self.fig = 121
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_trans[3]*1000, "C")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)

        elif index == 5:
            if self.tmp_para !=  DEMO.aveLoad_trans[4] and self.tmp_para != 0 and self.fig == 122:
                DEMO.aveLoad_trans[4] = self.tmp_para
                self.tmp_para = 0
            self.fig = 12
            self.customWidget = SubsubWindow_Para(DEMO.aveLoad_trans[4]*1000, "D")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
############################## 低电压时间 ##################################
    def showSubsubWindow_lowVPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.lowV_in_years and self.tmp_para != 0 and self.fig == 123:
                DEMO.lowV_in_years = self.tmp_para
                self.tmp_para = 0
            self.fig = 123
            self.customWidget = SubsubWindow_Para(DEMO.lowV_in_years*1000, "低电压时间在全年的占比")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
############################## 低电压时间 ##################################
    def showSubsubWindow_unqualifiedPara(self, index):
        if index == 1: 
            if self.tmp_para !=  DEMO.unqualified and self.tmp_para != 0 and self.fig == 124:
                DEMO.unqualified = self.tmp_para
                self.tmp_para = 0
            self.fig = 124
            self.customWidget = SubsubWindow_Para(DEMO.unqualified*1000, "低电压不合格的时间的占比")
            self.customWidget.show()
            self.customWidget.signal_.connect(self.receive_)
        else:
            QMessageBox.about(self,"错误","不合法操作")
########################################################################
########################################################################
class SubsubWindow_Para(QWidget):
    signal_ = QtCore.pyqtSignal(float)
    def __init__(self, init_value, label):
        super().__init__()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setSingleStep(1)
        self.slider.setMaximum(50000000)
        self.slider.setTickInterval(1)
        self.lineEdit = QLineEdit()
        self.slider.setValue(init_value)
        self.lineEdit.setText(str(init_value/1000))
        self.label = QLabel(label)
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.syncLineEdit_Cost)
        self.lineEdit.textChanged.connect(self.syncSlider_Cost)
   
    def syncLineEdit_Cost(self, value):
        self.lineEdit.setText(str(value/1000))
        # DEMO.repairCost_Mtrans = value/10000
        self.tmp_value = value/1000
        self.signal_.emit(self.tmp_value)

        
    def syncSlider_Cost(self, text):
        if text.isdigit():
            self.slider.setValue(float(text)*1000)
# ##############################################################################
# ############################## LCC修理成本事件 ##################################
# class SubsubWindow_Para(QWidget):
#     def __init__(self, factor, init_value, label):
#         super().__init__()
#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(0)
#         self.slider.setSingleStep(10)
#         self.slider.setMaximum(500000)
#         self.slider.setTickInterval(10)
#         self.lineEdit = QLineEdit()
#         self.slider.setValue(init_value)
#         self.lineEdit.setText(str(init_value/10000))
#         self.label = QLabel(label)
#         layout = QVBoxLayout()
#         layout.addWidget(self.slider)
#         layout.addWidget(self.lineEdit)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         self.slider.valueChanged.connect(self.syncLineEdit_repairCost)
#         self.lineEdit.textChanged.connect(self.syncSlider_repairCost)
#         self.tmp_value = tmp_value

#     def syncLineEdit_repairCost(self, value):
#         self.lineEdit.setText(str(value/10000))
#         # DEMO.repairCost_Mtrans = value/10000
#         tmp_value = value/10000
        
#     def syncSlider_repairCost(self, text):
#         if text.isdigit():
#             self.slider.setValue(float(text)*10000)
# ##############################################################################
# ############################## LCC故障成本事件 ##################################
# class SubsubWindow_Para(QWidget):
#     def __init__(self, factor, init_value, label):
#         super().__init__()
#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(0)
#         self.slider.setSingleStep(10)
#         self.slider.setMaximum(500000)
#         self.slider.setTickInterval(10)
#         self.lineEdit = QLineEdit()
#         self.slider.setValue(init_value)
#         self.lineEdit.setText(str(init_value/10000))
#         self.label = QLabel(label)
#         layout = QVBoxLayout()
#         layout.addWidget(self.slider)
#         layout.addWidget(self.lineEdit)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         self.slider.valueChanged.connect(self.syncLineEdit_repairCost)
#         self.lineEdit.textChanged.connect(self.syncSlider_repairCost)
#         factor = tmp_value
#         print(factor)

#     def syncLineEdit_repairCost(self, value):
#         self.lineEdit.setText(str(value/10000))
#         # DEMO.repairCost_Mtrans = value/10000
#         tmp_value = value/10000
        
#     def syncSlider_repairCost(self, text):
#         if text.isdigit():
#             self.slider.setValue(float(text)*10000)
# ##############################################################################
# ############################## LCC拆除费用事件 ##################################
# class SubsubWindow_Para(QWidget):
#     def __init__(self, factor, init_value, label):
#         super().__init__()
#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(0)
#         self.slider.setSingleStep(10)
#         self.slider.setMaximum(500000)
#         self.slider.setTickInterval(10)
#         self.lineEdit = QLineEdit()
#         self.slider.setValue(init_value)
#         self.lineEdit.setText(str(init_value/10000))
#         self.label = QLabel(label)
#         layout = QVBoxLayout()
#         layout.addWidget(self.slider)
#         layout.addWidget(self.lineEdit)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         self.slider.valueChanged.connect(self.syncLineEdit_removalCost)
#         self.lineEdit.textChanged.connect(self.syncSlider_removalCost)
#         factor = tmp_value

#     def syncLineEdit_removalCost(self, value):
#         self.lineEdit.setText(str(value/10000))
#         # DEMO.repairCost_Mtrans = value/10000
#         tmp_value = value/10000
        
#     def syncSlider_removalCost(self, text):
#         if text.isdigit():
#             self.slider.setValue(float(text)*10000)
# ##############################################################################
# ############################## 电价损耗事件 ##################################
# class SubsubWindow_Para(QWidget):
#     def __init__(self, factor, init_value, label):
#         super().__init__()
#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(0)
#         self.slider.setSingleStep(10)
#         self.slider.setMaximum(500000)
#         self.slider.setTickInterval(10)
#         self.lineEdit = QLineEdit()
#         self.slider.setValue(init_value)
#         self.lineEdit.setText(str(init_value/10000))
#         self.label = QLabel(label)
#         layout = QVBoxLayout()
#         layout.addWidget(self.slider)
#         layout.addWidget(self.lineEdit)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         self.slider.valueChanged.connect(self.syncLineEdit_removalCost)
#         self.lineEdit.textChanged.connect(self.syncSlider_removalCost)
#         factor = tmp_value

#     def syncLineEdit_removalCost(self, value):
#         self.lineEdit.setText(str(value/10000))
#         # DEMO.repairCost_Mtrans = value/10000
#         tmp_value = value/10000
        
#     def syncSlider_removalCost(self, text):
#         if text.isdigit():
#             self.slider.setValue(float(text)*10000)
# ##############################################################################
# ############################## 中压线路过载事件 ##################################
# class SubsubWindow_Para(QWidget):
#     def __init__(self, factor, init_value, label):
#         super().__init__()
#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(0)
#         self.slider.setSingleStep(10)
#         self.slider.setMaximum(100000)
#         self.slider.setTickInterval(10)
#         self.lineEdit = QLineEdit()
#         self.slider.setValue(init_value)
#         self.lineEdit.setText(str(init_value/10000))
#         self.label = QLabel(label)
#         layout = QVBoxLayout()
#         layout.addWidget(self.slider)
#         layout.addWidget(self.lineEdit)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         self.slider.valueChanged.connect(self.syncLineEdit_overloadlineCost)
#         self.lineEdit.textChanged.connect(self.syncSlider_overloadlineCost)
#         factor = tmp_value

#     def syncLineEdit_overloadlineCost(self, value):
#         self.lineEdit.setText(str(value/10000))
#         # DEMO.repairCost_Mtrans = value/10000
#         tmp_value = value/10000
        
#     def syncSlider_overloadlineCost(self, text):
#         if text.isdigit():
#             self.slider.setValue(float(text)*10000)
##############################################################################

############## 子窗口1 ##############################
class SubWindow_input(QWidget):
    def __init__(self, parent):
        super().__init__()
############################### 四个按钮 ############################################3 
        self.btn_pro_sheet = QPushButton('导入')
        self.btn_pro_sheet.setFixedSize(200, 100) 
        # layout.addWidget(self.btn_pro_sheet)
##########
        self.text_pro_sheet = QLineEdit(self)
        self.text_pro_sheet.setPlaceholderText("导入项目库表")
        self.text_pro_sheet.setReadOnly(True)
        self.text_pro_sheet.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.text_pro_sheet.setFixedSize(200, 50)
        # layout.addWidget(self.text_pro_sheet)

        self.progress_pro_sheet = QProgressBar(self)
        self.progress_pro_sheet.hide()
        self.progress_pro_sheet.setFixedSize(200, 50)
        # layout.addWidget(self.progress_pro_sheet)
############################################# text 1 ##########################################
        self.btn_trans_sheet = QPushButton('导入')
        self.btn_trans_sheet.setFixedSize(200, 100)  # 设置按钮大小
        # layout.addWidget(self.btn_trans_sheet)
##########
        self.text_trans_sheet = QLineEdit(self)
        self.text_trans_sheet.setPlaceholderText("导入配变表")
        self.text_trans_sheet.setReadOnly(True)
        self.text_trans_sheet.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.text_trans_sheet.setFixedSize(200, 50)
        # layout.addWidget(self.text_trans_sheet)

        self.progress_trans_sheet = QProgressBar(self)
        self.progress_trans_sheet.hide()
        self.progress_trans_sheet.setFixedSize(200, 50)
        # layout.addWidget(self.progress_trans_sheet)
############################################# text 2 ##########################################
        self.btn_line_sheet = QPushButton('导入')
        self.btn_line_sheet.setFixedSize(200, 100)  # 设置按钮大小
        # layout.addWidget(self.btn_line_sheet)
##########
        self.text_line_sheet = QLineEdit(self)
        self.text_line_sheet.setPlaceholderText("导入中压线路表")
        self.text_line_sheet.setReadOnly(True)
        self.text_line_sheet.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.text_trans_sheet.setFixedSize(200, 50)
        # layout.addWidget(self.text_line_sheet)

        self.progress_line_sheet = QProgressBar(self)
        self.progress_line_sheet.hide()
        self.progress_line_sheet.setFixedSize(200, 50)
        # layout.addWidget(self.progress_line_sheet)
############################################# text 3 ##########################################
        self.btn_lowU_sheet = QPushButton('导入')
        self.btn_lowU_sheet.setFixedSize(200, 100)  # 设置按钮大小
        # layout.addWidget(self.btn_lowU_sheet)
##########
        self.text_lowU_sheet = QLineEdit(self)
        self.text_lowU_sheet.setPlaceholderText("导入低压问题表")
        self.text_lowU_sheet.setReadOnly(True)
        self.text_lowU_sheet.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.text_lowU_sheet.setFixedSize(200, 50)
        # layout.addWidget(self.text_lowU_sheet)

        self.progress_lowU_sheet = QProgressBar(self)
        self.progress_lowU_sheet.hide()
        self.progress_lowU_sheet.setFixedSize(200, 50)

############################################# 四个按钮的布局 ####################
        layout1 = QVBoxLayout() 
        layout2 = QVBoxLayout()
        layout1.addWidget(self.btn_pro_sheet)
        layout2.addWidget(self.text_pro_sheet)
        layout2.addWidget(self.progress_pro_sheet)
        
        layout1.addWidget(self.btn_trans_sheet)
        layout2.addWidget(self.text_trans_sheet)
        layout2.addWidget(self.progress_trans_sheet)

        layout1.addWidget(self.btn_line_sheet)
        layout2.addWidget(self.text_line_sheet)
        layout2.addWidget(self.progress_line_sheet)

        layout1.addWidget(self.btn_lowU_sheet)
        layout2.addWidget(self.text_lowU_sheet)
        layout2.addWidget(self.progress_lowU_sheet)

        layout_all = QHBoxLayout()
        layout_all.addLayout(layout1)
        layout_all.addLayout(layout2)
        self.setWindowTitle("导入子窗口")
        parent_global_pos = parent.mapToGlobal(QPoint(0, 0))
        x = parent_global_pos.x() - parent.width() 
        y = parent_global_pos.y()
        # self.move(x, y)
        self.hide()
        self.setGeometry(x, y, 300, 600)
        self.setLayout(layout_all)

        self.btn_pro_sheet.clicked.connect(self.loadFileDialog_Lib)
        self.btn_trans_sheet.clicked.connect(self.loadFileDialog_trans)
        self.btn_line_sheet.clicked.connect(self.loadFileDialog_line)
        self.btn_lowU_sheet.clicked.connect(self.loadFileDialog_lowV)


    def loadFileDialog_Lib(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', '所有文件 (*)')
        if fname:
            print(f'选择的文件是: {fname}')

        self.text_pro_sheet.hide()
        self.progress_pro_sheet.show()

        for i in range(100001):
            k = i/100
            self.progress_pro_sheet.setValue(k)
            QApplication.processEvents()
            if i == 100000:
                self.Pro_Lib, self.Ass_line, self.Ass_trans = dataprocessing.read_ProjectLib_f(fname)
                self.progress_pro_sheet.hide()
                self.text_pro_sheet.show()
                self.text_pro_sheet.setText("文件导入成功！✅")


    def loadFileDialog_trans(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', '所有文件 (*)')
        if fname:
            print(f'选择的文件是: {fname}')

        self.text_trans_sheet.hide()
        self.progress_trans_sheet.show()

        for i in range(100001):
            k = i/100
            self.progress_trans_sheet.setValue(k)
            QApplication.processEvents()
            if i == 100000:
                self.Dis_Trans = dataprocessing.read_DistributionTrans_f(fname)
                self.progress_trans_sheet.hide()
                self.text_trans_sheet.show()
                self.text_trans_sheet.setText("文件导入成功！✅")

    def loadFileDialog_line(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', '所有文件 (*)')
        if fname:
            print(f'选择的文件是: {fname}')

        self.text_line_sheet.hide()
        self.progress_line_sheet.show()

        for i in range(100001):
            k = i/100
            self.progress_line_sheet.setValue(k)
            QApplication.processEvents()
            if i == 100000:
                self.mid_Volt = dataprocessing.read_MidVoltage_f(fname)
                self.progress_line_sheet.hide()
                self.text_line_sheet.show()
                self.text_line_sheet.setText("文件导入成功！✅")

    def loadFileDialog_lowV(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', '所有文件 (*)')
        if fname:
            print(f'选择的文件是: {fname}')

        self.text_lowU_sheet.hide()
        self.progress_lowU_sheet.show()

        for i in range(100001):
            k = i/100
            self.progress_lowU_sheet.setValue(k)
            QApplication.processEvents()
            if i == 100000:
                self.lowV_trans = dataprocessing.read_lowVtrans_f(fname)
                self.progress_lowU_sheet.hide()
                self.text_lowU_sheet.show()
                self.text_lowU_sheet.setText("文件导入成功！✅")
        
############## 子窗口3 ##############################
class SubWindow_analysis(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.btn_analysis = QPushButton('统计分析')
        self.btn_analysis.setFixedSize(200, 80)
        self.layout_analysis = QVBoxLayout()
        self.layout_analysis.addWidget(self.btn_analysis)
        self.setWindowTitle("分析子窗口")
        parent_global_pos = parent.mapToGlobal(QPoint(0, 0))
        x = parent_global_pos.x()
        y = parent_global_pos.y()
        # self.move(x, y)
        self.hide()
        self.setGeometry(x, y, 300, 600)
        self.setLayout(self.layout_analysis)
        self.btn_analysis.clicked.connect(self.getAnalysis)
    
    def getAnalysis(self):
        Analysis_excel.Analysis()
    
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = FileDialogDemo()
    demo.show()
    sys.exit(app.exec_())

