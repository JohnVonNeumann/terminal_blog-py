__author__ = 'lw'

from models.post import Post

post = Post("trees", "memes", "jeeves")
post2 = Post("things and things", "poetry", "jeeves")


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


