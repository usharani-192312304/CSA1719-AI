% Planets Database

planet(mercury).
planet(venus).
planet(earth).
planet(mars).
planet(jupiter).
planet(saturn).
planet(uranus).
planet(neptune).

% Display all planets
display :-
    planet(Name),
    write('Planet: '),
    write(Name),
    nl,
    fail.

display.
