# psutil模块使用

## psutil简介

​		psutil是一个跨平台库(http://pythonhosted.org/psutil/)能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。它主要用来做系统监控，性能分析，进程管理。它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。目前支持32位和64位的Linux、Windows、OS X、FreeBSD和Sun Solaris等操作系统.

## 安装

```
#5.6.7版本
pip install psutil
```

## 使用

### 引入

```python
import psutil
```

### 系统相关的类(CPU的利用率)

+ CPU逻辑数量

  ```python
  psutil.cpu_count()#12
  ```

  + 获得可用cpu数量

    ```python
    len(psutil.Process().cpu_affinity())#12
    ```

+ CPU物理核心（核数）

  ```python
  psutil.cpu_count(logical=False) #6
  ```

+ 统计CPU的用户／系统／空闲时间

  ```python
  #将系统CPU时间作为命名元组返回。每个属性表示CPU在给定模式下花费的秒数.
  psutil.cpu_times(percpu=False)
  #scputimes(user=89032.34375, system=41367.96874999977, idle=1934495.203125, interrupt=8451.265625, dpc=1379.0625)
  ```

  + user: 正常进程在用户模式下执行所花费的时间.
  + system: 在内核模式下执行的进程所花费的时间.
  + idle:空闲
  + interrupt:中断
  + dpc:延迟
  + 当percpu是True返回一个名为元组的列表在系统上的每个逻辑CPU。列表的第一个元素是指第一个CPU，第二个元素是第二个CPU.

+ cpu的利用率

  ```python
  psutil.cpu_percent(interval=None, percpu=False)#4.4
  ```

  + 返回一个浮点数，表示当前系统范围的CPU利用率百分比.当percpu是True返回表示利用率的浮点数列表，以每个CPU的百分比表示。列表的第一个元素是指第一个CPU，第二个元素是第二个CPU.
  
+ 提供每个特定cpu时间的利用率百分比

  ```python
  psutil.cpu_times_percent(interval = None,percpu = False)
  ```

+ 将各种CPU统计信息作为命名元组返回

  ```python
  psutil.cpu_stats()
  #scpustats(ctx_switches=600616428, interrupts=3274477530, soft_interrupts=0, syscalls=2091194656)
  ```

  + ctx_switches：启动后的上下文切换次数
  + interrupts: 自引导以来的中断数.
  + soft_interrupts：自引导以来的软件中断次数
  + syscalls：自引导以来的系统调用次数。

+ 将CPU频率作为名称包返回，包括 以Mhz表示的当前，最小和最大频率

  ```python
  psutil.cpu_freq(percpu=False)
  #scpufreq(current=2208.0, min=0.0, max=2208.0)
  ```

  + 当percpu为True并且系统支持每CPU频率检索,为每个CPU返回一个频率列表，否则返回包含单个元素的列表.

+ 将过去1、5和15分钟内的平均系统负载作为一个元组返回。

  ```python
  psutil.getloadavg()
  ```

### 内存相关的类(Memory)

+ 以命名元组的形式返回关于系统内存使用情况的统计信息(物理内存)

  ```python
  psutil.virtual_memory()
  #svmem(total=17047015424, available=9379643392, percent=45.0, used=7667372032, free=9379643392)#约16GB，
  ```

  + 返回的是字节为单位的整数
  + total: 总物理内存
  + available: 在没有系统进入交换的情况下立即提供给进程的内存.
  + used: 使用的内存.
  + free: 空闲的内存.
  + active: 正在使用的内存.
  + inactive: 未使用的内存.
  + buffers: 缓存文件系统元数据.
  + cached: 缓存各种内容.
  + shared: 共享内存.
  + slab: 内核数据结构缓存

+ 将系统交换内存统计信息作为命名元组返回

  ```python
  psutil.swap_memory()
  #sswap(total=18120757248, used=12224544768, free=5896212480, percent=67.5, sin=0, sout=0)
  ```

  + total: 总交换内存(以字节为单位)
  + used: 以字节为单位使用的swap内存
  + free: 以字节为单位的自由交换内存.
  + percent: 计算的百分比使用率(total - available) / total * 100
  + sin: 系统从磁盘交换的字节数.
  + sout: 系统从磁盘换出的字节数.

### 磁盘相关的类(Disks)

+ 将所有已安装的磁盘分区作为命名元组列表返回，包括设备，挂载点和文件系统类型

  ```python
  psutil.disk_partitions(all=False)
  ----------------
  [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'),
   sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'),
   sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'),
   sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed')]
  ```

  + `rw`表示可读写

+ 磁盘使用情况

  ```python
  psutil.disk_usage('/')#默认C:\\
  -------------
  sdiskusage(total=510770802688, used=224876806144, free=285893996544, percent=44.0)
  ```

  + 查看每个磁盘分区的使用率

    ```python
    disk = psutil.disk_partitions()
    TRAN = 1/ 1024 / 1024 / 1024
    for i in disk:
        print("磁盘：%s 分区格式:%s" % (i.device, i.fstype)) # 盘符 分区格式
        disk_use = psutil.disk_usage(i.device) 
    
        print("使用了：%.1f GB,空闲：%.1f GB,总共：%.1f GB,使用率%.1f%%," % (
        disk_use.used * TRAN, disk_use.free * TRAN, disk_use.total * TRAN,
        disk_use.percent))
    -------------------------------
    磁盘：C:\ 分区格式:NTFS
    使用了：209.4 GB,空闲：266.2 GB,总共：475.7 GB,使用率44.0%,
    磁盘：D:\ 分区格式:NTFS
    使用了：8.9 GB,空闲：71.1 GB,总共：80.0 GB,使用率11.2%,
    磁盘：E:\ 分区格式:NTFS
    使用了：7.2 GB,空闲：418.8 GB,总共：426.0 GB,使用率1.7%,
    磁盘：F:\ 分区格式:NTFS
    使用了：167.9 GB,空闲：257.2 GB,总共：425.1 GB,使用率39.5%,
    ```

    

+ 将系统范围的磁盘I / O统计信息作为命名元组返回

  ```python
  #合并统计所有磁盘
  psutil.disk_io_counters(perdisk=False,nowrap=True)
  ------------
  sdiskio(read_count=2074182, write_count=2581574, read_bytes=86650592256, write_bytes=119182960640, read_time=3331, write_time=2154)
  ```

  + perdisk为True,系统上安装的每个物理磁盘返回相同的信息，作为字典.分区名称为键,命名元组为值

  ```python
  #分开统计所有磁盘
  psutil.disk_io_counters(perdisk=True,nowrap=True)
  --------------
  {'PhysicalDrive0': sdiskio(read_count=1880682, write_count=2508832, read_bytes=59234438144, write_bytes=99150924288, read_time=1021, write_time=1547),
   'PhysicalDrive1': sdiskio(read_count=193500, write_count=72753, read_bytes=27416154112, write_bytes=20032101888, read_time=2310, write_time=607)}
  ```

  + 当nowrap为True,psutil将在函数调用中检测并调整这些数字，并将“旧值”添加到“新值”，以便返回的数字将始终增加或保持不变，但永远不会减少
  + `psutil.disk_io_counters.cache_clear()` 用于使nowrap 缓存无效
  + read_count: 读取次数
  + write_count: 写入次数.
  + read_bytes: 读取的字节数
  + write_bytes: 写入的字节数
  + read_time: 从磁盘读取的时间(以毫秒为单位).
  + write_time: 写入磁盘所花费的时间(以毫秒为单位).
  + busy_time: 在实际I/O上的时间.(以毫秒为单位).
  + read_merged_count: 合并读取的数量
  + write_merged_count: 合并写入次数.

### 网络相关的类(Network)

+ 将系统范围的网络I/O统计信息作为命名元组返回(获取网络读写字节／包的个数)

  ```python
  psutil.net_io_counters(pernic=False,nowrap=True)
  ------------
  snetio(bytes_sent=1064070572, bytes_recv=24946619330, packets_sent=8911425, packets_recv=2360279, errin=0, errout=0, dropin=0, dropout=0)
  ```

  + bytes_sent：发送的字节数.

  + bytes_recv：接收的字节数.

  + packets_sent：发送的包数.

  + packets_recv：接收的包数.

  + errin：接收时的错误总数.

  + errout：发送时的错误总数

  + dropin：丢弃的传入数据包总数.

  + dropout：丢弃的传出数据包总数

  + 当pernic为True,系统上安装的每个网络接口返回相同的信息作为字典,网络接口名称作为键,命名元组为值

    ```python
    psutil.net_io_counters(pernic=True,nowrap=True)
    -----------------
    {'WLAN 2': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
     '本地连接* 4': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
     '本地连接* 5': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
     '以太网 2': snetio(bytes_sent=1064083991, bytes_recv=24946677266, packets_sent=8911484, packets_recv=2360611, errin=0, errout=0, dropin=0, dropout=0),
     '蓝牙网络连接 2': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
     'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0)}
    ```

  + `psutil.net_io_counters.cache_clear()` 用于使nowrap 缓存无效

  + 监控宽带或WLAN的上传和下载速度

    ```python
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
    ```

    

+ 将系统范围的套接字连接作为命名元组列表返回

  ```python
  psutil.net_connections(kind='inet')
  ----------------
  [sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=50473), raddr=addr(ip='127.0.0.1', port=50472), status='ESTABLISHED', pid=9744),
   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=50500), raddr=addr(ip='127.0.0.1', port=50499), status='ESTABLISHED', pid=24212),
   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.34.170', port=5353), raddr=(), status='NONE', pid=5336),
   sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5355), raddr=(), status='NONE', pid=2988),
   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.34.170', port=51250), raddr=addr(ip='103.72.47.247', port=80), status='CLOSE_WAIT', pid=23716),
   ………………
   ]
  ```

  + fd: 套接字文件描述符.
  + family：地址簇.
  + type：地址类型
  + laddr：作为命名元组的本地地址或 AF_UNIX套接字的情况.
  + raddr：作为命名元组的远程地址或UNIX套接字的绝对地址
  + status：表示TCP连接的状态.
  + pid: 打开套接字的进程的PID.

+ 将与系统上安装的每个NIC（网络接口卡）关联的地址作为字典返回.键为NIC名称,值是分配给NIC的每个地址的命名元组列表.

  ```python
  psutil.net_if_addrs()
  ---------------
  {'WLAN 2': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='D8-9C-67-9C-4C-5F', netmask=None, broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.158.202', netmask='255.255.0.0', broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::1a1:5746:d244:9eca', netmask=None, broadcast=None, ptp=None)],
   '本地连接* 4': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='DA-9C-67-9C-4C-5F', netmask=None, broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.125.67', netmask='255.255.0.0', broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::c5ad:9f88:ee4f:7d43', netmask=None, broadcast=None, ptp=None)],
   '本地连接* 5': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='FA-9C-67-9C-4C-5F', netmask=None, broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.85.217', netmask='255.255.0.0', broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::9dfb:bcf9:2b87:55d9', netmask=None, broadcast=None, ptp=None)],
   '以太网 2': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='E8-6A-64-02-64-00', netmask=None, broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.34.170', netmask='255.255.255.0', broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::a171:fc30:e483:5660', netmask=None, broadcast=None, ptp=None)],
   '蓝牙网络连接 2': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='D8-9C-67-9C-4C-60', netmask=None, broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.63.178', netmask='255.255.0.0', broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::ddb6:c363:2af7:3fb2', netmask=None, broadcast=None, ptp=None)],
   'Loopback Pseudo-Interface 1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None),
    snicaddr(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)]}
  ```

  + family：地址簇.
  + address: 主NIC地址
  + netmask：网络掩码地址
  + broadcast: 广播地址.
  + ptp: 点对点接口上的目标地址.

+ 将有关每个NIC（网络接口卡）的信息作为字典返回

  ```python
  psutil.net_if_stats()
  ----------------
  {'以太网 2': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500),
   '蓝牙网络连接 2': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=3, mtu=1500),
   'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500),
   'WLAN 2': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500),
   '本地连接* 4': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500),
   '本地连接* 5': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500)}
  ```

  + isup: 指示NIC是否已启动并运行的bool。
  + duplex：双工通信类型.
  + speed：以兆位(MB)表示的NIC速度
  + mtu：NIC的最大传输单位，以字节为单位.

### learn more

```
https://blog.51cto.com/liyuanjie/2437327?source=dra
https://www.liaoxuefeng.com/wiki/1016959663602400/1183565811281984
https://psutil.readthedocs.io/en/latest/#cpu
```

