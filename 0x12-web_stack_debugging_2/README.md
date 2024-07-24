# Web Stack Debugging 2

This project focuses on debugging web stack issues on an Ubuntu 20.04 LTS server. The tasks involve running software as another user and configuring Nginx to run under a non-root user.

## Requirements
- All files are interpreted on Ubuntu 20.04 LTS.
- Each file should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- All Bash scripts must be executable.
- All Bash scripts must pass Shellcheck without any error.
- Bash scripts should run without error.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining what the script does.

## Tasks

### 0. Run Software as Another User
**File:** `0-iamsomeoneelse`

The root user on Linux is the "superuser" and can perform any action. It is good practice to avoid being logged in as the root user to prevent accidental commands that could cause system-wide issues. This task involves writing a Bash script to run the `whoami` command as a different user.

#### Requirements:
- The script accepts one argument.
- The script runs the `whoami` command under the user passed as an argument.

#### Example:
```bash
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
```

### 1. Run Nginx as Nginx
**File:** `1-run_nginx_as_nginx`

Running web servers as the root user is a security risk. This task involves configuring Nginx to run as the `nginx` user and listen on port 8080.

#### Requirements:
- Nginx must be running as the `nginx` user.
- Nginx must be listening on all active IPs on port 8080.
- You cannot use `apt-get remove`.

#### After Debugging:
```bash
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

## Repository Structure
```
alx-system_engineering-devops/
├── 0x12-web_stack_debugging_2/
│   ├── 0-iamsomeoneelse
│   ├── 1-run_nginx_as_nginx
│   └── README.md
```

## Usage
### Task 0: Run Software as Another User
```bash
./0-iamsomeoneelse <username>
```

### Task 1: Run Nginx as Nginx
```bash
./1-run_nginx_as_nginx
```

## Author
- **Your Name** - [taus95](https://github.com/Tausi95)
