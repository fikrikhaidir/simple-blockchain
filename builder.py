#!/usr/bin/python3

#required dependencies
import hashlib


#required classes
class Block:
    def __init__(self,index,previous,timestamp,data):
        self.index = index
        self.previous_block = previous
        self.timestamp = timestamp,
        self.data = data
        # print (self.timestamp)
        self.hash = self.create_hash()

    def create_hash(self):

        i = str(self.index)
        p = str(self.previous_block)
        t = str(self.timestamp)
        d = str(self.data)
        print (i,p,t,d)
        body = "{0} {1} {2} {3}".format(str(self.index), str(self.previous_block), str(self.timestamp),str(self.data))
        body = body.encode('utf-8')
        hash = hashlib.sha256(body)
        hash = hash.hexdigest()
        print (hash)
        return hash
