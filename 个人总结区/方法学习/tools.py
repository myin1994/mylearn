import functools
class Tools:
    def __init__(self):
        pass

    def values(self, dic, *args):
        """

        :param dic: 获取到的字典
        :param args: 需要的字典中的键
        :return: 目标键值对
        """
        return {k: dic[k] for k in args}

def change_suffix(file_path, suffix,to=None):
    """
    修改文件名后缀

    file_path:str-待修改文件路径
    suffix：后缀
    to：转移路径（无则至默认路径同级文件夹,相同文件夹则原地修改）
    """
    changed_path = to or file_path+"havechanged"
    try:
        shutil.copytree(file_path,changed_path)
    except:
        pass
    file_list = os.listdir(changed_path)
    for file_name in file_list:
        old_name = os.path.join(changed_path, file_name)
        new_name = os.path.join(changed_path, file_name.split('.')[0])
        os.rename(old_name, f"{new_name}.{suffix}")