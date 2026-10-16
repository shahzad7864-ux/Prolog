# Practical 12: Solve the N-Queens problem using backtracking to satisfy CSP constraints

## Assignment
Experiment 12: Implement the N-Queens problem in Prolog using backtracking, ensuring no two queens attack each other.

## Aim and concept
Place one queen per row. Selecting from unused columns prevents column conflicts. A pair of queens attacks diagonally when the absolute column difference equals their row distance.

## Algorithm
1. Create available columns 1 through N.
2. Pick an unused column for the next row.
3. Check its diagonals against previous rows.
4. Recurse or backtrack until all rows are assigned.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- n_queens(4,Q).
Q = [2,4,1,3] ; Q = [3,1,4,2].
?- n_queens(2,_).
false.
?- findall(Q,n_queens(8,Q),Qs), length(Qs,Count).
Count = 92.
?- once(n_queens(4,Q)), print_board(Q).
. Q . .
. . . Q
Q . . .
. . Q .
Q = [2,4,1,3].
```

## Result
Backtracking finds valid N-Queens arrangements; N=4 has two solutions and N=8 has 92 when rotations/reflections are counted separately.

## Assumptions and limitations
N must be a bound integer ≥1. N=2 and N=3 have no solutions. The basic backtracking method becomes expensive for large N. The list contains columns in increasing row order.
