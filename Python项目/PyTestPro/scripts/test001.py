import xlrd
import pytest
import requests
import json
import allure
import os
from func_toos.email_sender import EmailHander


def setup_module():
    # 删除result中的文件
    path = '.\\report\\result'
    jsonfiles = os.listdir(path)
    for file in jsonfiles:
        os.remove(os.path.join(path, file))


def excel_data():
    book = xlrd.open_workbook('./接口测试示例.xlsx')
    sheet1 = book.sheets()[0]
    rows = sheet1.nrows
    title = sheet1.row_values(0)
    lst = [dict(zip(title, sheet1.row_values(row))) for row in range(1, rows)]
    return lst


test_list = excel_data()


class Test01:
    @pytest.mark.parametrize('data', test_list)
    def test001(self, data):
        response = requests.get(url=data.get('case_url'))
        test_data = json.loads(data.get('case_expect'))
        allure.dynamic.title(data.get("case_project"))
        allure.dynamic.description(data.get("case_description"))
        try:
            tested_data = response.json()
        except:
            assert 0
        for k, v in test_data.items():
            assert v == tested_data.get(k, None)


def teardown_module():
    os.system('allure generate report/result/ -o report/allure_html --clean')
    # 打包压缩发邮件
    email = EmailHander("244797519@qq.com", "aznoqsuizykcbiba")
    email.set_sender('244797519@qq.com')
    email.set_receivers(['244797519@qq.com'])
    email.email_info('马洋', '张开老师', '自动化homework')
    email.email_content('已完成！')
    email.carry_file('.\\report', zip=True)
    email.send_submit()
