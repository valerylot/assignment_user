class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("Already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Not enough points!")
        return self


#create some user
user1=User("Jane", "Doe", "janedoe@gmail.com", "35")
user2=User("Bob", "Builder", "bob@gmail.com", "45")
user3=User("Kanye", "East", "east@gmail.com", "25")

# print(user1.first_name)
# user1.display_info()

# user1.enroll()
# user1.display_info()

# user1.spend_points(50)
# user1.display_info()

# user2.enroll()
# user2.display_info()

# user2.spend_points(80)
# user2.display_info()

# user1.display_info()
# user2.display_info()
# user3.display_info()

# user3.spend_points(40)
# user3.display_info

user1.display_info().enroll().spend_points(150).display_info()