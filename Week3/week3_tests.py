"""Tests for Week 3 Lab.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

import unittest
import sys
week3 = None
try:
    import week3
except ImportError:
    pass  # swallow the error here, will be reported in test_1

STUDENT_CODE = ["week3.py"]


class TestWeek3(unittest.TestCase):
    """Main testing class for Week 3 Lab."""

    def test_1_module_exists(self):
        """Test if the week3 module exists."""
        self.assertIsNotNone(week3,
                             "Cannot import week3, make sure week3.py exists "
                             "in this directory.")

    def test_2_class_exists(self):
        """Test if the week3 module contains a class Country."""
        self.assertIn("Country", week3.__dict__,
                      "You must define a class called Country in week3.py.")
        self.assertIsInstance(week3.Country, type, "Country is not a class!")

    def _initializer_test_helper(self, args):
        try:
            country = week3.Country(args["name"], args["population"],
                                    args["area"])
        except TypeError:
            country = None

        self.assertIsNotNone(country,
                             "You must define an initializer on Country that "
                             "takes name, population, and area as arguments.")

        for var in args:
            self.assertIn(var, country.__dict__,
                          "The initializer for Country must initialize member "
                          f"variable {var}.")
            self.assertEqual(country.__dict__[var], args[var],
                             f"The initializer for Country must initialize "
                             f"member variable {var} to the provided "
                             f"value.")

    def test_3_initializer(self):
        """Test that the Country initializer functions properly."""
        arg_sets = [{"name": "test country",
                     "population": 1000,
                     "area": 200001},
                    {"name": "another test country",
                     "population": 100234530,
                     "area": 200034501}]
        for args in arg_sets:
            self._initializer_test_helper(args)

    def _init_countries(self):
        return [week3.Country("Kingdom of Awesome", 10, 2),
                week3.Country("Beautiful Land", 1, 10),
                week3.Country("Chromeria", 1000, 1)]

    def test_4_is_larger(self):
        """Test that the is_larger method functions properly."""
        self.assertIn("is_larger", week3.Country.__dict__,
                      "Country must define a method 'is_larger'.")
        countries = self._init_countries()
        self.assertTrue(countries[0].is_larger(countries[2]),
                        "Country.is_larger must return True if the calling "
                        "Country is larger than the provided Country.")
        self.assertFalse(countries[0].is_larger(countries[0]),
                         "Country.is_larger must return False if the calling "
                         "Country is not larger than the provided Country.")
        self.assertFalse(countries[0].is_larger(countries[1]),
                         "Country.is_larger must return False if the calling "
                         "Country is not larger than the provided Country.")

    def test_5_population_density(self):
        """Test that the population_density method functions properly."""
        self.assertIn("population_density", week3.Country.__dict__,
                      "Country must define a method 'population_density'.")
        countries = self._init_countries()
        for country in countries:
            self.assertEqual(country.population_density(),
                             country.population / country.area,
                             "Country.population_density must return the "
                             "population density of the calling Country.")

    def test_6_summary(self):
        """Test the the summary method functions properly."""
        countries = self._init_countries()
        self.assertIn("summary", week3.Country.__dict__,
                      "Country must define a method 'summary'.")
        expected_results = """\
Kingdom of Awesome has a population of 10 people and is 2 square km. \
It therefore has a population density of 5.0000 people per square km.
Beautiful Land has a population of 1 people and is 10 square km. \
It therefore has a population density of 0.1000 people per square km.
Chromeria has a population of 1000 people and is 1 square km. \
It therefore has a population density of 1000.0000 people per square km."""
        for country, expected_result in zip(countries,
                                            expected_results.split("\n")):
            summary = country.summary()
            self.assertEqual(summary, expected_result,
                             f"Calling summary on '{country.name}' returned "
                             f"'{summary}', but "
                             f"should return '{expected_result}')")

    def test_7_style(self):
        """Run the linter and check that the header is there."""
        try:
            from flake8.api import legacy as flake8
            # noqa on the following since just importing to test installed
            import pep8ext_naming  # noqa
            import flake8_docstrings  # noqa
            print("\nLinting Code...\n" + "=" * 15)

            style_guide = flake8.get_style_guide()

            report = style_guide.check_files(STUDENT_CODE)

            self.assertEqual(report.total_errors, 0,
                             "You should fix all linting errors "
                             "before submission in order to receive full "
                             "credit!")

            for module in STUDENT_CODE:
                self.check_header(module)

            print("Passing linter tests!")

        except ImportError:
            print("""
### WARNING: Unable to import flake8 and/or extensions, so cannot \
properly lint your code. ###

Please install flake8, pep8-naming, and flake8-docstrings to auto-check \
whether you are adhering to proper style and docstring conventions.

To install, run:

pip install flake8 pep8-naming flake8-docstrings

""")

    def check_header(self, module):
        """Check the header of the given module."""
        docstring = sys.modules[module[:-3]].__doc__
        for check in ['Author:', 'Class:', 'Assignment:',
                      'Certification of Authenticity:']:
            self.assertIn(check, docstring,
                          "Missing '{}' in {}'s docstring".format(
                            check, module))


if __name__ == '__main__':
    unittest.main(failfast=True)
