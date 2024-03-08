from library import LibraryItem,Book,DVD
"""
Catalog has attributes:
name
a "private" list for holding a collection of LibraryItems

Catalog must implement:
The ability to add a list of LibraryItems 
The ability to remove a list of LibraryItems
The ability to search for items, including the ability to filter the search by the type of item.  The search feature should search all attributes of the the item.  This means that the attributes checked will be different for different sub-classes."""
class Catalog():
  name="CSI Library"
  __items__=[]

  def __init__(self):
    print("CSI Library created")
    
  def add(self):
      
      type=int(input("What kind of item are you adding (Book:1,DVD:2?)"))
      if type == 1:
        item=self.addBook()
      elif type==2:
        item=self.addDVD()
      self.__items__.append(item)
      
  def addBook(self):
      # Adds a book to catalog
      # And returns an Instance of the Class Book
      name = input("Enter the name of the book: ")
      description = input("Enter the description fo the Book: ")
      author = input("Enter the author of the book: ")
      isbn = input("Enter the ISBN of the book: ")
      tags = []
      return Book(name, description, author, isbn, tags)
    
  def addDVD(self):
      # Adds a DVD to catalog
      # And returns an Instance of the Class DVD
      name = input("Enter the name of the DVD: ")
      call_number = input("Enter the call number: ")
      director = input("Enter the director of the DVD: ")
      description = input("Enter the description of the DVD: ")
      release_date = input("Enter the release date of the DVD: ")
      tags = []
      return DVD(name, call_number, director, description, release_date, tags)
      
  def remove(self,listOfItems):
      for item in listOfItems:
          if item in self.__items__:
              self.__items__.remove(item)

  def printAll(self):
      print ("******* CATALOG LIST *******")
      for item in self.__items__:
        print(item)
      print ("******* ******* *******")

  def search(self, search_term, search_type):
      filtered_results = []
      for item in self.__items__:
          if search_type == "Book" and isinstance(item, Book):
              if item.match(search_term):
                  filtered_results.append(item)
          elif search_type == "DVD" and isinstance(item, DVD):
              if item.match(search_term):
                  filtered_results.append(item)
          elif search_type == "":
              if item.match(search_term):
                  filtered_results.append(item)
      return filtered_results
