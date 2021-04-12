from datetime import datetime

print('Welcome to ABC ATM Bank, Login to your account')

username  = input('Enter your username? \n')

allowed_users = ['raymond', 'micheal', 'lucy']
allowed_password = ['raymond10', 'micheal10', 'lucy10']

if(username in allowed_users):
  password = input('Enter your password? \n')
  user_id = allowed_users.index(username)

  if(password == allowed_password[user_id]):

    now = datetime.now()
    date_time_now = now.strftime('%d/%m/%Y %H:%M:%S')

    print('Welcome %s' % username + ' ' + 'and the current date and time is %s' % date_time_now)
    print('To proceed, select from the available options:')
    print('1. Withdraw Money')
    print('2. Deposit Cash')
    print('3. Write a complaint')

    select_options = int(input('Please select an option:'))

    if(select_options == 1):
      print('You selected option %s' % select_options)

      withdraw = int(input('Please enter amount to withdraw \n'))

      print('Take your cash %s' % withdraw)
    elif(select_options == 2):
      print('You selected option %s' % select_options)

      deposit = int(input('Please enter amount to deposit \n'))

      print('Current balance %s' % deposit)
    elif(select_options == 3):
      print('You selected option %s' % select_options)

      report_issue = input('What issue would you like to report? \n')

      print('Thank you for contacting us, issue: %s' % report_issue)      
    else:
      print('Invalid option, please try again')
  else:
    print('Password is incorrect, please try again')
else:
  print('Username not found, try again!')