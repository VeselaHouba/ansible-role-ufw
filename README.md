# Ansible veselahouba.ufw role

> `veselahouba.ufw` is an [Ansible](http://www.ansible.com) role which:
>
> * installs ufw
> * configures ufw
> * configures ufw rules
> * configures service

## Installation

Using `ansible-galaxy`:

```shell
$ ansible-galaxy install veselahouba.ufw
```

Using `requirements.yml`:

```yaml
- name: veselahouba.ufw
```

Using `git`:

```shell
$ git clone https://github.com/veselahouba/ansible-role-ufw.git veselahouba.ufw
```

## Dependencies

* Ansible >= 2.8

## Variables

Please consult `defaults/main.yml`.

## Based on We Are Interactive UFW role
