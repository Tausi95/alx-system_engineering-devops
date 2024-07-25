```markdown
# 0x0B. SSH

## Description
This project involves configuring SSH to securely connect to a remote server using RSA keys. The tasks will cover generating RSA key pairs, configuring the SSH client, and setting up public key authentication.

## Learning Objectives
By the end of this project, you should be able to explain:
- What a server is and where servers usually reside
- What SSH is and how it works
- How to create and use an SSH RSA key pair for authentication
- The advantages of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the folder is mandatory
- All Bash scripts must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

## Tasks

### Task 0: Use a Private Key
Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

### Task 1: Create an SSH Key Pair
Write a Bash script that creates an RSA key pair named `school` with 4096 bits, protected by the passphrase `betty`.

### Task 2: Client Configuration File
Configure your local SSH client to use the private key `~/.ssh/school` and refuse to authenticate using a password.

### Task 3: Let Me In!
Add the given public key to your server to allow connections using the `ubuntu` user.

## Resources
- [What is a (physical) server - text](https://example.com)
- [SSH essentials](https://example.com)
- [SSH Config File](https://example.com)
- [Public Key Authentication for SSH](https://example.com)
- [How Secure Shell Works](https://example.com)
- [SSH Crash Course](https://example.com)

## Reference Materials
- [Understanding the SSH Encryption and Connection Process](https://example.com)
- [Secure Shell Wiki](https://example.com)
- [IETF RFC 4251](https://example.com)

## Usage
Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/alx-system_engineering-devops.git
cd alx-system_engineering-devops/0x0B-ssh
```

## Author
Chancy Tsonga
``
