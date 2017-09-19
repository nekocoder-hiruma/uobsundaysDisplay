UOBSundays
---
This is a micro-website for UOB bank to release information with regards to UOBSundays event back in 2014.

The website is assigned to Kamiworks dev team by Avantworks and maintained by Wai Keat and Damien.

Setup
===
> Python VirtualEnv
> ---
>     * Ensure that your python version is 2.7.11
>     mkvirtualenv uobsundays(For pyenv, run pyenv virtualenv 2.7.11 uobsundays)
>     workon uobsundays
>     pip install -r requirements.txt
>
> Setup of Database in Postgres
> ---
>     Replace with desire values for database in fabfile.py
>     Run fab create_databases in console
>
> Compile Static Files
> ---
>     Run fab build in console
>   

Running
---

    src/uobsundays/manage.py runserver
    
Test
---

    src/uobsundays/manage.py test
    