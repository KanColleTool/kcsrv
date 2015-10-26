kcsrv (aka Kan'tColle Server)
=====
**kcsrv** is a project to try to implement an open source KanColle server using Python 3.x.  
It's currently under very heavy development. Check back later, but if you're really curious, read on and get yourself a copy.

What Currently Works
--------------------
- Game login
- First ship enlistment (Fubuki and friends)
- Main port screen
- Resources things (furniture, sound, etc)
- Ship building (sort of)
- Heartlocking (sort of)

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
* PHP is [an ungodly clusterfuck](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design).
* Ruby is a massive resource hog, and this server needs to be able to scale well.  
* NodeJS is actually a good candidate, mostly thanks to being blazing fast.  
  Unfortunately, nearly everything around it (including the runtime itself) is in beta.

Python isn't the fastest thing around, but both it and its ecosystem are very stable and mature.

### Q: Why PostgreSQL?
* ***MySQL*** is [notoriously awful](http://grimoire.ca/mysql/choose-something-else), with the most important piece of incompetent nonsense being the lack of Transactional DDL... which means a failed migration (for whatever reason) may leave the database in an inconsistent state.
* ***SQLite*** is a good second choice, but it sometimes behaves oddly, and lacks some more advanced features. It'll also slow down with a lot of data, not that a development server is really in any danger of hitting that point.
* ***MS SQL and Oracle*** lol I hope you like enterprise nonsense.

Development Setup
---

### Ingredients:

* Python 3
* ```virtualenv```
* PostgreSQL (+ development headers)

Cooking Instructions:
---  
1.  **Set up the environment.**

    	git clone http://github.com/kancolletool/kcsrv.git kcsrv
    	cd kcsrv
    	virtualenv -p /usr/bin/python3 .
    	source ./bin/activate
        
    Now, enter the project's Virtual Environment. This contraption allows you to install packages locally, without conflicting with system packages. It's activated per-terminal, and must be activated before interacting with the project in any way:
  
        # Not a typo; `.` is an alias for `source`  
        . bin/activate
        
    If you wish to exit it again, simply run:

        deactivate
        
1. **Install dependencies.**  
    Inside the virtualenv, simply run:

    	pip install -r requirements.txt

    If you ever get issues with things not being found, try re-running this and seeing what happens.
    
1. **Set up the database***  
    First, make sure you have a database user for the account you plan on running the server as. Postgres can automatically authorize as the user a process is running as, which means there's no need to put passwords in configuration files.

        sudo -u postgres createuser --superuser $USER
        
    Then, create a database for kcsrv to use:
    
        createdb kcsrv  

    Change postgres to what user the server installs as. On Debian/Ubuntu it's postgres.
    And fill it with data - repeat this after every upgrade:
    
        ./manage.py db upgrade   # Run migrations
        ./manage.py update_db # Imports ship data into the database
        
    First Boot? You'll need to set up a few things.
    
        ./manage.py setup

1. **Download the DMM assets.**  
    This will take a while... you may want to re-run it after game patches, to stay up-to-date. At this point, grab a coffee.

    Please note that this won't pull new ships automatically, you'll need to feed the server a new api_start2.json every time DMM introduces more ships to collect. Gotta ship 'em all!

        ./manage.py dlassets
1.  **Setup your config file.**
    Make sure to edit the file and add password salts and your secret key.
    
        cp ./config.example.py ./config.py
    
1.  **Create an account for yourself.**  
    Be sure to give yourself the `admin` and `staff` roles!
    Depending on your terminal, you may need to put the email address in quotation marks.

        ./manage.py user create username user@localhost
    
1.  **Run the server.**  
    It will run on port 5000 by default.

        ./kcsrv.py
        
    Or, if you want to use the gunicorn server, run this:
    
        ./start.sh
        

1.  **Connect to the game**  
  Since the game will always connect on Port 80 (blame Flash), you need to proxy the dev server to your local Port 80:

      sudo ssh $USER@localhost -L 80:localhost:5000 -N
  
  On Windows, you can also use [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) - look under SSH Options -> Tunnels in the connection dialog to set up the tunnel.