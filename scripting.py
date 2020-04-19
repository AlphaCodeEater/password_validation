# import os
# path = "C:/Users/Administrator/Desktop/tests.txt"
# path = os.path.realpath(path)
# os.startfile(path)
from translate import Translator
import pdb

translator = Translator(to_lang = "ko")
try:
	with open('amen1.txt','r',encoding = "UTF-8",errors ="ignore") as my_files:
	  # pdb.set_trace()
	  text = my_files.read()
	  translation = translator.translate(text)
	  # pdb.set_trace()
	  print(translation)
	  with open('./amen1-ja','w',encoding = "UTF-8",errors = "ignore") as jap_file:
	               jap_file.write(translation)
	               
except FileNotFoundError as err:
	print('file not found here bro')
	
except IOError as erwa:
	print('error here')
# 	print('errror iss here')
# my_file.close()
# my_file.seek(0)
# print(my_file.readline())
# my_file.seek(0)
# print(my_file.readline())
