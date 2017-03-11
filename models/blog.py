import uuid
import datetime
from models.post import Post
from database import Database


class Blog(object):

    def __init__(self, author, title, description, blog_id=None):
        self.author = author
        self.title = title
        self.description = description
        self.blog_id = uuid.uuid(uuid.NAMESPACE_DNS, author).hex if blog_id is None else blog_id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYY): ")
        post = Post(blog_id=self.blog_id,
                    title=title,
                    content=content,
                    author=self.author,
                    date_created=datetime.datetime.strptime(date, "%d%m%Y"))  #string parse time
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.blog_id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return{
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'blog_id': self.blog_id
        }

    @staticmethod
    def get_from_mongo(cls, blog_id):
        blog_data = Database.find_one(collection="blogs",
                                      query={'blog_id': blog_id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   blog_id=blog_data['blog_id'])
