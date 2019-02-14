#coding:utf-8

import time
import datetime
from dateutil.relativedelta import relativedelta




class Loan(object):
    now = datetime.datetime.now()
    d = now.day
    y = now.year
    m = now.month

    # print(now,d,y,m)
    # print(time.localtime())

    def __init__(self,amount,period,rate,rate1,repayment,date1=time.strftime("%Y-%m-%d", time.localtime()),date2=datetime.date(y,m,d)+relativedelta(months=+1)):
        self.amount = amount
        self.period = period
        self.rate = rate
        self.rate1 = rate1
        self.repayment = repayment
        self.date1 = date1
        self.date2 = date2

    def res(self):
        # 贷款额为a，月利率为i，年利率为I，日利率为j，还款月数为n
        a = self.amount
        ssss = []
        if self.rate == 0:
            # 输入年利率
            I = self.rate1
            i = I / 12
            j = I / 365
        elif self.rate == 1:
            # 输入月利率
            i = self.rate1
            I = i * 12
            j = I/365
        elif self.rate == 2:
            #方案3，输入日利率
            j = self.rate1
            I = j * 365
            i = I/12

        # print(i * 100, I * 100, j * 100)

        n = self.period

        print("借款金额：", a)
        print("借款期数：", n)


        if self.repayment == 0:
            # 首次还款日
            y1 = 2019
            m1 = 2
            d1 = 21

            y2 = 2019
            m2 = 1
            d2 = 21

            # #每期还款本金
            ds = a / n
            # 利息
            ss = 0

            # 4.695833

            day1 = datetime.date(y1, m1, d1)
            day2 = datetime.date(y2, m2, d2)
            ee = (day1 - day2).days
            fs = a * j * ee  # 每月应还利息
            gs = ds + fs

            # print("第1个月%s应还天数%d，应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s" % (
            # str(day1), ee, round(fs, 2), round(ds, 2), round(gs, 2)))
            # print("第1个月应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s" % (round(fs,2), round(ds,2), round(gs,2)))
            ssss.append("第1个月%s应还天数%d，应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s" % (
            str(day1), ee, round(fs, 2), round(ds, 2), round(gs, 2)))

            for l in range(2, n + 1):
                day1 += relativedelta(months=+1)
                # print(day1)
                day2 = day1 - relativedelta(months=+1)
                # print(day2)

                ee = (day1 - day2).days
                f = (a - ds * (l - 1)) * j * ee  # 每月应还利息
                g = ds + f
                sa = a - ds * (l - 1)  # 剩余本金
                # print("第%d个月%s应还天数%d，应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s，剩余本金%s" % (
                # l, str(day1), ee, round(f, 2), round(ds, 2), round(g, 2), round(sa, 2)))
                # print("第%d个月应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s"%(l,round(f,2),round(ds,2),round(g,2)))
                ssss.append("第%d个月%s应还天数%d，应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s，剩余本金%s" % (
                l, str(day1), ee, round(f, 2), round(ds, 2), round(g, 2), round(sa, 2)))

                ss += f
            print("等额本金总利息:", round(ss + fs, 2))
        elif self.repayment == 1:

            print("-----等额本息计算,以" + str(n) + "个月为例-----")
            # 月均还款(本金+利息)
            b = a * i * pow((1 + i), n) / (pow((1 + i), n) - 1)
            # 还款利息总和
            Y = n * a * i * pow((1 + i), n) / (pow((1 + i), n) - 1) - a
            print("等额本息总利息:", round(Y, 2))
            # 第一个月还款利息
            c1 = a * i
            # 剩余利息
            e1 = Y - c1
            # 剩余本金
            a1 = a - (b - c1)
            print("第1个月应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s" % (round(c1, 2), round(b - c1, 2), round(b, 2)))
            # 第2 - n个月还款利息
            for t in range(2, n + 1):
                ci = (a * i - b) * pow((1 + i), (t - 1)) + b
                bi = b - ci
                print("第%d个月应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s" % (t, round(ci, 2), round(bi, 2), round(b, 2)))

            print("-----等额本金计算,以" + str(n) + "个月为例-----")
        elif self.repayment == 2:
            print("-----分期还款(等本等息),以" + str(n) + "个月为例-----")
            # 每月应还本金
            dd = a / n
            # 每月应还利息
            df = j * a * (365 / 12)
            for m in range(1,n+1):
                ssss.append("第%d个月应还利息为%s,应还本金为%s,还款总额（本金+利息）为%s"%(m,round(df,2),round(dd,2),round(dd+df,2)))
            print("分期总利息:", round(df * n, 2))


        # return (l, str(day1), ee, round(f, 2), round(ds, 2), round(g, 2), round(sa, 2),round(ss + fs, 2))
        return(ssss)


# s = Loan(1500000,360,0,0.05635,2)
# print(s.date1,s.date2)
# print(s.res())




'''
输入项：
借款金额
借款期数
利率方式下拉：月利率、年利率、日利率
利率输入框
贷款方式：等额本金、等额本息、等本等息
非必填：放款日期、第一还款日
输出项：

'''