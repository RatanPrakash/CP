class CloudxLab:
    def process(self):
        print("Process is Running")

class User(CloudxLab):
    def process(a=10):
        print(1)
    
    def process(self):
        print(2)

# Create an instance of User
obj = User()

# Call the process method
obj.process()