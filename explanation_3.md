# Explanation Problem 3

## Hufman Coding


I used a mini-heap instead of a list to create a priority queue. Mini-heaps are faster than lists and easier to use as priority queues. I also made use of dictionary class to store characters, frequencies, and bit values.

    Time Complexity

        heappop - Pop and return the smallest item from the heap O(1)

        heappush/complexity of inserting into a heap - Push the value item on the heap tree. Newly inserted node has to be swapped at each levelfrom bottom up. Heap is a complete binary tree which is O(log(n))

        For Loops and Recursions - O(n)

    Space Complexity
        Inserting into a heap and sorting - O(N)



