% Fruit and Colour Database

fruit(apple, red).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grapes, green).
fruit(mango, yellow).
fruit(guava, green).

% Display fruits using backtracking
display :-
    fruit(Fruit, Colour),
    write('Fruit: '),
    write(Fruit),
    write(', Colour: '),
    write(Colour),
    nl,
    fail.

display.
