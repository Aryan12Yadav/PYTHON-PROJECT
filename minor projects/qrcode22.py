import qrcode as qr  # qr is alias name or pet name
  
# img = qr.make('https://www.youtube.com/watch?v=FtJRfsJgtYI&t=1691s')
# img.save('r2haryan.png')
from PIL import Image
# img = Image.open('r2haryan.png')
# img.show()



class my_qr:

    def __init__(self,url):
        self.__my_url = url

    def img_make(self):
        self.img = qr.make(self.__my_url)

class saved(my_qr):

    def save_qr(self):
        self.img_make()
        self.img.save('r2h_aryan.png')
        return self.open()
        

    def open(self):
        self.image = Image.open('r2h_aryan.png')
        return self.image.show()
         


 
link = 'https://www.youtube.com/watch?v=FtJRfsJgtYI&t=1691s'

obj = saved(link)
obj.save_qr()



 
 


