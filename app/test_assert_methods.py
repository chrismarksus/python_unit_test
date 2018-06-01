import unittest

class TestAssertMethods(unittest.TestCase):

  def setUp(self):
    self.five = 5
    self.list = ['tim', 'bob', 'sue', 'ann']

  def testForEqual(self):
    self.assertEqual(self.five, 5)

  def testForNotEqual(self):
    self.assertNotEqual(self.five, 10)

  def testForTrue(self):
    self.assertTrue(True)

  def testforFalse(self):
    self.assertFalse(False)

  def testItemInList(self):
    self.assertIn('bob', self.list)

  def testItemNotInList(self):
    self.assertNotIn('ron', self.list)

if __name__ == '__main__':
  unittest.main()
    
