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
    else:
        str1 = 'quickLookItem'
        totalItem = body.count(str1)
        print 'total relevent search item :', totalItem


    return

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
    else:
        str1 = 'quickLookItem'
        totalItem = body.count(str1)
        print 'total relevent search item :', totalItem

    return

itemCount('macbook');
itemCountPageWise('apple','4')


