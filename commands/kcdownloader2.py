#!/usr/bin/env python3
# ^ can someone check if that works? (i got ": No such file or directory" from bash).
# -*- coding: utf-8 -*-

# Kantai Collection Downloader Script for assets.
# Written by Coburn (SoftwareGuy on GitHub)
# Please make sure you have json and requests installed!
import json
import os.path

import requests


# Define some stuff for later use.
# Thank you for KCT's uppfinnarn for this code snippet that I've adapted
def load_datadump(filename) -> dict:
    with open(os.path.join(filename)) as f:
        o = json.loads(f.read(), 'utf-8')
        return o if not 'api_data' in o else o['api_data']


def get_file(file):
    r = requests.get("http://203.104.209.39/" + file, stream=True)
    if r.status_code == 200:
        return r
    else:
        return None


def get_standard_swf():
    print("NOTE: This may take a while, so grab a tea, coffee or a drink.")
    # These arrays will need to be updated with extra SWF filenames.
    core_swf_files = ["Core.swf", "mainD2.swf", "PortMain.swf"]  # Core game files. Wrappers?
    resource_swf_files = ["commonAssets.swf", "font.swf", "icons.swf", "sound_bgm.swf",
                          "sound_se.swf", "itemicons.swf"]  # Core game resources
    scene_swf_files = ["AlbumMain.swf", "ArsenalMain.swf", "DutyMain.swf", "InteriorMain.swf", "ItemlistMain.swf",
                       "OrganizeMain.swf", "RecordMain.swf", "RemodelMain.swf", "RepairMain.swf", "SallyMain.swf",
                       "SupplyMain.swf", "TitleMain.swf", "tutorial.swf"]  # All the scenes I can remember.

    print("Getting core files...")
    for file in core_swf_files:
        with open("kcs/" + file, 'wb') as out:
            f = get_file('kcs/' + file)
            if f:
                for chunk in f.iter_content(2048):
                    out.write(chunk)
                print("... Downloaded " + file)
            else:
                print("... No such file " + file)

    print("Getting resource files...")
    for file in resource_swf_files:
        with open("kcs/resources/swf/" + file, 'wb') as out:
            f = get_file("kcs/resources/swf/" + file)
            if f:
                for chunk in f.iter_content(2048):
                    out.write(chunk)
                print("... Downloaded " + file)
            else:
                print("... No such file " + file)

    print("Getting scene files...")
    for file in scene_swf_files:
        with open("kcs/scenes/" + file, 'wb') as out:
            f = get_file("kcs/scenes/" + file)
            if f:
                for chunk in f.iter_content(2048):
                    out.write(chunk)
                print("... Downloaded " + file)
            else:
                print("... No such file " + file)


def get_ship_girl_data(filename):
    dump = load_datadump(filename)
    ships = dump['api_mst_shipgraph']
    count = 1
    for ship in ships:
        if not os.path.exists("kcs/sound/ship/kc{}".format(ship['api_filename'])):
            os.makedirs("kcs/sound/ship/kc{}".format(ship['api_filename']))
        with open("kcs/resources/swf/ships/" + ship['api_filename'] + ".swf", 'wb') as out:
            print("Getting ship graphics. API ID: {}, file name: {}, shipgirl ID.".format(count, ship['api_filename'],
                                                                                          ship['api_sortno']))
            f = get_file("kcs/resources/swf/ships/" + ship['api_filename'] + '.swf')
            if f:
                for chunk in f.iter_content(2048):
                    out.write(chunk)
                print(".. Downloaded GFX for shipgirl ID " + str(ship['api_sortno']) + "(" + str(count) + ")")
            else:
                print("... No such file " + ship['api_filename'])
            print("Downloading ship sounds...")
        for x in range(1, 70): # 1-70 is a reasonable guess.
            f = get_file("kcs/sound/kc{}/{}.mp3".format(ship['api_filename'], x))
            if f:
                with open("kcs/sound/ship/kc{}/{}.mp3".format(ship['api_filename'], x), 'wb') as out:
                    for chunk in f.iter_content(2048):
                        out.write(chunk)
                    print("Downloaded sound ID {} for shipgirl ID {}".format(x, ship['api_sortno']))
            else:
                print("... No such file kc" + ship['api_filename'] + "/" + str(x) + ".mp3")
        count += 1


def setup_directories():
    print("Prep work: Setting up directories, if they don't exist already...")
    if not os.path.exists("kcs"): os.makedirs("kcs")
    if not os.path.exists("kcs/scenes"): os.makedirs("kcs/scenes")
    if not os.path.exists("kcs/sound"): os.makedirs("kcs/sound")

    if not os.path.exists("kcs/resources"): os.makedirs("kcs/resources")
    if not os.path.exists("kcs/resources/bgm_p"): os.makedirs("kcs/resources/bgm_p")
    if not os.path.exists("kcs/resources/swf"): os.makedirs("kcs/resources/swf")
    if not os.path.exists("kcs/resources/swf/ships"): os.makedirs("kcs/resources/swf/ships")

    if not os.path.exists("kcs/sound/ship"): os.makedirs("kcs/sound/ship")
    print("Done prep work.")


def run():
    print("Starting download of Kantai Collection assets. Please wait...")
    print("If you have an error, please ensure you have Python-Requests installed.")
    print("Usually on Debian and friends you can do 'apt-get install python3-requests' to install the correct version.")
    print("Otherwise, run \"pip install requests\".")
    # Load the datafile into memory.
    if os.path.isfile("data/api_start2.json"):
        print("Ok, found a JSON data dump.")

        print("Begin...")

        setup_directories()
        get_standard_swf()
        get_ship_girl_data("data/api_start2.json")

        print("...Finish")
        exit()
    else:
        print("Error! Can't find the api_start2.json file.")
        print(
            "This is fixable. Make a directory called 'data' and place the JSON dump (obtained from KCT or through other means) as 'api_start2.json' there.")
        print(
            "You can modify this script to change the path the script's looking for, but please - if it ain't broke, don't fix it.")
        exit()
