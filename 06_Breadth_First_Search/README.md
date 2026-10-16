# Practical 6: Implement Breadth-First Search (BFS) to find the shortest path in a graph

## Assignment
Experiment 6: Implement a graph traversal algorithm using Breadth-First Search (BFS) in Prolog to find the shortest path between two nodes.

## Aim and concept
BFS expands the earliest enqueued path first. On an unweighted graph it finds a path with the fewest edges. Nodes are marked seen when enqueued, preventing repeated expansion and cycles.

## Algorithm
1. Put the start path in a FIFO queue.
2. Remove the oldest path.
3. Return if its last node is the goal.
4. Enqueue paths extended to unseen neighbors.
5. Fail when the queue is empty.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- bfs(a,g,P).
P = [a,b,d,g].
?- bfs(a,a,P).
P = [a].
?- bfs(g,a,P).
false.
```

## Result
A shortest path from a to g has three edges. Cycles do not cause infinite traversal.

## Assumptions and limitations
Edges are directed and unweighted. For undirected graphs add reverse edges. The list-based queue is simple for teaching; repeated append and list membership make it slower than an optimized queue/set implementation.
