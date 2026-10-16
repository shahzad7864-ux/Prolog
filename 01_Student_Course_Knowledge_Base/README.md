# Practical 1: Create a simple Knowledge Base using facts, predicates, clauses, and goals (Student-Course Database)

## Assignment
Experiment 1: Write a basic Visual Prolog program to define a simple Knowledge Base of facts (e.g., student-course enrollment or a "likes" relationship database) to understand the core structure of Domains, Predicates, Clauses, and Goals.

## Aim and concept
Facts store students, courses, enrollment and teachers. A predicate describes a relation; a clause is a fact or rule; a goal asks whether a relation holds. Variables begin with uppercase letters. Rules combine facts through unification and backtracking.

## Algorithm
1. Define students and courses.
2. Add enrollment and teaching facts.
3. Join facts with shared variables to derive classmates and teachers.
4. Query the knowledge base.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- enrolled(amit, C).
C = ai ; C = python.
?- classmate(amit, X).
X = rahul.
?- student_teacher(neha, T).
T = rao.
?- enrolled(neha, ai).
false.
```

## Result
Enrollment and derived relationships can be retrieved without procedural database loops.

## Assumptions and limitations
Sample names/data are illustrative. A pair of classmates may be returned more than once if they share several courses; use setof/3 to remove duplicates. classic_visual_prolog.pro supplies the requested Domains/Predicates/Clauses/Goal structure for legacy Visual Prolog. It is not SWI syntax or a modern Visual Prolog project.
