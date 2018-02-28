# 阿里云CentOS服务器上的MariaDB的安装

操作系统: `CentOS 7.3 64-bit`

[MariaDB官网相关资料](https://mariadb.com/kb/en/library/mariadb-package-repository-setup-and-usage/)

### 通过官方推荐的yum安装数据库

1. 配置yum源

```bash
# 需要root
root@aliyun: ~# curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash

[info] Repository file successfully written to /etc/yum.repos.d/mariadb.repo.
[info] Adding trusted package signing keys...
[info] Succeessfully added trusted package signing keys.
```

2. 安装

```bash
root@aliyun: ~# yum install MariaDB-server -y

...
Complete!
```

3. 启动

```bash
# 启动方法和mysql相同
root@aliyun: ~# systemctl start mysqld.service

# Active: active (running)就代表成功
root@aliyun: ~# systemctl status mysqld.service
● mariadb.service - MariaDB 10.2.13 database server
   Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/mariadb.service.d
           └─migrated-from-my.cnf-settings.conf
   Active: active (running) since Sat 2018-02-24 21:35:57 CST; 24s ago
     Docs: man:mysqld(8)
           https://mariadb.com/kb/en/library/systemd/
  Process: 1722 ExecStartPost=/bin/sh -c systemctl unset-environment _WSREP_START_POSITION (code=exited, status=0/SUCCESS)
  Process: 1677 ExecStartPre=/bin/sh -c [ ! -e /usr/bin/galera_recovery ] && VAR= ||   VAR=`/usr/bin/galera_recovery`; [ $? -eq 0 ]   && systemctl set-environment _WSREP_START_POSITION=$VAR || exit 1 (code=exited, status=0/SUCCESS)
  Process: 1675 ExecStartPre=/bin/sh -c systemctl unset-environment _WSREP_START_POSITION (code=exited, status=0/SUCCESS)
 Main PID: 1690 (mysqld)
   Status: "Taking your SQL requests now..."
   CGroup: /system.slice/mariadb.service
           └─1690 /usr/sbin/mysqld

Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651737098368 [Note] InnoDB: 5.7.21 started; log sequence number 1619987
Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651031570176 [Note] InnoDB: Loading buffer pool(s) from /var/l...er_pool
Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651031570176 [Note] InnoDB: Buffer pool(s) load completed at 1...1:35:57
Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651737098368 [Note] Plugin 'FEEDBACK' is disabled.
Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651737098368 [Note] Server socket created on IP: '::'.
Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651737098368 [Note] Reading of all Master_info entries succeded
Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651737098368 [Note] Added new Master_info '' to hash table
Feb 24 21:35:57 aliyun mysqld[1690]: 2018-02-24 21:35:57 139651737098368 [Note] /usr/sbin/mysqld: ready for connections.
Feb 24 21:35:57 aliyun mysqld[1690]: Version: '10.2.13-MariaDB'  socket: '/var/lib/mysql/mysql.sock'  port: 3306  MariaDB Server
Feb 24 21:35:57 aliyun systemd[1]: Started MariaDB 10.2.13 database server.
Hint: Some lines were ellipsized, use -l to show in full.
```

到这里其实MariaDB就已经成功安装了,现在多数的数据库都可以通过yum几步完成快速安装,只有oracle仍然让人头痛。

4. 重置密码

```bash
root@aliyun: ~# mysqld_safe --skip-grant-table &
[1] 2685
root@aliyun: ~# 180224 22:56:29 mysqld_safe Logging to '/var/lib/mysql/aliyun.err'.
180224 22:56:29 mysqld_safe Starting mysqld daemon with databases from /var/lib/mysql

root@aliyun: ~# mysql -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.2.13-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

MariaDB [mysql]> UPDATE user SET Password=PASSWORD('newpass') WHERE User='root';
Query OK, 4 rows affected (0.01 sec)
Rows matched: 4  Changed: 4  Warnings: 0

MariaDB [mysql]> exit;
Bye

root@aliyun: ~# pkill mysqld

# 启动MariaDB
root@aliyun: ~# systemctl start mysqld.service

# 设置开机自动启动数据库
root@aliyun: ~# systemctl enable mysqld.service
```

### 常见的几个使用问题
1. 创建默认字符集为utf8的数据库

```SQL
MariaDB [(none)]> CREATE DATABASE blog DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
Query OK, 1 row affected (0.00 sec)
```

2. 服务器无法远程连接数据库

Host "xxx.xxx.xxx.xxx" is not allowed to connect to this MariaDB server.

```SQL
# 方案1
MariaDB [(none)]> CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass';
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'localhost' WITH GRANT OPTION;
Query OK, 0 rows affected (0.01 sec)

MariaDB [(none)]> CREATE USER 'monty'@'%' IDENTIFIED BY 'some_pass';
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.01 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)

# 方案2
# 若报错ERROR 1133 (28000): Can't find any matching row in the user table
MariaDB [(none)]> GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY 'your_root_password' WITH GRANT OPTION;
Query OK, 0 rows affected (0.01 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)
```

3. 创建新用户失败

可能是通过删除user表中的内容并不能彻底删除用户

```SQL
MariaDB [(none)]> CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass';
ERROR 1396 (HY000): Operation CREATE USER failed for 'monty'@'localhost'

MariaDB [(none)]> DROP USER 'monty'@'localhost';
Query OK, 0 rows affected (0.00 sec)
```

### 之后有别的使用再继续补充...