import pymysql as db

class database:

    def __init__(self, host, user, password, database):
        self.host = 'localhost',
        self.user = 'root',
        self.password = 'Adonispili2',
        self.database = database


    '''
    ssh conection module
    This module help us to bring the file that containt the paths that we needed
    to can connect to the tapeserver.
        -Paths to get the log files: this  containt the exactly path's logs file
        ubication.
        -Paths to get the teststat file: This file should containt the exactly
        teststat file ubication.
    PARAMETERS:
        Mandatory:
            - file_to_search: (string) The file name that is give to the file
                            that contain each one of the paths.
            -local_dest: (string) The local path to receive the file(s)
            -cred:(string)  Access Credentials from the VCAP_SERVICES
    '''
        
    def dbconnect(self):
        print(self.host,self.user,self.database,self.password)
        try:
            connection = db.connect(host= 'localhost',
                                user= 'root',
                                password= 'Adonispili2',
                                db= self.database,
                                charset='utf8mb4',
                                cursorclass=db.cursors.DictCursor)
            print ("conexión a la base:" + database + "fue exitosa")
            return connection 
        except:   
            print("Fallo en la conexión a la base de datos")

    
    # def checkuser(self, user, password):

        



# Intenta:
#Conectar a la base de datos
# if conn:
#then imprimir "Conexión a la base: " self.database  + " fue exitosa"
 #else:
#then imprimir FALLÓ EN CONEXION A LA BD