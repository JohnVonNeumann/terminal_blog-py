import uuid
import datetime
from models.blog import Blog
from database import Database


class Post(Blog):

    # allows us to build a new Post object
    # usage: post = Post(title="blah", content="text", author="hp")
    def __init__(self, post_title, content, author, blog_id=Blog.blog_id, date_created_post=datetime.datetime.utcnow(), post_id=None):
        Blog.__init__(self, blog_title, author, blog_id=None)
        self.post_title = post_title
        self.content = content
        self.date_created_post = date_created_post
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    # inserts posts into mongo collection in json format
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    @staticmethod
    # go into db with id param, search thru id's for param
    def from_mongo(post_id):
        return Database.find_one(collection='posts', query={'post_id': post_id})