class User:
    
    def __init__(self,user_id, user_name, followers=0, following=0) -> None:
        print("new user created...")
        self.user_id = user_id
        self.user_name = user_name
        self.followers = followers
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Angela")
user_2 = User("002","Jack")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)