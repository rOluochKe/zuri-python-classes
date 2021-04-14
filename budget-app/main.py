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
          print('You selected category %s' % select_options)

          self.deposit(food, cloth, entertainment)

        elif(select_options == 2):
          print('You selected category %s' % select_options)

          self.withdraw(food, cloth, entertainment)

        elif(select_options == 3):
          print('You selected category %s' % select_options)

          self.balance(food, cloth, entertainment)

        elif(select_options == 4):
          print('You selected category %s' % select_options)

          self.transfer(food, cloth, entertainment)

        else:
          print('Invalid category, please try again')


  def deposit(self, food, cloth, entertainment):

    self.food = food
    self.cloth = cloth
    self.entertainment = entertainment

    deposit_food_amount = food
    deposit_cloth_amount = cloth
    deposit_entertainment_amount = entertainment

    print('**********************************************************')
    print('Total amount to deposit for food', deposit_food_amount, 'cloth', deposit_cloth_amount, 'and entertainment', deposit_entertainment_amount)
    print('**********************************************************')

  def withdraw(self, food, cloth, entertainment):

    self.food = food
    self.cloth = cloth
    self.entertainment = entertainment

    withdraw_food_amount = food
    withdraw_cloth_amount = cloth
    withdraw_entertainment_amount = entertainment

    print('==========================================================')
    print('Total amount to withdraw for food', withdraw_food_amount, 'cloth', withdraw_cloth_amount, 'and entertainment', withdraw_entertainment_amount)
    print('==========================================================')

  def balance(self, food, cloth, entertainment):

    self.food = food
    self.cloth = cloth
    self.entertainment = entertainment

    balance_food_amount = food
    balance_cloth_amount = cloth
    balance_entertainment_amount = entertainment

    print('**********************************************************')
    print('Total balance for food', balance_food_amount, 'cloth', balance_cloth_amount, 'and entertainment', balance_entertainment_amount)
    print('**********************************************************')

  def transfer(self, food, cloth, entertainment):

    self.food = food
    self.cloth = cloth
    self.entertainment = entertainment

    transfer_food_amount = food
    transfer_cloth_amount = cloth
    transfer_entertainment_amount = entertainment

    print('==========================================================')
    print('Total amount to transfer for food', transfer_food_amount, 'cloth', transfer_cloth_amount, 'and entertainment', transfer_entertainment_amount)
    print('==========================================================')

budget_one = Budget(500, 200, 150)
# budget_one.deposit(300, 200, 150)
# budget_one.withdraw(300, 200, 150)
# budget_one.balance(300, 200, 150)
# budget_one.transfer(300, 200, 150)