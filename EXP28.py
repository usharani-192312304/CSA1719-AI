% Medical Diagnosis System

% Disease symptoms
symptom(fever, malaria).
symptom(headache, malaria).
symptom(chills, malaria).

symptom(fever, flu).
symptom(cough, flu).
symptom(cold, flu).

symptom(cough, covid).
symptom(fever, covid).
symptom(tiredness, covid).

% Diagnosis rule
diagnose(Disease) :-
    symptom(_, Disease),
    write('Possible Disease: '),
    write(Disease),
    nl.

% Main program
main :-
    write('Enter symptom: '),
    read(S),
    symptom(S, Disease),
    write('Possible Disease: '),
    write(Disease),
    nl,
    fail.

main.
