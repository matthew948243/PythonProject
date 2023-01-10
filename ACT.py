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
import FluentConnect as FLC
# pyinstaller 打包py文件成exe文件，执行打包后的程序，经常会出现程序使用的配置文件无法关联，或者，在打包后的路径下运行正常，
# 但是将打包后的程序放到其它路径下就有问题。
# 这些现象都很有可能是因为程序使用的文件路径发生改变产生的，因此在打包时候我们需要根据执行路径进行路径“冻结”。
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import actForm as w
import subprocess
import psutil
import xmloperation as XML


class ACTWind(QMainWindow):
    signal_run = pyqtSignal(QTextEdit, int)

    # signal_multi = pyqtSignal(QTextEdit)
    def __init__(self, parent=None):
        super(ACTWind, self).__init__(parent)
        # super().__init__(parent)
        self.rocket_name = None
        self.rocket_SCdoc = None
        self.spaceclaimpath = None
        self.ui = w.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("流体仿真界面")
        self.ui.rawmodellineEdit.setText(self.getxmlnodetext("raw_model"))
        self.ui.projectPathLinedit.setText(self.getxmlnodetext("defaultProjectPath"))
        self.ui.rocketPathLinedit.setText(self.getxmlnodetext("defaultRocketPath"))
        self.ui.multiCasesExcellineEdit.setText(self.getxmlnodetext("multicase_excel_path"))
        self.temppath = (self.GetUserInfo()[0] + "\\myrockettemp.bat").replace("\\", "/")

        self.fluentcase = self.createFluentCase()
        self.t1 = QThread()
        self.fluentcase.moveToThread(self.t1)
        self.signal_run.connect(self.fluentcase.run)
        self.t1.start()

        # self.ui.startBtn.clicked.connect(self.onrunSingle)

        # self.t2=QThread()
        # self.fluentcase.moveToThread(self.t1)
        # # self.signal_multi.connect(self.fluentcase.run_multi_cases)
        # # self.ui.multiCaseBtn.clicked.connect(self.onrunMulti)
        # # self.fluentcase.finishFlent.connect(self.on_destroyed)

        self.destroyed.connect(self.on_destroyed)

    def onrunSingle(self):
        # print("hello")
        if (self.ui.projectPathLinedit.text() == "") or (self.ui.rocketPathLinedit.text() == ""):
            QMessageBox.critical(self, "输入信息缺失", "请确保\"工程文件路径和火箭模型路径均不为空\"")
            return
        self.rocket_SCdoc = str(os.path.dirname(self.ui.rocketPathLinedit.text().replace("\\", "/")))
        path = self.ui.rocketPathLinedit.text().replace("\\", "/")

        print("hello")

    def onrunMulti(self):
        if str(self.ui.multiCasesExcellineEdit.text()) == "":
            QMessageBox.critical(self, "输入信息缺失", "请确保\"多工况输入文件\"路径不为空")
            return

        path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        if path == "":
            return
        self.signal_multi.emit(self.ui.textEdit)
        self.t1.start()

    @pyqtSlot()
    def on_destroyed(self):
        self.t1.quit()
        self.t1.wait()
        self.t1.deleteLater()

    def __str__(self):
        return "mand"

    def getxmlnodetext(self, nodename):
        tree = XML.read_xml("config.xml")
        nodes = XML.find_nodes(tree, nodename)
        nodetext = nodes[0].text.replace("\\", "/")
        return nodetext

    def createFluentCase(self):

        flucase = FLC.FluentCase(self.ui.projectPathLinedit.text().replace("\\", "/"),
                                 self.ui.multiCasesExcellineEdit.text().replace("\\", "/"),
                                 self.getxmlnodetext("workbenchpath"),
                                 self.getxmlnodetext("fluentpath")
                                 )
        return flucase

    # 反写新到xml中
    def modifynodetext(self, nodepath, newStr):
        tree = XML.read_xml("config.xml")
        nodes = XML.find_nodes(tree, nodepath)
        nodes[0].text = newStr
        XML.write_xml(tree, "config.xml") \
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

    # 选择原始模型文件的按钮事件
    @pyqtSlot()
    def on_rawmodelButton_clicked(self):
        rocketpath, fiter = QFileDialog.getOpenFileName(self, "请选择未处理的原始模型", self.raw_model)
        self.ui.rawmodellineEdit.setText(rocketpath)
        if rocketpath == "":
            return
        self.modifynodetext("raw_model", rocketpath.replace("\\", "/"))

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
        if path == "":
            return
        self.modifynodetext("defaultProjectPath", path.replace("\\", "/"))
        self.defaultProjectPath = self.ui.projectPathLinedit.text()

    # 选择火箭模型处理完后的保存目录事件
    @pyqtSlot()
    def on_rocketPathBtn_clicked(self):
        path, filter = QFileDialog.getSaveFileName(self, "请选择文件保存路径", self.defaultRocketPath, "*.scdoc")
        self.ui.rocketPathLinedit.setText(path.replace("\\", "/"))
        if path == "":
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
        self.rocket_SCdoc = str(os.path.dirname(self.ui.rocketPathLinedit.text().replace("\\", "/")))
        path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        ret = os.path.splitext(path)[0]
        self.rocket_name = str(os.path.basename(ret))
        self.signal_run.emit(self.ui.textEdit, 1)

    # 进行多工况计算的按钮事件
    # 禁止切换python版本为3.10,应该用3.7一下
    @pyqtSlot()
    def on_multiCaseBtn_clicked(self):
        if str(self.ui.multiCasesExcellineEdit.text()) == "":
            QMessageBox.critical(self, "输入信息缺失", "请确保\"多工况输入文件\"路径不为空")
            return

        path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        if path == "":
            return

        self.rocket_SCdoc = str(os.path.dirname(path))
        path = self.ui.rocketPathLinedit.text().replace("\\", "/")
        ret = os.path.splitext(path)[0]
        self.rocket_name = str(os.path.basename(ret))
        # self.createFluentCase().run_multicase()
        self.signal_run.emit(self.ui.textEdit, 2)
        # subprocess.Popen("\"D:\\Program Files\\ANSYS Inc\\v202\Framework\\bin\Win64\RunWB2.exe\" -I -R \"D:/WorkBench/newtest1/workbenchMultiCases.py\"", shell=True, stdout=None, stderr=None)

    # 读取多工况文件的按钮事件
    @pyqtSlot()
    def on_multiCasesExcelBtn_clicked(self):
        path, filter = QFileDialog.getOpenFileName(self, "请选择多工况输入文件,Excel文件",
                                                   "./", "*.xls;*.xlsx")
        self.ui.multiCasesExcellineEdit.setText(path)
        if path == "":
            return
        self.modifynodetext("multicase_excel_path", path.replace("\\", "/"))

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
        workbenchpath = Element("workbenchpath")
        workbenchpath.text = r"D:\Program Files\ANSYS Inc\v212\Framework\bin\Win64\RunWB2.exe"
        fluentpath = Element("fluentpath")
        fluentpath.text = r"D:\Program Files\ANSYS Inc\v212\fluent\ntbin\win64\fluent.exe"
        defaultProjectPath = Element("defaultProjectPath")
        defaultProjectPath.text = r"D:\WorkBench\SimpleModel"
        defaultRocketPath = Element("defaultRocketPath")
        defaultRocketPath.text = r"D:\WorkBench\SimpleModel"
        root.append(workbenchpath)
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
