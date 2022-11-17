import hashlib
import datetime


#Define Block Class applying node characteristics

class Block:

    def __init__(self, timestamp, data, previous_hash = 0):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      #Link Blocks
      self.next = None

    #Generate hash value
    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = repr(self).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()


    #String representation of Block object. Representation fails with self.hash: AttributeError: 'Block' object has no attribute 'hash'. Not sure why.
    def __repr__(self):
      #   return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") 


class BlockChain:
      #Initialize head of chain
      def __init__(self):
            self.head = None
      

      #Linked List append method
      def append(self, data):

            if data is "" or data is None or type(data) is not str:

                  print("Block with data: '{}' cannot be added to chain, so skipped".format(data))
                  return
                  
            if self.head is None:
                  self.head = Block(datetime.datetime.now(), data)
                  return
            
            
            block = self.head
            previous_hash = block.hash

            while block.next:
                  block = block.next
                  previous_hash = block.hash
            block.next = Block(datetime.datetime.now(), data, previous_hash)
            return

      #Store linked list in Python array and print values
      def to_list(self):
        
        toList = []
        
        block = self.head 
        while block:
            toList.append([block, block.hash])
            block = block.next
        
        return toList


#Test Case 1

print("Blockchain")
blockchain = BlockChain()
blockchain.append("First")
blockchain.append("Second")
blockchain.append("Third")

print(blockchain.to_list()) #[[2021-06-21 08:17:59.126803 | First | 0 | , 'ef4f6f70cae1ae24b51cea92dc1a36bb38da5364293cbc3a323134f679cff12f'], [2021-06-21 08:17:59.126846 | Second | ef4f6f70cae1ae24b51cea92dc1a36bb38da5364293cbc3a323134f679cff12f | , '3a9c0f0c5867484f1ebe0c0b323e2460062231efacb039502e07fb4377fe183b'], [2021-06-21 08:17:59.126858 | Third | 3a9c0f0c5867484f1ebe0c0b323e2460062231efacb039502e07fb4377fe183b | , 'c9496b97dde1b62907d8d952650022b972360f87402f0ce003b723def47287a4']]

#Test Case 2 - Skips block if empty or is of wrong type

print("+++++++++++++++++++++++++++++++++++++++++++++")
print("Blockchain 2")
blockchain2 = BlockChain()
blockchain2.append("Hello World")
blockchain2.append("")
blockchain2.append("Goodbye World")


print(blockchain2.to_list()) #[Block with data: '' cannot be added to chain, so skipped [2021-06-21 08:46:53.809317 | Hello World | 0 | , 'e463c08e44e79980bbbb26952506fe0717379d0ba27d312347e34cfc0d09e755'], [2021-06-21 08:46:53.809329 | Goodbye World | e463c08e44e79980bbbb26952506fe0717379d0ba27d312347e34cfc0d09e755 | , '60eb1e9205cee75160002ed4e599c7c80ef417338f93fb3cf2af51305baa31b1']]


#Test Case 3
print("+++++++++++++++++++++++++++++++++++++++++++++")
print("Blockchain 3")
blockchain3 = BlockChain()
blockchain3.append("")
blockchain3.append("")
blockchain3.append(4)


print(blockchain3.to_list()) #Block with data: '' cannot be added to chain, so skipped. Block with data: '' cannot be added to chain, so skipped. Block with data: '4' cannot be added to chain, so skipped. []

#Edge Case #1
print("+++++++++++++++++++++++++++++++++++++++++++++")
print("Blockchain 4")
blockchain4 = BlockChain()

print(blockchain4.to_list()) #[]

#Edge Case #2
print("+++++++++++++++++++++++++++++++++++++++++++++")
print("Blockchain 5")
blockchain5 = BlockChain()
blockchain5.append("One")
print(blockchain5.head.timestamp) #2021-08-18 08:22:33.950902
blockchain5.append("Two")
print(blockchain5.head.timestamp) #2021-08-18 08:22:33.950902
blockchain5.append("Three")
print(blockchain5.head.timestamp) #2021-08-18 08:22:33.950902

