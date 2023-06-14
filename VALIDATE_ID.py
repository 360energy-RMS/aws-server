# Ensures that whatever information that is sent to the server is from a trusted source
# IDS' must be numeric

class VALIDATE_ID():
    
    def isValid(ID):
        if ID:
            ID = ID[0]
            VALIDIDS = [360]
            
            if ID in VALIDIDS:

                return True
            
            else:
                
                return False
