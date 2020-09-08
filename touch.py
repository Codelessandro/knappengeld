#TrainingsPhase
-> Input
-> Output

#Test/Application
-> Input



#Model 1: Game Result Prediction
Input:  [
    (Wettquoten Anbietern)   #optional
    M1->Team,
    M2->Team,
    Schiedsrichter,
    M1: Platzierung in Tabelle letzten n Spieltagen: [ 1 2 3 1 2 3 1 5 4 2 2 ],   #was passiert bei Saisonende
    M2: Platzierung in Tabelle letzten n Spieltagen: [ 10 11, 12, 14 14 14 14 14 14],
    letzten n Ergebnisse von M1 vs. M2 [6:0, 1:1],
    Spieler M1: [
        [
            FifaIndexDS_1,FifaIndexDS_2,FifaIndexDS_3,FifaIndexDS_4,FifaIndexDS_5,... (11*)
        ]
    ],
    SPieler M2: [
    FifaIndexDS_1, FifaIndexDS_2, FifaIndexDS_3, FifaIndexDS_4, FifaIndexDS_5, ...(11 *)@
    ],
    Distanz M1 zu Stadion (0),  #fu0ball shreding
    Distanz M2 zu Stadion (800), #fu0ball shreding
]


Output :ERgebnis: [Winning M1, Draw, Winning M2]
Output: Wie viele Tore fallen?: [0-1;2-3;4+]


Aufgabe:
>> DummyData-Loader bauen +
>> Versuch einer ersten KI-Implementierung