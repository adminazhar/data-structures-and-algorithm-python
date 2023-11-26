class Youtube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers

user1 = Youtube("azhar", 5)

print(user1.username)
print(user1.subscribers)