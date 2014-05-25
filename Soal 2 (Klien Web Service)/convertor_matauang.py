 # Program dari client webservice yang akan mengconvert mata uang
 # darihttp://www.webservicex.net/CurrencyConvertor.asmx?op=ConversionRate
 # Menggunakan library Suds dan ElementTree
 #                                                25-Mei-20

 # Program dari client webservice yang akan membaca saham dari telkom dari NYSE
 #   Menggunakan library Suds dan ElementTree
 #                                                25-Mei-20


import suds
import xml.etree.ElementTree as ET

url = 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
client=suds.client.Client(url)
currency=['IDR','USD','MYR','GBP',]
print '======== Program konversi mata uang =========='
print ' == Opsi mata uang \t\t\t: ',
for c in currency:
    print c,
print
from_curr=raw_input('pilih mata uang asal \t\t: ')
from_val=raw_input('masukkan nilai mata uang  \t: ')
to_curr=raw_input('pilih mata uang tujuan \t\t: ')

datum=client.service.ConversionRate(from_curr,to_curr)

print 'hasil \t\t\t\t\t\t:  ',from_curr,' = ','{:2,.2f}'.format(float(from_val))
print '\t\t\t\t\t\t\t\t',to_curr,' = ','{:2,.2f}'.format(float(datum)*float(from_val))