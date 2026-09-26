# Q1.2

The solution path for DFS is 11 and the number of node expansions are 11. 
The solution path for BFS is 11 and the number of node expansions are 14.

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

# Q3.2

(some of the imported latex got messy, sorry!)

a. Let

$$ W(s)=2M_{left}+C_{left}. $$
Heuristic 1
$$ h_1(s)=2M_{left}+C_{left}. $$

This is admissible.

Every missionary still on the left must eventually cross the river and contributes a cost of at least 2. Every cannibal still on the left must eventually cross and contributes a cost of at least 1.
Therefore, regardless of how the crossings are arranged,

$$ h_1(s)=2M_{left}+C_{left} $$

The important point is that h₁ does not account for return trips, so it can underestimate the actual cost. It never overestimates it.

Thus:
h1The intended formula appears to be



$$ h_2(s)= \left\lceil \frac{2M_{left}+C_{left}}{3} \right\rceil. $$

The denominator 3 represents the maximum passenger weight that can theoretically be transported in one trip under the weight interpretation.

Since a boat trip can transport at most 3 units of passenger weight, at least

$$ \left\lceil\frac{2M_{left}+C_{left}}{3}\right\rceil $$

trips are required to transport the remaining weight.

This is a lower bound on the remaining cost, so it cannot overestimate the optimal solution cost.

Therefore:

$$ \boxed{h_2\text{ is admissible}} $$

However, \(h_2\) is substantially less informed than \(h_1\), because it compresses the remaining passenger weight into a number of hypothetical full-capacity trips.

​


b.  Total Cost = 11
    Same 11-Step path for all 3 heuristics
    Node Expansions of 14, 15, and 14 respectively.
    They are all the same cost of UCS.

c. Make a heuristic tighter is easier when recognizing something both \(h_1\) and \(h_2\) ignore:

Some states necessarily require an additional return trip.

Define

$$ h_3(s)= \begin{cases} 0 & \text{if } W(s)=0\\ W(s) & \text{if boat=L and } M_{left}+C_{left}\leq2\\ W(s)+1 & \text{otherwise} \end{cases} $$

Why is \(h_3\) admissible?

Component $$ 2M_{left}+C_{left}, $$ is already an admissable lower bound.
 
If the boat is on the right, but people remain on the left, the boat must eventually make a return trip to the left before those people can be transported. The cheapest possible return trip has cost 1.

Similarly, if the boat is on the left and more than two people remain, one crossing cannot finish the problem because the boat can transport at most two people. Therefore, after at least one forward crossing, another return trip is unavoidable. Again, the minimum possible return-trip cost is 1.

Therefore \(h_3\) never adds more cost than is guaranteed to occur:
so 
$$ h_3(s)\geq h_1(s) $$. So it also dominates.

This gives you a non-max(h1,h2) heuristic.

# 3.3

Consistency requires

$$ h(s)\leq c(s,s')+h(s') $$

for every valid edge.

\(h_1\)

Under Cost Model A, \(h_1\) is consistent.

For a forward trip, some passengers move from the left bank to the right bank. If the passengers have total weight \(w\), then

$$ h_1(s')=h_1(s)-w. $$

The crossing cost is also \(w\), so

$$ c(s,s')+h_1(s') =w+h_1(s)-w =h_1(s). $$

Thus equality holds.

For a return trip, the left-bank weight increases. Therefore

$$ h_1(s')>h_1(s), $$

while \(c(s,s')>0\), making

$$ h_1(s)\leq c(s,s')+h_1(s') $$

automatically true.

Therefore:

$$ \boxed{h_1\text{ is consistent}} $$
\(h_2\)
$$ h_2(s)=\left\lceil\frac{W(s)}3\right\rceil $$

is also consistent under this cost model.

A single crossing can change the remaining weight by at most 3, while the crossing cost is at least the weight of the passengers transported.

For a forward move,

$$ W(s')=W(s)-w $$

where \(w\leq3\).

Thus the ceiling value can decrease by at most 1, while the actual crossing cost is at least 1:

$$ h_2(s)\leq c(s,s')+h_2(s'). $$

For return moves, \(W(s')\geq W(s)\), so the inequality is again satisfied.

Therefore:
2 
Consider a state where the boat is on the right bank and people remain on the left. The additional \(+1\) accounts for the minimum cost of a return trip. After a return trip, the boat is on the left, and the passenger-weight portion of the heuristic increases. Therefore, the consistency inequality is satisfied.

For a forward trip, the passenger-weight portion decreases by the weight of the passengers transported. The cost of that trip is exactly the same passenger weight. The additional \(+1\) can disappear when the resulting state has the boat on the left with at most two people remaining. In that situation, the decrease in \(h_3\) caused by removing the \(+1\) is compensated by the crossing cost.

Therefore, for every valid transition,

$$ h_3(s)\leq c(s,s')+h_3(s'). $$

Thus,
h3
 is consistent