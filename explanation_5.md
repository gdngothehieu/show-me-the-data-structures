# Explanation Problem 5

## Blockchain

I made use of hashlib to create hash values for each block in the chain. I also made use of datetime to record the timestamp of when the block was created.

I followed the hierarchy presented in the problem statement to create a Blockchain. I created my Block Class using node characteristics. I initialized
a blockchain (linked list) as self.head = None. I created an append function inspired from single linked list course material to add blocks to the chain.
Iterating through chain using while loop to add block to end of list as well as saving linked list in Python Array for printing.


    Time Complexity

        Chain Iteration using While loop - > O(n) 

    Data Structures

        Using Node, linked list, and Python Lists.

    Space Complexity
        Blockchain increases in size -> O(n)