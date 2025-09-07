from model.student import Student

class StudentService:
    def __init__(self, db):
        self.db = db
    
    def addStudent(self, s:Student):
        return self.db.executeCommand("INSERT INTO Students (name, age, email, course) VALUES (%s, %s, %s, %s)", (s.name, s.age, s.email, s.course))
    
    def deleteStudent(self, email):
        row = self.db.executeCommand("SELECT * FROM Students WHERE email = %s", (email,), "fetchone")
        
        if not row:
            return "Student not found!"
        
        return self.db.executeCommand("DELETE FROM Students WHERE email = %s", (email,))
    
    def updateStudents(self, email, newData:dict):
        row = self.db.executeCommand("SELECT * FROM Students WHERE email = %s", (email,), "fetchone")
        
        if not row:
            return "Student not found!"
        
        allowedFields = ['name', 'age', 'email', 'course']
        
        updateFields = []
        updateValues = []
        
        for k,v in newData.items():
            if k in allowedFields:
                updateFields.append(f"{k} = %s")
                updateValues.append(v)
                
        updateValues.append(row['student_id'])
        query = f"UPDATE Students SET {', '.join(updateFields)} WHERE student_id = %s"
        self.db.executeCommand(query, tuple(updateValues))
        
    def getStudent(self, name):
        student = self.db.executeCommand("SELECT * FROM Students WHERE name LIKE %s", (f"{name}%",), "fetchall")
        
        if not student:
            return "Student not found!"
        
        return student
        