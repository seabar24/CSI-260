"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""

class LibraryItem:
    """Base class for all items stored in a library catalog

    Provides a simple LibraryItem with only a few attributes

    """
    def __init__(self, name, isbn, tags=None):
      """Initialize a LibraryItem
        :param name: (string) Name of item
        :param callNumber: (string) local identifying number for the item
        :param tags: (list) List of CategoryTags
      """
      self.name = name
      self.isbn=isbn
      
      if tags:
          self.tags = tags
      else:
          self.tags = list()
      
    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text match should be case insensitive and should search all attributes of the class. Depending on the attribute, match requires an exact match or partial match. match needs to be redefined for any subclasses. Please see the note/notebook case study from Chapter 2 as an example of how match is designed to work. :param filter_text: (string) string to search for :return: (boolean) whether the search_term is a match for this item """ 
        return filter_text.lower() in self.name.lower() or \
               filter_text.lower() == self.isbn.lower() or \
               filter_text.lower() in (str(tag).lower() for tag in self.tags) 

    def __str__(self):
        """Return a well formatted string representation of the item. All instance variables are included. All subclasses must provide a __str__ method"""
        return f'{self.name}\n{self.isbn}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item. String contains only the name of the item and the type of the item. I.E. Moby Dick - eBook. All subclasses must provide a to_short_string method"""
        return f'{self.name} - {self.isbn}'

class Book(LibraryItem):
    def __init__(self, name, author, description, isbn, tags=None):
        super().__init__(name, isbn, tags)
        self.author = author
        self.description = description

        if tags:
              self.tags = tags
        else:
              self.tags = list()

    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text match should be case insensitive and should search all attributes of the class. Depending on the attribute, match requires an exact match or partial match. match needs to be redefined for any subclasses. Please see the note/notebook case study from Chapter 2 as an example of how match is designed to work. :param filter_text: (string) string to search for :return: (boolean) whether the search_term is a match for this item """ 
        return super().match(filter_text) or \
               filter_text.lower() in self.author.lower() or \
               filter_text.lower() in self.description.lower()

    def __str__(self):
        """Return a well formatted string representation of the item. All instance variables are included. All subclasses must provide a __str__ method"""
        return f'{super().__str__()}\n{self.author}\n{self.description}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item. String contains only the name of the item and the type of the item. I.E. Moby Dick - eBook. All subclasses must provide a to_short_string method"""
        return f'{self.name} - {self.isbn}'

class DVD(LibraryItem):
    def __init__(self, name, director, description, isbn, release_date, tags=None):
        super().__init__(name, isbn, tags)
        self.director = director
        self.description = description
        self.release_date = release_date

        if tags:
              self.tags = tags
        else:
              self.tags = list()

    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text match should be case insensitive and should search all attributes of the class. Depending on the attribute, match requires an exact match or partial match. match needs to be redefined for any subclasses. Please see the note/notebook case study from Chapter 2 as an example of how match is designed to work. :param filter_text: (string) string to search for :return: (boolean) whether the search_term is a match for this item """ 
        return super().match(filter_text) or \
               filter_text.lower() in self.director.lower() or \
               filter_text.lower() in self.description.lower() or \
               filter_text.lower() in self.release_date.lower()

    def __str__(self):
        """Return a well formatted string representation of the item. All instance variables are included. All subclasses must provide a __str__ method"""
        return f'{super().__str__()}\n{self.director}\n{self.description}\n{self.release_date}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item. String contains only the name of the item and the type of the item. I.E. Moby Dick - eBook. All subclasses must provide a to_short_string method"""
        return f'{self.name} - {self.description}'
