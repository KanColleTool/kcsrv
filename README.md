kcsrv
=====
**kcsrv** is a project to try to implement an open source KanColle server using Python 3.x.
It's currently under very heavy development. Check back later, but if you're really curious, read on and get yourself a copy.

What Currently Works
--------------------
- Actually logging in (this is an achievement because of how temperamental KanColle is when it doesn't get the exact response it works back
- Main port screen
- Resources things (furniture, sound, etc)

What Doesn't Work
--------------------
- Anything not listed above.

FAQ
---

### Q: Will I be able to import my data from an official DMM server?
Theoretically, yes.   
The only downside is it will require your API key to import your ships2 data and your admiral information. This may get your account banned for whatever lame DMM reason.  
It is recommended you start fresh on your copy of this server. 

### Q: What is the recommended requirements?
- Debian or Ubuntu based distro. Fedora and friends may work, but please, YMMV.
- Python 3.x and knowledge about virtualenv (setup and activate).
- Internet connection to download the DMM assets.

Protip: Use a VM (VMWare, VirtualBox). If you mess up, simply hose it and start squeaky clean. Or you can use an ARM based linux box (R-Pi, ODROID, etc).

### Q: Why is it built on Python?
There aren't actually that many things you can build a web application on, and most of them were out from the start.  
There was a large rant by one the kcsrv owner, I (SoftwareGuy) who improved this FAQ have condensed it down to make it less ranty.

* PHP is [an ungodly clusterfuck](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/).
* Ruby and Java are both massive resource hogs, and this server needs to be able to scale well. Ruby / Java seem to eat the server alive.
* NodeJS is actually a good candidate, mostly thanks to being blazing fast.  
  Unfortunately, nearly everything around it (including the runtime itself) is in beta.

In short, Python isn't the fastest thing around, but both it and its ecosystem are very stable and mature. SQLAlchemy + Alembic alone makes an incredibly robust database abstraction layer.


Development Setup
---
Make sure you have postgresql, postgresql development libs, python3, python3-pip python3-requests, libcurl-openssl-dev and virtualenv packages installed. Consult your package manager for those packages to be installed (yum, apt-get...)

1.  **Set up the environment.**  

        git clone http://github.com/kancolletool/kcsrv.git kcsrv
        cd kcsrv
    Only run virtualenv once. You'll break the environment if you do it every time! (If you're booting the server after first time, just skip this line)
        virtualenv -p /usr/bin/python3 .
        (wait for output to cease)
        source ./bin/activate
    Ensure the terminal changes to something like (kcsrv)user@box:~/kcsrv/$ . You're now inside python's virtual environment.
        pip install -r requirements.txt
    If you get errors here, stop and install the packages it needs, then rerun the pip command. Consult your package manager.
        sudo -u postgres createuser -s $USER
        sudo -u postgres createdb kcsrv  
    Change postgres to what user the server installs as. On Debian/Ubuntu it's postgres.

1.  **Create the database.**  
        ./manage.py db upgrade
        ./manage.py setup
        ./manage.py update_db

    To update the server's SQL database at a, you will need to stop the server and run the following:
        ./manage.py db upgrade heads
    Running just "db upgrade" by itself when you've already got a working database throws errors with SQLAlchemy about braches, heads and oh my.

1. ** Download the DMM assets.**  
    This will take a while. 
        ./manage.py dlassets

1.  **Create an account for yourself.**  
    Be sure to give yourself the `admin` and `staff` roles!
        ./manage.py user create <username> <email>
    Where username is your admin username and email is your email. You may need to put a backslash in front of your @ sign or put the email in quotes.    

1.  **Run the development server.**  
    It will run on port 5000 by default.
        ./kcsrv.py

    You'll need to do a SSH Tunnel from remote port 5000 to local port 80, because the Kantai Collection Core SWF files communicate hardcodedly on port 80.  
    
    A nginx configuration for proxy server will come later.
