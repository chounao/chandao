
import requests
import xlrd
class chanDao():
    def login(self):
        self.chandao_data = {
            'account': 'zhouchaojie',
            'password': '7832aa62dbb4dba373c455fe849c5f2c'#md5加密
        }
        self.login_headers = {'Authorization': 'application/x-www-form-urlencoded; charset=UTF-8'}

        self.s = requests.session()
        self.s.headers.update(self.login_headers)

        self.login_url = 'http://chandao.rantron.biz:8083/user-login.html'
        self.login_data = self.s.post(self.login_url,self.chandao_data)
        return self.s

    def read_data(self):
        import time
        self.time_data = (time.strftime("%Y-%m-%d"))
        #项目模块 可以从前端页面看到
        self.set_model = {
                '打印发货':204,'打印发货/自动打印':205,'打印发货/远程打印':206,'打印发货/扫码打印':207,'打印发货/核单发货':208,'打印发货/拣货统计':209,'打印发货/运单导入发货':210,'打印列表':172,'自定义打印':173,
                '日志记录':174,'电子面单':175,'打印模板':176,'打印设置':177,'仓库管理':178,'订单管理列表':179,'多店铺关联':180,'子账号权限':181,'导航栏':182,'我的账户':183,'其他':184,'退款/售后':214,'店铺评价':215,'中差评防御':216
                }
        self.code = {"高":1,"中":2,"低":3,"极低":4}
        #表格的模块部分要和set_model值一致
        path ='C:/Users/Think/Desktop/禅道/千牛6.0问题反馈文档.xlsx'
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        nrows = table.nrows
        # ncols = table.ncols
        # print(nrows,ncols)

        for i in range(1,nrows):
            ss=table.row_values(i)

            module = ss[4]
            for s in self.set_model:
                if module in s:
                    module_code = self.set_model.get(s)

            title = 'prod环境-v6.0-'+ss[4]+'('+ss[5]+')' #拼bug标题

            #严重程度和优先级
            pri = ss[1]
            severity = ss[2]
            for m in self.code:
                if pri in m:
                    pri_code = self.code.get(m)
                if severity in m:
                    severity_code = self.code.get(m)

            # print(module_code,title,time,pri_code,severity_code)
            '''
            assignedTo:这个是指定开发或者产品记得修改
            '''
            self.data = {
                "product": 10,"module": module_code,"project": None,'openedBuild[]': 'trunk','assignedTo': 'xiepengfei','deadline': self.time_data,'type': 'codeerror','os': 'all','browser': 'chrome',
                'pri': pri_code,'severity': severity_code,'title': title,'task': 0,'oldTaskID': 0,'status': 'active','uid': '62400e8cec479','case': 0,'caseVersion': 0,'result': 0,'testtask': 0,
            }
            #a
            print(self.data)
            self.add_url = 'http://chandao.rantron.biz:8083/bug-create-10-0-moduleID=0.html'

            r = self.login().post(self.add_url, self.data)

if __name__ == '__main__':
    a = chanDao()
    a.read_data()