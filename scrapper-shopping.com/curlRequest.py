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
        print 'unable to parse the url'
    else:
        str1 = 'quickLookItem'
        totalItem = body.decode('iso-8859-1').count(str1)
        print 'total relevent search item :', totalItem


    return

itemCount("macbook");

