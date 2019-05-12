#流水线之构造新字典
import json
with open('guanzhu.json','r') as json_f:
    user_text=json.load(json_f)
user_text_list=user_text['content']
    
    
f1 = open('dict0.txt', 'r',encoding='utf-8')
#f2 = open('用户关注.txt','r')
f3 = open('真输出.txt','w',encoding='utf-8')
src_dict=f1.read()+'\n'

#for line in f2:
#    src_dict+=line[:-1]+' 10000 nt\n'
for i in user_text_list:
    src_dict+=i+' 10000 nt\n'

f1.close()
#f2.close()
f3.write(src_dict)
f3.close()

#流水线之内容筛选
import os
import json

#导入内容
f=open('.//交互文件夹//0--10万电销资源.json')
text=json.load(f)
f.close()
import re
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',text['comment'])
a=dd.replace('\n','')
b=a.replace('\t','')
text['comment'] = b
text['value']=text['value'].replace('\xa0','')

#文本第一次处理
import jieba
import jieba.posseg as psg
    
def get_flag(x):
    for word,flag in psg.cut(x):
        tmp1_flag=flag
    return tmp1_flag
#取出停用词
f = open('stopwords.txt', 'r')
sw=[]
for line in f:
    line=line[:len(line)-3]
    sw.append(line)
sw.append(' ')
f.close
#获取输入
cut=text['comment']+text['title']
cut=cut.replace('w','万条')
jieba.load_userdict('真输出.txt')
cut=jieba.cut(cut)
cutted=[]
for i in cut:
    cutted.append(i)
clean=[tok for tok in cutted if len(tok)>=1 and (tok not in sw)]
f2 = open('用户关注.txt','r')
tag_array=[]
for line in f2:
    if(line[:-1] in clean):
        tag_array.append(line[:-1])
f2.close()


#获取标记
f=open('meat.txt','w')
s=''
for i in clean:
    s+= i+' '
s=s[:-1]
f.write(s)
f.close()
import subprocess
(status,output) = subprocess.getstatusoutput('./fasttext predict model.bin ./meat.txt')

import time
msg={}
#############
level=output
##############
if(tag_array!= None):
    msg['username']='username'
    msg['time']=time.asctime( time.localtime(time.time()))
    tags=''
    for i in tag_array:
        tags+=i+','
    tags=tags[:-1]
    msg['tags']=tags
    msg['content']=text['comment']
    msg['level']=level
import json
json_str=json.dumps(msg)
with open('msg.json','w') as json_f:
    json_f.write(json_str)

