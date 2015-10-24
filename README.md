kcsrv (aka Kan'tColle Server) - db-remodel branch
=====
First of all, this branch is not intended to be used. I'll probably commit a lot of bad ideas and generally break everything everytime. If you want a "working" copy, clone the main branch.


The idea here is to begin to elaborate ideas to make the db stable and also make working the models easy. I'll start with this in mind:

I'll abandon Helpers as means to do models operations, using class methods instead. Mostly because admiral.grant\_resources(resources) is so much better than AdmiralHelper.admiral\_grant\_resources(admiral,resources).

The immediate problem this creates is the db file would get pretty much unmanegeable. So this is the hard part. How to partition the db file in a intuitive way? 

One file for each class is out of the question, because really, fuck that.

Other option would be making the most important classes in the same file (say 5-6), while the lesser ones would be grouped in another. This would just kill the point of making the file easy to use, since the most important classes will have the most number of methods.

So what's left is some arbitrary categorization that may or may not be clear, depending on the reader. Let's see how this goes.

The idea is that all the big "things" in the game will have their file with its name and the minor related things will be in the same file.

So the initial setup will be something like

  admiral.py
  
      Admiral, AdmiralItem,Fleet, Dock
      
  ship.py
  
      Ship,Remodel,Recipe
      
  admiralship.py
  
      AdmiralShip,AdmiralShipItem
      
  quest.py
  
      Quest,QuestRequirement,QuestBonus
  
  support.py
      
      Resources, Stats
      
etc, etc.

There are some clear issues and most certainly others that I'll find out soon enough, but as an starting point I think it's ok, at least to have an idea of what the code would look like.

And that's all the purpose of this branch. Please look forward for the chaos that ensues.

Oh, as a side note, I'll be definitely changing AdmiralShip class name. It's too important of a class to have an associative name. I'm thinking Kanmusu or Shipgirl, because it's clear that is a Ship owned by an Admiral. I'm leaning more towards Kanmusu because it rolls off the tongue better, but we'll see.
