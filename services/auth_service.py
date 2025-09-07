import bcrypt

class AuthService:
    def __init__(self, db):
        self.db = db
        
    def addUser(self, username, password, role):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return self.db.executeCommand("INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)", (username, hashed.decode(), role))
    
    def authenticate(self, username, password):
        row = self.db.executeCommand("SELECT * FROM Users WHERE username = %s LIMIT 1", (username,), "fetchone")
        if not row:
            return "User not found!"
        
        if bcrypt.checkpw(password.encode('utf-8'), row['password'].encode('utf-8')):
            print('Login succesfull!')
            return row['role']
        else:
            return "Invalid Password!"
        