BackupServer.py
================

This is back-up file script. <br />

***Link*** 

[Down Zip](#)   [BackupServer.py Info](http://www.conglin-site.com/2013/05/20/%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%A4%87%E4%BB%BD%E8%84%9A%E6%9C%ACpython-2-7-bate-0-9/)  [My Blog](http://www.conglin-site.com)   



***Over Preview*** 

BackupServer.py is a server backup script. Up to now it can zip floder and file, write backup procedure log and send result to email.

***Feature***

> 1. zip floder and file <br />
> 2. write backup procedure log <br />
> 3. backup send result to email <br />

***Versions***

### 
    Vesrion: Bate 1.0
    Date: 2013.05.21
    Log:
        Init BackupServer.py.

***Set up your script***

### please change your config.xml
    <?xml version="1.0" encoding="utf-8" ?>
    <config>
        <!-- backup file list -->
        <backup>
            <!-- file url-->
            <file>D:\project</file> <!-- windows url -->
            <file>/www</file> <!-- unix url -->
        </backup>
        <!-- save folder url-->
        <savefolder>E:\linshi</savefolder> <!-- windows url -->
        <!-- log file url-->
        <log>/linshi</log> <!-- unix url -->
        <!-- send mail account setting-->
        <mail>
            <!-- smtp server-->
            <host>smtp.gmail.com</host> <!-- gmail smtp -->
            <!-- user name-->
            <user>******@gmail.com</user> 
            <!-- user password-->
            <pwd>******</pwd>
            <!-- send user info-->
            <from>server@******.com</from>
            <!-- receiver email address-->
            <to>*******o@gmail.com</to>
        </mail>
    </config>

now, you can runing your script. But, if you runing this in cron, please you url is absolute path, in xml and .py
