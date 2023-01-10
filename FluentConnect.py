# encoding: utf-8
# 导入fluent_corba下的CORBA接口类和其他必要模块
# #该版本中不能用""对文件进行加引号 ,存control文件不需要ok 所有的报错均是tui命令错误?或者\"??????????/solve/set/solution-steering yes \"transonic\" yes yes
# #不能用""对文件进行加引号
# scheme.doMenuCommandToString("/file/import/cad yes  D:/WorkBench/SimpleModel/rocket.scdoc yes 40 yes mm")
#发送Scheme脚本读入网格文件 带有()
# result = scheme.doMenuCommandToString('file/read-mesh base-design.msh')
# 发送Scheme脚本并返回结果
# result = scheme.execSchemeToString('(grid-check)')
# 发送TUI命令并返回结果,与(grid-check)对应
# result = scheme.doMenuCommandToString("/mesh/check")
# print(result)

# 设置入口速度大小为0.987m/s
# scheme.doMenuCommand("/define/bc/set/velocity inlet () vmag no 0.987 quit")
# 设置迭代步数,并开始计算
# fluentUnit.setNrIterations(200)
# result = scheme.doMenuCommand("/file/write-case")
# fluentUnit.calculate()
# scheme.doMenuCommandToString("/exit ok")

# 记得每一个命令的开始是/

#打包的命令,需要用-p 命令行将自定义的包打包进去.用""可以防止空格的干扰
# pyinstaller -F .\FluentConnect.py -p "C:\Program Files\Python37\Lib\site-packages\fluent_corba"


import xlrd
import xlwt
import re
from fluent_corba import CORBA
import time
import pathlib
import os, sys
import subprocess
import psutil
import win32api
import win32gui
from win32con import WM_INPUTLANGCHANGEREQUEST
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class FluentCase(QObject):
    finishFlent=pyqtSignal()
    def __init__(self,workpath,multicase_excel_path,worbenchpath,fluentpath,parent=None):
        super().__init__(parent)
        # 定义Fluent的启动位置，例如2020R1版本
        self.workpath=workpath
        self.multicase_excel_path=multicase_excel_path
        # ansysPath = pathlib.Path(os.environ["AWP_ROOT202"])
        # self.fluentExe = str(ansysPath / "fluent" / "ntbin" / "win64" / "fluent.exe")
        self.fluentExe= fluentpath
        self.worbenchExe = worbenchpath
        # 定义工作目录
        self.workPath = pathlib.Path(workpath)
        self.aasFilePath = self.workPath / "aaS_FluentId.txt"
    def change_language(lang="EN"):
        """
        切换语言
        :param lang: EN––English; ZH––Chinese
        :return: bool
        """
        LANG = {
            "ZH": 0x0804,
            "EN": 0x0409
        }
        hwnd = win32gui.GetForegroundWindow()
        language = LANG[lang]
        result = win32api.SendMessage(
            hwnd,
            WM_INPUTLANGCHANGEREQUEST,
            0,
            language
        )
        if not result:
            return True

    def deletefilebyend(self,path, end):
        datanames = os.listdir(path)
        list = []
        for file_name1 in datanames:
            if file_name1.endswith(end):
                try:
                    filepath = path + "\\" + file_name1
                    os.remove(filepath)
                except Exception as e:
                    pass

    def KillFluentbench(self,name):
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            # get process name according to pid
            process_name = p.name()
            if name in process_name:
                print("Process name is: %s, pid is: %s" % (process_name, pid))

        for pid in pids:
            p = psutil.Process(pid)
            # get process name according to pid
            process_name = p.name()
            # kill process "sleep_test1"
            if name in process_name:
                cmd = r'taskkill /F /IM ' + process_name
                os.system(cmd)

    def paramterIsInList(self,item, lst):
        ret = False
        for value in lst:
            if item == value:
                ret = True
                return ret
        return False
    def paramterIsInList(self,item, lst):
        ret = False
        for value in lst:
            if item == value:
                ret = True
                return ret
        return False

    def getparameters(self,cmd):
        pat = "\{.*?\}"
        lst = re.findall(pat, cmd)
        # print(re.findall(pat, cmd))
        parameters = list()
        for name in lst:
            st = str(name)
            ret = st.replace("{", "").replace("}", "")
            if (ret not in parameters):
                parameters.append(ret)
        return parameters

    def write_to_excel(self,cmd, path):
        parameters = self.getparameters(cmd)
        book = xlwt.Workbook(encoding="utf-8")
        sheet = book.add_sheet("sheet1")
        style1 = xlwt.XFStyle()  # 设置单元格格式为文本
        style1.num_format_str = '@'
        i = 0
        for name in parameters:
            st = str(name)
            ret = st.replace("{", "").replace("}", "")
            sheet.write(i, 0, ret, style=style1)
            sheet.col(0).width = 500 * 20
            i += 1
        book.save(path)

    def readFile(self,path):
        with open(path, "r", encoding="utf-8") as f1:
            cmd = f1.read()
            # print(cmd)
            # write_to_excel(cmd,r'D:\WorkBench\SimpleModel\fluent.xls')
            return cmd

    # readFile()
    def get_fluent_excel_rowdata(self,path, col):

        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        rows = table.nrows
        # cols = table.ncols

        values_list = [str(table.cell_value(i, col)) for i in range(0, rows)]
        # typrlist=[table.cell_type(i, col) for i in range(0, rows)]
        # print(typrlist)
        # typrlist = [table.cell(i, col) for i in range(0, rows)]
        # print(typrlist)
        # 将字符串中的整形浮点数转换为整形字符串,比如5.0转5
        for i in range(0, len(values_list)):
            value = values_list[i]
            #有可能是数组,用" "分割
            pattern=r'\s'
            values_pace_split=re.split(pattern,value)
            # values_pace_split = value.split(" ")
            for j in range(0,len(values_pace_split)):
                val = values_pace_split[j].split(".")
                if len(val) == 2:
                    if val[1] == "0":
                        values_pace_split[j] = val[0]
            # print(values_pace_split)
            values_list[i]=" ".join(values_pace_split)

        return values_list

    def getfluentjou(self,new_fluent_joupath, raw_strpath, raw_excel, col):
        try:
            cmd = self.readFile(raw_strpath)
            paramters = self.getparameters(cmd)
            # paramters = self.get_fluent_excel_rowdata(raw_excel, 0)
            values_list = self.get_fluent_excel_rowdata(raw_excel, col)

            for i in range(0, len(values_list)):
                value = str(values_list[i])
                # print(value)
                paramter = str(paramters[i])
                paramter = paramter.replace("(", "\\(")
                paramter = paramter.replace(")", "\\)")
                pat = "\{"+"\s*"+paramter+"\s*?" +"\}"

                neadreplacestrs = re.findall(pat, cmd)
                # print(neadreplacestrs)
                for neadreplacestr in neadreplacestrs:
                    # print(neadreplacestr)
                    cmd = cmd.replace(neadreplacestr, value)
            # print(cmd)
            with open(new_fluent_joupath, "w", encoding="utf-8") as f1:
                f1.write(cmd)
            return cmd
        except Exception as e:
            print(e.args)


    def get_excel_cols(self,excelpath):
        data = xlrd.open_workbook(excelpath)
        table = data.sheets()[0]
        cols = table.ncols
        return cols
    def run_fluent(self, colnum,textEdit):
        cmd = self.getfluentjou("./newFluentJou.txt", "./fluent_raw_str.txt", self.multicase_excel_path, colnum)
        # 服务器会话连接之前，清除工作目录下存在的aaS*.txt文件
        for file in self.workPath.glob("aaS*.txt"): file.unlink()

        self.deletefilebyend(self.workpath, ".trn")

        self.deletefilebyend(self.workpath, ".log")

        # fluentpath = "\"" + fluentpath + "\"" + " 3ddp -meshing -t6 -i \"./FluidCMD.jou\""
        # 启动线程调用Fluent软件
        fluentProcess = subprocess.Popen(f'"{self.fluentExe}" 3ddp -meshing  -aas -t6',shell=False, cwd=str(self.workPath))
        #监控aaS_FluentId.txt文件生成，等待corba连接  如果存在这个文件,在fluent开启的情况下,可以注释部分,继续发送命令
        while True:
            try:
                if not self.aasFilePath.exists():
                    time.sleep(0.2)
                    continue
                else:
                    if "IOR:" in self.aasFilePath.open("r").read():
                        break
            except KeyboardInterrupt: sys.exit()
        # 初始化orb环境
        orb = CORBA.ORB_init()
        # 获得fluent服务器会话实例
        fluentUnit = orb.string_to_object(self.aasFilePath.open("r").read())
        # 获得scheme脚本控制器实例
        scheme = fluentUnit.getSchemeControllerInstance()
        # #该版本中不能用""对文件进行加引号 ,存control文件不需要ok 所有的报错均是tui命令错误?或者\"??????????/solve/set/solution-steering yes \"transonic\" yes yes

        try:
            for cm in cmd.split("\n"):
                result = scheme.doMenuCommandToString(cm)
                print(result)
                textEdit.append(result)
        except Exception as  e:
            print(e.args)
            textEdit.append(e.args)
        # print("Over")
        textEdit.append("第%d列工况运行完毕"%(colnum))
        fluentUnit.terminate()

    def run_multi_cases(self, textEdit):
        nums=self.get_excel_cols(self.multicase_excel_path)
        for i in range(1, nums):
            self.run_fluent(i,textEdit)
        self.finishFlent.emit()
    def run_single_case(self,textEdit):
        self.run_fluent(1,textEdit)
        self.finishFlent.emit()

    def run(self,textEdit,index):
        if(index==1):
            self.run_fluent(1,textEdit)
        elif(index==2):
            self.run_multi_cases(textEdit)
# fluentcase = FluentCase(r"D:\WorkBench\mutlicase",r'D:\WorkBench\SimpleModel\fluent.xls')
#
# fluentcase.run_single_case()

