kcsrv
=====

**kcsrv** is a project to try to implement an open source KanColle server.  
It's currently under very heavy development, and no part of the game server even works. Check back later.

FAQ
---

##### Q: Will I be able to import my data from an official server?

Yup, you will be able to zip up [KanColleTool](https://github.com/KanColleTool/KanColleTool)'s cache folder and thus import your old information. We will not ask for your API link to do this, nor touch your old server in any way.

#### Q: Why is it built on Python?

There aren't actually that many things you can build a web application on, and most of them were out from the start.

* PHP is [an ungodly clusterfuck](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/) that's insanely unwieldly, performs about as well as a football team in Antarctica and is a nightmare to maintain.
  
  I've written large applications in PHP before, and I'm not going there again.

* Ruby and Java are both massive resource hogs, and this server needs to be able to scale well, preferably without me having me hire another server I can't pay for.
  
  I run a JIRA (Java) and a Discourse (Ruby) instance, and they both chew up nearly everything their servers have to give.

* NodeJS is an actually good candidate, mostly thanks to being blazing fast.
  
  Unfortunately, nearly everything around it (including the runtime itself) is in beta, and many things (such as database abstraction layers) simply aren't mature enough for me to want to depend on it - I have yet to see a robust migration system, for instance.
  
  One day I might even port over at least parts of the server to it (the game API comes to mind), but not right now.

Python isn't the fastest thing around, but both it and its ecosystem are very stable and mature. SQLAlchemy + Alembic alone makes an incredibly robust database abstraction layer, that nothing I've seen in NodeJS can match. (Do feel free to prove me wrong though.)
