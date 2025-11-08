#represent an community member

class User:
    def __init__(self, name):
        self.name = name

    #represent a post in the community

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content

#manage users, posts and CLI menu

class CommunityApp:
    def __init__(self):
        self.users = {}
        self.posts = []

    #add a new user to the community

    def add_user(self):
        name = input("Enter user name: ").strip()

        if name in self.users:
            print("User already exists.")
        else:
            self.users[name] = User(name)
            print(f"User '{name} created.")

    #create a new post by an existing user

    def create_post(self):
        name = input("Author name: ").strip()
        if name not in self.users:
            print("User not found.")  
            return
        content = input("Post content: ").strip()
        self.posts.append(Post(name, content))    
        print("Post added.")

    #lists all posts in the community

    def list_posts(self):
        if not self.posts:
            print("No posts available.")
        for i, p in enumerate(self.posts, 1):
            print(f"{i}. {p.author}: {p.content}")
        
    #display the main menu and handle choices

    def run(self):
        menu = ("\n1) Add User\n2) Create Post\n3) List Posts\n4) Exit\n Choose: ")
        actions = {"1": self.add_user, "2": self.create_post,
                "3": self.list_posts}
        
        while True:
            choice = input(menu).strip()

            if choice == "4":
                print("Goodbye!")
                break
            actions.get(choice, lambda: print("Invalid choice"))()

#start the community application 

if __name__ == "__main__":
    CommunityApp().run()