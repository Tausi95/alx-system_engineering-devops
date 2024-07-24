, it looks like you have succeeded in configuring Nginx to run as the `nginx` user. Your `ps` command output shows that the Nginx master process is running as root, but the worker processes are running as the `nginx` user, which is the desired outcome. This indicates that Nginx has been correctly configured to drop its privileges and run its worker processes as a non-privileged user (`nginx`).

Here is a summary of your `ps` command output:
```
root      1036  0.0  0.0  51220  1500 ?        Ss   12:53   0:00      \_ nginx: master process /usr/sbin/nginx
nginx     1037  0.0  0.0  51784  5220 ?        S    12:53   0:00          \_ nginx: worker process
nginx     1038  0.0  0.0  51784  5220 ?        S    12:53   0:00          \_ nginx: worker process
```

- The Nginx master process is running as `root` (PID 1036).
- The Nginx worker processes are running as `nginx` (PIDs 1037 and 1038).

### Final Verification
To ensure everything is working correctly, you can also verify that Nginx is listening on port 8080:

```bash
nc -zv 127.0.0.1 8080
```

If the output shows that the connection is successful, then Nginx is correctly listening on port 8080.

### README.md Update
You can now update your `README.md` to reflect that the configuration changes have been successfully implemented. Here is the updated `README.md`:

```markdown
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
sudo ./1-run_nginx_as_nginx
```


## Author
Chancy Tsonga: Tausi95 [https//:github.com/Tausi95]
