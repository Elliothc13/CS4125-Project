from django.core.mail import send_mail

class EmailSender:
    @staticmethod
    def sendEmail(sender, receiver, subject, content):
        print('===== Sending email',
            subject,
            content,
            sender,
            [receiver],
            #fail_silently=False,
            )