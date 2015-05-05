#!/usr/bin/env python3
# ^ can someone check if that works? (i got ": No such file or directory" from bash).
# -*- coding: utf-8 -*-

# Kantai Collection Downloader Script for assets.
# Written by Coburn (SoftwareGuy on GitHub)
# Please make sure you have json and pyCURL installed!

import json
import os.path

# Define some stuff for later use.
# Thank you for KCT's uppfinnarn for this code snippet that I've adapted
# For some reason my python3.4 on Ubuntu 14.04 doesn't like utf-8. Da fuq?
def load_datadump(filename) -> dict:
    with open(os.path.join(filename)) as f:
        o = json.loads(f.read(), 'utf-8')
        return o if not 'api_data' in o else o['api_data']


def get_standardSWF():
    print("NOTE: This may take a while, so grab a tea, coffee or a drink.")
    # These arrays will need to be updated with extra SWF filenames.
    coreSwfFiles = ["Core.swf", "mainD2.swf", "PortMain.swf"]  # Core game files. Wrappers?
    resourceSwfFiles = ["commonAssets.swf", "font.swf", "icons.swf", "sound_bgm.swf",
                        "sound_se.swf"]  # Core game resources
    sceneSwfFiles = ["AlbumMain.swf", "ArsenalMain.swf", "DutyMain.swf", "InteriorMain.swf", "ItemlistMain.swf",
                     "OrganizeMain.swf", "RecordMain.swf", "RemodelMain.swf", "RepairMain.swf", "SallyMain.swf",
                     "SupplyMain.swf", "TitleMain.swf", "tutorial.swf"]  # All the scenes I can remember.

    print("Getting core files...")
    for file in coreSwfFiles:
        with open("kcs/" + file, 'wb') as outFile:
            c = pycurl.Curl()
            c.setopt(c.URL, "http://203.104.209.39/kcs/" + file)
            c.setopt(c.WRITEDATA, outFile)
            c.perform()
            c.close()
        print("... Downloaded " + file)

    print("Getting resource files...")
    for file in resourceSwfFiles:
        with open("kcs/resources/swf/" + file, 'wb') as outFile:
            c = pycurl.Curl()
            c.setopt(c.URL, "http://203.104.209.39/kcs/resources/swf/" + file)
            c.setopt(c.WRITEDATA, outFile)
            c.perform()
            c.close()
        print("... Downloaded " + file)

    print("Getting scene files...")
    for file in sceneSwfFiles:
        with open("kcs/scenes/" + file, 'wb') as outFile:
            c = pycurl.Curl()
            c.setopt(c.URL, "http://203.104.209.39/kcs/scenes/" + file)
            c.setopt(c.WRITEDATA, outFile)
            c.perform()
            c.close()
        print(".. Downloaded " + file)

    return


def get_shipGirlGFX(filename):
    dump = load_datadump(filename)
    shipGFX = dump['api_mst_shipgraph']
    count = 1
    for ship in shipGFX:
        with open("kcs/resources/swf/ships/" + ship['api_filename'] + ".swf", 'wb') as outFile:
            print("Getting ship graphics. API ID: " + str(count) + ", file name: " + ship[
                'api_filename'] + ", shipgirl ID " + str(ship['api_sortno']) + ".")
            c = pycurl.Curl()
            c.setopt(c.URL, "http://203.104.209.39/kcs/resources/swf/ships/" + ship['api_filename'] + ".swf")
            c.setopt(c.WRITEDATA, outFile)
            c.perform()
            c.close()
        print(".. Downloaded GFX for shipgirl ID " + str(ship['api_sortno']) + "(" + str(count) + ")")
        count += 1
    return


def setup_directories():
    print("Prep work: Setting up directories, if they don't exist already...")
    if not os.path.exists("kcs"): os.makedirs("kcs")
    if not os.path.exists("kcs/scenes"): os.makedirs("kcs/scenes")
    if not os.path.exists("kcs/sound"): os.makedirs("kcs/sound")

    if not os.path.exists("kcs/resources"): os.makedirs("kcs/resources")
    if not os.path.exists("kcs/resources/bgm_p"): os.makedirs("kcs/resources/bgm_p")
    if not os.path.exists("kcs/resources/swf"): os.makedirs("kcs/resources/swf")
    if not os.path.exists("kcs/resources/swf/ships"): os.makedirs("kcs/resources/swf/ships")

    # if not os.path.exists("kcs/resources/sound"): os.makedirs("kcs/resources/sound")
    print("Done prep work.")
    return

# End defines. Start main code.
if __name__ == "__main__":
    print("Starting download of Kantai Collection assets. Please wait...")
    print("If you have an error, please ensure you have cURL for python installed.")
    print("Usually on Debian and friends you can do 'apt-get install python3-pycurl' to install the correct version.")
    import pycurl
    # Load the datafile into memory.
    if os.path.isfile("data/api_start2.json"):
        print("Ok, found a JSON data dump.")

        print("Begin...")

        setup_directories()
        get_standardSWF()
        get_shipGirlGFX("data/api_start2.json")

        print("...Finish")
        exit()
    else:
        print("Error! Can't find the api_start2.json file.")
        print(
            "This is fixable. Make a directory called 'data' and place the JSON dump (obtained from KCT or through other means) as 'api_start2.json' there.")
        print(
            "You can modify this script to change the path the script's looking for, but please - if it ain't broke, don't fix it.")
        exit()
