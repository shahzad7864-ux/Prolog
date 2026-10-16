# Practical 11: Represent a Map-Coloring problem as a CSP and solve it using backtracking search

## Assignment
Experiment 11: Represent the Map-Coloring problem in Prolog as a CSP and solve it using backtracking search.

## Aim and concept
A constraint satisfaction problem has variables (regions), domains (three colors), and constraints (adjacent regions differ). Prolog backtracking tries alternative assignments when a constraint fails.

## Algorithm
1. Assign WA and NT and test their edge.
2. Assign each next region and immediately test edges to assigned neighbors.
3. Backtrack when a conflict occurs.
4. Assign Tasmania, which has no land-border constraints in this model.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- once(map_coloring(M)).
M = [wa-red,nt-green,sa-blue,q-red,nsw-green,v-red,t-red].
?- findall(M,map_coloring(M),Ms), length(Ms,N).
N = 18.
```

## Result
All land-adjacent regions have different colors. There are 18 assignments when color labels are distinct and Tasmania can use any color.

## Assumptions and limitations
The map uses WA–NT, WA–SA, NT–SA, NT–Q, SA–Q, SA–NSW, SA–V, Q–NSW and NSW–V. Island Tasmania is unconstrained. Ground inequality is applied only after color choices are bound.
