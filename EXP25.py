% Monkey Banana Problem

% Initial state: Monkey is at door, box is at window,
% bananas are hanging at middle.

move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

move(state(P, onfloor, P, H),
     climb,
     state(P, onbox, P, H)).

move(state(P1, onfloor, B, H),
     push(P1, P2),
     state(P2, onfloor, P2, H)).

move(state(P1, onfloor, B, H),
     walk(P1, P2),
     state(P2, onfloor, B, H)).

% Goal state
goal(state(_, _, _, has)).

% Solve the problem
solve(State, []) :-
    goal(State).

solve(State, [Action | Rest]) :-
    move(State, Action, NewState),
    solve(NewState, Rest).
