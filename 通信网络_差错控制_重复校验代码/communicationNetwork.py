'''
This program is for free
'''

def str_2_bin(str):
    """
    字符串转换为二进制
    """
    return ' '.join([bin(ord(c)).replace('0b', '') for c in str])
def bin_2_str(bin):
    """
    二进制转换为字符串
    """
    return ''.join([chr(i) for i in [int(b, 2) for b in bin.split(' ')]])
    return temp
def Coding(str):
    temp = ''.join([bin(ord(c)).replace('b', '') for c in str])
    return ''+temp
def Decoding(bin):

    return ''.join([chr(i) for i in [int(b, 2) for b in bin.split(' ')]])

longstr ='''whatever you want to type''' #请在这里输入你的文本
'''
以下是编码过程：
'''
storingArr = []
temp = Coding(longstr)
print('编码后的二进制流为：')
print(temp.replace(' ',''))
for i in range(len(temp)):
    if (temp[i] == '0'):
        for j in range(3):
            storingArr.append('0')
    else:
        for n in range(3):
            storingArr.append('1')

errorControlArr ="" .join (storingArr)
print('差错控制的二进制流为：')
print(errorControlArr)      #这里得到的是差错控制的二进制流（不包含任何heading和ending！请自己根据情况加）

'''
以下是解码过程（摸了，摸了，真有需要我再写吧.)
zeroCount = 0
oneCount = 0
decodingArr = ''''''
storingArrsec = []
for i in range(len(temp)):
        for j in range(3):
            if (decodingArr[i+j] == 0):
                zeroCount = zeroCount + 1
            else:
                oneCount = oneCount + 1

            if (oneCount > zeroCount):
                 storingArrsec.append(1)
            else:
                 storingArrsec.append(0)
        zeroCount = 0
        oneCount  = 0
print(storingArrsec)
'''




