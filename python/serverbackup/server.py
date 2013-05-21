#!/usr/bin/env python
# -*- coding:UTF-8 -*-
''' Backup file server of file system
@version: 1.0
@author: conglin
@contact: conglin.pro@gmail.com
@see: http://www.conglin-site.com
'''
import os, zipfile, time, sys, smtplib, email.mime.text
import xml.dom.minidom as Dom




class ServerBackup:
    '''the server backup
    @param global_log: the log file
    '''
    
    global_log = ''

    def __init__(self):
        #set log file
        self.global_log = self.createLog()

        #start file backup
        self.backup()

        #send maill
        self.sendMail(str(time.strftime('[%Y-%m-%d]',time.localtime(time.time()))) +'Server Backup Succeed','Server Backup Succeed')

    def backup(self):
        '''run file backup
        '''
        folderlist = self.getFolder()
        for value in folderlist:
            self.recursionZip(value, self.getSaveFolder())

    def createLog(self):
        '''get folder in config file
        @return: log file name
        @rtype filename: string
        '''

        filename = ''

        #get log file url
        configxml =  Dom.parse("config.xml")
        savefolderxml = configxml.documentElement.getElementsByTagName('log')[0]

        #linux change /
        filename = savefolderxml.childNodes[0].data + '/backup_log_' + self.getTime() + '.log'

        #create
        if not os.path.exists(filename):
            try:
                logfile = open(filename, 'w')
                logfile.close()
            except Exception, e:
                self.sendMail(str(time.strftime('[%Y-%m-%d]',time.localtime(time.time()))) +'[linux] Can\' create log file','Server Backup Fail')
                filename = ''
                print self.getNowTime() , '[error ] :' , sys.exc_info()[0],sys.exc_info()[1]

        return filename



    def getFolder(self):
        '''get folder in config file
        @return: folder list
        @rtype folderlist: list
        '''
        folderlist = []  #folder url list
        configxml =  Dom.parse("config.xml")
        backupxml = configxml.documentElement.getElementsByTagName('backup')[0]

        for node in backupxml.getElementsByTagName('file'):
            folderlist.append(node.childNodes[0].data)


        return folderlist

    def getSaveFolder(self):
        '''get save zip file of folder
        @return: save zip file of folder
        @rtype: string
        '''
        savefolder = ''
        configxml =  Dom.parse("config.xml")
        savefolderxml = configxml.documentElement.getElementsByTagName('savefolder')[0]
        savefolder = savefolderxml.childNodes[0].data

        return savefolder

    def getTime(self):
        '''get time string when runing program
        @return: now time string no separator
        @rtype: string
        '''
        nowtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        return nowtime

    def getNowTime(self):
        '''get time string when runing program
        @return: now time string no separator
        @rtype: string
        '''
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return nowtime

    def recursionZip(self, folder, savefolder):
        '''recursion folder or file
        @param folder: the folder while recursion
        @param savefolder: save zip file of folder
        '''
        filelist = []
        if not os.path.isfile(folder):
            for root, dirs, files in os.walk(folder):
                for filename in files:
                    filelist.append(os.path.join(root, filename))

                for dirname in dirs:
                    filelist.append(os.path.join(root, dirname))

    
        try:
            zip_file = zipfile.ZipFile(savefolder+'/'+os.path.split(folder)[-1] + self.getTime() + '.zip', 'w', zipfile.ZIP_DEFLATED)
            self.writeLog(self.getNowTime() + '[success] :  ' + zip_file.filename + ' create\n')
                 
        except Exception, e:
            if not self.global_log == '':
                self.writeLog(self.getNowTime() + ' [error ] : ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1])+'\n')
                
        for files in filelist:
            zip_file.write(files, files[len(folder):])
            self.writeLog(self.getNowTime() + '[success] : ' + 'add ' + files + ' success\n')

        self.writeLog(self.getNowTime() + '[success] :  ' + zip_file.filename + ' backup success\n')

        zip_file.close()

    def sendMail(self, title='this is mail title', text = 'this is mail contact', attachment=''):
        '''recursion folder or file
        @param title: mail title
        @param savefolder: save zip file of folder
        '''

        configxml =  Dom.parse("config.xml")


        mail = smtplib.SMTP()
        self.writeLog('****************************** mail ******************************\n')
        self.writeLog('connecting...\n')

        mail.set_debuglevel(1)

        try:
            print mail.connect(configxml.documentElement.getElementsByTagName('mail')[0].getElementsByTagName('host')[0].childNodes[0].data,'25')
        except Exception, e:
            self.writeLog('[error ] : ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + '\n')

        mail.starttls()

        try:
            self.writeLog('loginning...\n')
            mail.login(configxml.documentElement.getElementsByTagName('mail')[0].getElementsByTagName('user')[0].childNodes[0].data, configxml.documentElement.getElementsByTagName('mail')[0].getElementsByTagName('pwd')[0].childNodes[0].data)
        except Exception, e:
            self.writeLog('LOGIN ERROR ****\n')
            self.writeLog('[error ] : ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + '\n')
        
        msg = email.mime.text.MIMEText(text)
        msg['From'] = configxml.documentElement.getElementsByTagName('mail')[0].getElementsByTagName('from')[0].childNodes[0].data
        msg['To'] = configxml.documentElement.getElementsByTagName('mail')[0].getElementsByTagName('to')[0].childNodes[0].data
        msg['Subject'] = title
        mail.sendmail(msg['From'],msg['To'],msg.as_string())  
        self.writeLog('Sended\n')      
        mail.quit()

    def writeLog(self, connect):
        '''write log file
        @param connect: text
        '''
        logfile = ''        
        try:
            logfile = open(self.global_log, 'a+')
        except Exception, e:
            print 'log file is not exist'
            print '\n[info] : ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1])+'\n'
            pass
        finally:
            print connect

        if not logfile == '':
            print connect
            logfile.write(connect)

        logfile.close()



if __name__ == "__main__":
    #解决中文文件名
    reload(sys)
    #sys.setdefaultencoding('gbk')
    sys.setdefaultencoding('utf8')
    ServerBackup()

