kcsrv
=====

**kcsrv** is a project to try to implement an open source KanColle server.  
It's currently under very heavy development. Check back later.

What Currently Works
--------------------
- Actually logging in (this is an achievement because of how temperamental KanColle is when it doesn't get the exact response it works back
- Main port screen
- Resources things (furniture, sound, etc)


FAQ
---

### Q: Will I be able to import my data from an official server?

Theoretically, yes. The only downside is it will require your API key to import your ships2 data and your admiral information. This may get your account banned.

### Q: Why is it built on Python?

There aren't actually that many things you can build a web application on, and most of them were out from the start.

* PHP is [an ungodly clusterfuck](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/) that's insanely unwieldly, performs about as well as a football team in Antarctica and is a nightmare to maintain.  
  I've written large applications in PHP before, and I'm not going there again.

* Ruby and Java are both massive resource hogs, and this server needs to be able to scale well, preferably without me having me hire another server I can't pay for.  
  I run a JIRA (Java) and a Discourse (Ruby) instance, and they both chew up nearly everything their servers have to give.

* NodeJS is actually a good candidate, mostly thanks to being blazing fast.  
  Unfortunately, nearly everything around it (including the runtime itself) is in beta, and many things (such as database abstraction layers) simply aren't mature enough for me to want to depend on it - I have yet to see a robust migration system, for instance.  
  One day I might even port over at least parts of the server to it (the game API comes to mind), but not right now.

Python isn't the fastest thing around, but both it and its ecosystem are very stable and mature. SQLAlchemy + Alembic alone makes an incredibly robust database abstraction layer, that nothing I've seen in NodeJS can match. (Do feel free to prove me wrong though.)


Development Setup
---

Probably only works on Linux. Screw Ansible/Vagrant, too hard for me.

1.  **Set up the environment.**  

        pip install -r requirements.txt
        sudo -u postgre createuser -s $USER
        sudo -u postgre createdb kcsrv


1.  **Create the database.**  
    Repeat this to upgrade it later.
    
        ./manage.py db upgrade
        ./manage.py setup
        ./manage.py update_db

1.  **Create an account for yourself.**  
    Be sure to give yourself the `admin` and `staff` roles!
    
        ./manage.py user create


1.  **Run the development server.**  
    It will run on port 5000 by default.
    
        ./kcsrv.py
