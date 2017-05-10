import sys  
import struct  
import os
import shutil

def exactStock(filepath, code):
    ofile = open(filepath,'rb')
    buf=ofile.read()
    ofile.close()
    num=len(buf)
    no=num/32
    b=0
    e=32
    items = list()
    for i in range(int(no)):
        a=struct.unpack('IIIIIfII',buf[b:e]);
        year = int(a[0]/10000);
        m = int((a[0]%10000)/100);
        month = str(m);
        if m <10 :
            month = "0" + month;
        d = (a[0]%10000)%100;
        day=str(d);
        if d< 10 :
            day = "0" + str(d);
        dd = str(year)+"-"+month+"-"+day
        openPrice = a[1]/100.0
        high = a[2]/100.0
        low =  a[3]/100.0
        close = a[4]/100.0
        amount = a[5]/10.0
        vol = a[6]
        unused = a[7]
        if i == 0 :
            preClose = close
        ratio = round((close - preClose)/preClose*100, 2)
        preClose = close
        item=[str(code[0:8]), dd, str(openPrice), str(high), str(low), str(close), str(ratio), str(amount), str(vol)]
        items.append(item)
        b=b+32
        e=e+32
    return items
        
    
def clearTxtFilePath():
    path1 = "D:\\software\\new_tdx\\vipdoc\\sz\\lday\\txt\\"
    path2 = "D:\\software\\new_tdx\\vipdoc\\sh\\lday\\txt\\"
    if os.path.exists(path1):
        print("delete:" + path1)
        shutil.rmtree(path1)
    if os.path.exists(path2):
        print("delete:" + path2)
        shutil.rmtree(path2)
    os.mkdir(path1)
    os.mkdir(path2)
    
def generateTxtFile(items,fileName):
    if fileName[0:2]=='sz' :
        f = open("D:\\software\\new_tdx\\vipdoc\\sz\\lday\\txt\\" + str(fileName[0:8] + ".txt"),'wb')
        f.write(str(items))
    else:
        f = open("D:\\software\\new_tdx\\vipdoc\\sh\\lday\\txt\\"  + str(fileName[0:8] + ".txt"),'wb')
        f.write(str(items))
    print(fileName[2:8])
    
    
def buildTxtData():
    print("clearing old data")
#     clearTxtFilePath()
    rootDirs = set(["D:\\software\\new_tdx\\vipdoc\\sz\\lday" ,"D:\\software\\new_tdx\\vipdoc\\sh\\lday\\"])
    for pathes in rootDirs:
        list = os.listdir(pathes)
        for i in range(0,len(list)):
            filepath = os.path.join(pathes,list[i])
            if os.path.isfile(filepath):
                fileName = list[i]
                if fileName[2:5]=="000" or fileName[2:5]=="002" or fileName[2:5]=="600":
                    items = exactStock(filepath,fileName)
                    generateTxtFile(items,fileName)
                           
buildTxtData()