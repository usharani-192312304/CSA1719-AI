% Forward Chaining Program

% Initial facts
fact(sunny).
fact(warm).

% Rules
rule(can_go_out) :-
    fact(sunny),
    fact(warm).

rule(ice_cream) :-
    fact(sunny).

rule(rainbow) :-
    fact(rain),
    fact(sunshine).

% Forward chaining
forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    write('New Fact: '),
    write(X),
    nl,
    fail.

forward :-
    write('Forward Chaining Completed.').
