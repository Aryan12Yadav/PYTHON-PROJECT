# verify email id's 

class aryan_mail:

    def __init__(self,id):
        self.id = id
        

    def check_mail_id(self,inp_user):
        
        self.user = inp_user
        
        self.b = self.user[-1:-11:-1]
      
  
        if self.b[::-1] == '@gmail.com':
            if len(self.user)>=16:
                if  (self.user.count('@')==1):
                    if self.user.islower() == True :
                        
                        if '!#$%&' or '*+-/=?^_`{|}~' in self.user == True:     
                                                        
                                if self.user[0].isdigit() == False:
                                    
                                    return 'valid email' 
                                                               
                                return "invalid email  8"
                                                                  
                        else:
                            return 'invalid email 6'                           
                        

                    else:
                        return 'invalid input 4'

                else:
                    return 'invalid email 3'

            else:
                return "invalid email 2"
                
        else:
            return "invalid input 1 "


obj = aryan_mail('aryan')
a = "enter your email id"
while a!='stop':
    a = input('\n\n\n\n\nenter the your email id ')
    if a != 'stop':
        print(obj.check_mail_id(a)) 


# print(obj.check_mail_id('aryanyadav@gmail.com'))