def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name.title()


print('Enter "q" any time to quit.' )
while True:
    first = input("\nPlease give me a first name: ")
    if first =='q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

formatted_name = get_formatted_name(first, last)
print('\tNeatly formatted name: ' + formatted_name + '.')

import unittest

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'goppa')
        self.assertEqual(formatted_name, 'Janis Goppa')

if __name__ == '__main__':
    unittest.main()