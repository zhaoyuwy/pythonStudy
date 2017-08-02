# print("%+10x" % 10)
# print("%04d" % 5)
# print("%6.3f" % 2.3)

# print("%.*f" % (4, 1.2))
# import this
# a = this.s
# b = this.d
# c = ''
# print('=================1====================')
# print(a)
# print('=================2====================')
# print(b)
# print('=================3====================')
# for i in a :
#     temp = i
#     print("this is a temp   ############"+temp)
#     if i.isalpha() :
#         temp = b[i]
#     c = c + temp
# print('=================4====================')
# print(c)
#
#
# import re1
# m = re.search('[0-9]','abcd4ef')
# print(m.group(0))


#
# import time
# print('start')
# time.sleep(10)     # sleep for 10 seconds
# print('wake up')
#
#
# import datetime
# t = datetime.datetime(2012,9,3,21,30)
#
# print(t)
# import datetime
# last = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
# print (last)
# import datetime,time
# starttime = datetime.datetime.now()
# # starttime.second;
# #long running
# time.sleep(3)
# endtime = datetime.datetime.now()
# print ((endtime - starttime).seconds)
# print(starttime >endtime)

# import os.path
# path = '/home/vamei/doc/file.txt'
#
# print(os.path.basename(path))    # 查询路径中包含的文件名
# print(os.path.dirname(path))     # 查询路径中包含的目录
#
# info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
# path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')  # 使用目录名和文件名构成一个路径字符串
# print(path2)
# p_list = [path, path2]
# print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分

# import os.path
# path = '/home/vamei/doc/file.txt'
#
# print(os.path.exists(path))    # 查询文件是否存在
#
# print(os.path.getsize(path))   # 查询文件大小
# print(os.path.getatime(path))  # 查询文件上一次读取的时间
# print(os.path.getmtime(path))  # 查询文件上一次修改的时间
#
# print(os.path.isfile(path))    # 路径是否指向常规文件
# print(os.path.isdir(path))     # 路径是否指向目录文件
# import glob
# print(glob.glob('/home/vamei/*'))
# import os
# os.mkdir('/new')
# import pickle
#
# # define class
# class Bird(object):
#     have_feather = True
#     way_of_reproduction  = 'egg'
#
# summer       = Bird()                 # construct an object
# print(summer)
# picklestring = pickle.dumps(summer)   # serialize object
# print(picklestring)

# import subprocess
# rc = subprocess.cal
# l(["ls","-l"])
#
# import signal
# # Define signal handler function
# def myHandler(signum, frame):
#     print('I received: ', signum)
#
# # register signal.SIGTSTP's handler
# signal.signal(signal.SIG_DFL, myHandler)
# # signal.pause()
# print('End of Signal Demo')

# A program to simulate selling tickets in multi-thread way
# Written by Vamei

# import threading
# import time
# import os
#
# # This function could be any function to do other chores.
# def doChore():
#     time.sleep(0.5)
#
# # Function for each thread
# def booth(tid):
#     global i
#     global lock
#     while True:
#         lock.acquire()                # Lock; or wait if other thread is holding the lock
#         if i != 0:
#             i = i - 1                 # Sell tickets
#             print(tid,':now left:',i) # Tickets left
#             doChore()                 # Other critical operations
#         else:
#             print("Thread_id",tid," No more tickets")
#             os._exit(0)              # Exit the whole process immediately
#         lock.release()               # Unblock
#         doChore()                    # Non-critical operations
#
# # Start of the main function
# i    = 100                           # Available ticket number
# lock = threading.Lock()              # Lock (i.e., mutex)
#
# # Start 10 threads
# for k in range(10):
#     new_thread = threading.Thread(target=booth,args=(k,))   # Set up thread; target: the callable (function) to be run, args: the argument for the callable
#     new_thread.start()                                      # run the thread

import os
print(os.uname())
print(os.getgid())