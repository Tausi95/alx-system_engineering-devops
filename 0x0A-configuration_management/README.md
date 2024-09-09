---

# 0x0A-Configuration Management

This project involves using **Puppet** to automate configuration tasks such as creating files, installing packages, and executing commands. The tasks are aimed at familiarizing users with Puppet's basic syntax on Ubuntu 20.04 LTS.

## General Requirements

- All files are interpreted on **Ubuntu 20.04 LTS**.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- All Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
- All Puppet manifests must run without errors.
- Each Puppet manifest's first line must be a comment explaining its purpose.
- All Puppet manifests files must end with the `.pp` extension.

## Versioning Notes

- The Ubuntu 20.04 VM should have **Puppet 5.5** preinstalled.
- Puppet is not upgraded in this project. It focuses on familiarizing users with basic syntax, which is almost identical in newer versions.
- Install `puppet-lint` for syntax checking:
  ```bash
  gem install puppet-lint
  ```

## Tasks

### 0. Create a File (Mandatory)

Using Puppet, create a file at `/tmp/school`.

#### Requirements:
- File path: `/tmp/school`
- File permission: `0744`
- File owner and group: `www-data`
- File content: `I love Puppet`

#### Example:
```bash
puppet apply 0-create_a_file.pp
```

The file will be created with the specified properties and content.

#### Manifest:
```puppet
# This manifest creates a file in /tmp with specific permissions, ownership, and content
file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
```

---

### 1. Install a Package (Mandatory)

Using Puppet, install Flask from `pip3`.

#### Requirements:
- Install Flask version `2.1.0`.

#### Example:
```bash
puppet apply 1-install_a_package.pp
```

After applying the manifest, Flask version 2.1.0 will be installed, and you can verify the installation with:
```bash
flask --version
```

#### Manifest:
```puppet
# This manifest installs Flask version 2.1.0 using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
```

---

### 2. Execute a Command (Mandatory)

Using Puppet, create a manifest that kills a process named `killmenow`.

#### Requirements:
- Use the `exec` Puppet resource.
- Use the `pkill` command.

#### Example:
```bash
puppet apply 2-execute_a_command.pp
```

After running this manifest, the process named `killmenow` will be terminated.

#### Manifest:
```puppet
# This manifest kills a process named 'killmenow'
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
```

---

## Installation Guide

1. **Install Puppet**:
   ```bash
   apt-get install -y ruby=1:2.7+1 --allow-downgrades
   apt-get install -y ruby-augeas
   apt-get install -y ruby-shadow
   apt-get install -y puppet
   ```

2. **Install puppet-lint**:
   ```bash
   gem install puppet-lint
   ```

3. **Run Manifests**:
   Use `puppet apply` to execute each manifest. For example:
   ```bash
   puppet apply 0-create_a_file.pp
   ```

---

## Author
Chancy Tsonga
