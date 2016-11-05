from crate import client


class Database:
    def __init__(self, crateServer):
        self.server = crateServer

    '''
    Create database to store geese
    '''
    def Create(self):
        connection = client.connect(crateServer)
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE geese(
            ID INT PRIMARY KEY,
            HASHID VARCHAR(8),
            LIFESPAN FLOAT(8),
            AGE INT,
            HUNGER FLOAT(8),
            LOCATION_X FLOAT(16),
            LOCATION_Y FLOAT(16),
            HEALTH INT
        );
        """)

    '''
    Save function for geese table
    Accesses crate on ip provided and saves _geeseArray in it
    '''
    def Save(self, _geeseArray):
        connection = client.connect(crateServer)
        cursor = connection.cursor()
        cursor.execute("""
        #TODO
        """);

    '''
    Load function for geese table
    Accesses crate on ip provided and loads it into _geeseArray
    '''
    def Load(self, _geeseArray):
        connection = client.connect(crateServer)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM geese
        """);
