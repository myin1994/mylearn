def dict_filter(dic, error, *args):
    """

    :param dic: 获取到的字典
    :param error: 对应值为空或不存在抛出的异常值
    :param args: 需要的字典中的键
    :return: 目标键值对(如果键值为空则抛出异常NameError)
    """
    dic2 = {}
    for k in args:
        # if not dic.get(k) or dic.get(k).replace(" ",'') == '':
        if not dic.get(k) or " " in dic.get(k):
            print(type(dic.get(k)))
            print(k)
            raise NameError(error)
        dic2[k] = dic.get(k)
    return dic2
