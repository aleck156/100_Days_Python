class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def __str__(self):
        return f"Hi, my name is {self.username} and my ID number is {self.id}\nI have {self.followers} followers and I\'m following {self.following} other users"


    def followers(self, followers):
        self.followers = followers

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'Anderson Thomas')
user_2 = User('002', 'Michael Moore')

user_2.follow(user_1)


print(user_1)
print(user_2)