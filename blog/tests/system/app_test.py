from unittest import TestCase, TestLoader, TextTestRunner
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')


suite = TestLoader().loadTestsFromTestCase(AppTest)
testResult = TextTestRunner(verbosity=2).run(suite)
