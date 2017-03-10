class Post(object):

    # allows us to build a new Post object
    def __init__(self, blog_id, title, content, author, date, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id

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




