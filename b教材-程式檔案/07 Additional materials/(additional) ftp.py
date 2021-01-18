#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:17:14 2019

Easy FTP script

@author: benyiu
"""



# 本教學代碼分為2部份，第一部份教授 ftplib 用法，第二部份教授 paramiko 用法。
# ftplib 用於 FTP、FTPS (FTP over TLS) 連接
# paramiko 用於 SFTP (FTP over SSH) 連接



# ftplib 教學文件：
# https://docs.python.org/3/library/ftplib.html


# 匯入 ftplib
import ftplib


# 定義登入帳戶資料
ftp_server = "192.168.1.1"
ftp_user = "user"
ftp_password = "password"


# 連接到FTP伺服器
ftp = ftplib.FTP(ftp_server)
ftp.login(ftp_user, ftp_password)

# 改變 Working directory
ftp.cwd('/')

# 取得 Working directory files 列表
ftp.nlst()

# 下載檔案
ftp.retrbinary("RETR index.txt", open('index.txt', "wb").write)

# 上傳檔案
ftp.storbinary('STOR test.txt', open('test.txt','rb'))

# 删除檔案
ftp.delete('test.txt')

# 删除資料夾，注意如果資料夾內有檔案，則需要先删除裡面所有檔案
ftp.rmd('test')

# 建立資料夾
ftp.mkd('test')

# 重命名檔案 test.txt => test2.txt
ftp.rename('test.txt', 'test2.txt')

# 關閉連接
ftp.quit()





# paramiko 用於 SFTP (FTP over SSH) 連接
# paramiko 教學文件：
# http://docs.paramiko.org/en/2.4/api/sftp.html

# 匯入 paramiko
import paramiko


# 定義登入帳戶資料
ftp_server = "192.168.1.1"
ftp_port = 22
ftp_user = "user"
ftp_password = "password"


# 透過SSH連接到FTP伺服器
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ftp_server, ftp_port, ftp_user, ftp_password)

# 開啟SFTP連接
sftp = ssh.open_sftp()

# 改變 Working directory
sftp.chdir('/')

# 取得 Working directory files 列表
sftp.listdir()

# 下載檔案 remote => local
sftp.get('test.txt', 'test.txt')

# 上傳檔案 local => remote
sftp.put('test.txt', 'test.txt')

# 删除檔案
sftp.remove('test.txt')

# 删除資料夾，注意如果資料夾內有檔案，則需要先删除裡面所有檔案
sftp.rmdir('test')

# 建立資料夾
sftp.mkdir('test')

# 重命名檔案 test.txt => test2.txt
sftp.rename('test.txt', 'test2.txt')

# 關閉連接
sftp.close()





