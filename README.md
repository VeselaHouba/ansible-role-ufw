# Ansible veselahouba.ufw role

![Release](https://github.com/VeselaHouba/ansible-role-ufw/workflows/Release/badge.svg)
[![Build Status](https://drone.m-cloud.cz/api/badges/VeselaHouba/ansible-role-ufw/status.svg)](https://drone.m-cloud.cz/VeselaHouba/ansible-role-ufw)

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
