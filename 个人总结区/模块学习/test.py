import psutil
number_cpu = psutil.cpu_count() # CPU逻辑数量
print(number_cpu)
number_core = psutil.cpu_count(logical=False) # CPU物理核心
print(number_core)

disk = psutil.disk_partitions()
for i in disk:
    print("磁盘：%s 分区格式:%s" % (i.device, i.fstype))  # 盘符 分区格式
    disk_use = psutil.disk_usage(i.device)

    print("使用了：%.1f GB,空闲：%.1f GB,总共：%.1f GB,使用率%.1f%%," % (
        disk_use.used / 1024 / 1024 / 1024, disk_use.free / 1024 / 1024 / 1024, disk_use.total / 1024 / 1024 / 1024,
        disk_use.percent))
