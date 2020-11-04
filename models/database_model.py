import pymysql 

class database:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connection(self): 
        conn = pymysql.connect(host= self.host,
                               user= self.user,
                               password= self.password,
                               database= self.database)

        if conn:
            return conn
            
        else:
            return 'No jala' 
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
                                

    