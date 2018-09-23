from blog import Blog


blogs = dict() # blog_name: Blog object


def menu():
    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


if __name__ == '__main__':
    print_blogs()
