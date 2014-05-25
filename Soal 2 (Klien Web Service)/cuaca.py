'''
Created on May 25, 2014

@author: Prana Pratistha
'''
import suds
import xml.etree.ElementTree as ET

print ('Nama kota hanya ibukota dari suatu negara')
kota = raw_input('Nama kota : ')
negara = raw_input('Nama negara : ')
url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
client=suds.client.Client(url)
xml=client.service.GetWeather(kota,negara)
#print xml
xml=xml.encode('utf16')
parse=ET.fromstring(xml)
print 'Lokasi\t\t\t',parse.find('Location').text
print 'Waktu\t\t\t',parse.find('Time').text
print 'Angin\t\t\t',parse.find('Wind').text
print 'Pengelihatan\t\t',parse.find('Visibility').text
print 'Keadaan Cuaca\t\t',parse.find('SkyConditions').text
print 'Suhu Tinggi\t\t',parse.find('Temperature').text
print 'Suhu Rendah\t\t',parse.find('DewPoint').text
print 'Kelembaban\t\t',parse.find('RelativeHumidity').text
print 'Tekanan\t\t\t',parse.find('Pressure').text