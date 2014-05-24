from ladon.ladonizer import ladonize
import hashlib

class Server(object):
        @ladonize(int,int,rtype=int)
        def add(self,a,b):
                return a+b
        
        @ladonize(str, rtype=str)
        def md5(self,plaintext):
            m=hashlib.md5()
            m.update(plaintext)
            return m.hexdigest()
        
        @ladonize(str, rtype=str)
        def sha1(self,plaintext):
            m=hashlib.sha1()
            m.update(plaintext)
            return m.hexdigest()
        
        @ladonize(str, rtype=str)
        def sha224(self,plaintext):
            m=hashlib.sha224()
            m.update(plaintext)
            return m.hexdigest()
        
        @ladonize(str, rtype=str)
        def sha256(self,plaintext):
            m=hashlib.sha224()
            m.update(plaintext)
            return m.hexdigest()
        
        @ladonize(str, rtype=str)
        def sha384(self,plaintext):
            m=hashlib.sha224()
            m.update(plaintext)
            return m.hexdigest()
        
        @ladonize(str, rtype=str)
        def sha512(self,plaintext):
            m=hashlib.sha224()
            m.update(plaintext)
            return m.hexdigest()
        