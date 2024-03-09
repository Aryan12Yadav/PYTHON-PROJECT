import pywhatkit as pw
txt = ''' python is a interpreted high level general purpost programming language.
  Its design emphasize code readibilty with its use of signigiant '''

pw.text_to_handwriting(txt,'aryan.png',[0,0,138])  # text_to_handwriting is a funtion
print('End')