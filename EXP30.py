% Backward Chaining Program

% Facts
fact(sunny).
fact(warm).
fact(holiday).

% Rules
can_go_out :-
    fact(sunny),
    fact(warm).

play_cricket :-
    can_go_out,
    fact(holiday).

eat_icecream :-
    fact(sunny).

% Main rule
check(Goal) :-
    call(Goal),
    write('Goal is proved: '),
    write(Goal),
    nl.

check(Goal) :-
    \+ call(Goal),
    write('Goal cannot be proved: '),
    write(Goal),
    nl.
