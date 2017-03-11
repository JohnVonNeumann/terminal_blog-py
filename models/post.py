import uuid
import datetime
from database import Database


class Post(object):

    # allows us to build a new Post object
    def __init__(self, title, content, author, blog_id=None, date_created=None, post_id=None):
        self.blog_id = uuid.uuid4().hex if blog_id is None else blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = datetime.date.today() if date_created is None else date_created
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    # Database not setup yet, coming soon.
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    # convert to json for mongo db
    def json(self):
        return {
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created': self.date_created,
            'post_id': self.post_id
        }

    @staticmethod
    # go into db with id param, search thru id's for param
    def from_mongo(post_id):
        return Database.find_one(collection='posts', query={'post_id': post_id})

    @staticmethod
    # go into db with id param, search thru blog_id for param
    def from_blog(post_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': post_id})]
