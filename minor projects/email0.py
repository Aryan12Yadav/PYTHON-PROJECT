class aryan_mail:
    def check_mail_id(self, inp_user):
        self.user = inp_user

        # Check for valid email format first
        if not self.user.count("@") == 1 or not self.user.endswith(".com"):
            return "Sorry! You entered an invalid mail id."

        # Check for Gmail address
        if "@gmail.com" in self.user:
            return "Your mail id is valid."
        else:
            return "Sorry! Your mail id is not a Gmail address."

obj = aryan_mail()

# Prompt for email before the loop
a = input("Enter your email id (or 'stop' to quit): ")

# while a != 'stop':
#     print(obj.check_mail_id(a))
#     a = input('\nEnter another email id (or "stop" to quit): ')
