import requests
import pandas as pd

url = "http://125.35.6.84:81/xk/"


def get_detail_id_list(total_page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    EPS_url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
    detail_id_list = []
    for page in range(1, total_page + 1):
        data = {
            "on": True,
            "page": page,
            "pageSize": 15,
            "productName": "",
            "conditionType": 1,
            "applyname": "",
            "applysn": "",
        }
        response = requests.post(url=EPS_url, headers=headers, data=data)
        detail_id_list += [i.get("ID") for i in response.json().get("list")]
    return detail_id_list


def get_detail(total_page, write_to_excel=False):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    DETAIL_url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
    all_detail_message = {}
    detail_id_list = get_detail_id_list(total_page)
    for detail_id in detail_id_list:
        detail_data = {
            "id": detail_id
        }
        detail_response = requests.post(url=DETAIL_url, headers=headers, data=detail_data)
        detail_data = detail_response.json()
        detail_message = {
            "企业名称": detail_data["epsName"],
            "许可证编号": detail_data["productSn"],
            "许可项目": detail_data["certStr"],
            "企业住所": detail_data["epsAddress"],
            "生产地址": detail_data["epsProductAddress"],
            "社会信用代码": detail_data["businessLicenseNumber"],
            "法定代表人": detail_data["businessPerson"],
            "企业负责人": detail_data["legalPerson"],
            "质量负责人": detail_data["qualityPerson"],
            "发证机关": detail_data["qfManagerName"],
            "签发人": detail_data["xkName"],
            "日常监督管理机构": detail_data["rcManagerDepartName"],
            "日常监督管理人员": detail_data["rcManagerUser"],
            "有效期至": detail_data["xkDate"],
            "发证日期": detail_data["xkDateStr"],
            "状态": "正常" if detail_data["isimport"] == "Y" else "不正常",
            "投诉举报电话": "12331"
        }
        all_detail_message[detail_data["epsName"]] = detail_message
    if write_to_excel:
        pd.DataFrame(all_detail_message).T.to_excel("data.xls", index=False)
    return all_detail_message

detail = get_detail(5, write_to_excel=True)
