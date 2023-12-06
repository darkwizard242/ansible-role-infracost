[![build-test](https://github.com/darkwizard242/ansible-role-infracost/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-infracost/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-infracost/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-infracost/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/59436?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/59436?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/59436?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-infracost&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-infracost) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-infracost&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-infracost) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-infracost&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-infracost) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-infracost&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-infracost) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-infracost?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-infracost?color=orange&style=flat-square)

# Ansible Role: infracost

Role to install (_by default_) [infracost](https://www.infracost.io) on **Debian/Ubuntu** and **EL** systems. **infracost** shows cloud cost estimates for [Terraform](https://www.terraform.io/).

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
infracost_app: infracost
infracost_version: 0.10.31
infracost_os: linux
infracost_arch: amd64
infracost_dl_url: https://github.com/{{ infracost_app }}/{{ infracost_app }}/releases/download/v{{ infracost_version }}/{{ infracost_app }}-{{ infracost_os }}-{{ infracost_arch }}.tar.gz
infracost_bin_path: /usr/local/bin
infracost_file_owner: root
infracost_file_group: root
infracost_file_permission_mode: '0755'
```

### Variables table:

Variable                       | Description
------------------------------ | -----------------------------------------------------------------------------------------------------------------------------------------------------------
infracost_app                  | Defines the app to install i.e. **infracost**
infracost_version              | Defined to dynamically fetch the desired version to install. Defaults to: **0.10.31**
infracost_os                   | Defines os type. Defaults to: **linux**
infracost_arch                 | Defines os architecture. Defaults to: **amd64**
infracost_dl_url               | Defines URL to download the infracost binary from.
infracost_bin_path             | Defined to dynamically set the appropriate path to store infracost binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
infracost_file_owner           | Owner for the binary file of infracost.
infracost_file_group           | Group for the binary file of infracost.
infracost_file_permission_mode | Defines the permission mode level for the file. Defaults to: `0755`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **infracost**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.infracost
```

For customizing behavior of role (i.e. specifying the desired **infracost** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.infracost
  vars:
    infracost_version: 0.10.0
```

For customizing behavior of role (i.e. placing binary of **infracost** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.infracost
  vars:
    infracost_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-infracost/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
