# Practical 9: Implement Hill Climbing for optimization problems

## Assignment
Experiment 9: Implement the Hill Climbing Algorithm to find the optimum solution for a numerical optimization problem.

## Aim and concept
Hill climbing moves to the best adjacent state only when its value is strictly better. This finite one-dimensional objective has a local maximum at x=2 and a global maximum at x=8.

## Algorithm
1. Start at a valid integer x.
2. Evaluate x−1 and x+1 within the domain.
3. Move to the highest-scoring neighbor if it improves the score.
4. Stop otherwise.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- hill_climb(0,X,V,T).
X = 2, V = 6, T = [0,1,2].
?- hill_climb(5,X,V,T).
X = 8, V = 12, T = [5,6,7,8].
```

## Result
From 0, hill climbing stops at the local maximum 2. Starting at 5 reaches the global maximum 8.

## Assumptions and limitations
The numeric objective is an explicitly tabulated function, not a real dataset. Strict improvement guarantees termination on this finite domain, but not global optimality. Ties choose the larger x due to term sorting.
