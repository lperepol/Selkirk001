
import sys
import os
from datetime import datetime
import csv
from collections import OrderedDict

def main():
    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\logs\\'

    files = []
    perSecondDict = dict()
    ipCount = dict()
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if 'error' not in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)
        with open(f) as fp:
            cnt = 0
            for line in fp:
                try:
                    date = line.split()
                    dt = date[3]
                    ip = date[0]
                    if ip in ipCount:
                        ipCount[ip] = ipCount[ip] +1
                    else:
                        ipCount[ip] = 1

                    dt = dt[1:]
                    datetime_object = datetime.strptime(dt, '%d/%b/%Y:%H:%M:%S')
                    dt = dt[:17]
                    #datetime_object = datetime.strptime(dt, '%d/%b/%Y:%H:%M')
                    if datetime_object in perSecondDict:
                        perSecondDict[datetime_object] = perSecondDict[datetime_object]+1
                    else:
                        perSecondDict[datetime_object] = 1
                except:
                    print("exception")

    
    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\RequestsPerSecond2.csv'
    with open(path, 'w') as f:
        f.write("Datetime,Requests/Second\n")
        for t in sorted(perSecondDict.keys()):
            dd = '{0:%Y-%m-%d %H:%M:%S}'.format(t)
            f.write("%s,%s\n"%(dd,str(perSecondDict[t])))

    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\IpCount2.csv'
    with open(path, 'w') as f:
        f.write("IP,Count\n")
        for t in sorted(ipCount.keys()):
            f.write("%s,%s\n"%(t,str(ipCount[t])))


if __name__ == '__main__':
   main()