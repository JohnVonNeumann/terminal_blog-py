import uuid
import datetime
from database import Database


class Blog(object):

    def __init__(self, title, author, date_created=datetime.datetime.utcnow(), blog_id=None):
        self.blog_id = uuid.uuid3(uuid.NAMESPACE_DNS, author).hex if blog_id is None else blog_id
        self.title = title
        self.author = author
        self.date_created = date_created
