from django.core.mail import send_mail


def email_message(message_dict):
   contents = f"""
   Hi, thank you for trying to reset your password.
   Your token is: {message_dict['token']}
   """
   send_mail(
      'Password Reset Token',
      contents,
      'joshkap2015@gmail.com',
      [message_dict['email']],
      fail_silently=False
   )


def admin_order_email(message_dict):
   send_mail(
      '[Pizza Express] Order #' + [message_dict['order_id']] + ' Placed By Joshua Kaplan',
      'Joshua Kaplan placed order #' +[message_dict['order_id']]+ 'today. See more details about the order here: http://127.0.0.1:/thank_you/'+[message_dict['order_id']],
      'noreply@pizzaexpress.com',
      'joshkap2015@gmail.com',
      fail_silently=False,
   )
   print('Admin order email sent for Order #' + [message_dict['order_id']])

def user_order_email(message_dict):
   send_mail(
      '[Pizza Express] Your order #' + [message_dict['order_id']] + 'has been placed.',
      'You successfully placed order #' +[message_dict['order_id']]+ '. See more details about the order here: http://127.0.0.1:/thank_you/'+[message_dict['order_id']],
      'noreply@pizzaexpress.com',
      'joshkap2015@gmail.com',
      fail_silently=False,
   )
   print('User order email sent for Order #' + [message_dict['order_id']])