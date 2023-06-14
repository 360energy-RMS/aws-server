# Calls and manages functions/objects from other scripts
from SOCKET_SERVER import *
from DATA_FORMAT import *
from DATA_WRITER import *
from VALIDATE_ID import *


def main():
    print("STARTING RMS SERVER...")
    print("DO NOT CLICK INSIDE THIS WINDOW")
    
    data = None
    
    while True: # Automatic server restart after each transaction
        print("READY")

        try:
            data = SOCKET_SERVER.startServer()

            print("DATA RECIEVED")
            
            # Data error detecting try block
            try: 
                data = DATA_FORMAT.convert(data)
            except:
                print("CONNECTION DATA IS NOT VALID")
                
            # If data is validated by its ID
            if VALIDATE_ID.isValid(data) and not data is None:

                DATA_WRITER.writeToFile(data)
                
                print("FILE WRITE SUCCESS")
                
            else:
                print("CONNECTION REQUEST IS NOT AUTHORIZED")
                
        except:
            print("AN UNKNOWN CONNECTION WAS MADE")

        
main()