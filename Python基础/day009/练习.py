# # 加减乘除的函数
# # "1 + 1+4*8 -4-6/2"
# def results():
#     results = 0
#     str1 = input("输入加减乘除：").replace(" ","")
#     for i in str1:
#         results += int(i)
#     return results
# print(results())

import re
def atom_cal(m_str):
    """最小计算单位"""
    if "*" in m_str:
        m1,m2 = m_str.split("*")
        return str(float(m1) * float(m2))
    elif "/" in m_str:
        m1,m2 = m_str.split("/")
        return str(float(m1)/float(m2))

def format_str(f_str):
    """格式化字符串"""
    f_str = f_str.replace("++","+")
    f_str = f_str.replace("+-","-")
    f_str = f_str.replace("--","+")
    f_str = f_str.replace("-+","-")
    return f_str

def mul_div(exp):
    """计算乘除"""
    while True:
        exp_res = re.search(r"\d+(\.\d+)?[*/]-?\d+(\.\d+)?", exp)   # 找出乘除法的表达式
        if exp_res:
            atom_exp = exp_res.group()  # group取出最小的表达式
            res = atom_cal(atom_exp)  # 计算最小单位乘除得到结果
            exp = exp.replace(atom_exp, res)  # 将结果替换回原来的字符串
        else:
            return str(exp)

def add_sub(exp):
    """计算加减"""
    exp_sum = 0
    while True:
        exp_res = re.findall(r"-?\d+(?:\.\d+)?", exp)  # 用findall将符号连带数字一起找出来,直接相加就行了,这样还省去了去括号的麻烦,这个思想不错
        if exp_res:
            for i in exp_res:
                exp_sum += float(i)
            return exp_sum

def cal(exp):
    """计算加减乘除并返回值"""
    exp = mul_div(exp)  # 先计算乘除
    exp = format_str(exp)   # 格式化字符串
    exp = add_sub(exp)  # 计算加减
    return exp

def main(exp):
    exp = exp.replace(' ','')   # 先去空格
    while True:
        exp_res = re.search(r"\([^()]+\)", exp)     # 找括号
        if exp_res:
            exp_group = exp_res.group() # 取值
            cal_res = cal(exp_group)       #计算括号内的值,返回数值结果
            exp = exp.replace(exp_group, str(cal_res))  # 在这里str转字符串而不是在返回值转是因为想最终返回给用户的计算值为float类型
        else:
            return cal(exp)
s = "1 +3*2/4- 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
print(eval(s))  # python计算出来的结果
print(main(s))  # 自己写的计算出来的结果