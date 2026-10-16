'''this is cos-tools trading application code'''
import time
class vendor:
    '''trading application'''
    def __init__(self,vName,vGST):
        '''vendor enrollment'''
        self.vName = vName
        self.vGST = vGST
        print(f'Vendor {self.vName} enrollment is done!!')
    def billing(self,pName,pQTY,pCost=0.0):
        '''product billing details'''
        self.pName = pName
        self.pQTY = pQTY
        self.pCost = pCost
        self.total = self.pQTY * self.pCost
        self.tax = 0.18
        self.gs = self.total * 0.18 + self.total
        with open('vendorInfo.log','a') as wobj:
            s1 = f'Vendor Name:{self.vName} GST:{self.vGST} '
            s2 = f'Product Name:{self.pName} Qty:{self.pQTY} '
            s3 = f'Product Cost:{self.pCost} Total(includingTax):{self.gs} '
            s4 = f'PO Date/time:{time.ctime()}\n'
            wobj.write(s1+s2+s3+s4)
