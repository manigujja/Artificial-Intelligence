% State: state(X,Y) where X = 4L jug, Y = 3L jug

move(state(X,Y), state(4,Y)) :- X < 4.          % Fill 4L
move(state(X,Y), state(X,3)) :- Y < 3.          % Fill 3L
move(state(X,Y), state(0,Y)) :- X > 0.          % Empty 4L
move(state(X,Y), state(X,0)) :- Y > 0.          % Empty 3L

% Pour 4L -> 3L
move(state(X,Y), state(X1,Y1)) :-
    X > 0, Y < 3,
    T is min(X, 3-Y),
    X1 is X - T,
    Y1 is Y + T.

% Pour 3L -> 4L
move(state(X,Y), state(X1,Y1)) :-
    Y > 0, X < 4,
    T is min(Y, 4-X),
    Y1 is Y - T,
    X1 is X + T.

goal(state(2,_)).
