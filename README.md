# Facebook Puzzle 
## The house robber

> You are trying to rob houses on a street. Each house has some amount of cash. Your goal is to rob houses such that you maximize the total robbed amount. The constraint is once you rob a house you cannot rob a house adjacent to that house.

> [Source](http://designtaxi.com/news/380581/The-Toughest-Job-Interview-Questions-Asked-By-Facebook-Will-Puzzle-You/)


To find out the maximum amount of money you can rob this solution uses the dynamic programming technique. 

Let A(i) be the amount of money at the i-th house and M(i) the maximum amount of money possible to obtain considering the first _i_ houses.
- M(0)=0
- M(1)=A(1)
- M(i)=max(M(i−2)+A(i), M(i−1)) 

The maximum amount for the whole _n_ houses corresponds to M(n).

Usage example
--------------
```
python fb_house_robber.py -i 20,18,16,14,12,10,4,1,5,9,3,2,7,8,6,11,15,17,19,13
```

Example Output:
```
Best rob: 112
```