class EmailContainer(object):
    subject = ''
    message = ''
    from_email = 'info@gmail.com'
    recipient_list = []
    email_template = None
    context = None


class TestEmail(EmailContainer):
    subject = 'Test mail'
    message = 'Some test body.'
    email_template = 'email_templates/test_template.html'
