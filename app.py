from models.post import Post
from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(author="Jose",
            title="Sample title",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

blog.get_posts()
# More ways of doing the same thing:
# ----------------------------------
#
# students = [each['mark'] for each in collection.find({})]
# print(students)
#
#            OR
#
# students = collection.find({})
# student_list = []
# for student in students:
#     student_list.append(student)
#
#             OR
#
# students = collection.find({})
# for each in students:
#     print(each)
