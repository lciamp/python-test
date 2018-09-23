from unittest import TestLoader, TextTestRunner

tests = TestLoader().discover('.', pattern="*_test.py")
testResult = TextTestRunner(verbosity=2).run(tests)