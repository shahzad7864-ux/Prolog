# Practical 4: Develop a timetable database and answer queries regarding faculty, subjects, and classrooms

## Assignment
Experiment 4: Develop a Visual Prolog program to represent a College Timetable Knowledge Base and answer queries about faculty, subjects, and classrooms.

## Aim and concept
A timetable is a relation over day, time, subject, teacher and room. Query patterns retrieve selected columns. Negation-as-failure means a slot is considered free when no matching booking is recorded.

## Algorithm
1. Store timetable facts.
2. Write faculty and subject lookup rules.
3. Enumerate known rooms/days/times before testing absence of a booking.
4. Run queries for the requested schedule.

## Run
Open SWI-Prolog in this folder and enter `['solution.pl'].` Then run the queries below. The `?-` is the console prompt; do not type it twice. Press `;` for more answers or Enter to stop.

## Sample queries and expected results
```prolog
?- faculty_schedule(mehta,D,T,S,R).
D = monday, T = nine, S = ai, R = r101 ;
D = tuesday, T = ten, S = ai, R = r101.
?- subject_room(database,D,T,R).
D = monday, T = ten, R = r102.
?- room_busy(lab1,tuesday,nine).
true.
?- room_free(r101,monday,ten).
true.
```

## Result
Faculty, subject, occupied-room and free-room queries are answered from a timetable knowledge base.

## Assumptions and limitations
The database is an illustrative weekly schedule; it is not an automatic timetable generator. Absence of a booking implies free only within this complete sample database. The included classic_visual_prolog.pro demonstrates the legacy Visual Prolog section format; modern versions need a project-specific port.
