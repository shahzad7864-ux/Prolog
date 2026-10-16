# Practical 7: Implement Greedy Best-First Search using a heuristic function to find a path in a graph

## Assignment
Experiment 7: Implement Greedy Best-First Search in Prolog, using a heuristic function to guide node expansion toward the goal.

## Aim and concept
Greedy Best-First Search prioritizes the smallest heuristic h(n), ignoring accumulated cost when choosing what to expand. Cost is tracked only to report the resulting route.

## Algorithm
1. Add the start state with priority h(start).
2. Remove the lowest-priority state.
3. Stop at g, or expand unclosed successors.
4. Sort the frontier by heuristic and repeat.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- greedy(s,g,P,C).
P = [s,a,g], C = 10.
?- greedy(g,g,P,C).
P = [g], C = 0.
```

## Result
Greedy chooses a because h(a)=1 is lower than h(b)=3; it returns cost 10 although a cost-5 route exists.

## Assumptions and limitations
The heuristic is defined for goal g only. Greedy is not guaranteed optimal, even with an admissible heuristic. Edges and heuristic values are illustrative. Each node is expanded at most once; an empty frontier fails.
