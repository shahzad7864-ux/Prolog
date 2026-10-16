# Practical 3: Perform append, reverse, member search, and list length operations

## Assignment
Experiment 3: Write a Prolog program to perform list manipulation operations (appending two lists, reversing a list, and searching for an element).

## Aim and concept
Lists consist of a head and tail, written [H|T]. Structural recursion processes one element at a time. The empty list is the base case. An accumulator makes reversal linear in list length.

## Algorithm
1. Append by copying heads from the first list.
2. Reverse by moving each head to an accumulator.
3. Match the head or search the tail for membership.
4. Add one per element for length.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- my_append([1,2],[3,4],R).
R = [1,2,3,4].
?- my_reverse([a,b,c],R).
R = [c,b,a].
?- my_member(b,[a,b,c]).
true.
?- my_member(z,[a,b,c]).
false.
?- my_length([a,b,c],N).
N = 3.
?- my_reverse([],R).
R = [].
```

## Result
Append, reverse, member search and list length are implemented without calling their built-in equivalents.

## Assumptions and limitations
Use finite proper lists. my_length/2 is intended for a supplied list, not generation from a length. Membership can return multiple proofs for repeated elements.
