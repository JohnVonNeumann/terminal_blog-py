import uuid
import datetime
from database import Database


class Blog(object):

    def __init__(self, blog_title, author, date_created=datetime.datetime.utcnow(), blog_id=None):
        self.blog_id = uuid.uuid3(uuid.NAMESPACE_DNS, author).hex if blog_id is None else blog_id
        self.blog_title = blog_title
        self.author = author
        self.date_created = date_created

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
            'created': self.date_created,
            'post_id': self.post_id
        }

    @staticmethod
    # go into db with id param, search thru blog_id for param
    def from_blog(blog_id):
        return [blog for blog in Database.find(collection='posts', query={'blog_id': blog_id})]

