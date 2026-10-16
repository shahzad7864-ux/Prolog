# AIML practical solutions — 1 to 12

Based on rows 2–13 of the **Practicals** worksheet in `Intro to AIML _Practicals_Tutorials_Unitwise_Updated 21 Sep.xlsx`. Tutorials and practicals 13 onward are outside this package.

## Start here
1. Extract the entire ZIP folder.
2. Use a SWI-Prolog installation for the `solution.pl` files. No Python packages are needed to run the practicals.
3. Open one practical folder and read `README.md`, or open `Solutions_Guide.html` in a browser for all solutions in one printable guide.
4. Start SWI-Prolog, load `['solution.pl'].`, then enter the sample goals. Alternatively run `swipl -q -s solution.pl` from that folder.
5. Load each practical in a **fresh Prolog session**. Independent exercises intentionally reuse predicate names, especially 7/8 and 9/10.
6. Exit with `halt.`. Prolog atoms start lowercase; variables start uppercase; each query ends in a period.

## Visual Prolog compatibility
The workbook explicitly names Visual Prolog for practicals 1 and 4 and refers to Domains, Predicates, Clauses and Goals. Those folders include `classic_visual_prolog.pro` using the legacy 5.x-style sections. Their failure-driven goal prints every answer and then fails intentionally. Modern Visual Prolog uses project/class structures and cannot directly compile these legacy files. The `solution.pl` editions use SWI-Prolog and cannot be passed unchanged to Visual Prolog. Confirm your lab's compiler version if Visual Prolog submission is mandatory.

## Data and output conventions
All sample facts, score thresholds, graphs and numerical objectives were chosen for these solutions because the workbook supplies tasks rather than datasets. Sample results are expected logical answers, not captured execution logs. Prolog may show different spacing or additional `true`/`false` prompts. Practical 10 is stochastic and deliberately does not invent exact measured outputs.

## Verification
No Prolog executable was available in the preparation environment; these programs were reviewed but not executed here. `verify.py` runs the supplied behavioral checks in separate SWI-Prolog processes when Python 3 and `swipl` are available. Run `python verify.py` from this extracted folder. It checks boundary cases, search costs, CSP counts and annealing invariants; it does not require annealing to reach the global optimum. Legacy Visual Prolog files require their own compiler and are not covered by that script.

## Contents
- **01** — Create a simple Knowledge Base using facts, predicates, clauses, and goals (Student-Course Database) (`01_Student_Course_Knowledge_Base`)
- **02** — Implement arithmetic operations, Factorial, and Fibonacci Series using recursion (`02_Arithmetic_Factorial_Fibonacci`)
- **03** — Perform append, reverse, member search, and list length operations (`03_List_Operations`)
- **04** — Develop a timetable database and answer queries regarding faculty, subjects, and classrooms (`04_College_Timetable`)
- **05** — Classify students as topper, average, and fail using rule-based reasoning (`05_Student_Performance`)
- **06** — Implement Breadth-First Search (BFS) to find the shortest path in a graph (`06_Breadth_First_Search`)
- **07** — Implement Greedy Best-First Search using a heuristic function to find a path in a graph (`07_Greedy_Best_First_Search`)
- **08** — Implement the A* Search algorithm to find the optimal path using path cost and heuristic estimate (`08_A_Star_Search`)
- **09** — Implement Hill Climbing for optimization problems (`09_Hill_Climbing`)
- **10** — Solve an optimization problem using Simulated Annealing to escape local optima (`10_Simulated_Annealing`)
- **11** — Represent a Map-Coloring problem as a CSP and solve it using backtracking search (`11_Map_Coloring_CSP`)
- **12** — Solve the N-Queens problem using backtracking to satisfy CSP constraints (`12_N_Queens_CSP`)
