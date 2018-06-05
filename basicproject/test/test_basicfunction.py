import unittest
from basicfunction import BasicFunction

class TestBasicFunction(unittest.TestCase):
  def setUp(self):
    self.func = BasicFunction()

  def test_canary(self):
    self.assertTrue(True)

  def test_default_state(self):
    self.assertEqual(self.func.state, 0)

  def test_increment(self):
    self.func.increment_state()
    self.assertEqual(self.func.state, 1)

  def test_reset(self):
    self.func.increment_state()
    self.func.increment_state()
    self.func.clear_state()
    self.assertEqual(self.func.state, 0)

if __name__ == '__main__':
  unittest.main()
