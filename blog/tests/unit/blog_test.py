from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test by Test Author (0 posts)', b.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test by Test Author (0 posts)', b.__repr__())
        b.posts = ['test']
        self.assertEqual('Test by Test Author (1 post)', b.__repr__())
        b2 = Blog('Test', 'Test Author')
        b2.posts = [1, 2]
        self.assertEqual('Test by Test Author (2 posts)', b2.__repr__())

