 # Program dari client webservice yang akan membaca saham dari telkom dari NYSE
 #   Menggunakan library Suds dan ElementTree
 #                                                25-Mei-20


import suds
import xml.etree.ElementTree as ET

url = 'http://www.webservicex.net/stockquote.asmx?WSDL'
client=suds.client.Client(url)
xmlstr=client.service.GetQuote('TLK')
xmlroot=ET.fromstring(xmlstr)
print 'Name\t\t\t\t',xmlroot.find('Stock/Name').text
print 'Symbol\t\t\t\t',xmlroot.find('Stock/Symbol').text
print 'Last\t\t\t\t',xmlroot.find('Stock/Last').text
print 'Date\t\t\t\t',xmlroot.find('Stock/Date').text
print 'Time\t\t\t\t',xmlroot.find('Stock/Time').text
print 'Change\t\t\t\t',xmlroot.find('Stock/Change').text
print 'Open\t\t\t\t',xmlroot.find('Stock/Open').text
print 'High\t\t\t\t',xmlroot.find('Stock/High').text
print 'Low\t\t\t\t\t',xmlroot.find('Stock/Low').text
print 'Volume\t\t\t\t',xmlroot.find('Stock/Volume').text
print 'MktCap\t\t\t\t',xmlroot.find('Stock/MktCap').text
print 'PreviousClose\t\t',xmlroot.find('Stock/PreviousClose').text
print 'PercentageChange\t',xmlroot.find('Stock/PercentageChange').text
print 'Earns\t\t\t\t',xmlroot.find('Stock/Earns').text
