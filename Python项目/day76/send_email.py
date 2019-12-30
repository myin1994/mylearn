import os
import zipfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class EmailHander:
    message = MIMEMultipart()

    def __init__(self,mail_user,mail_pass,mail_host="smtp.qq.com"):
        """
        初始化服务器
        :param mail_host: 设置服务器
        :param mail_user: 用户名
        :param mail_pass: 口令
        """
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = None
        self.receivers = []

    def set_sender(self,sender):
        """

        :param sender: 发送方邮箱
        :return:
        """
        self.sender = sender

    def set_receivers(self,receivers_list:list):
        """

        :param receivers_list: 接收方邮箱列表
        :return:
        """
        self.receivers += receivers_list

    def email_info(self,sender_name='未命名',receiver_name='未命名',subject='无主题'):
        """

        :param sender_name: 发送者姓名
        :param receiver_name: 接收方姓名
        :param subject: 邮件主题
        :return:
        """
        self.message['From'] = Header(sender_name, 'utf-8')  # 发件人
        self.message['To'] = Header(receiver_name, 'utf-8')  # 收件人
        self.message['Subject'] = Header(subject, 'utf-8') #主题

    def email_content(self,send_content):
        """
        :param send_content: 邮件正文
        :return:
        """
        content_obj = MIMEText(send_content, 'plain', 'utf-8')  # 第一个参数为邮件内容
        self.message.attach(content_obj)

    def carry_file(self,filepath,zip=False):
        """
        :param filepath: 携带文件路径(非文件夹)
        :return:
        """
        if zip:
            filepath = self.zip_file(filepath)
        att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        filename = os.path.basename(filepath)
        att["Content-Disposition"] = f'attachment; filename="{filename}"'
        self.message.attach(att)
        if zip:
            os.remove(filepath)

    def send_submit(self):
        if not self.sender:
            print('发送者不能为空')
            return
        if not self.receivers:
            print('接收者不能为空')
            return
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


    def zip_file(self,filepath, targtepath=None):
        """

        :param filepath: 待压缩文件/文件夹
        :param targtepath: 压缩文件存储位置
        :return:
        """
        base_dir, file_name = os.path.split(filepath)
        zip_name = file_name.split('.')[0] + '.zip'
        zip_path = os.path.join(targtepath or base_dir, zip_name)
        f = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
        if os.path.isfile(filepath):
            f.write(filepath, file_name)
        else:
            for dir_path, dir_name, file_names in os.walk(filepath):
                # 要是不replace，就从根目录开始复制
                file_path = dir_path.replace(base_dir, '')
                # 实现当前文件夹以及包含的所有文件
                file_path = file_path and file_path + os.sep or ''
                for file_name in file_names:
                    f.write(os.path.join(dir_path, file_name), file_path + file_name)
        f.close()
        return zip_path

#设置服务器及口令
email = EmailHander("244797519@qq.com","aznoqsuizykcbiba")
#设置发送者接受者
email.set_sender('244797519@qq.com')
email.set_receivers(['244797519@qq.com'])
#编辑发件人，收件人，主题,邮件内容
email.email_info('张三','李四','测试邮件')
email.email_content('hello')
#设置发送的文件
email.carry_file('test.xlsx')
# email.carry_file('send_email.py')
#发送
email.send_submit()
