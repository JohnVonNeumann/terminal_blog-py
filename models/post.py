import uuid
import datetime
from database import Database


class Post(object):

    # allows us to build a new Post object
    # usage: post = Post(title="blah", content="text", author="hp")
    def __init__(self, title, content, author, blog_id=None, date_created=datetime.datetime.utcnow(), post_id=None):
        self.blog_id = uuid.uuid3(uuid.NAMESPACE_DNS, author).hex if blog_id is None else blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date_created
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    # inserts posts into mongo collection in json format
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
            'date_created': self.date_created,
            'post_id': self.post_id
        }

    @staticmethod
    # go into db with id param, search thru id's for param
    def from_mongo(cls, post_id):
        post_data = Database.find_one(collection='posts', query={'post_id': post_id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['date_created'],
                   post_id=post_data['post_id'])

    @staticmethod
    # go into db with id param, search thru blog_id for param
    def from_blog(blog_id):
        return [blog for blog in Database.find(collection='posts', query={'blog_id': blog_id})]
