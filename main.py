import re
def Main():
	key=input("Nhập key của bạn vào đây:")
	steamkeyregex=re.match('[a-zA-Z0-9]{4,6}\-?[a-zA-Z0-9]{4,6}\-?[a-zA-Z0-9]{4,6}', key)
	if steamkeyregex is None:
	  
	  print("Key không hợp lệ")
	  
	else:
	  
	  print("Key hợp lệ")
	  
Main()
