import datetime
class Member :
    def __init__(self, name, age,id=0):
        self.name=name
        self.age=age
        self.id=id
        self.posts=[]

    def __str__(self):
        return self.name





class Post :
    def __init__(self, title, content, member_id=0):
        self.id = 0
        self.title = title
        self.content = content
        self.member_id = member_id
        self.date = datetime.datetime.now()
        self.id=0

    def __str__(self):
        return self.title
