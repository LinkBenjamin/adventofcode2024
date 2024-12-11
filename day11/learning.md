Today I learned about caching in recursive functions.  

This problem looked so easy at first.  I got the first star in just a few minutes.  Then the second part just said "up the iteration count to 75"... and I had a mess on my hands.

I was out of ideas on how to make my program run faster and saw a note that suggested using lrucache on the recursive function to reduce the number of duplicated computations.  I added that and poof, everything ran in less than a second.