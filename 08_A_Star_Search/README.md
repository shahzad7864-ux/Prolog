# Practical 8: Implement the A* Search algorithm to find the optimal path using path cost and heuristic estimate

## Assignment
Experiment 8: Implement the A* Search algorithm in Prolog, combining path cost (g) and heuristic estimate (h) to find the optimal path.

## Aim and concept
A* ranks states by f(n)=g(n)+h(n). It stores the cheapest discovered cost for each node, skips stale entries and reopens nodes when a cheaper route is discovered.

## Algorithm
1. Initialize the start with g=0.
2. Pop minimum f.
3. Discard stale entries.
4. Return when the goal is popped.
5. Relax outgoing edges, retaining only cost improvements.
6. Re-sort the frontier.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- astar(s,g,P,C).
P = [s,b,c,g], C = 5.
?- astar(g,g,P,C).
P = [g], C = 0.
```

## Result
A* finds cost 5 on the same graph where Greedy returns cost 10. The expansion sequence is s, a, b, c, g.

## Assumptions and limitations
The supplied heuristic is admissible and consistent for goal g, and edge costs are nonnegative. These conditions justify optimality here. h(s)=4 ≤ true cost 5; h(a)=1 ≤ 8; h(b)=3 = 3; h(c)=2 = 2. Do not reuse these heuristic values for a different goal.
