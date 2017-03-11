from models.post import Post
from database import Database

Database.initialize()

posts = Post.from_blog(blog_id="6939757a82fc3149990a9d5843dc7f0a")
for post in posts:
    print(posts)

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
