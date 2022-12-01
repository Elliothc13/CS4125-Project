from django.core.mail import send_mail


class EmailSender:
    @staticmethod
    def sendEmail(sender, receiver, subject, content):
        assert ('@' in sender) #checks that sender is an email
        print('===== Sending email',
              subject,
              content,
              sender,
              [receiver],
              )
