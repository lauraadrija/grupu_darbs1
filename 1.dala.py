#links uz sql datubāzes skici: https://drawsql.app/teams/programmesana-26/diagrams/kafejnicutiklssql
CREATE TABLE Kafejnicas (
    KafejnicaID INT PRIMARY KEY AUTO_INCREMENT,
    Nosaukums VARCHAR(100) NOT NULL,
    Adrese VARCHAR(255)
);