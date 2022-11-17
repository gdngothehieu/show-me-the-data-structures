# Explanation Problem 6

## Union and Intersection

I made use of our Node and Linkedlist classes implemented in our course to build out unions and intersections. I added an append function to chain elements of a list into a linked list. I created a to_list() function to convert a linked_list to list. Doing so allowed me to combine lists based off of unions and intersection. And then transforming them back into linked lists. 

I iterated through linked list and appended elements to these lists using while and for loops. 


    Time Complexity

        Chain Iteration using While loop - > O(n) 
        Append -> O(n)
        while -> append -> O(n^2)
            Example: 

            for i in py_f_list:
                intersection_list.append(i)


        set -> O(1)

    Problem is of time complexity O(n^2)

    Data Structures

        Using Node, linked list, and Python Lists.

    Space Complexity

        Appending elements to a linked list (size is variable) -> O(n)