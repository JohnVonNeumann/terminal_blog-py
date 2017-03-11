import uuid

class Post(object):

    # allows us to build a new Post object
    def __init__(self, blog_id, title, content, author, date, id):
        self.blog_id = uuid.uuid1() #randomises using host and time
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid1()

    # Database not setup yet, coming soon
    def save_to_mongo(self):
        Database.insert(collection = 'posts',
                        data = self.json())

    # convert to json for mongo db
    def json(self):
        return {
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': date,
            'id': self.id
        }

    @staticmethod
    # go into db with id param, search thru id's for param
    def from_mongo(id):
        return Database.find_one(collection='posts', query={'id': id})

    @staticmethod
    # go into db with id param, search thru blog_id for param
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]




