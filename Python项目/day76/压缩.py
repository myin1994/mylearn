import os
import zipfile  # 导入模块
# BASE_STATIC_CASE_RESULT:我Django static下面的某个路径
def zip_file(filepath):
    BASE = os.path.dirname(os.path.abspath(__file__))
    base_dir = filepath
    zip_file_name = 'temp.zip'
    f = zipfile.ZipFile(os.path.join(BASE, zip_file_name), 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_name, file_names in os.walk(base_dir):
        # 要是不replace，就从根目录开始复制
        file_path = dir_path.replace(base_dir, '')
        # 实现当前文件夹以及包含的所有文件
        file_path = file_path and file_path + os.sep or ''
        for file_name in file_names:
            print('11',os.path.join(dir_path, file_name), file_path + file_name)
            f.write(os.path.join(dir_path, file_name), file_path + file_name)
    f.close()
zip_file(r'C:\Users\24479\Desktop\作业上传\Python项目\day76\dirfiles')