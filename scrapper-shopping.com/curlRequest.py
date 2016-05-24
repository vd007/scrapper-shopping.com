import sys
import unittest

def itemCount(str):
    import pycurl
    from io import BytesIO

    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://www.shopping.com/macbook/products?CLT=SCH&KW='+str)
    c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue()
    # Body is a byte string.
    # We have to know the encoding in order to print it to a text file
    # such as standard output.
    # print(body.decode('iso-8859-1'))
    if not body.decode('iso-8859-1'):
        print 'Unable to parse the url. Pleases try again.'
	totalItem =0
    else:
        str1 = 'quickLookItem'
        totalItem = body.count(str1)
        print 'total relevent search item :', totalItem


    return totalItem

def itemCountPageWise(str,pageNumber):
    import pycurl
    from io import BytesIO

    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://www.shopping.com/apple/products~PG-'+pageNumber+'?KW='+str)
    c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue()
    # Body is a byte string.
    # We have to know the encoding in order to print it to a text file
    # such as standard output.
    #print(body.decode('iso-8859-1'))
    if not body.decode('iso-8859-1'):
        print 'Unable to parse the url. Pleases try again.'
	totalItem =0 
    else:
        str1 = 'quickLookItem'
        totalItem = body.count(str1)
        print 'total relevent search item :', totalItem

    return totalItem

# variables for verify the test cases.
function1 = itemCount('macbook');
function2 = itemCountPageWise('macbook+pro','4')

#function processing and returing the output as per the args
argLength = len(sys.argv)
if argLength == 2:
	itemCount(sys.argv[1])
elif argLength == 3:
	itemCountPageWise(sys.argv[1],sys.argv[2])
else:
	print 'please provide correct arguement'


############ Test Cases #########33

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(function1, 15)

    def test1(self):
        self.assertEqual(function2, 40)
