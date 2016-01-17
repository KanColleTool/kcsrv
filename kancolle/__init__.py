"""
So we gonna need a way to check quest progress.
This might be as simple as checking if Admiral has a Ship or we might have to check if he completed 1-1 4 times while jumping in one leg
I have no idea.

At first I intended to write a simple function for each Quest, but the Admiral can activate and deactivate stuff at will, so we have to
make it persistent somehow.

So my idea is to have a column in the AdmiralQuest table that saves a JSON with quest data and then the function reads and interprets this. 

Please look forward for the chaos that ensues.
"""
