from models.blog import Blog
from database import Database

class Menu(object):

    def __init__ (self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        pass

    def _user_has_account(self):
        Database.find_one('blogs', {'author': self.user}) is not None

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == "R":
            # list blogs in database
            # allow users to pick one
            # display posts
        elif read_or_write == "W":
            # prompt them to write a post
        else:
            print("Thank you for blogging!")


