
# Web Stack Debugging #3

## Project Overview

This project focuses on debugging a Wordpress website running on a LAMP stack (Linux, Apache, MySQL, PHP). The goal is to identify and fix issues causing a 500 Internal Server Error using `strace` and automate the fix using Puppet.

## Requirements

- **Operating System**: Ubuntu 14.04 LTS
- **Puppet Version**: 3.4
- **Puppet Lint Version**: 2.1.1

## Tasks

### 0. Strace is Your Friend

**Objective**: Diagnose and fix a 500 Internal Server Error in Apache using `strace`, then automate the fix with Puppet.

1. **Diagnose the Issue**:
   - Use `strace` to identify the root cause of the 500 error.
   - `strace` can attach to a running process and trace system calls and signals.

2. **Fix the Issue**:
   - Apply the fix manually and verify the resolution by checking the HTTP status code and response content.

3. **Automate with Puppet**:
   - Create a Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix.
   - Ensure that the manifest passes `puppet-lint` and runs successfully.

## Usage

1. **Install Puppet and Puppet Lint**:
   ```bash
   $ apt-get install -y ruby
   $ gem install puppet-lint -v 2.1.1
   ```

2. **Apply the Puppet Manifest**:
   ```bash
   $ puppet apply 0-strace_is_your_friend.pp
   ```

3. **Verify the Fix**:
   - Check the HTTP status code:
     ```bash
     $ curl -sI 127.0.0.1
     ```
   - Ensure it returns `200 OK` instead of `500 Internal Server Error`.

## Files

- `0-strace_is_your_friend.pp`: Puppet manifest to automate the fix for the identified issue.

## Notes

- Ensure all Puppet manifests end with a `.pp` extension.
- All files should end with a new line.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
