
```markdown
# 0x14. MySQL

## Description
This project focuses on setting up and managing a MySQL primary-replica infrastructure. The tasks involved include installing MySQL, creating users with appropriate permissions, setting up a database and tables, and configuring replication between primary and replica servers.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the role and purpose of a database.
- Explain the concept and benefits of database replication.
- Implement a MySQL primary-replica setup.
- Manage database users and permissions effectively.
- Ensure robust database backup strategies.

## Tasks

### 0. Install MySQL
- Install MySQL version 5.7.x on both web-01 and web-02 servers.

### 1. Let us in!
- Create a MySQL user `holberton_user` on both web-01 and web-02 with access permissions required for replication status checks.

### 2. If only you could see what I've seen with your eyes
- Set up a database named `tyrell_corp` with a table named `nexus6` and at least one entry on the primary server (web-01).

### 3. Quite an experience to live in fear, isn't it?
- Create a user `replica_user` on the primary server (web-01) with the necessary permissions to replicate the MySQL server.

### 4. Setup a Primary-Replica infrastructure using MySQL
- Configure the MySQL primary-replica setup where `web-01` acts as the primary server and `web-02` as the replica.
- Verify that replication is working by adding data to the primary server and checking its presence on the replica server.

## Requirements
- All tasks are to be performed on Ubuntu 16.04 LTS.
- Ensure that MySQL installation and configurations are correct as per the guidelines.
- All scripts and configuration files should pass the Shellcheck validation without errors.
- Ensure that UFW is configured to allow MySQL connections on port 3306.

## Repository Structure
```bash
├── 0x14-mysql/
│   ├── 4-mysql_configuration_primary
│   ├── 4-mysql_configuration_replica
│   ├── ...
│   └── README.md
```

## Usage
To verify your installation:
```bash
$ mysql --version
```
To verify replication status:
```bash
$ mysql -uholberton_user -p -e "SHOW SLAVE STATUS\G"
```

## Authors
- Chancy Tsonga -
```
