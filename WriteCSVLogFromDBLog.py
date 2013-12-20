#!usr/bin/env python

import os
import sys
import sqlite3

class WriteLog():
    def __init__(self,rtPath,log_path,selectsql):
        print "Begin Process\n"
        self.rtPath         =   rtPath
        self.log_path       =   log_path
        self.log_csv_path   =   log_path+".csv"            
        self.sqlite_conn=sqlite3.connect( self.rtPath )
        self.sqlite_cursor=self.sqlite_conn.cursor()
        self.paserselect(selectsql)
    def excutesql(self,selectstr):
        self.sqlite_cursor.execute( selectstr )
        self.res = self.sqlite_cursor.fetchall()
    def writecsv(self):
        print self.res
        writecsvdatafile = open( self.log_csv_path, "a")
        for record in self.res:
            linestr = ''
            for field in record:
                linestr = linestr +  str(field) +','
            print linestr[:-1]
            writecsvdatafile.write(linestr[:-1])
            writecsvdatafile.write("\r")
        writecsvdatafile.close()  
    def paserselect(self,selectsql):
        self.selectsqlstr = selectsql.split(';')
    def process(self):
        for selectstr in self.selectsqlstr: 
            if selectstr != '': 
                self.excutesql(selectstr)
                self.writecsv()
        self.close()
    def close(self):
        self.sqlite_conn.close()
        print "End Process\n"
        

if __name__=='__main__': 
    os.chdir( os.getcwd())
    if len(sys.argv) != 4 :
        print "app rootDiffDataPath, logDBPath, SelectSql\n"
        sys.exit(0)       
    rt_dif_path =   sys.argv[1]
    log_path    =   sys.argv[2]
    selectsql   =   sys.argv[3]
    stater = WriteLog( rt_dif_path,  log_path, selectsql )
    stater.process( )

