Ansible *Discogs Proxy-Server* Role
========================================

A minimal Ansible role that installs and configureas a minimal [Discogs](http://discogs.org/) proxy-server.

The setup here only aims to provide proxyed/local access to the Discogs API (a.k.a. Web-Service). The web-frontend it self however
is included, but not treated with too much love...


Requirements
------------

 - Debian 8.x
   + Debian < 8.x: We don't have any reasons to support older versions. Most things actually should work fine, but `wheezy`does not include `nodejs`/`npm`
   + ubuntu: Should/could work as well, but has never been tested.

 - The instance used to deploy to must have at least **25GB** of free disk space (for replication-data).
 - Patience. Running this role for the first time (and having the replication-data loaded) will take ine to two hours.
   (even longer on a slow uplink, as the required dumps are 2GB+)

Role Variables
--------------

- `discogs_include_common`: include common packages & settings
- `discogs_hostname`: my.local.proxy.example.com
- `discogs_include_nginx`: install local nginx instance


Example Playbook
----------------

Minimal usage example:

    - hosts: dgs-proxys
      roles:
        - {
            role: hzlf.discogs-proxy,
            discogs_hostname: "my.local.proxy.example.com",
          }


License
-------

BSD
