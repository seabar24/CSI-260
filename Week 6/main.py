from catalog import Catalog
from library import LibraryItem,Book,DVD
"""DESCRIPTION OF THE MODULE GOES HERE

Author: Sean Barrick
Class: CSI-260-01
Assignment: Library Project
Due Date: 2/27/2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
exit=False

#mb=Book("title","1234","a and B","describe","ppppp","1234")

menu ="""Library Catalog Menu

1. Search catalog
2. Print the entire catalog
3. Add item to catalog
4. remove item from catalog
5. exit
"""
def search_items():
    search_term = input("Enter search term: ")
    search_type = input("Enter search type (Book or DVD): ")

    results = myLib.search(search_term, search_type)
    if results:
        for result in results:
            print(result)
    else:
        print("The item described was not found within the Catalog! Try adding this item.")

def remove_item():
    remove_term = input("Enter item(s) to remove separated by commas: ")
    remove_items = [item.strip() for item in remove_term.split(',')]
    items_to_remove = [item for item in myLib.__items__ if item.name in remove_items]
    if items_to_remove:
        myLib.remove(items_to_remove)
        print("Items successfully removed.")
    else:
        print("This item was not found within the Catalog!")
    
myLib=Catalog()
while not exit:
  
  print (menu)
  
  choice=int(input("Choose an option:"))
  match (choice):
    case 1:
      search_items()
    case 2:
      myLib.printAll()
    case 3:
      myLib.add()
    case 4:
      remove_item()
    case 5:
      exit=True
    case default:
      print("ERROR ERROR ERROR")
