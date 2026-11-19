sum_n(0, 0).

sum_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_n(N1, S1),
    Sum is N + S1.

main :-
    write('Enter a number: '),
    read(N),
    sum_n(N, Sum),
    write('Sum = '),
    write(Sum),
    nl.
    //output
    //?- main.
//Enter a number: 5.
//Sum = 15
//true.
