from email_validator import validate_email, EmailNotValidError

def student_validator(name, age, email, course):
    if not name or not isinstance(name, str) or len(name) < 2:
        return "Incalid Name."
    if not isinstance(age, int) or age < 0 or age > 120:
        return "Invalid Age."
    if isinstance(email, str) and len(email) > 5:
        try:
            validate_email(email)
        except EmailNotValidError as e:
            return str(e)
    else:
        return "Invalid Email."
    if not course or not isinstance(course, str) or len(course) < 2:
        return "Invalid Course."
    
    return None
        

def user_validator(username, password, role):
    if not username or not isinstance(username, str) or len(username) < 3:
        return "Invalid Username."
    if not password or not isinstance(password, str) or len(password) < 6:
        return "Invalid Password."
    if role not in ['admin', 'viewer']:
        return "Role must be either 'admin' or 'viewer'."
    return None