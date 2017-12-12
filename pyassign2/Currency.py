"""Currency.py: Calculation of currency exchange.

__author__ = "LiXianghao"
__pkuid__  = "1700011711"
__email__  = "1700011711@pku.edu.cn"
"""

from urllib.request import urlopen
def exchange(cur_from, cur_to, amount_from):        #the exchange function
    a = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+str(cur_from)+'&to='+str(cur_to)+'&amt='+str(amount_from)+''
    doc = urlopen(a)        #use the function of calculation
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    l = jstr.split()
    num = l[9]        #cut off the number part from the original URL
    num = num.replace('"','')
    return float(num)

def main():        #main function
    cur_from = input('From which currency:')
    cur_to = input('Into which currency:')
    amount_from = input('Amount of money before calculation:')
    result = exchange(cur_from,cur_to,amount_from)
    return result

def test_input(cur_from,cur_to,amount_from):        #test function of input
    assert(len(cur_from)==3)
    assert(len(cur_to)==3)
    assert(cur_from.isalpha())
    assert(cur_to.isalpha())
    assert(float(amount_from)>0)
    print("test_input pass")

def test_output(cur_from,cur_to,amount_from):        #test function of output
    amount_to=exchange(cur_from,cur_to,amount_from)
    assert(type(amount_to)==float)
    print("test_output pass")

def testAll():        #test function of all
    cur_from=input('From which currency:')        #test of cur_from
    cur_to=input('Into which currency:')        #test of cur_to
    amount_from=input('Amount of money before calculation:')        #test of amount_from
    test_input(cur_from,cur_to,amount_from)
    test_output(cur_from,cur_to,amount_from)
    print("All tests passed")

if __name__ == '__main__':
    print('The result is',main())
testAll()
