from config import CONN, CURSOR

class Song:

    all_songs= set()

    def __init__(self , name , album):
        self.id= None
        self.name = name
        self.album = album
        Song.get_all_songs(name)
        Song.create_table()
        # Song.save(self)
    
#classmethod to get the list of created instances
    @classmethod
    def get_all_songs(cls, song):
        return cls.all_songs.add(song);

#classmethod to create table
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS songs ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL, 
                album TEXT NOT NULL);"""
        CURSOR.execute(sql)

#instance method to add instance attributes to the created table
    def save(self):
        sql= """
            INSERT INTO songs (name,album)
            VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
        self.id= CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

# Classmethod to handle create and save of our instances to the  database and return the object created
    @classmethod
    def create(cls, name , album):
        song= Song(name, album)
        song.save()
        return song


blinding_lights = Song.create("Blinding Lights", "After Hours")
# blinding_lights.save()

one_direction_world_of_dreams = Song.create("World of Dreams", "One Direction")
# one_direction_world_of_dreams.save()

hello = Song.create("Hello", "25")
# hello.save()

despacito = Song.create("Despacito", "Vida")
# despacito.save()

print(hello.id)
print(despacito.id)

print(Song.all_songs)
