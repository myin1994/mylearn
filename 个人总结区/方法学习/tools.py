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

