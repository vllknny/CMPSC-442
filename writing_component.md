# Q1.2

The solution path for DFS is 11 and the number of node expansions are 11. 

# Q2.2

When running UCS with cost model A, the total cost is 23 and the number of node expansions are 14. The solution path is: 

3, 3, 0, 0, L
3, 1, 0, 2, R
3, 2, 0, 1, L
3, 0, 0, 3, R
3, 1, 0, 2, L
1, 1, 2, 2, R
2, 2, 1, 1, L
0, 2, 3, 1, R
0, 3, 3, 0, L
0, 1, 3, 2, R
0, 2, 3, 1, L
0, 0, 3, 3, R

But when running wth cost model B, the total cost is 17 and the number of node expansions are 14. The solution path is: 

3, 3, 0, 0, L
2, 2, 1, 1, R
3, 2, 0, 1, L
3, 0, 0, 3, R
3, 1, 0, 2, L
1, 1, 2, 2, R
2, 2, 1, 1, L
0, 2, 3, 1, R
0, 3, 3, 0, L
0, 1, 3, 2, R
0, 2, 3, 1, L
0, 0, 3, 3, R

