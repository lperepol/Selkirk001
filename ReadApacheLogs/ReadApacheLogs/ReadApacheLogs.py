
import sys
import os
from datetime import datetime
import csv
from collections import OrderedDict

def main():
    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\logs\\'
    path = 'C:\\Cygwin64\\home\\lperepolkin1\\logs\\logs\\'

    files = []
    perSecondDict = dict()
    perDayDict = dict()
    ipCount = dict()
    urlCount = dict()
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if 'error' not in file:
                files.append(os.path.join(r, file))

    datetime_Start = datetime.strptime("01/Nov/2019", '%d/%b/%Y')
    for f in files:
        print(f)
        with open(f) as fp:
            cnt = 0
            for line in fp:
                try:
                    date = line.split()
                    htmlCode = str(date[8]).strip()
                    if (htmlCode != '200'):
                        continue
                    url = str(date[6]).strip()
                    url = url.replace(',','~')
                    if ('.' in url):
                        continue
                    if ('?' in url):
                        continue
                    x =0
                    if url == "408":
                        x=1
                    else:
                        x=2
                    dt = date[3]
                    ip = date[0]

                    dt = dt[1:]
                    datetime_object = datetime.strptime(dt, '%d/%b/%Y:%H:%M:%S')
                    if datetime_object < datetime_Start:
                        continue
                    date1 = '{0:%Y-%m}'.format(datetime_object)
                    dateDay = datetime.strptime('{0:%Y-%m-%d}'.format(datetime_object), '%Y-%m-%d')
                    dt = dt[:17]

                    if ip in ipCount:
                        ipCount[ip] = ipCount[ip] +1
                    else:
                        ipCount[ip] = 1

                    #datetime_object = datetime.strptime(dt, '%d/%b/%Y:%H:%M')
                    if datetime_object in perSecondDict:
                        perSecondDict[datetime_object] = perSecondDict[datetime_object]+1
                    else:
                        perSecondDict[datetime_object] = 1

                    if dateDay in perDayDict:
                        perDayDict[dateDay] = perDayDict[dateDay]+1
                    else:
                        perDayDict[dateDay] = 1

                    key = date1 + ',' + url
                    if key in urlCount:
                        urlCount[key] = urlCount[key]+1
                    else:
                        urlCount[key] = 1

                except:
                    print("exception")

    
    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\RequestsPerSecond2.csv'
    path = 'C:\\Cygwin64\\home\\lperepolkin1\\logs\\RequestsPerSecond2.csv'
    with open(path, 'w') as f:
        f.write("Datetime,Requests/Second\n")
        for t in sorted(perSecondDict.keys()):
            dd = '{0:%Y-%m-%d %H:%M:%S}'.format(t)
            f.write("%s,%s\n"%(dd,str(perSecondDict[t])))

    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\RequestsPerDay.csv'
    path = 'C:\\Cygwin64\\home\\lperepolkin1\\logs\\RequestsPerDay.csv'
    with open(path, 'w') as f:
        f.write("Datetime,Requests/Day\n")
        for t in sorted(perDayDict.keys()):
            dd = '{0:%Y-%m-%d}'.format(t)
            f.write("%s,%s\n"%(dd,str(perDayDict[t])))

    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\IpCount2.csv'
    path = 'C:\\Cygwin64\\home\\lperepolkin1\\logs\\IpCount2.csv'
    with open(path, 'w') as f:
        f.write("IP,Count\n")
        for t in sorted(ipCount.keys()):
            f.write("%s,%s\n"%(t,str(ipCount[t])))

    path = 'C:\\cygwin\\home\\Lawrence Perepolkin\\logs\\UrlCount.csv'
    path = 'C:\\Cygwin64\\home\\lperepolkin1\\logs\\UrlCount.csv'
    with open(path, 'w') as f:
        f.write("Datetime,URL,Count\n")
        for t in sorted(urlCount.keys()):
            f.write("%s,%s\n"%(t,str(urlCount[t])))


if __name__ == '__main__':
   main()