kcsrv
=====
**kcsrv** is a project to try to implement an open source KanColle server using Python 3.x.  
It's currently under very heavy development. Check back later, but if you're really curious, read on and get yourself a 
copy.

What Currently Works
--------------------
- Game login
- First ship enlistment (Fubuki and friends)
- Main port screen
- Resources things (furniture, sound, etc)
- Ship building (sort of ehh)
- Remodelling/Modernization (sort of)

What Doesn't Work
--------------------
- Anything not listed above. This is basically everything.

FAQ
---
### Q: Will I be able to import my data from an official DMM server?
Theoretically, yes.   
The only downside is it will require your API key to import your ships2 data and your admiral information. This may get 
your account banned for whatever lame DMM reason.  
It is recommended you start fresh on your copy of this server. 

### Q: What are the requirements?
- For a dev environment, nothing more than Vagrant and Ansible are required. These will automatically fire up a toaster, 
a virtual machine, and a shipgirl ready to go to war at the local beach, ready for you to develop on.


### Q: Why is it built on Python?
* PHP is [an ungodly clusterfuck](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design).
* Ruby is a massive resource hog, and this server needs to be able to scale well.  
* NodeJS is hipster Javascript technology, and JS isn't exactly the best thing.

Python, with a sufficient WSGI server, can hold its own against Ruby and NodeJS in terms of performance, and this app 
requires little more than database accesses.

### Q: Why PostgreSQL?
* ***MySQL*** is [notoriously awful](http://grimoire.ca/mysql/choose-something-else), with the most important piece of 
incompetent nonsense being the lack of Transactional DDL... which means a failed migration (for whatever reason) may 
leave the database in an inconsistent state.
* ***SQLite*** is a good second choice, but it sometimes behaves oddly, and lacks some more advanced features. It'll 
also slow down with a lot of data.
* ***MS SQL and Oracle*** lol I hope you like enterprise nonsense.

Development Setup
---

The development environment is all taken care of by Vagrant and the Ansible provisioner.

Running `vagrant up` will automatically pull in and add all the dependencies. The default config.example.py supplies 
correct defaults for the provisioned database.  

The server will become accessible on IP 10.1.1.4, port 80, by default after your first reboot. The development server 
will be proxied through the index, and the gunicorn production will be proxied through /kcsprod/.  
The dev server will automatically restart when you make your changes. If you save with broken code, supervisor will 
stop restarting, and you'll have to login and start it manually.



