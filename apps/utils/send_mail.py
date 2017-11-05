from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from random import Random
from jiaoyu.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'QWETREHIOPJASNDVKSABMDSasdfghjkzxcvbnm1234567890'
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,len(chars)-1)]
    return str



def register_seng_mail(email,send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(9)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''
    if send_type =='register':

        email_title = '在线教育网在线激活链接'
        email_body = '请点击此链接进行激活http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type =='forget':
        email_title = '在线教育网密码重置'
        email_body = '请点击此链接进行修改密码http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass




