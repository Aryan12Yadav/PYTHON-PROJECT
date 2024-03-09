#  quick response code (QR) to store the information inside the code code 


import qrcode
code = qrcode.QRCode( # QRCode is a class in the module qrcode
    version = 15,
    box_size = 10,
    border = 5
)

data ='https://bard.google.com/chat/9d2e429a8e6642d2'
code.add_data(data)      # these are method of QRCode class
code.make(fit = True)
img = code.make_image(fill = 'blakc',back_color = 'white')
img.save('qrcode.png')