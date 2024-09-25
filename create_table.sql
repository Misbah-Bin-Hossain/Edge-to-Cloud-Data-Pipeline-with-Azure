CREATE TABLE dbo.SensorData (
    id INT PRIMARY KEY NOT NULL,
    timestamp DATETIME NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL
);
