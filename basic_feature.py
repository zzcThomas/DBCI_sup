# encoding: utf-8
'''
Created on 2017年10月17日

@author: c
'''
import pandas as pd
import csv

tr=pd.read_csv('./data/train_utf.csv')
tr['销售日期']=pd.to_datetime(tr['销售日期'],format='%Y%m%d')
tr['weekday']=tr['销售日期'].apply(lambda x:x.dayofweek)
  
all_dates=pd.DataFrame(tr['销售日期'].drop_duplicates())
tr['商品编码']=tr['商品编码'].apply(lambda x:x[3:])

print(tr['商品编码'].head(5))

big_code=pd.DataFrame(tr.drop_duplicates(['大类编码']))
mid_code=pd.DataFrame(tr.drop_duplicates(['中类编码']))
sma_code=pd.DataFrame(tr.drop_duplicates(['小类编码']))
tin_code=pd.DataFrame(tr.drop_duplicates(['商品编码']))
print (len(all_dates),len(big_code),len(mid_code),len(sma_code),len(tin_code))
  
big_f=open('all.csv','w')
big_f.write('BIG,MID,SMA,TINY,DATE\n')
for ix,day in all_dates.iterrows():
    for iy,bc in big_code.iterrows():
            big_f.write(str(bc['大类编码'])+','+str(0)+','+str(0)+','+str(0)+','+str(day['销售日期'])+'\n')
# big_f.close()
  
# big_f=open('mid.csv','w')
for ix,day in all_dates.iterrows():
    for iy,bc in mid_code.iterrows():
            big_f.write(str(bc['大类编码'])+','+str(bc['中类编码'])+','+str(0)+','+str(0)+','+str(day['销售日期'])+'\n')
# big_f.close()
  
# big_f=open('sma.csv','w')
for ix,day in all_dates.iterrows():
    for iy,bc in sma_code.iterrows():
            big_f.write(str(bc['大类编码'])+','+str(bc['中类编码'])+','+str(bc['小类编码'])+','+str(0)+','+str(day['销售日期'])+'\n')
            
for ix,day in all_dates.iterrows():
    for iy,bc in tin_code.iterrows():
            big_f.write(str(bc['大类编码'])+','+str(bc['中类编码'])+','+str(bc['小类编码'])+','+str(bc['商品编码'])+','+str(day['销售日期'])+'\n')            

big_f.close()
 
li=[20150101,20150102,20150218,20150219,20150220,20150221,20150222,20150223,20150224,20150405,20150406,20150501,20150502,20150503]
bx=[20150104,20150227,20150228,20150301]
t=[]
for i in range(0,len(li)):
    li[i]=pd.to_datetime(li[i],format='%Y%m%d')
for i in range(0,len(bx)):
    bx[i]=pd.to_datetime(bx[i],format='%Y%m%d')
 
print (t)
all=csv.DictReader(open('all.csv'))
fn=all.fieldnames
fn.append('isholiday')
fn.append('weekday')
new=csv.DictWriter(open('new_all.csv','w',newline=''),fieldnames=fn)
new.writeheader()
for rec in all:
    date=pd.to_datetime(rec['DATE'])
    print (date)
    rec['isholiday']=0
    rec['weekday']=date.dayofweek
    if date in li or date.dayofweek in [0,6]:
        rec['isholiday']=1
    if date in bx:
        rec['isholiday']=0
    new.writerow(rec)

