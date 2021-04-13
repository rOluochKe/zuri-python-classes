class Budget:
  def __init__(self, food = 0, cloth = 0, entertainment = 0):
      self.food = food
      self.cloth = cloth
      self.entertainment = entertainment

      username  = input('Enter your username? \n')
      if(username):
        print('Welcome %s' % username + ' ' + 'to Budget App')
        print('To proceed, select from the available categories:')
        print('1. Deposit Cash')
        print('2. Widthraw Cash')
        print('3. Check Balance')
        print('4. Transfer Cash')

        select_options = int(input('Please select a category:'))
        if(select_options == 1):
          print('You selected option %s' % select_options)

          self.deposit()

        elif(select_options == 2):
          print('You selected option %s' % select_options)

          self.withdraw()

        elif(select_options == 3):
          print('You selected option %s' % select_options)

          self.balance()

        elif(select_options == 4):
          print('You selected option %s' % select_options)

          self.transfer()

        else:
          print('Invalid option, please try again')


  def deposit(self):

    deposit_food_amount = int(self.food)
    deposit_cloth_amount = int(self.cloth)
    deposit_entertainment_amount = int(self.entertainment)

    print('**********************************************************')
    print('Total amount to deposit for food %s' % deposit_food_amount)
    print('Total amount to deposit for cloth %s' % deposit_cloth_amount)
    print('Total amount to deposit for entertainment %s' % deposit_entertainment_amount)
    print('**********************************************************')

  def withdraw(self):

    withdraw_food_amount = int(self.food)
    withdraw_cloth_amount = int(self.cloth)
    withdraw_entertainment_amount = int(self.entertainment)

    print('==========================================================')
    print('Total amount to withdraw for food %s' % withdraw_food_amount)
    print('Total amount to withdraw for cloth %s' % withdraw_cloth_amount)
    print('Total amount to withdraw for entertainment %s' % withdraw_entertainment_amount)
    print('==========================================================')

  def balance(self):
    balance_food_amount = int(self.food)
    balance_cloth_amount = int(self.cloth)
    balance_entertainment_amount = int(self.entertainment)

    print('**********************************************************')
    print('Total balance for food %s' % balance_food_amount)
    print('Total balance for cloth %s' % balance_cloth_amount)
    print('Total balance for entertainment %s' % balance_entertainment_amount)
    print('**********************************************************')

  def transfer(self):
    transfer_food_amount = int(self.food)
    transfer_cloth_amount = int(self.cloth)
    transfer_entertainment_amount = int(self.entertainment)

    print('==========================================================')
    print('Total amount to transfer for food %s' % transfer_food_amount)
    print('Total amount to transfer for cloth %s' % transfer_cloth_amount)
    print('Total amount to transfer for entertainment %s' % transfer_entertainment_amount)
    print('==========================================================')

budget_one = Budget(500, 200, 150)
# budget_one.deposit(300, 200, 150)
# budget_one.withdraw(300, 200, 150)
# budget_one.balance(300, 200, 150)
# budget_one.transfer(300, 200, 150)