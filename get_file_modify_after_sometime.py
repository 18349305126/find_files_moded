import time;
import os;
import sys;
import re;
date='';
def get_time(path):
    modified_time = time.localtime(os.stat(path).st_mtime);
    m_time = time.strftime('%Y-%m-%d %H:%M:%S', modified_time)
    return m_time;

def visit(path):
    try:
        file_time=get_time(path);
        file_size=os.path.getsize(path)/1024;
        if(file_time>date and file_size>5): '此处限定选取大小超过5M的文件'
            print(path,end=' ');
            print(file_time,'文件大小：',file_size,'MB');
    except OSError:
        print(path,'无法访问');

def walk(path):
    try:
        list=os.listdir(path);
        for i in range(len(list)):
            really_path=path+'\\'+list[i];
            visit(really_path);
            if(os.path.isdir(really_path)==True):
                walk(really_path);
        return;
    except OSError:
        print(path,'无法访问');

def main():
    if(len(sys.argv)!=4):
        print('请输入正确的参数：文件夹名 年-月-日 时:分:秒');
        sys.exit(0);
    elif(os.path.exists(sys.argv[1])==False):
        print("请输入存在的文件夹");
        sys.exit(0);
    else:
        date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d');
        global  date;
        date = sys.argv[2] + ' ' + sys.argv[3];
        if (date_regex.search(date) == None):
            print('请输入正确的日期格式：\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d');
            sys.exit(0);
        walk(sys.argv[1]);

main();
