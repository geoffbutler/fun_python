from app import App
import unittest

class TestGame(unittest.TestCase):

  def test_can_be_created(self):  
    app = App()

    self.assertTrue(app is not None)


  def test_can_return_false(self):
    result = App.return_false()

    self.assertFalse(result)

  
  def test_can_return_true(self):
    app = App()
    result = app.return_true()

    self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

