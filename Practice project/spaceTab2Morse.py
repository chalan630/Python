'''
@Descripttion: 空格和制表符转摩尔斯密码
@Author: chalan630
@Date: 2020-03-07 10:41:57
@LastEditTime: 2020-03-09 17:33:06
'''

dict = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---':'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.'
}

def hex_to_str(str_):
    flag = ''
    for i in range(0, len(str_), 2):
        flag += chr(int(str_[i:i+2], 16))
    return flag

str1 = '  	 		 	  	 			   	 			   	 			   	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 		 	  	 			   	 		 	  	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 			   	 		 	  	 		 	  	 		 	  	 		 	  	       	 		 	  	 			   	 			   	 			   	 			   	       	 		 	  	 		 	  	 			   	 			   	 			   	       	 		 	  	 		 	  	 			   	 			   	 			   	       	 		 	  	 			   	 			   	 			   	       	 			   	 			   	 			   	 			   	 		 	  	       	 		 	  	 			   	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 			   	 			   	 			   	 			   	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 		 	  	 		 	  	 			   	 			   	 			   	       	 			   	 			   	 			   	 			   	 		 	  	       	 		 	  	 			   	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 			   	 			   	 			   	 			   	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 			   	       	 		 	  	 			   	 			   	 			   	 			   	       	 		 	  	 		 	  	 			   	 			   	 			   	       	 			   	 			   	 			   	 			   	 		 	  	       	 			   	 			   	 			   	 			   	 		 	  	       	 		 	  	 			   	 			   	 			   	 			   	       	 			   	 		 	  	 		 	  	 		 	  	 		 	  	       	 		 	  	 		 	  	 			   	 			   	 			   	       	 		 	  	 			   	 			 '
temp = ''
# print('StrLn=',len(str1))
for i in str1:
    if ord(i) == 32:
        temp += '0'
    elif ord(i) == 9:
        temp += '1'

int_ = temp
str_= "".join([chr(int(int_[i:i+8], 2)) for i in range(0, len(int_), 8)])
list_ = str_.split(' ')
flag = ''
for item in list_:
    flag += (dict[item])

print(hex_to_str(flag))