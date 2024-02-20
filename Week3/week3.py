"""Creates instances of the Class Countries and compares/contrast them to one another

Author: Sean Barrick
Class: CSI-260-01
Assignment: Week 3 Lab
Due Date: February 11, 2024 11:59 PM

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

class Country:
    def __init__(self, name, population, area):
        self._name = name
        self.population = population
        self.area = area
        print(self._name, "is created")

    def get_name(self):
        return self._name

    def is_larger(self, country):
        if self.area > country.area:
            return True
        else:
            return False

    def population_density(self):
        density = self.population // self.area
        return density

    def summary(self):
        print(self._name, "has the population of", self.population, \
              "people and is", self.area, \
              "square km. It therefore has a population density of", \
              self.population_density())

    def __str__(self):
        s=self._name + " has a population of" + self.population,\
        "people and is" + self.area + "square km."
        return s

c1 = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914848, 9826675)
if c1.is_larger(usa):
    print(c1.get_name(), "is larger.")
else:
    print(usa.get_name(), "is larger.")

usa.summary()
