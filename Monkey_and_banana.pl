% State representation
% state(MonkeyPosition, BoxPosition, MonkeyOnBox, HasBanana)

% Initial State
initial_state(state(door, window, off, no)).

% Goal State
goal_state(state(_, _, _, yes)).

% Move: Monkey walks from one place to another
move(state(P, B, off, H),
     walk(P, NewP),
     state(NewP, B, off, H)) :-
     P \= NewP.

% Move: Monkey pushes box
move(state(P, P, off, H),
     push(P, NewP),
     state(NewP, NewP, off, H)) :-
     P \= NewP.

% Move: Monkey climbs box
move(state(P, P, off, H),
     climb,
     state(P, P, on, H)).

% Move: Monkey grabs banana
move(state(middle, middle, on, no),
     grab,
     state(middle, middle, on, yes)).

% Possible locations
place(door).
place(window).
place(middle).

% Solve the problem
solve(State, []) :-
    goal_state(State).

solve(State, [Action | Rest]) :-
    move(State, Action, NewState),
    solve(NewState, Rest).
