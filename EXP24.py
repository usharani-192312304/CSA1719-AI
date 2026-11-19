% Family Tree Database

% Parent facts
parent(john, mary).
parent(john, david).
parent(mary, alice).
parent(mary, bob).
parent(david, peter).

% Gender facts
male(john).
male(david).
male(bob).
male(peter).

female(mary).
female(alice).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
