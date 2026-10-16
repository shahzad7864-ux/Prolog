# Practical 10: Solve an optimization problem using Simulated Annealing to escape local optima

## Assignment
Experiment 10: Implement Simulated Annealing in Prolog and compare its ability to escape local optima against plain Hill Climbing.

## Aim and concept
Simulated annealing can accept a downhill move with probability exp((new−current)/T) for maximization. High temperature favors exploration; cooling reduces that probability. The best visited state is retained separately from the current state.

## Algorithm
1. Use the same landscape and start as Practical 9.
2. Pick a random neighbor.
3. Always accept an equal/better candidate; probabilistically accept a worse one.
4. Update the best visited state.
5. Cool by 0.99 and stop after 500 moves.
6. Compare five seeded runs with hill climbing.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- hill_climb(0,X,V,_).
X = 2, V = 6.
?- anneal(0,42,B,V,Trace), length(Trace,N).
% N = 501. B and V depend on the pseudo-random run.
% Global best, if reached: B = 8, V = 12.
?- compare.
% Prints hill-climbing result followed by five measured seeded runs.
```

## Result
Annealing can cross the valley at x=3 and x=4 to escape x=2. Use compare/0 to observe actual run outcomes; no stochastic success is guaranteed.

## Assumptions and limitations
Fixed seeds aid reproducibility within a runtime, but outputs may differ across versions. The trace includes rejected steps as repeated states. The reported result is the best visited point, not necessarily the final point. The finite budget does not prove global optimality.
