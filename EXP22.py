% Bird Database

bird(parrot).
bird(pigeon).
bird(eagle).
bird(sparrow).
bird(ostrich).
bird(penguin).

% Flying birds
can_fly(parrot).
can_fly(pigeon).
can_fly(eagle).
can_fly(sparrow).

% Non-flying birds
cannot_fly(ostrich).
cannot_fly(penguin).

% Rule to check flying ability
check_fly(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.').

check_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.').

check_fly(Bird) :-
    \+ bird(Bird),
    write('Bird not found in database.').
