import unittest
from code import CodeRepository

class TestCodeRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CodeRepository()

    def test_runExtension(self):
        self.repository.run("incoming")

    def test_runRawCommand(self):
        self.repository.run("status")

if __name__ == "__main__": #pragma: no cover
    unittest.main()
