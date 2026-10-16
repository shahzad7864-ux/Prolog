# Practical 5: Classify students as topper, average, and fail using rule-based reasoning

## Assignment
Experiment 5: Create a Prolog program for Student Performance Analysis that identifies toppers, average performers, and failed students using rules.

## Aim and concept
Rule-based reasoning applies explicit conditions to facts. Disjoint score intervals ensure each valid mark receives exactly one classification.

## Algorithm
1. Store marks.
2. Define topper as 85–100, average as 40–below 85, and fail as 0–below 40.
3. Join student marks with the category rules.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- topper(S).
S = amit ; S = sara.
?- average(S).
S = neha ; S = kiran ; S = isha.
?- failed(S).
S = rahul.
?- category(40,C).
C = average.
?- category(85,C).
C = topper.
?- category(101,_).
false.
```

## Result
Students are classified into three mutually exclusive categories.

## Assumptions and limitations
Thresholds are explicitly assumed for this exercise because the workbook does not specify them. Topper means threshold-based high performer, not necessarily the unique highest-scoring student.
