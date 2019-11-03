# Ansible Role: jeremyweber72.ansible_role_maven

An Ansible role that installs Apache Maven on linux.  Forked from aholbreich.maven

## Requirements

Linux/Unix

## Role Variables

maven_version: 3.3.9 (Default)

## Dependencies

No hard dependencies for installation. But you keep in mind that you need java.

## Example Playbook

    - hosts: webservers
      roles:
        - { role: jeremyweber72.ansible_role_maven }

## License

MIT