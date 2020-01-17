import psutil
import time


def net_state():
    recv1 = psutil.net_io_counters(pernic=True)['以太网 2'][1]  # 接收数据
    send1 = psutil.net_io_counters(pernic=True)['以太网 2'][0]  # 上传数据
    time.sleep(1)  # 每隔1s监听端口接收数据
    recv2 = psutil.net_io_counters(pernic=True)['以太网 2'][1]
    send2 = psutil.net_io_counters(pernic=True)['以太网 2'][0]
    # 上传数据
    return 'upload:%.1f kb/s.' % ((send2 - send1) / 1024.0), 'download:%.1f kb/s.' % ((recv2 - recv1) / 1024.0)


while True:
    s1 = net_state()[0]
    s2 = net_state()[1]
    print('当前上传和下载速度为:')
    print(s1)
    print(s2)
    print('---------------------')