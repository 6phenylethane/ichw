currency_from = input()  
currency_to = input()  
amount_from = input()  
'''输入两个货币缩写名称，和要兑换的货币数量'''  
  
def exchange(currency_from, currency_to, amount_from):  
    '''定义一个函数可以实现汇率转化计算'''  
  
    '''访问URL并得到正常字符串'''  
    from urllib.request import urlopen  
    web = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from  
    doc = urlopen(web)  
    docstr = doc.read()  
    doc.close()  
    jstr = docstr.decode('ascii')  
    '''用str方法提取数字'''  
    a_list = jstr.split('"')  
    b_list = a_list[7].split(' ')  
    return b_list[0]  
  
def test_exchange():  
    '''测试函数'''  
    assert('13.7042' == exchange('USD', 'CNY', '2.0'))  
    assert('257.99675532586' == exchange('EUR', 'JPY', '2.0'))  
    assert('5.5049602355823' == exchange('KWD', 'KYD', '2.0'))  
  
def test_ALL():  
    '''调用测试函数'''  
    test_exchange()  
    print("All tests passed")  
  
def main():  
    print(exchange(currency_from, currency_to, amount_from))  
    test_ALL()  
if __name__ == '__main__':  
    main()  
