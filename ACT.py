# -*- coding: utf-8 -*- 
# @Time : 2022/10/13 16:10 
# @Author : KeJun 
# @File : ACT.py
# D:/WorkBench/PythonProject/rocket/rocket_files/dp0/FFF/DM
import os
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import socket
import getpass
import xlrd
import UIVaribles
import re

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import actForm as w
import subprocess
import psutil
import xmloperation as XML


class ACTWind(QMainWindow):
    def __init__(self, parent=None):
        super(ACTWind, self).__init__(parent)
        # super().__init__(parent)
        self.rocket_name = None
        self.rocket_SCdoc = None
        self.spaceclaimpath = None
        self.ui = w.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("流体仿真界面")
        tree = XML.read_xml("config.xml")

        nodes = XML.find_nodes(tree, "defaultProjectPath")
        self.defaultProjectPath = nodes[0].text.replace("\\", "/")
        self.ui.projectPathLinedit.setText(self.defaultProjectPath)

        nodes = XML.find_nodes(tree, "defaultRocketPath")
        self.defaultRocketPath = nodes[0].text.replace("\\", "/")
        self.ui.rocketPathLinedit.setText(self.defaultRocketPath)

        nodes = XML.find_nodes(tree, "raw_model")
        self.raw_model = nodes[0].text.replace("\\", "/")
        self.ui.rawmodellineEdit.setText(self.raw_model)

        self.temppath = (self.GetUserInfo()[0] + "\\myrockettemp.bat").replace("\\", "/")
    def __str__(self):
        return "mand"
    #反写新到xml中
    def modifynodetext(self,nodepath,newStr):
        tree = XML.read_xml("config.xml")
        nodes = XML.find_nodes(tree, nodepath)
        nodes[0].text=newStr
        XML.write_xml(tree, "config.xml")
    # 获得用户目录信息
    def GetUserInfo(self):
        user_name = getpass.getuser()
        hostname = socket.gethostname()
        user_name = ('C:\\Users\\' + user_name + '\\AppData\Local\Temp\\').replace("\\", "/")
        return user_name, hostname

    # 修改UIVaribles.py文件中的变量信息
    def Modify_UIVaribles_File(self, varName, new_str, isStr=False):
        file = "./UIVaribles.py"
        with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:

            for line in f1:
                if varName in line:
                    if (isStr):
                        line = varName + "=\"" + str(new_str) + "\"\n"
                    else:
                        line = varName + "=" + str(new_str) + "\n"
                f2.write(line)
        os.remove(file)
        os.rename("%s.bak" % file, file)

    # 单工况的脚本命令创建
    def WriteCMDScriptToPy(self):
        with open("./CMDscript.py", "r", encoding="utf-8") as f1, open("./FluidCMD.jou", "w", encoding="utf-8") as f2:
            workpath = self.ui.projectPathLinedit.text().replace("\\", "/")
            rawStr = f1.read()
            newstr = rawStr.format(
                minSzie=self.ui.minSizelineEdit.text(), maxSzie=self.ui.maxSizelineEdit.text(),
                curvature_Normal_Angle=self.ui.curvatureNormalAnglineEdit.text(),
                feature_Angle=self.ui.featureAnglelineEdit.text(),
                firstAspectRatio=self.ui.firstAspectRatiolineEdit.text(),
                boundaryNum=self.ui.boundaryNumlineEdit.text(),
                boiSize=self.ui.boiSizelineEdit.text(), inletVelocity=self.ui.inletVelocitylineEdit.text(),
                inletTemp=self.ui.inletTemplineEdit.text(), outPressurelineEdit=self.ui.outPressurelineEdit.text(),
                iterNum=self.ui.iterNumlineEdit.text(), rocketPath=self.ui.rocketPathLinedit.text().replace("\\", "/"),
                rockettempsizepath=workpath + "/tempsize.sf",
                rocketWriteCasePath=workpath + "/" + self.rocket_name + ".cas.h5"
            )       
            f2.write(newstr)
    # 多工况脚本命令创建
    def WriteMultiCmd(self):

        self.multiRawStr=self.ui.projectPathLinedit.text()+"/workbenchMultiCases.py"
        with open("./workbenchMultiCasesRawStr.py", "r", encoding="utf-8") as f1, open( self.multiRawStr, "w",
                                                                                       encoding="utf-8") as f2:
            workpath = self.ui.projectPathLinedit.text().replace("\\", "/")
            rawStr = f1.read()
            mytempsizeFile = workpath + "/tempsize.sf"
            myRocketDp0File = workpath + "/" + self.rocket_name + "_files/dp0/Geom/DM/Geom.scdoc"
            myrocketWriteCasePath = workpath + "/" + self.rocket_name + ".cas.h5"
            myresult_csv = "\"" + workpath + "/" + self.rocket_name + ".csv" + "\""
            newstr = rawStr.format(
                totalheight=self.totalheight,
                rocketMoveHeight= self.rocketMoveHeight,
                rotationDeg=self.rotationDeg,
                WBProjectPathWbj=str(self.ui.projectPathLinedit.text() + "/" + self.rocket_name + ".wbpj"),
                SCDMFilePath=str(self.ui.rocketPathLinedit.text()),
                feature_Angle=str(self.ui.featureAnglelineEdit.text()),
                minSzie=str(self.ui.minSizelineEdit.text()),
                maxSzie=str(self.ui.maxSizelineEdit.text()),
                curvature_Normal_Angle=str(self.ui.curvatureNormalAnglineEdit.text()),
                boiSize=str(self.ui.boiSizelineEdit.text()),
                rockettempsizepath=str(mytempsizeFile),
                RocketDp0File=str(myRocketDp0File),
                firstAspectRatio=str(self.ui.firstAspectRatiolineEdit.text()),
                boundaryNum=str(self.ui.boundaryNumlineEdit.text()),
                inletVelocity=str(self.ui.inletVelocitylineEdit.text()),
                inletTemp=str(self.ui.inletTemplineEdit.text()),
                outPressurelineEdit=str(self.ui.outPressurelineEdit.text()),
                iterNum=str(self.ui.iterNumlineEdit.text()),
                rocketWriteCasePath=str(myrocketWriteCasePath),
                nullPath="{}",
                result_csv=str(myresult_csv)
            )
            f2.write(newstr)

    # 选择原始模型文件的按钮事件
    @pyqtSlot()
    def on_rawmodelButton_clicked(self):
        rocketpath, fiter = QFileDialog.getOpenFileName(self, "请选择未处理的原始模型", self.raw_model)
        self.ui.rawmodellineEdit.setText(rocketpath)
        if rocketpath=="":
            return
        self.modifynodetext("raw_model",rocketpath.replace("\\","/"))

    # 打开spaceclaim程序的按钮事件
    @pyqtSlot()
    def on_openSpaceClaimBtn_clicked(self):
        self.set_rocket_name()
        self.outRocket = self.ui.rocketPathLinedit.text().replace("\\", "/")
        if self.outRocket == "":
            QMessageBox.critical(self, "输入信息缺失", "请选择处理后的模型输出路径")
            return
        with open(self.temppath, "w", encoding="utf-8") as f2:
            f2.write(self.outRocket)
        self.Modify_UIVaribles_File("WBProjectPath", self.ui.projectPathLinedit.text().replace("\\", "/"), True)
        self.Modify_UIVaribles_File("SCDMFilePath", self.outRocket, True)
        self.Modify_UIVaribles_File("RawRocketModel", self.ui.rawmodellineEdit.text(), True)
        self.Modify_UIVaribles_File("WBProjectPathWbj",
                                    self.ui.projectPathLinedit.text().replace("\\",
                                                                              "/") + "/" + self.rocket_name + ".wbpj",
                                    True)

        with open("./spaceclaimRun.py", "w", encoding="utf-8") as f2:
            runscript = """
importOptions = ImportOptions.Create()
DocumentOpen.Execute("{0}", importOptions)
            """.format(self.ui.rawmodellineEdit.text())
            f2.write(runscript)

        tree = XML.read_xml("config.xml")
        nodes = XML.find_nodes(tree, "spaceclaimpath")
        self.spaceclaimpath = nodes[0].text.replace("\\", "/")
        spaceclaimCmd = "\"" + self.spaceclaimpath + "\"" + " /RunScript=spaceclaimRun.py"

        subprocess.Popen(spaceclaimCmd, shell=True, stdout=None, stderr=None)

    # 选择工程路径的按钮事件
    @pyqtSlot()
    def on_projectPathBtn_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "请选择一个文件夹", self.defaultProjectPath)
        self.ui.projectPathLinedit.setText(path.replace("\\", "/"))
        if path=="":
            return
        self.modifynodetext("defaultProjectPath", path.replace("\\", "/"))
        self.defaultProjectPath=self.ui.projectPathLinedit.text()
    # 选择火箭模型处理完后的保存目录事件
    @pyqtSlot()
    def on_rocketPathBtn_clicked(self):
        path, filter = QFileDialog.getSaveFileName(self, "请选择文件保存路径", self.defaultRocketPath, "*.scdoc")
        self.ui.rocketPathLinedit.setText(path.replace("\\", "/"))
        if path=="":
            return
        self.modifynodetext("defaultRocketPath", path.replace("\\", "/"))
        self.set_rocket_name()
    def set_rocket_name(self):
        self.rocket_SCdoc = str(os.path.dirname(self.ui.rocketPathLinedit.text().replace("\\", "/")))
        path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        ret = os.path.splitext(path)[0]
        self.rocket_name = str(os.path.basename(ret))


    # 创建系统并进行模型预处理的按钮事件
    @pyqtSlot()
    def on_createSysAndPreModBtn_clicked(self):
        pass

    # 结束模型处理的按钮事件
    @pyqtSlot()
    def on_endModePreBtn_clicked(self):
        # self.KillWorkbench()
        pass
        # wmi1 = win32com.client.GetObject('winmgmts')
        # c = wmi.WMI()
        # for p in wmi1.InstancesOf('win32_process'):
        #     if p.Name == 'MSACCESS.EXE':  # 某个程序名字
        #         for process in c.win32_Process(ProcessId=p.Properties_('ProcessId')):
        #             process.Terminate()

        # from win32com.client import GetObject
        # mywmi = GetObject("winmgmts:")
        # objs = mywmi.InstancesOf("Win32_Service")
        # for obj in objs:
        #     print (obj.PathName)

    # 开始单工况计算的按钮事件
    @pyqtSlot()
    def on_startBtn_clicked(self):
        if (self.ui.projectPathLinedit.text() == "") or (self.ui.rocketPathLinedit.text() == ""):
            QMessageBox.critical(self, "输入信息缺失", "请确保\"工程文件路径和火箭模型路径均不为空\"")
            return
        self.Modify_UIVaribles_File("minSzie", float(self.ui.minSizelineEdit.text()))
        self.Modify_UIVaribles_File("maxSzie", self.ui.maxSizelineEdit.text())
        self.Modify_UIVaribles_File("curvature_Normal_Angle", self.ui.curvatureNormalAnglineEdit.text())
        self.Modify_UIVaribles_File("feature_Angle", self.ui.featureAnglelineEdit.text())
        self.Modify_UIVaribles_File("firstAspectRatio", self.ui.firstAspectRatiolineEdit.text())
        self.Modify_UIVaribles_File("boundaryNum", self.ui.boundaryNumlineEdit.text())
        self.Modify_UIVaribles_File("boiSize", self.ui.boiSizelineEdit.text())
        self.Modify_UIVaribles_File("inletVelocity", self.ui.inletVelocitylineEdit.text())
        self.Modify_UIVaribles_File("inletTemp", self.ui.inletTemplineEdit.text())
        self.Modify_UIVaribles_File("outPressurelineEdit", self.ui.outPressurelineEdit.text())
        self.Modify_UIVaribles_File("iterNum", self.ui.iterNumlineEdit.text())

        self.rocket_SCdoc = str(os.path.dirname(self.ui.rocketPathLinedit.text().replace("\\", "/")))

        path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        ret = os.path.splitext(path)[0]
        self.rocket_name = str(os.path.basename(ret))

        self.WriteCMDScriptToPy()
        tree = XML.read_xml("config.xml")
        nodes = XML.find_nodes(tree, "fluentpath")
        fluentpath = nodes[0].text
        fluentpath = "\"" + fluentpath + "\"" + " 3ddp -meshing -t6 -i \"./FluidCMD.jou\""
        subprocess.Popen(fluentpath, shell=True, stdout=None, stderr=None)


    # 进行多工况计算的按钮事件
    #禁止切换python版本为3.10,应该用3.7一下
    @pyqtSlot()
    def on_multiCaseBtn_clicked(self):
        # if str(self.ui.multiCasesExcellineEdit.text()) == "":
        #     QMessageBox.critical(self, "输入信息缺失", "请确保\"多工况输入文件\"路径不为空")
        #     return
        # self.readMultiCaseExcel(self.ui.multiCasesExcellineEdit.text().replace("\\", "/"))
        #
        # path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        # if path == "":
        #     return
        #
        # self.rocket_SCdoc = str(os.path.dirname(path))
        # path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        # ret = os.path.splitext(path)[0]
        # self.rocket_name = str(os.path.basename(ret))


        # self.WriteMultiCmd()

        # tree = XML.read_xml("config.xml")
        #
        # nodes = XML.find_nodes(tree, "worbenchpath")
        # worbenchpath = nodes[0].text
        # cmdBat = self.defaultProjectPath + "/run.bat"

        worbenchpath = "D:/Program Files/ANSYS Inc/v202/Framework/bin/Win64/RunWB2.exe"
        cmdBat="D:/WorkBench/newtest1/run.bat"

        # cmdstr = "\"" + worbenchpath + "\"" + " -I -R "+self.multiRawStr
        cmdstr = "\"" + worbenchpath + "\"" + " -I -R " + "D:/WorkBench/newtest1/workbenchMultiCases.py"

        # with open(cmdBat, "w",encoding="utf-8") as f2:
        #     f2.write(cmdstr)
        # os.system(cmdBat)
        opt=0
        if (opt==0):
            subprocess.Popen(cmdBat, shell=True, stdout=None, stderr=None)
        elif (opt==1):
            subprocess.Popen(cmdstr, shell=True, stdout=None, stderr=None)
        else:
            subprocess.Popen("\"D:\\Program Files\\ANSYS Inc\\v202\Framework\\bin\Win64\RunWB2.exe\" -I -R \"D:/WorkBench/newtest1/workbenchMultiCases.py\"", shell=True, stdout=None, stderr=None)


    # 读取多工况Excel文件
    def readMultiCaseExcel(self, path):
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        # table = data.sheet_by_index(sheet_indx)  # 通过索引顺序获取
        # table = data.sheet_by_name(sheet_name)  # 通过名称获
        nrows = table.nrows
        totalheight_list = [table.cell_value(i, 0) for i in range(1, nrows)]
        self.Modify_UIVaribles_File("totalheight", str(totalheight_list))
        self.totalheight = str(totalheight_list)

        rocketMoveHeight_list = [table.cell_value(i, 1) for i in range(1, nrows)]
        self.Modify_UIVaribles_File("rocketMoveHeight", str(rocketMoveHeight_list))
        self.rocketMoveHeight = str(rocketMoveHeight_list)

        rotationDeg_list = [table.cell_value(i, 2) for i in range(1, nrows)]
        self.Modify_UIVaribles_File("rotationDeg", str(rotationDeg_list))
        self.rotationDeg = str(rotationDeg_list)

    # 读取多工况文件的按钮事件
    @pyqtSlot()
    def on_multiCasesExcelBtn_clicked(self):
        path, filter = QFileDialog.getOpenFileName(self, "请选择多工况输入文件,Excel文件",
                                            "./", "*.xls;*.xlsx")
        self.ui.multiCasesExcellineEdit.setText(path)

    # 结束workbench后台程序
    def KillWorkbench(self):
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            # get process name according to pid
            process_name = p.name()
            if 'AnsysFWW' in process_name:
                print("Process name is: %s, pid is: %s" % (process_name, pid))

        for pid in pids:
            p = psutil.Process(pid)
            # get process name according to pid
            process_name = p.name()
            # kill process "sleep_test1"
            if 'AnsysFWW' in process_name or 'SpaceClaim' in process_name:
                cmd = r'taskkill /F /IM ' + process_name
                os.system(cmd)

    # XML文件处理函数
    @classmethod
    def __indent(cls, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                cls.__indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    # 写入xml
    @classmethod
    def writexml(cls):
        root = ET.Element('Root')
        tree = ET.ElementTree(root)
        worbenchpath = Element("worbenchpath")
        worbenchpath.text = r"D:\Program Files\ANSYS Inc\v212\Framework\bin\Win64\RunWB2.exe"
        fluentpath = Element("fluentpath")
        fluentpath.text = r"D:\Program Files\ANSYS Inc\v212\fluent\ntbin\win64\fluent.exe"
        defaultProjectPath = Element("defaultProjectPath")
        defaultProjectPath.text = r"D:\WorkBench\SimpleModel"
        defaultRocketPath = Element("defaultRocketPath")
        defaultRocketPath.text = r"D:\WorkBench\SimpleModel"
        root.append(worbenchpath)
        root.append(fluentpath)
        root.append(defaultProjectPath)
        root.append(defaultRocketPath)
        cls.__indent(root)
        tree.write("config.xml", encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    mainwind = ACTWind()
    mainwind.show()
    # print(mainwind)
    sys.exit(qApp.exec_())

#
#
#
# # pat="(\{[\s*\u4e00-\u9fa5\s*\w+\s*]{1,}\}){1,}"
# pat = "\{.*?\}"
# myst="scoped-sizing/create  boi object-faces yes yes *boi* {boiSize} 1.2{ 何时去额为 we}kjk"
# print(re.findall(pat, myst))
# myst="""
# /scoped-sizing/create \"control-1\" boi object-faces yes yes *boi* {boiSize} 1.2
# /scoped-sizing/compute
# /file/write-size-field \"{rockettempsizepath}\" ok
# /file/import/cad-options/tessellation  cfd-surface-mesh yes \"{rockettempsizepath}\"
# /file/import/cad yes \"{RocketDp0File}\" no yes 40 yes mm ok
# /objects/volumetric-regions/compute *myfluideeclosuretobecuted* no
# /objects/volumetric-regions/rename * *myfluideeclosuretobecuted* *myfluideeclosuretobecuted* myfluid
# /objects/volumetric-regions/change-type *myfluideeclosuretobecuted* * () fluid
# /boundary/manage/type inlet* () velocity-inlet
# /boundary/manage/type outlet* () pressure-outlet
# /objects/volumetric-regions/scoped-prism/set/create "control-1" aspect-ratio {firstAspectRatio} {boundaryNum} 1.2 myfluideeclosuretobecutedcomponent:myfluideeclosuretobecutedcomponent-myfluideeclosuretobecuted1 fluid-regions selected-labels *wall*
# /mesh/auto-mesh * no  scoped  pyramids hexcore  yes
# /report/cell-quality-limits *()
# /switch-to-solution-mode yes
# /define/models/viscous/ke-realizable? yes
# /define/models/viscous/near-wall-treatment enhanced-wall-treatment? yes quit
# /define/boundary-conditions/fluid myfluid no no no no no 0 no 0 no 0 no 0 no 0 no 0 no no no no no
# /define/boundary-conditions/set/velocity-inlet *inlet_velocity* () vmag no {inletVelocity} quit
# /define/models/energy? yes no no no yes
# /define/boundary-conditions/set/velocity-inlet *inlet_velocity* () temperature no {inletTemp} quit
# /define/boundary-conditions/set/pressure-outlet *outlet_pressure* () gauge-pressure no {outPressurelineEdit} quit
# /solve/report-definitions/add out-vel-rdef surface-areaavg surface-names *outlet_pressure* () field velocity-magnitude quit
# /solve/report-plots/add out-vel-rplot report-defs out-vel-rdef () quit
# /display/surface/plane-surface xz-plane-0 zx-plane 0
# /file/write-case-data "{rocketWriteCasePath}" ok
# /solve/iterate {iterNum}
# /display/objects/create contour vel-mid surfaces-list xz-plane-0 () field velocity-magnitude quit
# """
# print(re.findall(pat, myst))
# print("heolllllllllllllllllllllllllllllll")
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))
#
# phone = "2004-959-559 # 这是一个电话号码"
#
# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码 : ", num)