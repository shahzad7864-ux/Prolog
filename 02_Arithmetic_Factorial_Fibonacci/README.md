# Practical 2: Implement arithmetic operations, Factorial, and Fibonacci Series using recursion

## Assignment
Experiment 2: Implement a Prolog program to demonstrate basic arithmetic operations, finding the Factorial of a number, and generating the Fibonacci series.

## Aim and concept
Recursion reduces a problem to a smaller instance until a base case is reached. Factorial uses N! = N × (N−1)! and 0! = 1. Fibonacci uses F(0)=0, F(1)=1. Accumulators avoid recomputing earlier Fibonacci values.

## Algorithm
1. Evaluate arithmetic with is/2.
2. Guard division against zero.
3. Recursively multiply for factorial.
4. Carry the previous two terms for Fibonacci.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- arithmetic(10,3,S,D,P).
S = 13, D = 7, P = 30.
?- quotient(10,4,Q).
Q = 2.5.
?- quotient(10,0,_).
false.
?- factorial(5,F).
F = 120.
?- fibonacci(7,F).
F = 13.
?- fibonacci_series(8,L).
L = [0,1,1,2,3,5,8,13].
?- factorial(-1,_).
false.
```

## Result
The program computes arithmetic values, factorials and a series of N Fibonacci terms.

## Assumptions and limitations
N must be a bound nonnegative integer. Invalid arguments fail. These arithmetic predicates calculate forward; they do not solve for unknown inputs. Factorial uses linear recursion; Fibonacci runs in O(N) arithmetic steps.
