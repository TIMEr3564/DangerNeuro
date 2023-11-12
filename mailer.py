import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def set_photo_camera(frame):
    photo_camera = frame
    return photo_camera


photo_camera = set_photo_camera(frame)


def set_id_camera(id_camera):
    id_camera = id_camera
    return id_camera


id_camera = set_id_camera(id_camera)


def get_to_mail():
    common_mail = 'm1nerva0@mail.ru'
    to_mail = input(f'Введите почту получателя (по умолчанию {common_mail}) и нажмите ENTER: ')
    if to_mail:
        common_mail = to_mail
    return common_mail


class Mailer:
    def __init__(self):
        self.login = 'khakaton1@inbox.ru'
        self.password = 'EvJygsdhaDpjwmpB16Nk'
        self.smtp_server_url = 'smtp.mail.ru'
        self.smtp_port = 587

        self.smtp_server = smtplib.SMTP(self.smtp_server_url, self.smtp_port)
        self.smtp_server.starttls()
        self.smtp_server.login(self.login, self.password)

    def send_email(self, recipient, subject, file_path, text):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = recipient
        message['Subject'] = subject

        # Создаем текстовую часть письма
        text_part = MIMEText(text)
        message.attach(text_part)

        with open(file_path, 'rb') as file:
            image = MIMEImage(file.read())
            image.add_header('Content-Disposition', 'attachment', filename=file_path)
            message.attach(image)

        self.smtp_server.sendmail(self.login, recipient, message.as_string())

    def disconnect(self):
        self.smtp_server.quit()


mailer = Mailer()


def send_message(to_mail, text, photo):
    mailer.send_email(to_mail, 'Нарушение ТБ', file_path=photo, text=text)
    mailer.disconnect()


send_message(to_mail=get_to_mail(), text=id_camera, photo=photo_camera)
