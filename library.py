# entity -> Book, User, Library
# function -> add user, add Book


class User:
  def __init__(self, id, name, password) -> None:
    self.id = id
    self.name = name
    self.password = password
    self.borrowList = []
    self.returnList = []


class Book:
  def __init__(self, id, name, category, quantity) -> None:
    self.id = id
    self.name = name
    self.category = category
    self.quantity = quantity


class Library:
  def __init__(self, name, owner,) -> None:
    self.name = name
    self.owner = owner
    self.books = []
    self.users = []

  def addBook(self, id, name, category, quantity):
    book = Book(id, name, category, quantity)
    self.books.append(book)
    print('\tBook added successfully!')
    return book
  
  def showBooks(self):
    print('ID \t Book Name \t Category \t Quantity')
    for i in self.books:
      print(f"{i.id} \t {i.name} \t {i.category} \t\t {i.quantity}")

  def addUser(self, id, name, password):
    user = User(id, name, password)
    self.users.append(user)
    print('\nUser added successfully!')
    return user
  
  def showUsers(self):
    print('ID \t User Name \t Password')
    for i in self.users:
      print(f"{i.id} \t {i.name} \t\t {i.password}")
  
  def borrowBook(self, user, b_id):
    for i in self.books:
      if i.id==b_id:
        if i in user.borrowList:
          print("\nAlready Borrowed! ")
          return
        elif i.quantity<1:
          print("\n No Available Copies! ")
          return
        else:
          user.borrowList.append(i)
          i.quantity -= 1
          print(f"\n {i.name} borrowed successfully! ")
          return
    
    print(f"\nBook not found!")




l1 = Library('abc', 'Sumaiya')
admin = l1.addUser(1, 'admin', 'admin')
u1 = l1.addUser(50, 'rohan', 1234)
b1 = l1.addBook('1', 'Am atir vepu', 'novel', 20)



run = True
currentUser = admin
while run:
  if currentUser == None:
    print(f"\nno logged in User! ")
    option = input('Login ? registration(L/R): ')

    if  option=='R':
      id = int(input('\tEnter id: '))
      name = input('\tEnter name: ')
      password = input('\tEnter Password: ')

      user = l1.addUser(id, name, password) 
      currentUser = user

    elif option=='L':
      id = int(input('\tEnter id: '))
      password = input('\tEnter Password: ')

      found = False
      for i in l1.users:
        if i.id==id and i.password:
          currentUser = i
          found = True
          break
      if found==False:
        print(f"\n\tNo User found! ")
  else:
    if currentUser.name=='admin':
      print('\nOptions:  ')
      print('1: Add Book')
      print('2: Show Users')
      print('3: Show Books')
      print('4: Logout')

      choice = int(input('\nEnter Option: '))
      if choice==1:
        id = int(input('\tEnter id: '))
        name = input('\tEnter Name: ')
        category = input('\tEnter Category: ')
        quantity = input('\tEnter quantity: ')

        l1.addBook(id, name, category, quantity)
      elif choice==2:
        l1.showUsers()
      elif choice==3:
        l1.showBooks()
      elif choice==4:
        currentUser = None

    else: # admin na -> currentUser = None
      print('\nOptions:  ')
      print('1: Borrow Book')
      print('2: return Users')
      print('3: Show Books')
      print('4: Show borrowed books')
      print('4: Logout')

      choice = int(input('\nEnter Options'))
      if choice==1:
        id = input('\tEnter id: ')
        l1.borrowBook(currentUser, id)











        
