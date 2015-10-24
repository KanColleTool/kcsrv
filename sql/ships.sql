-- Dumped 2015-07-23.

--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = ON;
SET check_function_bodies = FALSE;
SET client_min_messages = WARNING;

SET search_path = public, pg_catalog;

--
-- Data for Name: ship; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (1, 20, '100,100', 3, '{1,1,4,0}', 15, 15, '睦月', 31, 2, 0, '{1,1,0,0}', 12, 6, 18, 5, 7, 0, 0, 0, 49, 29, 59, 18, 29,
                                                                                                        0, 2, 0, 0, 24,
                                                                                                        1,
   '睦月です。<br>はりきって、まいりましょー！', 18, '0,0,0,0,0', 13, FALSE, 254);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (2, 20, '100,100', 2, '{1,1,4,0}', 15, 15, '如月', 32, 2, 0, '{0,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18, 29,
                                                                                                        0, 2, 0, 0, 24,
                                                                                                        1,
   '如月と申します。<br>おそばに置いてくださいね。', 18, '0,0,0,0,0', 13, FALSE, 255);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (3, 20, '100,100', 2, '{1,1,4,0}', 15, 15, '長月', 35, 2, 0, '{0,1,0,0}', 15, 6, 18, 5, 7, 0, 0, 0, 69, 29, 49, 18, 29,
                                                                                                        0, 2, 0, 0, 24,
                                                                                                        1,
   '長月だ。<br>駆逐艦と侮るなよ。役に立つはずだ。', 18, '0,0,0,0,0', 13, FALSE, 258);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (4, 20, '100,100', 1, '{1,1,4,0}', 15, 15, '三日月', 37, 2, 0, '{0,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18, 29,
                                                                                                         0, 2, 0, 0, 24,
                                                                                                         1,
   'あなたが司令官ですね。三日月です。<br>どうぞお手柔らかにお願いします。', 18, '0,0,0,0,0', 13, FALSE, 260);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (5, 20, '100,100', 3, '{1,1,5,0}', 20, 15, '吹雪', 11, 2, 0, '{1,1,0,0}', 17, 10, 27, 5, 10, 0, 0, 0, 49, 29, 79, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   'はじめまして吹雪です。<br>よろしくお願い致します。', 20, '0,0,0,0,0', 15, FALSE, 201);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (6, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '白雪', 12, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 10, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   '白雪です。<br>よろしくお願いします。', 20, '0,0,0,0,0', 15, FALSE, 202);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (7, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '深雪', 14, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 10, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   '深雪だよ。<br>よろしくな！', 20, '0,0,0,0,0', 15, FALSE, 204);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (8, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '磯波', 16, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 10, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   'あ、あの…磯波と申します。<br>よろしくお願いいたします。', 20, '0,0,0,0,0', 15, FALSE, 206);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (9, 20, '100,100', 3, '{1,1,5,0}', 20, 15, '綾波', 17, 2, 0, '{1,1,0,0}', 12, 10, 27, 5, 12, 0, 0, 0, 49, 29, 79, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   'ごきげんよう。<br>特型駆逐艦、綾波と申します。', 20, '0,0,0,0,0', 15, FALSE, 207);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (10, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '敷波', 18, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 29, 1,
   'アタシの名は敷波。<br>以後よろしく。', 20, '0,0,0,0,0', 15, FALSE, 208);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (11, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '曙', 68, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   '特型駆逐艦「曙」よ。<br>って、こっち見んな！　この糞提督！', 20, '0,0,0,0,0', 15, FALSE, 231);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (12, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '潮', 70, 2, 0, '{0,1,0,0}', 20, 10, 27, 5, 12, 0, 0, 0, 79, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   '特型駆逐艦…綾波型の「潮」です。<br>もう下がってよろしいでしょうか…。', 20, '0,0,0,0,0', 15, FALSE, 233);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (13, 20, '100,100', 3, '{1,1,6,0}', 20, 15, '陽炎', 91, 2, 0, '{1,1,0,1}', 12, 10, 24, 6, 12, 0, 0, 0, 49, 29, 79, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 34, 1,
   'やっと会えた！　陽炎よ。<br>よろしくねっ！', 24, '0,0,0,0,0', 16, FALSE, 225);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (14, 20, '100,100', 2, '{1,1,6,0}', 20, 15, '不知火', 92, 2, 0, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 34, 1,
   '不知火です。<br>ご指導ご鞭撻、よろしくです。', 24, '0,0,0,0,0', 16, FALSE, 226);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (15, 20, '100,100', 1, '{1,1,6,0}', 20, 15, '黒潮', 93, 2, 0, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 34, 1,
   '黒潮や、よろしゅうな。', 24, '0,0,0,0,0', 16, FALSE, 227);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (16, 20, '100,100', 6, '{1,1,6,0}', 20, 15, '雪風', 5, 2, 0, '{0,1,1,1}', 50, 10, 24, 7, 12, 0, 0, 0, 99, 29, 79, 29,
                                                                                                          49, 0, 2, 0,
                                                                                                          0, 39, 1,
   '陽炎型駆逐艦８番艦、雪風です。<br>どうぞ、よろしくお願いしますっ！', 24, '0,0,0,0,0', 16, FALSE, 228);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (17, 20, '200,200', 4, '{2,2,10,0}', 25, 25, '長良', 42, 3, 0, '{0,1,0,2}', 12, 14, 24, 10, 13, 0, 0, 0, 49, 49, 89, 29,
                                                                                                             59, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   '軽巡、長良です。<br>よろしくお願いします！', 60, '1,1,0,0,0', 26, FALSE, 218);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (18, 12, '200,200', 2, '{2,2,10,0}', 25, 25, '五十鈴', 43, 3, 0, '{0,1,0,1}', 10, 14, 24, 10, 13, 0, 0, 0, 49, 39, 79,
                                                                                                              29, 49, 0,
                                                                                                              2, 0, 0,
                                                                                                              39, 2,
   '五十鈴です。水雷戦隊の指揮ならお任せ。<br>全力で提督を勝利に導くわ。よろしくね。', 60, '1,1,0,0,0', 26, FALSE, 219);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (19, 20, '200,200', 1, '{2,2,10,0}', 25, 25, '由良', 45, 3, 0, '{0,1,0,1}', 10, 14, 24, 10, 13, 0, 0, 0, 49, 39, 79, 29,
                                                                                                             49, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   '長良型軽巡四番艦の「由良」です。<br>どうぞ、よろしくお願いいたしますっ！', 60, '1,1,0,0,0', 26, FALSE, 220);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (20, 10, '100,400', 5, '{2,2,9,0}', 25, 25, '大井', 19, 3, 1, '{0,1,0,1}', 17, 14, 24, 11, 13, 0, 0, 0, 49, 49, 89, 29,
                                                                                                            59, 0, 2, 0,
                                                                                                            0, 39, 2,
   'こんにちはー。軽巡洋艦、大井です。<br>どうぞ、よろしくお願い致しますね。', 60, '0,0,0,0,0', 25, FALSE, 57);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (21, 10, '100,400', 4, '{2,2,9,0}', 25, 25, '北上', 20, 3, 1, '{0,1,0,1}', 15, 14, 24, 10, 13, 0, 0, 0, 69, 39, 79, 29,
                                                                                                            49, 0, 2, 0,
                                                                                                            0, 39, 2,
   'アタシは軽巡、北上。<br>まーよろしく。', 60, '0,0,0,0,0', 25, FALSE, 58);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (22, 20, '500,150', 4, '{9,18,36,3}', 120, 85, '扶桑', 26, 9, 0, '{4,0,1,3}', 5, 74, 0, 59, 23, 0, 0, 0, 39, 94, 0, 79,
                                                                                                             79, 0, 4,
                                                                                                             0, 0, 89,
                                                                                                             3,
   '扶桑型超弩級戦艦、姉の扶桑です。<br>妹の山城ともども、よろしくお願い致します。', 260, '3,3,3,3,0', 67, FALSE, 286);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (23, 20, '500,150', 4, '{9,18,36,3}', 120, 85, '山城', 27, 9, 0, '{4,0,1,3}', 5, 74, 0, 59, 23, 0, 0, 0, 39, 94, 0, 79,
                                                                                                             79, 0, 4,
                                                                                                             0, 0, 89,
                                                                                                             3,
   '扶桑型戦艦姉妹、妹のほう、山城です。<br>あの、扶桑姉さま、見ませんでした？', 260, '3,3,3,3,0', 67, FALSE, 287);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (24, 20, '100,100', 2, '{1,1,4,0}', 15, 15, '皐月', 33, 2, 0, '{0,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18, 29,
                                                                                                         0, 2, 0, 0, 24,
                                                                                                         1,
   '皐月だよっ。<br>よろしくな！', 18, '0,0,0,0,0', 13, FALSE, 256);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (25, 20, '100,100', 2, '{1,1,4,0}', 15, 15, '文月', 34, 2, 0, '{0,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18, 29,
                                                                                                         0, 2, 0, 0, 24,
                                                                                                         1,
   'あたし、文月っていうの。<br>よろしくぅ～。', 18, '0,0,0,0,0', 13, FALSE, 257);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (26, 20, '100,100', 1, '{1,1,4,0}', 15, 15, '菊月', 36, 2, 0, '{0,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18, 29,
                                                                                                         0, 2, 0, 0, 24,
                                                                                                         1,
   '私が菊月だ、共にゆこう。', 18, '0,0,0,0,0', 13, FALSE, 259);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (27, 20, '100,100', 1, '{1,1,4,0}', 15, 15, '望月', 38, 2, 0, '{0,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18, 29,
                                                                                                         0, 2, 0, 0, 24,
                                                                                                         1,
   'ん？あぁ、望月でーす。', 18, '0,0,0,0,0', 13, FALSE, 261);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (28, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '初雪', 13, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 10, 0, 0, 0, 49, 29, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 29, 1,
   '初雪……です……よろしく。', 20, '0,0,0,0,0', 15, FALSE, 203);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (29, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '叢雲', 15, 2, 1, '{0,1,0,0}', 10, 10, 27, 5, 10, 0, 0, 0, 49, 29, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 29, 1,
   'あんたが司令官ね。<br>ま、せいぜい頑張りなさい！', 20, '0,0,0,0,0', 15, FALSE, 205);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (30, 20, '100,100', 3, '{1,1,5,0}', 20, 15, '暁', 71, 2, 0, '{1,1,0,0}', 12, 10, 27, 6, 12, 0, 0, 0, 49, 29, 79, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 30, 1,
   '暁よ。<br>一人前のレディーとして扱ってよね！', 20, '0,0,0,0,0', 15, FALSE, 234);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (31, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '響', 72, 2, 0, '{0,1,0,0}', 10, 10, 27, 6, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 30, 1,
   '響だよ。<br>その活躍ぶりから不死鳥の通り名もあるよ。', 20, '0,0,0,0,0', 15, FALSE, 235);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (32, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '雷', 73, 2, 0, '{0,1,0,0}', 10, 10, 27, 6, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 30, 1,
   '雷よ！　かみなりじゃないわ！<br>そこのとこもよろしく頼むわねっ！', 20, '0,0,0,0,0', 15, FALSE, 236);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (33, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '電', 74, 2, 0, '{0,1,0,0}', 10, 10, 27, 6, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 30, 1,
   '電です。<br>どうか、よろしくお願いいたします。', 20, '0,0,0,0,0', 15, FALSE, 237);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (34, 20, '100,100', 3, '{1,1,5,0}', 20, 15, '初春', 75, 2, 0, '{1,1,0,0}', 12, 10, 27, 6, 12, 0, 0, 0, 49, 29, 79, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 31, 1,
   'わらわが初春じゃ。<br>よろしく頼みますぞ。', 20, '0,0,0,0,0', 16, FALSE, 238);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (35, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '子日', 76, 2, 0, '{0,1,0,0}', 10, 10, 27, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 31, 1,
   '初めまして、ねのひ、だよぉ！<br>艦名、読みづらくなんか、ないよね？ね？', 20, '0,0,0,0,0', 16, FALSE, 239);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (36, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '若葉', 77, 2, 0, '{0,1,0,0}', 10, 10, 27, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 31, 1,
   '駆逐艦、若葉だ。', 20, '0,0,0,0,0', 16, FALSE, 240);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (37, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '初霜', 78, 2, 0, '{0,1,0,0}', 10, 10, 27, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 31, 1,
   '初春型四番艦、初霜です。<br>皆さん、よろしくお願いします！', 20, '0,0,0,0,0', 16, FALSE, 241);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (38, 20, '100,100', 3, '{1,1,5,0}', 20, 15, '白露', 79, 2, 0, '{1,1,0,0}', 12, 10, 24, 6, 12, 0, 0, 0, 49, 29, 79, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 32, 1,
   '白露型駆逐艦一番艦、「白露」です！<br>はい、一番艦ですっ！', 22, '0,0,0,0,0', 16, FALSE, 242);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (39, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '時雨', 80, 2, 1, '{0,1,0,0}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 32, 1,
   '僕は白露型駆逐艦、「時雨」。<br>これからよろしくね。', 22, '0,0,0,0,0', 16, FALSE, 243);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (40, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '村雨', 81, 2, 0, '{0,1,0,0}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 32, 1,
   'はいはーい！白露型駆逐艦「村雨」だよ。<br>みんな、よろしくね！', 22, '0,0,0,0,0', 16, FALSE, 244);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (41, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '夕立', 82, 2, 1, '{0,1,0,0}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 32, 1,
   'こんにちは、白露型駆逐艦「夕立」よ。<br>よろしくね！', 22, '0,0,0,0,0', 16, FALSE, 245);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (42, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '五月雨', 83, 2, 0, '{0,1,0,0}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 32, 1,
   '五月雨っていいます！よろしくお願いします。<br>護衛任務はお任せください！', 22, '0,0,0,0,0', 16, FALSE, 246);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (43, 20, '100,100', 3, '{1,1,5,0}', 20, 15, '涼風', 84, 2, 0, '{1,1,0,0}', 12, 10, 24, 6, 9, 0, 0, 0, 49, 29, 79, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 32, 1,
   'ちわ！涼風だよ。<br>私が艦隊に加われば百人力さ！', 22, '0,0,0,0,0', 16, FALSE, 247);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (44, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '霰', 89, 2, 0, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19, 39,
                                                                                                         0, 2, 0, 0, 33,
                                                                                                         1,
   '霰です…<br>んちゃ…とかはいいません…よろしく…', 22, '0,0,0,0,0', 16, FALSE, 252);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (45, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '霞', 90, 2, 0, '{0,1,0,1}', 15, 10, 24, 6, 9, 0, 0, 0, 59, 29, 69, 19, 39,
                                                                                                         0, 2, 0, 0, 33,
                                                                                                         1,
   '霞よ。<br>ガンガンいくわよ。ついてらっしゃい。', 22, '0,0,0,0,0', 16, FALSE, 253);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (46, 20, '120,100', 6, '{1,1,5,0}', 25, 20, '島風', 10, 2, 0, '{0,2,1,1}', 10, 12, 45, 8, 14, 0, 0, 0, 49, 29, 89, 29,
                                                                                                           49, 0, 2, 0,
                                                                                                           0, 39, 1,
   '駆逐艦島風です。スピードなら誰にも負けません。<br>速きこと、島風の如し、です！', 30, '0,0,0,0,0', 19, FALSE, 229);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (47, 20, '150,200', 3, '{1,1,8,0}', 20, 25, '天龍', 28, 3, 0, '{0,1,0,1}', 17, 11, 18, 7, 8, 0, 0, 0, 49, 39, 59, 29,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 35, 2,
   'オレの名は天龍。<br>フフフ、怖いか？', 60, '0,0,0,0,0', 23, FALSE, 213);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (48, 20, '150,200', 3, '{1,1,8,0}', 20, 25, '龍田', 29, 3, 0, '{0,1,0,1}', 17, 11, 18, 7, 8, 0, 0, 0, 49, 39, 59, 29,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 35, 2,
   '初めまして、龍田だよ。<br>天龍ちゃんがご迷惑かけてないかなあ～。', 60, '0,0,0,0,0', 23, FALSE, 214);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (49, 20, '200,200', 2, '{2,2,10,0}', 25, 25, '名取', 44, 3, 0, '{0,1,0,1}', 10, 14, 24, 10, 13, 0, 0, 0, 49, 39, 79, 29,
                                                                                                             49, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   '名取といいます。<br>ご迷惑をおかけしないように、が、頑張ります。', 60, '1,1,0,0,0', 26, FALSE, 221);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (50, 20, '200,200', 4, '{2,2,10,0}', 25, 25, '川内', 46, 3, 0, '{0,1,0,2}', 12, 14, 24, 11, 13, 0, 0, 0, 49, 49, 89, 29,
                                                                                                             59, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   '川内、参上。<br>夜戦なら任せておいて！', 60, '1,1,0,0,0', 26, FALSE, 222);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (51, 20, '200,200', 1, '{2,2,10,0}', 25, 25, '神通', 47, 3, 0, '{0,1,0,1}', 10, 14, 24, 11, 13, 0, 0, 0, 49, 39, 79, 29,
                                                                                                             49, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   'あの……軽巡洋艦、神通です。<br>どうか、よろしくお願い致します……', 60, '1,1,0,0,0', 26, FALSE, 223);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (52, 20, '200,200', 2, '{2,2,10,0}', 25, 25, '那珂', 48, 3, 0, '{0,1,0,1}', 10, 14, 24, 11, 13, 0, 0, 0, 49, 39, 79, 29,
                                                                                                             49, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   '艦隊のアイドル、那珂（なか）ちゃんだよー！<br>よっろしくぅ！', 60, '1,1,0,0,0', 26, FALSE, 224);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (53, 50, '400,770', 6, '{2,6,9,0}', 50, 25, '大井改', 97, 4, 3, '{0,4,0,1}', 10, 8, 80, 12, 13, 0, 0, 0, 49, 39, 99, 39,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 49, 2,
   '重雷装艦として、生まれ変わった大井です。<br>お久しぶりです！', 75, '0,0,0,0,0', 32, TRUE, 118);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (54, 50, '400,770', 6, '{2,6,9,0}', 50, 25, '北上改', 98, 4, 3, '{0,4,0,1}', 15, 8, 80, 12, 13, 0, 0, 0, 69, 39, 99, 39,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 49, 2,
   '新しい北上、それがアタシ。<br>酸素魚雷を満載して、ちょっと大人になったでしょ。', 75, '0,0,0,0,0', 32, TRUE, 119);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (55, 25, '250,300', 3, '{2,2,10,1}', 50, 35, '古鷹', 52, 5, 0, '{2,1,0,2}', 10, 30, 12, 25, 16, 0, 0, 0, 49, 54, 59, 34,
                                                                                                             59, 0, 3,
                                                                                                             0, 0, 49,
                                                                                                             2,
   '古鷹と言います。<br>重巡洋艦のいいところ、たくさん知ってもらえると嬉しいです。', 60, '2,2,2,0,0', 36, FALSE, 262);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (56, 25, '250,300', 1, '{2,2,10,1}', 50, 35, '加古', 53, 5, 0, '{2,1,0,2}', 10, 30, 12, 25, 16, 0, 0, 0, 49, 49, 49, 34,
                                                                                                             49, 0, 3,
                                                                                                             0, 0, 49,
                                                                                                             2,
   '古鷹型重巡の2番艦、加古ってんだ、よっろしくぅー！', 60, '2,2,2,0,0', 36, FALSE, 263);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (57, 25, '250,300', 3, '{2,2,10,1}', 50, 35, '青葉', 54, 5, 0, '{2,1,0,2}', 20, 30, 12, 26, 16, 0, 0, 0, 69, 54, 59, 37,
                                                                                                             59, 0, 3,
                                                                                                             0, 0, 49,
                                                                                                             2,
   'ども、恐縮です、青葉ですぅ！<br>一言お願いします！', 60, '2,2,2,0,0', 37, FALSE, 264);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (58, 25, '300,450', 4, '{2,2,12,1}', 65, 40, '妙高', 55, 5, 0, '{2,1,0,2}', 10, 40, 24, 32, 16, 0, 0, 0, 49, 59, 59, 49,
                                                                                                             64, 0, 3,
                                                                                                             0, 0, 60,
                                                                                                             2,
   '私、妙高型重巡洋艦、妙高と申します。<br>共に頑張りましょう。', 80, '2,2,2,0,0', 44, FALSE, 265);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (59, 25, '300,450', 1, '{2,2,12,1}', 65, 40, '那智', 56, 5, 0, '{2,1,0,2}', 10, 40, 24, 32, 16, 0, 0, 0, 49, 54, 49, 49,
                                                                                                             54, 0, 3,
                                                                                                             0, 0, 56,
                                                                                                             2,
   '貴様が司令官か。<br>私は那智。よろしくお願いする。', 80, '2,2,2,0,0', 44, FALSE, 266);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (60, 25, '300,450', 2, '{2,2,12,1}', 65, 40, '足柄', 57, 5, 0, '{2,1,0,2}', 10, 40, 24, 32, 16, 0, 0, 0, 49, 54, 49, 49,
                                                                                                             54, 0, 3,
                                                                                                             0, 0, 56,
                                                                                                             2,
   '足柄よ。砲雷撃戦が得意なの。<br>ふふ、よろしくね。', 80, '2,2,2,0,0', 44, FALSE, 267);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (61, 25, '300,450', 1, '{2,2,12,1}', 65, 40, '羽黒', 58, 5, 0, '{2,1,0,2}', 10, 40, 24, 32, 16, 0, 0, 0, 49, 54, 49, 49,
                                                                                                             54, 0, 3,
                                                                                                             0, 0, 56,
                                                                                                             2,
   '羽黒です。妙高型重巡洋艦姉妹の末っ娘です。<br>あ、あの…ごめんなさいっ！', 80, '2,2,2,0,0', 44, FALSE, 268);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (62, 25, '300,450', 4, '{2,2,12,1}', 65, 40, '高雄', 59, 5, 0, '{2,1,0,2}', 10, 40, 24, 35, 18, 0, 0, 0, 49, 59, 59, 49,
                                                                                                             66, 0, 3,
                                                                                                             0, 0, 60,
                                                                                                             2,
   'こんにちは。高雄です。<br>貴方のような素敵な提督で良かったわ。', 85, '2,2,2,0,0', 45, FALSE, 269);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (63, 25, '300,450', 4, '{2,2,12,1}', 65, 40, '愛宕', 60, 5, 0, '{2,1,0,2}', 10, 40, 24, 35, 18, 0, 0, 0, 49, 54, 59, 49,
                                                                                                             56, 0, 3,
                                                                                                             0, 0, 60,
                                                                                                             2,
   '私は愛宕、提督、覚えてくださいね。', 85, '2,2,2,0,0', 45, FALSE, 270);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (64, 18, '250,300', 1, '{2,2,12,1}', 65, 40, '摩耶', 61, 5, 0, '{2,1,0,2}', 10, 40, 24, 35, 18, 0, 0, 0, 49, 54, 49, 49,
                                                                                                             56, 0, 3,
                                                                                                             0, 0, 57,
                                                                                                             2,
   'よ！アタシ、摩耶ってんだ、よろしくな。', 85, '2,2,2,0,0', 45, FALSE, 271);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (65, 25, '300,450', 1, '{2,2,12,1}', 65, 40, '鳥海', 62, 5, 0, '{2,1,0,2}', 10, 40, 24, 35, 18, 0, 0, 0, 49, 54, 49, 49,
                                                                                                             56, 0, 3,
                                                                                                             0, 0, 57,
                                                                                                             2,
   '私が鳥海です。よろしくです。', 85, '2,2,2,0,0', 45, FALSE, 272);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (66, 10, '210,70', 4, '{2,3,12,1}', 65, 40, '最上', 51, 5, 1, '{2,1,0,2}', 10, 40, 18, 31, 20, 0, 0, 0, 49, 59, 69, 59,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 59, 2,
   'ボクが最上さ。<br>大丈夫、今度は衝突しないって。ホントだよ。', 90, '2,2,2,0,0', 41, FALSE, 73);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (67, 25, '300,450', 4, '{2,2,13,2}', 60, 45, '利根', 63, 5, 0, '{2,1,1,2}', 10, 32, 24, 36, 20, 0, 0, 0, 49, 59, 59, 59,
                                                                                                             67, 0, 3,
                                                                                                             0, 0, 62,
                                                                                                             2,
   '吾輩が利根である！<br>吾輩が艦隊に加わる以上、もう、索敵の心配はないぞ！', 90, '3,3,3,0,0', 44, FALSE, 273);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (68, 25, '300,450', 4, '{2,2,13,2}', 60, 45, '筑摩', 64, 5, 0, '{2,1,1,2}', 10, 32, 24, 36, 20, 0, 0, 0, 49, 59, 59, 59,
                                                                                                             67, 0, 3,
                                                                                                             0, 0, 62,
                                                                                                             2,
   'はじめまして、利根型２番艦、筑摩と申します。', 90, '3,3,3,0,0', 44, FALSE, 274);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (69, 0, '0,0', 6, '{2,2,13,4}', 55, 50, '最上改', 101, 6, 3, '{2,1,3,2}', 10, 24, 18, 37, 20, 0, 0, 0, 69, 75, 69, 71,
                                                                                                          59, 0, 4, 0,
                                                                                                          0, 67, 2,
   '提督、また会ったね？最上だよ。<br>ボクの飛行甲板どう？似合ってる？', 100, '5,6,5,3,0', 50, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (70, 25, '380,210', 4, '{2,2,13,4}', 35, 35, '祥鳳', 94, 7, 0, '{0,0,2,2}', 10, 0, 0, 19, 14, 0, 0, 0, 49, 19, 0, 39,
                                                                                                           29, 0, 3, 0,
                                                                                                           0, 55, 1,
   '軽空母、祥鳳です。<br>はい、ちょっと小柄ですけど、ぜひ提督の機動部隊に加えてくださいね！', 160, '18,9,3,0,0', 32, FALSE, 282);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (71, 25, '500,250', 4, '{6,6,20,6}', 40, 40, '飛鷹', 65, 7, 0, '{0,0,3,2}', 10, 0, 0, 21, 21, 0, 0, 0, 49, 19, 0, 39,
                                                                                                           59, 0, 4, 0,
                                                                                                           0, 64, 1,
   '名前は出雲ま…じゃなかった、飛鷹です。<br>航空母艦よ。よろしくね、提督！', 180, '12,18,18,10,0', 40, FALSE, 283);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (72, 25, '400,220', 4, '{2,2,14,4}', 35, 35, '龍驤', 30, 7, 0, '{0,0,2,2}', 10, 0, 0, 17, 16, 0, 0, 0, 49, 19, 0, 39,
                                                                                                           29, 0, 3, 0,
                                                                                                           0, 54, 1,
   '軽空母、龍驤や。独特なシルエットでしょ？<br>でも、艦載機を次々繰り出す、ちゃーんとした空母なんや。期待してや！', 170, '9,24,5,0,0', 31, FALSE, 281);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (73, 10, '500,150', 5, '{9,18,37,3}', 120, 85, '伊勢', 3, 9, 0, '{4,0,1,4}', 15, 74, 0, 70, 28, 0, 0, 0, 69, 89, 0, 89,
                                                                                                             79, 0, 4,
                                                                                                             0, 0, 89,
                                                                                                             3,
   '超弩級戦艦、伊勢型の１番艦、伊勢。<br>参ります！', 270, '3,3,3,3,0', 74, FALSE, 82);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (74, 25, '400,600', 5, '{10,14,33,3}', 110, 80, '金剛', 21, 8, 0, '{3,0,1,3}', 12, 63, 0, 52, 24, 0, 0, 0, 49, 89, 0,
                                                                                                               69, 69,
                                                                                                               0, 3, 0,
                                                                                                               0, 79, 3,
   '英国で生まれた帰国子女の金剛デース。<br>ヨロシクオネガイシマース！', 240, '3,3,3,0,0', 63, FALSE, 209);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (75, 25, '400,600', 5, '{10,14,33,3}', 110, 80, '榛名', 23, 8, 0, '{3,0,1,3}', 15, 63, 0, 52, 24, 0, 0, 0, 69, 89, 0,
                                                                                                               69, 69,
                                                                                                               0, 3, 0,
                                                                                                               0, 79, 3,
   '高速戦艦、榛名、着任しました。<br>あなたが提督なのね？　よろしくお願い致します。', 240, '3,3,3,0,0', 63, FALSE, 211);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (76, 30, '800,900', 7, '{10,20,40,3}', 130, 100, '長門', 1, 9, 0, '{5,0,1,4}', 20, 82, 0, 75, 31, 0, 0, 0, 79, 99, 0,
                                                                                                               89, 89,
                                                                                                               0, 4, 0,
                                                                                                               0, 94, 3,
   '私が、戦艦長門だ。よろしく頼むぞ。<br>敵戦艦との殴り合いなら任せておけ。', 300, '3,3,3,3,0', 80, FALSE, 275);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (77, 30, '800,900', 7, '{10,20,40,3}', 130, 100, '陸奥', 2, 9, 0, '{5,0,1,4}', 3, 82, 0, 75, 31, 0, 0, 0, 39, 99, 0, 89,
                                                                                                              89, 0, 4,
                                                                                                              0, 0, 94,
                                                                                                              3,
   '長門型戦艦２番艦の陸奥よ。よろしくね。<br>あまり火遊びはしないでね…お願いよ。', 300, '3,3,3,3,0', 80, FALSE, 276);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (78, 0, '0,0', 6, '{10,15,36,3}', 105, 95, '伊勢改', 102, 10, 0, '{4,0,3,4}', 30, 63, 0, 74, 45, 0, 0, 0, 79, 79, 0, 92,
                                                                                                             89, 0, 4,
                                                                                                             0, 0, 89,
                                                                                                             3,
   '航空戦艦、伊勢です。<br>後部飛行甲板と、カタパルト２基で航空戦力を運用可能よ！', 270, '11,11,11,14,0', 77, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (79, 30, '700,300', 6, '{8,12,30,7}', 55, 60, '赤城', 6, 11, 1, '{0,0,5,3}', 12, 0, 0, 28, 32, 0, 0, 0, 49, 39, 0, 54,
                                                                                                            69, 0, 4, 0,
                                                                                                            0, 79, 1,
   '航空母艦、赤城です。<br>空母機動部隊を編制するなら、私にお任せくださいませ。', 270, '18,18,27,10,0', 69, FALSE, 277);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (80, 30, '750,300', 5, '{8,14,32,9}', 55, 60, '加賀', 7, 11, 1, '{0,0,5,3}', 10, 0, 0, 29, 28, 0, 0, 0, 49, 39, 0, 59,
                                                                                                            69, 0, 4, 0,
                                                                                                            0, 89, 1,
   '航空母艦、加賀です。<br>貴方が私の提督なの？　それなりに期待はしているわ。', 260, '18,18,45,12,0', 71, FALSE, 278);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (81, 25, '400,600', 5, '{10,14,33,3}', 110, 80, '霧島', 24, 8, 0, '{3,0,1,3}', 10, 63, 0, 52, 24, 0, 0, 0, 49, 89, 0,
                                                                                                               69, 69,
                                                                                                               0, 3, 0,
                                                                                                               0, 79, 3,
   'マイク音量大丈夫…？チェック、1，2……。<br>よし。はじめまして、私、霧島です。', 240, '3,3,3,0,0', 63, FALSE, 212);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (82, 25, '400,600', 5, '{10,14,33,3}', 110, 80, '比叡', 22, 8, 0, '{3,0,1,3}', 10, 63, 0, 52, 24, 0, 0, 0, 49, 89, 0,
                                                                                                               69, 69,
                                                                                                               0, 3, 0,
                                                                                                               0, 79, 3,
   '金剛お姉さまの妹分、比叡です。<br>経験を積んで、姉さまに少しでも近づきたいです。', 240, '3,3,3,0,0', 63, FALSE, 210);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (83, 10, '500,150', 5, '{9,18,37,3}', 120, 85, '日向', 4, 9, 0, '{4,0,1,4}', 15, 74, 0, 70, 28, 0, 0, 0, 69, 94, 0, 89,
                                                                                                             79, 0, 4,
                                                                                                             0, 0, 89,
                                                                                                             3,
   'あなたが提督？ふうん。いいけど。<br>伊勢型戦艦２番艦、日向よ。一応覚えておいて。', 270, '3,3,3,3,0', 74, FALSE, 88);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (84, 0, '0,0', 6, '{10,15,36,3}', 105, 95, '日向改', 103, 10, 0, '{4,0,3,4}', 30, 63, 0, 74, 45, 0, 0, 0, 79, 79, 0, 92,
                                                                                                             89, 0, 4,
                                                                                                             0, 0, 89,
                                                                                                             3,
   '伊勢型航空戦艦、日向。<br>推して参る。', 270, '11,11,11,14,0', 77, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (85, 25, '350,150', 3, '{2,1,12,2}', 25, 25, '鳳翔', 25, 7, 0, '{0,0,1,2}', 20, 0, 0, 15, 10, 0, 0, 0, 69, 19, 0, 39,
                                                                                                           29, 0, 2, 0,
                                                                                                           0, 49, 1,
   '航空母艦、鳳翔です。<br>ふつつか者ですが、よろしくお願い致します。', 120, '8,11,0,0,0', 30, FALSE, 285);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (86, 30, '650,300', 5, '{7,10,26,6}', 50, 50, '蒼龍', 8, 11, 0, '{0,0,4,3}', 10, 0, 0, 27, 26, 0, 0, 0, 49, 29, 0, 49,
                                                                                                            69, 0, 4, 0,
                                                                                                            0, 79, 1,
   '航空母艦、蒼龍です。<br>空母機動部隊を編制するなら、私もぜひ入れてね！', 250, '12,27,18,7,0', 50, FALSE, 279);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (87, 30, '650,300', 6, '{7,10,26,6}', 50, 50, '飛龍', 9, 11, 0, '{0,0,4,3}', 35, 0, 0, 27, 26, 0, 0, 0, 89, 29, 0, 49,
                                                                                                            69, 0, 4, 0,
                                                                                                            0, 79, 1,
   '航空母艦、飛龍です。<br>空母戦ならお任せ！どんな苦境でも戦えます！', 250, '12,27,18,7,0', 50, FALSE, 280);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (88, 25, '500,250', 4, '{6,6,20,6}', 40, 40, '隼鷹', 66, 7, 0, '{0,0,3,2}', 20, 0, 0, 21, 21, 0, 0, 0, 79, 19, 0, 39,
                                                                                                           59, 0, 4, 0,
                                                                                                           0, 64, 1,
   '商船改装空母、隼鷹でーすっ！<br>ひゃっはぁー！', 180, '12,18,18,10,0', 40, FALSE, 284);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (89, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '朧', 67, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   'アタシ、綾波型駆逐艦「朧」。<br>誰にも負けない…たぶん……', 20, '0,0,0,0,0', 15, FALSE, 230);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (90, 20, '100,100', 2, '{1,1,5,0}', 20, 15, '漣', 69, 2, 0, '{0,1,0,0}', 10, 10, 27, 5, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 29, 1,
   '綾波型駆逐艦「漣」です、ご主人さま。<br>こう書いてさざなみと読みます。', 20, '0,0,0,0,0', 15, FALSE, 232);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (91, 20, '100,100', 3, '{1,1,5,0}', 20, 15, '朝潮', 85, 2, 0, '{1,1,0,0}', 12, 10, 24, 6, 12, 0, 0, 0, 49, 29, 79, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 33, 1,
   '駆逐艦、朝潮です。<br>勝負ならいつでも受けて立つ覚悟です。', 22, '0,0,0,0,0', 16, FALSE, 248);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (92, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '大潮', 86, 2, 0, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 33, 1,
   '駆逐艦、大潮です～！<br>小さな体に大きな魚雷！　お任せください。', 22, '0,0,0,0,0', 16, FALSE, 249);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (93, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '満潮', 87, 2, 0, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 33, 1,
   '満潮よ。<br>私、なんでこんな部隊に配属されたのかしら。', 22, '0,0,0,0,0', 16, FALSE, 250);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (94, 20, '100,100', 1, '{1,1,5,0}', 20, 15, '荒潮', 88, 2, 0, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                          39, 0, 2, 0,
                                                                                                          0, 33, 1,
   'あら。自己紹介まだでしたかー。<br>私、荒潮です。', 22, '0,0,0,0,0', 16, FALSE, 251);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (95, 20, '200,200', 4, '{2,2,10,0}', 25, 25, '球磨', 39, 3, 0, '{0,1,0,2}', 12, 14, 24, 10, 13, 0, 0, 0, 49, 49, 89, 29,
                                                                                                             59, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   'クマー。<br>よろしくだクマ。', 60, '1,1,0,0,0', 25, FALSE, 215);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (96, 20, '200,200', 2, '{2,2,10,0}', 25, 25, '多摩', 40, 3, 0, '{0,1,0,1}', 10, 14, 24, 10, 13, 0, 0, 0, 49, 39, 79, 29,
                                                                                                             49, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   '軽巡、多摩です。<br>猫じゃないにゃ。', 60, '1,1,0,0,0', 25, FALSE, 216);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (97, 20, '200,200', 1, '{2,2,10,0}', 25, 25, '木曾', 41, 3, 0, '{0,1,0,1}', 10, 14, 24, 10, 13, 0, 0, 0, 49, 39, 79, 29,
                                                                                                             49, 0, 2,
                                                                                                             0, 0, 39,
                                                                                                             2,
   '木曾だ、お前に最高の勝利を与えてやる。', 60, '1,1,0,0,0', 25, FALSE, 217);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (98, 10, '70,40', 2, '{3,1,13,4}', 35, 35, '千歳', 49, 16, 0, '{0,0,1,2}', 10, 9, 0, 18, 14, 0, 0, 0, 49, 29, 0, 39, 29,
                                                                                                          0, 2, 0, 0,
                                                                                                          59, 1,
   '千歳です。<br>日本では初めての水上機母艦なのよ。よろしくね！', 140, '12,12,0,0,0', 40, FALSE, 104);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (99, 10, '70,40', 1, '{3,1,13,4}', 35, 35, '千代田', 50, 16, 0, '{0,0,1,2}', 10, 9, 0, 18, 14, 0, 0, 0, 49, 29, 0, 39,
                                                                                                           29, 0, 2, 0,
                                                                                                           0, 59, 1,
   '水上機母艦、千代田です。<br>姉の千歳が、いつも迷惑かけてないですか？', 140, '12,12,0,0,0', 40, FALSE, 105);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (100, 12, '70,80', 3, '{3,1,14,4}', 40, 35, '千歳改', 95, 16, 1, '{0,0,2,2}', 10, 9, 0, 20, 15, 0, 0, 0, 49, 29, 29, 39,
                                                                                                            29, 0, 3, 0,
                                                                                                            0, 59, 1,
   'ダイエットして空母になった千歳です！<br>足も速くなったの。本でも出そうかしら！', 150, '12,6,6,0,0', 41, TRUE, 106);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (101, 12, '70,80', 3, '{3,1,14,4}', 40, 35, '千代田改', 96, 16, 1, '{0,0,2,2}', 10, 9, 0, 20, 15, 0, 0, 0, 49, 29, 29, 39,
                                                                                                             29, 0, 3,
                                                                                                             0, 0, 59,
                                                                                                             1,
   '空母になった千代田です。<br>ぜひ、千歳お姉と一緒に機動部隊を編制してね！', 150, '12,6,6,0,0', 41, TRUE, 107);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (102, 15, '100,60', 3, '{3,3,15,3}', 45, 35, '千歳甲', 99, 16, 3, '{0,2,1,2}', 10, 9, 15, 21, 17, 0, 0, 0, 59, 29, 72,
                                                                                                              39, 39, 0,
                                                                                                              3, 0, 0,
                                                                                                              59, 1,
   'ダイエットして空母になった千歳です！<br>足も速くなったの。本でも出そうかしら！', 160, '12,6,6,0,0', 42, FALSE, 108);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (103, 15, '100,60', 3, '{3,3,15,3}', 45, 35, '千代田甲', 100, 16, 3, '{0,2,1,2}', 10, 9, 15, 21, 17, 0, 0, 0, 59, 29, 72,
                                                                                                                39, 39,
                                                                                                                0, 3, 0,
                                                                                                                0, 59,
                                                                                                                1,
   '空母になった千代田です。<br>ぜひ、千歳お姉と一緒に機動部隊を編制してね！', 160, '12,6,6,0,0', 42, FALSE, 109);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (104, 35, '550,250', 4, '{5,5,17,4}', 40, 40, '千歳航', 104, 7, 3, '{0,0,3,2}', 10, 0, 0, 25, 20, 0, 0, 0, 59, 19, 0, 39,
                                                                                                              49, 0, 3,
                                                                                                              0, 0, 59,
                                                                                                              1,
   'ダイエットして空母になった千歳です！<br>足も速くなったの。本でも出そうかしら！', 190, '21,9,6,0,0', 47, FALSE, 291);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (105, 35, '550,250', 4, '{5,5,17,4}', 40, 40, '千代田航', 105, 7, 3, '{0,0,3,2}', 10, 0, 0, 25, 20, 0, 0, 0, 59, 19, 0,
                                                                                                               39, 49,
                                                                                                               0, 3, 0,
                                                                                                               0, 59, 1,
   '空母になった千代田です。<br>ぜひ、千歳お姉と一緒に機動部隊を編制してね！', 190, '21,9,6,0,0', 47, FALSE, 292);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (106, 30, '750,350', 5, '{7,10,30,10}', 55, 55, '翔鶴', 106, 11, 3, '{0,0,4,3}', 10, 0, 0, 33, 29, 0, 0, 0, 49, 39, 0,
                                                                                                                49, 69,
                                                                                                                0, 4, 0,
                                                                                                                0, 79,
                                                                                                                1,
   '翔鶴型航空母艦１番艦、翔鶴です。<br>一航戦、二航戦の先輩方に、少しでも近づけるように<br>瑞鶴と一緒に頑張ります！', 360, '21,21,21,12,0', 62, FALSE, 288);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (133, 35, '300,220', 5, '{3,4,13,1}', 35, 30, '阿賀野', 137, 3, 3, '{1,1,1,2}', 10, 20, 24, 17, 17, 0, 0, 0, 49, 42, 72,
                                                                                                                32, 60,
                                                                                                                0, 3, 0,
                                                                                                                0, 45,
                                                                                                                2,
   'こんにちはーっ！<br>最新鋭軽巡の阿賀野でーすっ。ふふ。', 60, '2,2,2,0,0', 30, FALSE, 305);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (107, 25, '750,350', 6, '{7,10,30,10}', 55, 55, '瑞鶴', 107, 11, 3, '{0,0,4,3}', 40, 0, 0, 33, 29, 0, 0, 0, 89, 39, 0,
                                                                                                                49, 69,
                                                                                                                0, 4, 0,
                                                                                                                0, 79,
                                                                                                                1,
   '翔鶴型航空母艦２番艦、妹の瑞鶴です。<br>幸運の空母ですって？そうじゃないの、一生懸命やってるだけ…よ。艦載機がある限り、負けないわ！', 360, '21,21,21,12,0', 62, FALSE, 112);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (108, 0, '0,0', 7, '{7,10,30,10}', 70, 65, '瑞鶴改', 108, 11, 3, '{0,0,4,3}', 42, 0, 0, 42, 40, 0, 0, 0, 89, 39, 0, 72,
                                                                                                            79, 0, 4, 0,
                                                                                                            0, 90, 1,
   '翔鶴型航空母艦２番艦、妹の瑞鶴です。<br>幸運の空母ですって？そうじゃないの、一生懸命やってるだけ…よ。艦載機がある限り、負けないわ！', 360, '24,24,24,12,0', 75, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (109, 17, '200,200', 4, '{2,2,10,0}', 25, 25, '鬼怒', 109, 3, 3, '{0,1,0,1}', 12, 14, 24, 10, 13, 0, 0, 0, 49, 39, 79,
                                                                                                               29, 49,
                                                                                                               0, 2, 0,
                                                                                                               0, 39, 2,
   'きたきたぁ！　鬼怒、いよいよ到着しましたよ！', 75, '1,1,0,0,0', 26, FALSE, 289);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (110, 17, '200,200', 5, '{2,2,10,0}', 25, 25, '阿武隈', 110, 3, 3, '{0,1,0,1}', 12, 14, 24, 10, 13, 0, 0, 0, 49, 39, 79,
                                                                                                                29, 49,
                                                                                                                0, 2, 0,
                                                                                                                0, 39,
                                                                                                                2,
   'こ、こんにちは、軽巡、阿武隈です。', 75, '1,1,0,0,0', 27, FALSE, 290);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (111, 25, '280,240', 5, '{2,2,7,0}', 30, 20, '夕張', 111, 3, 3, '{1,1,1,1}', 12, 17, 20, 10, 10, 0, 0, 0, 49, 42, 69,
                                                                                                              29, 42, 0,
                                                                                                              3, 0, 0,
                                                                                                              33, 2,
   'はーい、お待たせ？<br>兵装実験軽巡、夕張、到着いたしました！', 82, '0,0,0,0,0', 19, FALSE, 293);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (112, 25, '380,210', 5, '{2,2,13,4}', 35, 35, '瑞鳳', 112, 7, 3, '{0,0,2,2}', 30, 0, 0, 19, 14, 0, 0, 0, 79, 19, 0, 39,
                                                                                                             29, 0, 3,
                                                                                                             0, 0, 55,
                                                                                                             1,
   '瑞鳳です。<br>軽空母ですが、練度があがれば、正規空母並の活躍をおみせできます。', 160, '18,9,3,0,0', 32, FALSE, 117);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (113, 0, '0,0', 6, '{4,6,20,6}', 40, 40, '瑞鳳改', 113, 7, 3, '{0,0,3,2}', 40, 0, 0, 25, 18, 0, 0, 0, 89, 29, 0, 59, 39,
                                                                                                         0, 4, 0, 0, 69,
                                                                                                         1,
   '瑞鳳です。<br>軽空母ですが、練度があがれば、正規空母並の活躍をおみせできます。', 160, '18,12,12,6,0', 45, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (114, 0, '0,0', 7, '{2,9,9,0}', 75, 25, '大井改二', 114, 4, 3, '{1,5,0,1}', 13, 17, 90, 23, 15, 0, 0, 0, 49, 63, 139, 63,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 59, 2,
   '重雷装艦として、生まれ変わった大井です。<br>お久しぶりです！', 75, '0,0,0,0,0', 43, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (115, 0, '0,0', 7, '{2,6,9,0}', 75, 25, '北上改二', 115, 4, 3, '{1,5,0,1}', 30, 17, 90, 23, 15, 0, 0, 0, 79, 63, 139, 63,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 59, 2,
   '新しい北上、それがアタシ。<br>酸素魚雷を満載して、ちょっと大人になったでしょ。', 75, '0,0,0,0,0', 43, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (116, 30, '270,110', 5, '{2,3,12,1}', 65, 40, '三隈', 116, 5, 3, '{2,1,0,2}', 5, 40, 18, 30, 18, 0, 0, 0, 49, 59, 69,
                                                                                                              59, 59, 0,
                                                                                                              3, 0, 0,
                                                                                                              59, 2,
   'ごきげんよう、三隈です。<br>最上さんはどこにいらっしゃるのかしら？', 90, '2,2,2,0,0', 40, FALSE, 121);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (117, 0, '0,0', 6, '{2,2,13,4}', 55, 50, '三隈改', 117, 6, 3, '{2,1,3,2}', 10, 24, 18, 37, 20, 0, 0, 0, 69, 75, 69, 71,
                                                                                                           59, 0, 4, 0,
                                                                                                           0, 67, 2,
   '提督、三隈、新型になりましてよ', 100, '5,6,5,3,0', 50, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (118, 20, '100,100', 4, '{1,1,6,0}', 20, 15, '舞風', 119, 2, 3, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   'こんにちは！陽炎型駆逐艦、舞風です。<br>暗い雰囲気は苦手です！', 24, '0,0,0,0,0', 16, FALSE, 294);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (119, 25, '250,300', 4, '{2,2,10,1}', 50, 35, '衣笠', 120, 5, 3, '{2,1,0,2}', 20, 30, 12, 26, 16, 0, 0, 0, 69, 54, 59,
                                                                                                               37, 59,
                                                                                                               0, 3, 0,
                                                                                                               0, 49, 2,
   'はーいっ！衣笠さんの登場よ！<br>青葉ともども、よろしくね！', 60, '2,2,2,0,0', 37, FALSE, 295);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (120, 35, '270,110', 4, '{2,3,12,1}', 65, 40, '鈴谷', 124, 5, 3, '{2,1,0,2}', 5, 40, 18, 30, 18, 0, 0, 0, 49, 59, 69,
                                                                                                              59, 59, 0,
                                                                                                              3, 0, 0,
                                                                                                              59, 2,
   '鈴谷だよ！にぎやかな艦隊だね！<br>よろしくね！', 90, '2,2,2,0,0', 40, FALSE, 129);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (121, 35, '270,110', 4, '{2,3,12,1}', 65, 40, '熊野', 125, 5, 3, '{2,1,0,2}', 5, 40, 18, 30, 18, 0, 0, 0, 49, 59, 69,
                                                                                                              59, 59, 0,
                                                                                                              3, 0, 0,
                                                                                                              59, 2,
   'ごきげんよう、<br>わたくしが重巡、熊野ですわ！', 90, '2,2,2,0,0', 40, FALSE, 130);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (122, 50, '130,200', 3, '{1,2,2,1}', 20, 10, '伊168', 126, 13, 3, '{0,2,0,0}', 10, 2, 24, 3, 0, 0, 0, 0, 49, 7, 59, 17,
                                                                                                              0, 0, 1,
                                                                                                              0, 0, 17,
                                                                                                              1,
   '伊１６８よ。何よ、言いにくいの？<br>じゃ、イムヤでいいわ…よろしくねっ！', 22, '0,0,0,0,0', 10, FALSE, 398);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (123, 50, '140,200', 4, '{1,2,2,1}', 20, 10, '伊58', 127, 13, 3, '{0,2,0,0}', 40, 2, 30, 4, 0, 0, 0, 0, 79, 9, 69, 19,
                                                                                                             0, 0, 1, 0,
                                                                                                             0, 19, 1,
   'こんにちは！ 伊五十八です。<br>ゴーヤって呼んでもいいよ！苦くなんかないよぉ！', 22, '0,0,0,0,0', 14, FALSE, 399);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (124, 50, '150,200', 5, '{1,2,2,1}', 20, 10, '伊8', 128, 13, 3, '{0,2,0,0}', 20, 2, 30, 4, 0, 0, 0, 0, 59, 9, 69, 19,
                                                                                                            0, 0, 1, 0,
                                                                                                            0, 19, 1,
   'グーテンターク…あ、違った、ごめんなさいね…<br>「はち」と呼んでくださいね。', 22, '0,0,0,0,0', 15, FALSE, 400);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (125, 0, '0,0', 5, '{2,2,13,4}', 55, 50, '鈴谷改', 129, 6, 3, '{2,1,3,2}', 10, 24, 18, 37, 20, 0, 0, 0, 69, 75, 69, 71,
                                                                                                           59, 0, 4, 0,
                                                                                                           0, 67, 2,
   '鈴谷だよ！にぎやかな艦隊だね！<br>よろしくね！', 100, '5,6,5,3,0', 50, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (126, 0, '0,0', 5, '{2,2,13,4}', 55, 50, '熊野改', 130, 6, 3, '{2,1,3,2}', 10, 24, 18, 37, 20, 0, 0, 0, 69, 75, 69, 71,
                                                                                                           59, 0, 4, 0,
                                                                                                           0, 67, 2,
   'ごきげんよう、<br>わたくしが重巡、熊野ですわ！', 100, '5,6,5,3,0', 50, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (127, 60, '3000,2500', 8, '{35,50,100,10}', 300, 250, '大和', 131, 9, 3, '{7,0,2,5}', 12, 96, 0, 88, 50, 0, 0, 0, 79,
    129, 0, 108, 94, 0, 4, 0, 0, 98, 4, '大和型戦艦、一番艦、大和。<br>推して参ります！', 480, '7,7,7,7,0', 93, FALSE, 136);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (128, 30, '110,120', 4, '{1,1,6,0}', 20, 15, '秋雲', 132, 2, 3, '{0,1,0,1}', 14, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   '秋雲、着任！<br>提督よろしくねっ！', 24, '0,0,0,0,0', 16, FALSE, 301);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (129, 30, '110,130', 4, '{1,1,6,0}', 20, 15, '夕雲', 133, 2, 3, '{0,1,0,1}', 12, 10, 24, 6, 9, 0, 0, 0, 49, 30, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   '夕雲型一番艦、夕雲、着任しました。<br>提督、甘えてくれても、いいんですよ？', 24, '0,0,0,0,0', 16, FALSE, 302);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (130, 30, '110,120', 4, '{1,1,6,0}', 20, 15, '巻雲', 134, 2, 3, '{0,1,0,1}', 11, 10, 24, 6, 9, 0, 0, 0, 49, 30, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   '夕雲型駆逐艦、巻雲といいます。<br>夕雲姉さんを見習って、頑張ります！', 24, '0,0,0,0,0', 16, FALSE, 303);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (131, 30, '110,130', 4, '{1,1,6,0}', 20, 15, '長波', 135, 2, 3, '{0,1,0,1}', 13, 10, 24, 6, 9, 0, 0, 0, 49, 30, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   '夕雲型駆逐艦四番艦、長波サマだよ！<br>さーいくぜ、オーッ！', 24, '0,0,0,0,0', 16, FALSE, 304);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (132, 0, '0,0', 8, '{35,50,110,20}', 325, 250, '大和改', 136, 9, 3, '{6,0,3,6}', 13, 92, 0, 92, 68, 0, 0, 0, 79, 139, 0,
                                                                                                                118,
                                                                                                                104, 0,
                                                                                                                4, 0, 0,
                                                                                                                108, 4,
   '大和型戦艦、一番艦、大和。<br>対空火器を大幅強化致しました！', 480, '7,7,7,7,0', 96, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (134, 35, '300,220', 5, '{3,4,13,1}', 35, 30, '能代', 138, 3, 3, '{1,1,1,2}', 10, 20, 24, 17, 17, 0, 0, 0, 49, 42, 72,
                                                                                                               32, 60,
                                                                                                               0, 3, 0,
                                                                                                               0, 45, 2,
   '阿賀野型軽巡二番艦、能代。<br>着任しました。よろしくどうぞ！', 60, '2,2,2,0,0', 30, FALSE, 306);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (135, 35, '300,220', 6, '{3,4,13,1}', 35, 30, '矢矧', 139, 3, 3, '{1,1,1,2}', 13, 20, 24, 17, 17, 0, 0, 0, 59, 42, 72,
                                                                                                               33, 63,
                                                                                                               0, 3, 0,
                                                                                                               0, 45, 2,
   '軽巡矢矧、着任したわ。<br>提督、最後まで頑張っていきましょう！', 60, '2,2,2,0,0', 31, FALSE, 307);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (136, 35, '300,220', 5, '{3,4,13,1}', 35, 30, '酒匂', 140, 3, 3, '{1,1,1,2}', 20, 19, 23, 17, 17, 0, 0, 0, 49, 41, 71,
                                                                                                               32, 62,
                                                                                                               0, 3, 0,
                                                                                                               0, 45, 2,
   'ぴゃん♪　阿賀野型軽巡四番艦、酒匂です！<br>司令、よろしくね！', 60, '2,2,2,0,0', 31, FALSE, 314);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (137, 0, '0,0', 5, '{2,2,10,0}', 30, 25, '五十鈴改二', 141, 3, 1, '{1,2,4,2}', 13, 18, 24, 30, 45, 0, 0, 0, 67, 59, 79, 69,
                                                                                                             84, 0, 3,
                                                                                                             0, 0, 59,
                                                                                                             1,
   '五十鈴です。水雷戦隊の指揮ならお任せ。<br>全力で提督を勝利に導くわ。よろしくね。', 60, '0,0,0,0,0', 44, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (138, 0, '0,0', 6, '{3,7,16,1}', 65, 35, '衣笠改二', 142, 5, 3, '{2,1,1,2}', 13, 38, 24, 35, 22, 0, 0, 0, 65, 78, 74, 73,
                                                                                                            66, 0, 4, 0,
                                                                                                            0, 65, 2,
   'はーいっ！衣笠さんの登場よ！<br>青葉ともども、よろしくね！', 60, '2,2,2,2,0', 53, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (139, 40, '3000,2500', 7, '{35,50,100,10}', 300, 250, '武蔵', 143, 9, 3, '{7,0,2,5}', 10, 96, 0, 88, 50, 0, 0, 0, 79,
    129, 0, 108, 94, 0, 4, 0, 0, 98, 4, 'フッ、随分待たせたようだな……。<br>大和型戦艦二番艦、武蔵。参る！', 480, '7,7,7,7,0', 94, FALSE, 148);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (140, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '夕立改二', 144, 2, 1, '{2,2,1,1}', 20, 17, 37, 14, 16, 0, 0, 0, 59, 73, 93, 52,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 58, 1,
   'こんにちは、白露型駆逐艦「夕立」よ。<br>よろしくね！', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (141, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '時雨改二', 145, 2, 3, '{2,2,1,1}', 50, 13, 28, 14, 24, 0, 0, 0, 79, 57, 84, 52,
                                                                                                            72, 0, 3, 0,
                                                                                                            0, 49, 1,
   '僕は白露型駆逐艦、「時雨」。<br>これからよろしくね。', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (142, 0, '0,0', 6, '{2,6,9,0}', 50, 25, '木曾改二', 146, 4, 1, '{1,5,0,1}', 13, 18, 80, 24, 24, 0, 0, 0, 69, 64, 110, 65,
                                                                                                           72, 0, 3, 0,
                                                                                                           0, 59, 2,
   '木曾だ、お前に最高の勝利を与えてやる。', 75, '0,0,0,0,0', 44, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (143, 0, '0,0', 6, '{1,3,11,0}', 25, 15, 'Верный', 147, 2, 3, '{1,2,1,1}', 20, 13, 30, 15, 18, 0, 0, 0, 77, 54, 89,
                                                                                                              54, 59, 0,
                                                                                                              3, 0, 0,
                                                                                                              49, 1,
   'ヴェールヌイだ。<br>その活躍ぶりから不死鳥の通り名もあるよ。', 20, '0,0,0,0,0', 37, FALSE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (144, 0, '0,0', 7, '{35,50,110,20}', 325, 250, '武蔵改', 148, 9, 3, '{6,0,3,6}', 9, 92, 0, 92, 60, 0, 0, 0, 79, 139, 0,
                                                                                                               119, 99,
                                                                                                               0, 4, 0,
                                                                                                               0, 108,
                                                                                                               4,
   '大和型二番艦、武蔵、推参する。<br>どうだ…この色、装束も似合うだろう？', 480, '7,7,7,7,0', 97, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (145, 0, '0,0', 7, '{10,14,33,3}', 125, 100, '金剛改二', 149, 8, 3, '{4,0,2,4}', 15, 76, 0, 70, 30, 0, 0, 0, 79, 98, 0,
                                                                                                               94, 84,
                                                                                                               0, 4, 0,
                                                                                                               0, 99, 3,
   '英国で生まれた帰国子女の金剛デース。<br>ヨロシクオネガイシマース！', 240, '3,3,3,3,0', 82, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (146, 0, '0,0', 7, '{10,14,33,3}', 125, 100, '比叡改二', 150, 8, 3, '{4,0,2,4}', 13, 76, 0, 72, 30, 0, 0, 0, 79, 98, 0,
                                                                                                               95, 82,
                                                                                                               0, 4, 0,
                                                                                                               0, 99, 3,
   '金剛お姉さまの妹分、比叡です。<br>経験を積んで、姉さまに少しでも近づきたいです。', 240, '3,3,3,3,0', 83, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (147, 0, '0,0', 7, '{10,14,33,3}', 125, 100, '榛名改二', 151, 8, 3, '{4,0,2,4}', 41, 75, 0, 70, 41, 0, 0, 0, 89, 96, 0,
                                                                                                               93, 92,
                                                                                                               0, 4, 0,
                                                                                                               0, 99, 3,
   '高速戦艦、榛名、着任しました。<br>あなたが提督なのね？　よろしくお願い致します。', 240, '3,3,3,3,0', 81, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (148, 0, '0,0', 7, '{10,14,33,3}', 125, 100, '霧島改二', 152, 8, 3, '{4,0,2,4}', 14, 78, 0, 70, 30, 0, 0, 0, 79, 104, 0,
                                                                                                               92, 82,
                                                                                                               0, 4, 0,
                                                                                                               0, 99, 3,
   'マイク音量大丈夫…？チェック、1，2……。<br>よし。はじめまして、私、霧島です。', 240, '3,3,3,3,0', 82, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (149, 40, '900,450', 7, '{8,15,36,12}', 65, 70, '大鳳', 153, 18, 3, '{0,0,5,5}', 2, 0, 0, 40, 42, 0, 0, 0, 19, 49, 0,
                                                                                                               79, 79,
                                                                                                               0, 4, 0,
                                                                                                               0, 87, 1,
   'そう…私が大鳳。<br>出迎え、ありがとうございます。<br>提督…貴方と機動部隊に勝利を！', 400, '18,18,18,7,0', 67, FALSE, 156);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (150, 35, '400,120', 4, '{3,1,10,0}', 15, 30, '香取', 154, 21, 1, '{0,1,0,1}', 10, 14, 12, 9, 14, 0, 0, 0, 49, 28, 28,
                                                                                                               27, 42,
                                                                                                               0, 3, 0,
                                                                                                               0, 48, 2,
   '練習巡洋艦、香取です。<br>心配しないで…。色々と優しく、指導させて頂きますから。', 70, '1,1,1,0,0', 36, FALSE, 343);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (151, 35, '300,100', 6, '{1,2,3,2}', 15, 20, '伊401', 155, 14, 3, '{0,1,1,1}', 20, 2, 36, 5, 0, 0, 0, 0, 59, 9, 72, 24,
                                                                                                              0, 0, 1,
                                                                                                              0, 0, 24,
                                                                                                              1,
   '提督、ごきげんよう。潜特型二番艦伊401です。<br>しおいって呼んでね。', 200, '3,0,0,0,0', 20, FALSE, 403);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (152, 0, '0,0', 7, '{9,16,36,14}', 75, 90, '大鳳改', 156, 18, 3, '{0,0,5,5}', 4, 0, 0, 44, 45, 0, 0, 0, 39, 59, 0, 84,
                                                                                                           86, 0, 4, 0,
                                                                                                           0, 90, 1,
   'おはようございます、改装済み大鳳です。<br>甲板装甲を強化、防御力もさらに向上、提督のために…露天駐機で艦載機数も充実です！', 400, '30,24,24,8,0', 70, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (153, 0, '0,0', 6, '{4,12,22,6}', 45, 40, '龍驤改二', 157, 7, 1, '{0,0,3,3}', 15, 0, 0, 28, 24, 0, 0, 0, 59, 40, 0, 62,
                                                                                                           48, 0, 4, 0,
                                                                                                           0, 72, 1,
   '軽空母、龍驤や。独特なシルエットでしょ？<br>でも、艦載機を次々繰り出す、ちゃーんとした空母なんや。期待してや！', 170, '18,28,6,3,0', 50, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (154, 0, '0,0', 6, '{2,2,10,0}', 35, 25, '川内改二', 158, 3, 1, '{1,1,1,2}', 14, 24, 26, 29, 20, 0, 0, 0, 79, 67, 88, 69,
                                                                                                            70, 0, 3, 0,
                                                                                                            0, 64, 2,
   '川内、参上。<br>夜戦なら任せておいて！', 60, '1,1,1,0,0', 48, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (155, 0, '0,0', 6, '{2,2,10,0}', 35, 25, '神通改二', 159, 3, 1, '{1,1,1,2}', 13, 27, 38, 29, 18, 0, 0, 0, 79, 70, 98, 69,
                                                                                                            68, 0, 3, 0,
                                                                                                            0, 63, 2,
   'あの……軽巡洋艦、神通です。<br>どうか、よろしくお願い致します……', 60, '1,1,1,0,0', 50, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (156, 0, '0,0', 6, '{2,2,10,0}', 35, 25, '那珂改二', 160, 3, 1, '{1,1,1,2}', 13, 22, 28, 29, 24, 0, 0, 0, 69, 68, 84, 68,
                                                                                                            72, 0, 3, 0,
                                                                                                            0, 62, 2,
   '艦隊のアイドル、那珂（なか）ちゃんだよー！<br>よっろしくぅ！', 60, '1,1,1,0,0', 48, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (157, 25, '200,80', 5, '{2,2,12,2}', 10, 40, 'あきつ丸', 161, 17, 3, '{0,0,1,1}', 10, 6, 0, 13, 13, 0, 0, 0, 39, 19, 0,
                                                                                                               33, 29,
                                                                                                               0, 2, 0,
                                                                                                               0, 49, 1,
   '自分、あきつ丸であります。<br>艦隊にお世話になります。', 150, '0,0,0,0,0', 38, FALSE, 166);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (158, 20, '50,20', 5, '{1,0,1,0}', 5, 10, 'まるゆ', 163, 13, 3, '{0,0,0,1}', 7, 1, 0, 2, 0, 0, 0, 0, 77, 3, 9, 9, 0, 0,
                                                                                                        0, 0, 0, 9, 1,
   '初めまして…まるゆ着任しました。<br>え？聞いてないって…そんなあ！', 17, '0,0,0,0,0', 6, FALSE, 402);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (159, 20, '100,100', 4, '{1,1,4,0}', 15, 15, '弥生', 164, 2, 1, '{1,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18,
                                                                                                           29, 0, 2, 0,
                                                                                                           0, 24, 1,
   '初めまして、弥生、着任…。<br>あ、気を使わないでくれていい…です。', 18, '0,0,0,0,0', 13, FALSE, 308);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (160, 25, '100,100', 4, '{1,1,4,0}', 15, 15, '卯月', 165, 2, 1, '{0,1,0,0}', 10, 6, 18, 5, 7, 0, 0, 0, 49, 29, 49, 18,
                                                                                                           29, 0, 2, 0,
                                                                                                           0, 24, 1,
   'やったぁ！ でたっぴょん！ 卯月でっす！ <br>うーちゃんって呼ばれてまっす！', 18, '0,0,0,0,0', 13, FALSE, 309);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (161, 0, '0,0', 6, '{2,2,13,5}', 25, 45, 'あきつ丸改', 166, 17, 3, '{1,0,1,1}', 13, 8, 0, 15, 15, 0, 0, 0, 49, 33, 0, 43,
                                                                                                            37, 0, 3, 0,
                                                                                                            0, 59, 1,
   '自分、航空兵力を充実させてみたのであります。<br>これはもう空母…であります…。', 150, '8,8,8,0,0', 40, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (162, 45, '140,160', 5, '{1,1,6,0}', 20, 15, '磯風', 167, 2, 1, '{0,1,0,1}', 16, 10, 24, 6, 14, 0, 0, 0, 54, 29, 69, 19,
                                                                                                             44, 0, 2,
                                                                                                             0, 0, 34,
                                                                                                             1,
   '陽炎型駆逐艦十二番艦、磯風。<br>大丈夫、私が護ってあげる。', 24, '0,0,0,0,0', 16, FALSE, 320);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (163, 35, '110,140', 4, '{1,1,6,0}', 20, 15, '浦風', 168, 2, 0, '{0,1,0,1}', 13, 10, 24, 6, 10, 0, 0, 0, 49, 29, 69, 19,
                                                                                                             40, 0, 2,
                                                                                                             0, 0, 34,
                                                                                                             1,
   'うち、浦風じゃ、よろしくね！', 24, '0,0,0,0,0', 16, FALSE, 317);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (164, 30, '100,100', 4, '{1,1,6,0}', 20, 15, '谷風', 169, 2, 0, '{0,1,0,1}', 14, 10, 24, 6, 10, 0, 0, 0, 49, 29, 69, 19,
                                                                                                             40, 0, 2,
                                                                                                             0, 0, 34,
                                                                                                             1,
   '提督、谷風だよ。<br>これからお世話になるね！', 24, '0,0,0,0,0', 16, FALSE, 313);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (165, 30, '100,100', 4, '{1,1,6,0}', 20, 15, '浜風', 170, 2, 0, '{0,1,0,1}', 15, 10, 24, 6, 13, 0, 0, 0, 49, 29, 69, 19,
                                                                                                             42, 0, 2,
                                                                                                             0, 0, 34,
                                                                                                             1,
   '駆逐艦、浜風です。<br>これより貴艦隊所属となります。', 24, '0,0,0,0,0', 16, FALSE, 312);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (166, 30, '600,800', 7, '{10,16,38,4}', 110, 90, 'Bismarck', 171, 8, 1, '{3,0,1,3}', 8, 64, 0, 67, 18, 0, 0, 0, 69,
    88, 0, 83, 48, 0, 4, 0, 0, 96, 3, 'Guten Tag.<br>私はビスマルク型戦艦のネームシップ、ビスマルク。<br>よおく覚えておくのよ。', 300, '4,4,4,4,0', 90,
   FALSE, 172);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (167, 50, '1200,1600', 7, '{12,18,40,4}', 115, 95, 'Bismarck改', 172, 8, 3, '{4,0,1,4}', 10, 70, 0, 77, 24, 0, 0, 0,
                                                                             79, 93, 0, 93, 58, 0, 4, 0, 0, 99, 3,
   'Guten Tag.<br>私はビスマルク型戦艦のネームシップ、ビスマルク。<br>よおく覚えておくのよ。', 300, '4,4,4,4,0', 94, TRUE, 173);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (168, 75, '1800,2400', 7, '{12,18,40,4}', 135, 105, 'Bismarck zwei', 173, 8, 3, '{4,0,2,4}', 20, 70, 0, 80, 25, 0, 0,
                                                                                  0, 82, 97, 0, 94, 62, 0, 4, 0, 0, 99,
                                                                                         3,
   'Guten Tag.<br>私はビスマルク型戦艦のネームシップ、ビスマルク。<br>よおく覚えておくのよ。', 300, '4,4,4,4,0', 96, FALSE, 178);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (169, 30, '170,150', 5, '{1,1,6,0}', 20, 20, 'Z1', 174, 2, 1, '{1,1,0,0}', 6, 8, 24, 8, 12, 0, 0, 0, 39, 26, 60, 22,
                                                                                                           42, 0, 3, 0,
                                                                                                           0, 29, 1,
   'Guten Morgen.<br>僕の名前はレーベレヒト・マース。<br>レーベでいいよ…うん。', 24, '0,0,0,0,0', 18, FALSE, 310);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (170, 30, '170,150', 5, '{1,1,6,0}', 20, 20, 'Z3', 175, 2, 1, '{1,1,0,0}', 6, 8, 24, 8, 12, 0, 0, 0, 39, 26, 60, 22,
                                                                                                           42, 0, 3, 0,
                                                                                                           0, 29, 1,
   'Guten Tag.<br>私は駆逐艦マックス・シュルツよ。<br>マックス…でもいいけれど。よろしく。', 24, '0,0,0,0,0', 18, FALSE, 311);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (171, 45, '700,600', 6, '{2,3,15,2}', 70, 50, 'Prinz Eugen', 176, 5, 1, '{2,1,0,2}', 30, 38, 32, 38, 16, 0, 0, 0, 79,
    56, 64, 64, 44, 0, 3, 0, 0, 72, 2, 'Guten Morgen！<br>私は、重巡プリンツ・オイゲン。よろしくね！', 200, '3,3,3,0,0', 50, FALSE, 177);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (172, 0, '0,0', 7, '{4,8,22,3}', 75, 55, 'Prinz Eugen改', 177, 5, 3, '{3,2,1,3}', 40, 48, 40, 48, 18, 0, 0, 0, 89, 75,
                                                                                                                    84,
                                                                                                                    82,
                                                                                                                    60,
                                                                                                                    0,
                                                                                                                    4,
                                                                                                                    0,
                                                                                                                    0,
                                                                                                                    79,
                                                                                                                    2,
   'Guten Morgen！<br>私は、重巡プリンツ・オイゲン。よろしくね！', 200, '3,3,3,3,0', 63, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (173, 0, '0,0', 7, '{12,20,42,4}', 155, 110, 'Bismarck drei', 178, 8, 3, '{4,1,2,4}', 22, 74, 16, 82, 35, 0, 0, 0, 84,
    99, 36, 95, 70, 0, 4, 0, 0, 99, 3, 'Guten Tag.<br>私はビスマルク型戦艦のネームシップ、ビスマルク。<br>よおく覚えておくのよ。', 300, '4,4,4,4,0', 96,
   FALSE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (174, 0, '0,0', 7, '{1,1,6,0}', 25, 20, 'Z1 zwei', 179, 2, 3, '{1,1,0,0}', 15, 12, 27, 18, 20, 0, 0, 0, 49, 49, 71,
                                                                                                              53, 64, 0,
                                                                                                              3, 0, 0,
                                                                                                              59, 1,
   'Guten Morgen.<br>僕の名前はレーベレヒト・マース。<br>レーベでいいよ…うん。', 24, '0,0,0,0,0', 35, FALSE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (175, 0, '0,0', 7, '{1,1,6,0}', 25, 20, 'Z3 zwei', 180, 2, 3, '{1,1,0,0}', 15, 10, 27, 18, 24, 0, 0, 0, 49, 47, 71,
                                                                                                              53, 68, 0,
                                                                                                              3, 0, 0,
                                                                                                              59, 1,
   'Guten Tag.<br>私は駆逐艦マックス・シュルツよ。<br>マックス…でもいいけれど。よろしく。', 24, '0,0,0,0,0', 35, FALSE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (176, 20, '120,100', 6, '{1,1,6,0}', 20, 20, '天津風', 181, 2, 1, '{1,1,1,1}', 18, 10, 28, 7, 22, 0, 0, 0, 59, 29, 79,
                                                                                                              25, 53, 0,
                                                                                                              3, 0, 0,
                                                                                                              37, 1,
   'いい風きてる？<br>次世代型駆逐艦のプロトタイプ、<br>あたし、天津風の出番ね。', 30, '0,0,0,0,0', 18, FALSE, 316);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (177, 35, '1500,200', 6, '{3,1,15,3}', 10, 50, '明石', 182, 19, 1, '{0,0,1,1}', 10, 4, 0, 7, 10, 0, 0, 0, 39, 14, 0, 19,
                                                                                                              24, 0, 3,
                                                                                                              0, 0, 48,
                                                                                                              1,
   '工作艦、明石です。<br>少々の損傷だったら、私が泊地でばっちり直してあげますね。<br>お任せください！', 220, '0,0,0,0,0', 39, FALSE, 187);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (178, 35, '400,320', 6, '{4,2,14,2}', 30, 35, '大淀', 183, 3, 1, '{1,0,2,2}', 24, 24, 0, 19, 18, 0, 0, 0, 69, 48, 39,
                                                                                                              34, 62, 0,
                                                                                                              3, 0, 0,
                                                                                                              47, 2,
   '提督、軽巡大淀、戦列に加わりました。<br>艦隊指揮、運営はどうぞお任せください。', 80, '0,6,6,0,0', 34, FALSE, 321);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (179, 25, '700,450', 4, '{2,2,12,2}', 10, 35, '大鯨', 184, 20, 1, '{0,0,1,2}', 20, 5, 0, 15, 16, 0, 0, 0, 59, 15, 0, 37,
                                                                                                              36, 0, 3,
                                                                                                              0, 0, 55,
                                                                                                              1,
   'こんにちわあ。潜水母艦大鯨です。<br>不束者ですが、よろしくお願い致します。', 150, '2,3,3,0,0', 39, FALSE, 185);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (180, 50, '450,550', 5, '{2,3,13,4}', 35, 35, '龍鳳', 185, 7, 3, '{0,0,2,2}', 20, 0, 0, 18, 24, 0, 0, 0, 69, 20, 0, 38,
                                                                                                             48, 0, 3,
                                                                                                             0, 0, 57,
                                                                                                             1,
   '潜水母艦改装空母の龍鳳です。<br>航空母艦として、私、頑張ります！', 160, '18,7,6,0,0', 39, FALSE, 318);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (181, 30, '120,110', 5, '{1,1,6,0}', 20, 15, '時津風', 186, 2, 1, '{0,1,0,1}', 13, 10, 24, 6, 10, 0, 0, 0, 49, 29, 69,
                                                                                                              19, 40, 0,
                                                                                                              2, 0, 0,
                                                                                                              34, 1,
   '陽炎型駆逐艦十番艦。<br>時津風……出るよ。', 24, '0,0,0,0,0', 16, FALSE, 322);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (182, 0, '0,0', 7, '{3,2,16,3}', 15, 55, '明石改', 187, 19, 3, '{0,0,1,1}', 12, 6, 0, 9, 16, 0, 0, 0, 49, 24, 0, 27, 36,
                                                                                                         0, 4, 0, 0, 58,
                                                                                                         1,
   '工作艦、明石です。<br>少々の損傷だったら、私が泊地でばっちり直してあげますね。<br>お任せください！', 150, '0,0,0,0,0', 45, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (183, 0, '0,0', 7, '{5,8,18,5}', 65, 50, '利根改二', 188, 6, 1, '{3,1,3,2}', 15, 46, 32, 48, 32, 0, 0, 0, 69, 77, 82, 79,
                                                                                                            82, 0, 4, 0,
                                                                                                            0, 72, 2,
   '吾輩が利根である！<br>吾輩が艦隊に加わる以上、もう、索敵の心配はないぞ！', 90, '2,2,9,5,0', 59, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (184, 0, '0,0', 7, '{5,8,18,5}', 65, 50, '筑摩改二', 189, 6, 1, '{3,1,3,2}', 14, 46, 33, 48, 33, 0, 0, 0, 67, 77, 83, 79,
                                                                                                            83, 0, 4, 0,
                                                                                                            0, 72, 2,
   'はじめまして、利根型２番艦、筑摩と申します。', 90, '2,2,9,5,0', 58, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (185, 20, '100,100', 4, '{1,1,6,0}', 20, 15, '初風', 118, 2, 3, '{0,1,0,1}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   '初風です、よろしく。<br>提督さんにとって私は何人目の私かしら？', 24, '0,0,0,0,0', 16, FALSE, 300);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (186, 50, '140,200', 4, '{1,2,2,1}', 20, 10, '伊19', 123, 13, 3, '{0,2,0,0}', 12, 2, 36, 4, 0, 0, 0, 0, 49, 9, 79, 18,
                                                                                                             0, 0, 1, 0,
                                                                                                             0, 19, 1,
   '素敵な提督で嬉しいのね。<br>伊十九なの。そう、イクって呼んでもいいの！', 22, '0,0,0,0,0', 14, FALSE, 401);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (187, 0, '0,0', 6, '{4,7,20,2}', 75, 45, '那智改二', 192, 5, 1, '{3,1,2,2}', 18, 50, 34, 48, 33, 0, 0, 0, 70, 80, 84, 78,
                                                                                                            83, 0, 4, 0,
                                                                                                            0, 71, 2,
   '貴様が司令官か。<br>私は那智。よろしくお願いする。', 80, '2,2,4,4,0', 56, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (188, 0, '0,0', 6, '{4,7,20,2}', 75, 45, '足柄改二', 193, 5, 3, '{3,1,2,2}', 20, 53, 34, 47, 26, 0, 0, 0, 72, 82, 84, 79,
                                                                                                            74, 0, 4, 0,
                                                                                                            0, 71, 2,
   '足柄よ。砲雷撃戦が得意なの。<br>ふふ、よろしくね。', 80, '2,2,4,4,0', 56, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (189, 0, '0,0', 5, '{4,7,20,2}', 75, 45, '羽黒改二', 194, 5, 1, '{3,1,2,2}', 19, 52, 34, 47, 24, 0, 0, 0, 70, 84, 84, 77,
                                                                                                            72, 0, 4, 0,
                                                                                                            0, 71, 2,
   '妙高型重巡洋艦、羽黒です。<br>皆さんと共に、全力で戦線を支えます！', 80, '2,2,4,4,0', 57, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (190, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '綾波改二', 195, 2, 3, '{2,2,1,1}', 40, 17, 30, 15, 16, 0, 0, 0, 77, 70, 87, 54,
                                                                                                            52, 0, 3, 0,
                                                                                                            0, 54, 1,
   'ごきげんよう。<br>特型駆逐艦、綾波と申します。', 20, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (191, 0, '0,0', 8, '{10,14,32,11}', 75, 70, '飛龍改二', 196, 11, 0, '{0,0,4,5}', 50, 0, 0, 37, 33, 0, 0, 0, 92, 64, 0, 76,
                                                                                                              82, 0, 4,
                                                                                                              0, 0, 89,
                                                                                                              1,
   '航空母艦、飛龍です。<br>空母戦ならお任せ！どんな苦境でも戦えます！', 250, '18,36,22,3,0', 67, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (192, 0, '0,0', 8, '{10,14,32,11}', 75, 70, '蒼龍改二', 197, 11, 0, '{0,0,4,5}', 15, 0, 0, 36, 34, 0, 0, 0, 59, 57, 0, 75,
                                                                                                              84, 0, 4,
                                                                                                              0, 0, 89,
                                                                                                              1,
   '航空母艦、蒼龍です。<br>空母機動部隊を編制するなら、私もぜひ入れてね！', 250, '18,35,20,6,0', 67, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (193, 0, '0,0', 7, '{2,2,10,0}', 35, 25, '阿武隈改二', 200, 3, 3, '{1,2,2,2}', 20, 16, 34, 29, 35, 0, 0, 0, 74, 56, 94, 68,
                                                                                                             78, 0, 3,
                                                                                                             0, 0, 61,
                                                                                                             1,
   'こ、こんにちは、軽巡、阿武隈です。', 75, '1,1,1,0,0', 45, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (194, 70, '230,270', 4, '{1,2,10,0}', 20, 15, '吹雪改', 1301, 2, 3, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79,
                                                                                                                 49, 49,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 49, 1,
   'はじめまして吹雪です。<br>よろしくお願い致します。', 20, '0,0,0,0,0', 30, TRUE, 426);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (195, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '白雪改', 1302, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   '白雪です。<br>よろしくお願いします。', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (196, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '初雪改', 1303, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   '初雪……です……よろしく。', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (197, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '深雪改', 1304, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   '深雪だよ。<br>よろしくな！', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (198, 70, '210,250', 4, '{1,2,10,0}', 20, 15, '叢雲改', 1305, 2, 3, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79,
                                                                                                                 49, 49,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 49, 1,
   'あんたが司令官ね。<br>ま、せいぜい頑張りなさい！', 20, '0,0,0,0,0', 30, TRUE, 420);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (199, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '磯波改', 1306, 2, 0, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   'あ、あの…磯波と申します。<br>よろしくお願いいたします。', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (200, 70, '200,280', 4, '{1,2,10,0}', 20, 15, '綾波改', 1307, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79,
                                                                                                                 49, 49,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 49, 1,
   'ごきげんよう。<br>特型駆逐艦、綾波と申します。', 20, '0,0,0,0,0', 30, TRUE, 195);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (201, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '敷波改', 1308, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 49, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   'アタシの名は敷波。<br>以後よろしく。', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (202, 75, '2400,2400', 6, '{10,14,33,3}', 120, 90, '金剛改', 1309, 8, 1, '{4,0,2,3}', 12, 72, 0, 67, 28, 0, 0, 0, 69, 94,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     79,
                                                                                                                     0,
                                                                                                                     4,
                                                                                                                     0,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     3,
   '英国で生まれた帰国子女の金剛デース。<br>ヨロシクオネガイシマース！', 240, '3,3,3,3,0', 75, TRUE, 149);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (203, 75, '2400,2400', 6, '{10,14,33,3}', 120, 90, '比叡改', 1310, 8, 1, '{4,0,2,3}', 12, 72, 0, 67, 28, 0, 0, 0, 69, 94,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     79,
                                                                                                                     0,
                                                                                                                     4,
                                                                                                                     0,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     3,
   '金剛お姉さまの妹分、比叡です。<br>経験を積んで、姉さまに少しでも近づきたいです。', 240, '3,3,3,3,0', 75, TRUE, 150);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (204, 80, '2400,2400', 6, '{10,14,33,3}', 120, 90, '榛名改', 1311, 8, 1, '{4,0,2,3}', 20, 72, 0, 67, 28, 0, 0, 0, 69, 94,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     79,
                                                                                                                     0,
                                                                                                                     4,
                                                                                                                     0,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     3,
   '高速戦艦、榛名、着任しました。<br>あなたが提督なのね？　よろしくお願い致します。', 240, '3,3,3,3,0', 75, TRUE, 151);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (205, 75, '2400,2400', 6, '{10,14,33,3}', 120, 90, '霧島改', 1312, 8, 1, '{4,0,2,3}', 12, 72, 0, 67, 28, 0, 0, 0, 69, 94,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     79,
                                                                                                                     0,
                                                                                                                     4,
                                                                                                                     0,
                                                                                                                     0,
                                                                                                                     89,
                                                                                                                     3,
   'マイク音量大丈夫…？チェック、1，2……。<br>よし。はじめまして、私、霧島です。', 240, '3,3,3,3,0', 75, TRUE, 152);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (206, 0, '0,0', 4, '{1,1,8,0}', 25, 25, '天龍改', 1313, 3, 1, '{1,1,1,2}', 12, 20, 24, 28, 12, 0, 0, 0, 59, 59, 79, 59,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 54, 2,
   'オレの名は天龍。<br>フフフ、怖いか？', 60, '0,0,0,0,0', 40, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (207, 0, '0,0', 4, '{1,1,8,0}', 25, 25, '龍田改', 1314, 3, 1, '{1,1,1,2}', 12, 20, 24, 28, 12, 0, 0, 0, 59, 59, 79, 59,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 54, 2,
   '初めまして、龍田だよ。<br>天龍ちゃんがご迷惑かけてないかなあ～。', 60, '0,0,0,0,0', 40, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (208, 0, '0,0', 5, '{2,2,10,0}', 30, 25, '球磨改', 1315, 3, 1, '{2,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 69, 89, 69,
                                                                                                            69, 0, 3, 0,
                                                                                                            0, 59, 2,
   'クマー。<br>よろしくだクマ。', 60, '1,1,1,0,0', 42, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (209, 0, '0,0', 4, '{2,2,10,0}', 30, 25, '多摩改', 1316, 3, 1, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59, 79, 59,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 59, 2,
   '軽巡、多摩です。<br>猫じゃないにゃ。', 60, '1,1,1,0,0', 42, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (210, 65, '400,750', 4, '{2,2,10,0}', 30, 25, '木曾改', 1317, 3, 0, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59, 79,
                                                                                                                 59, 59,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 59, 2,
   '木曾だ、お前に最高の勝利を与えてやる。', 60, '1,1,1,0,0', 42, TRUE, 146);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (211, 0, '0,0', 5, '{2,2,10,0}', 30, 25, '長良改', 1318, 3, 0, '{2,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 69, 89, 69,
                                                                                                            69, 0, 3, 0,
                                                                                                            0, 59, 2,
   '軽巡、長良です。<br>よろしくお願いします！', 60, '1,1,1,0,0', 43, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (212, 50, '270,360', 4, '{2,2,10,0}', 30, 25, '五十鈴改', 1319, 3, 0, '{1,1,4,2}', 12, 18, 24, 29, 40, 0, 0, 0, 59, 59,
                                                                                                                  79,
                                                                                                                  59,
                                                                                                                  59, 0,
                                                                                                                  3, 0,
                                                                                                                  0, 59,
                                                                                                                  2,
   '五十鈴です。水雷戦隊の指揮ならお任せ。<br>全力で提督を勝利に導くわ。よろしくね。', 60, '1,1,1,0,0', 37, TRUE, 141);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (213, 0, '0,0', 4, '{2,2,10,0}', 30, 25, '由良改', 1320, 3, 0, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59, 79, 59,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 59, 2,
   '長良型軽巡四番艦の「由良」です。<br>どうぞ、よろしくお願いいたしますっ！', 60, '1,1,1,0,0', 43, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (214, 0, '0,0', 4, '{2,2,10,0}', 30, 25, '名取改', 1321, 3, 0, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 69, 89, 59,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 59, 2,
   '名取といいます。<br>ご迷惑をおかけしないように、が、頑張ります。', 60, '1,1,1,0,0', 43, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (215, 60, '300,480', 5, '{2,2,10,0}', 30, 25, '川内改', 1322, 3, 1, '{2,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59, 79,
                                                                                                                 69, 69,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 59, 2,
   '川内、参上。<br>夜戦なら任せておいて！', 60, '1,1,1,0,0', 44, TRUE, 158);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (216, 60, '300,480', 4, '{2,2,10,0}', 30, 25, '神通改', 1323, 3, 1, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59, 79,
                                                                                                                 59, 59,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 59, 2,
   'あの……軽巡洋艦、神通です。<br>どうか、よろしくお願い致します……', 60, '1,1,1,0,0', 44, TRUE, 159);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (217, 48, '480,400', 4, '{2,2,10,0}', 30, 25, '那珂改', 1324, 3, 1, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59, 79,
                                                                                                                 59, 59,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 59, 2,
   '艦隊のアイドル、那珂（なか）ちゃんだよー！<br>よっろしくぅ！', 60, '1,1,1,0,0', 44, TRUE, 160);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (218, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '陽炎改', 1325, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   'やっと会えた！　陽炎よ。<br>よろしくねっ！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (219, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '不知火改', 1326, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                             49, 0, 3,
                                                                                                             0, 0, 49,
                                                                                                             1,
   '不知火です。<br>ご指導ご鞭撻、よろしくです。', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (220, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '黒潮改', 1327, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   '黒潮や、よろしゅうな。', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (221, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '雪風改', 1328, 2, 0, '{1,1,2,2}', 60, 12, 28, 14, 16, 0, 0, 0, 99, 59, 89, 59,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 49, 1,
   '陽炎型駆逐艦８番艦、雪風です。<br>どうぞ、よろしくお願いしますっ！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (222, 0, '0,0', 6, '{1,3,15,0}', 25, 20, '島風改', 1329, 2, 1, '{1,2,1,2}', 12, 14, 48, 14, 16, 0, 0, 0, 59, 59, 99, 59,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 59, 1,
   '駆逐艦島風です。スピードなら誰にも負けません。<br>速きこと、島風の如し、です！', 30, '0,0,0,0,0', 36, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (223, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '朧改', 1330, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 49, 1,
   'アタシ、綾波型駆逐艦「朧」。<br>誰にも負けない…たぶん……', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (224, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '曙改', 1331, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 49, 1,
   '特型駆逐艦「曙」よ。<br>って、こっち見んな！　この糞提督！', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (225, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '漣改', 1332, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 49, 1,
   '綾波型駆逐艦「漣」です、ご主人さま。<br>こう書いてさざなみと読みます。', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (226, 60, '170,30', 4, '{1,2,10,0}', 20, 15, '潮改', 1333, 2, 1, '{1,1,1,1}', 20, 12, 28, 13, 15, 0, 0, 0, 79, 49, 79,
                                                                                                               49, 49,
                                                                                                               0, 3, 0,
                                                                                                               0, 49, 1,
   '特型駆逐艦…綾波型の「潮」です。<br>もう下がってよろしいでしょうか…。', 20, '0,0,0,0,0', 30, TRUE, 407);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (227, 70, '190,190', 4, '{1,2,10,0}', 20, 15, '暁改', 1334, 2, 3, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79,
                                                                                                                49, 49,
                                                                                                                0, 3, 0,
                                                                                                                0, 49,
                                                                                                                1,
   '暁よ。<br>一人前のレディーとして扱ってよね！', 20, '0,0,0,0,0', 30, TRUE, 437);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (228, 70, '240,200', 4, '{1,2,10,0}', 20, 15, '響改', 1335, 2, 0, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79,
                                                                                                                49, 49,
                                                                                                                0, 3, 0,
                                                                                                                0, 49,
                                                                                                                1,
   '響だよ。<br>その活躍ぶりから不死鳥の通り名もあるよ。', 20, '0,0,0,0,0', 30, TRUE, 147);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (229, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '雷改', 1336, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 49, 1,
   '雷よ！　かみなりじゃないわ！<br>そこのとこもよろしく頼むわねっ！', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (230, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '電改', 1337, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 49, 1,
   '電です。<br>どうか、よろしくお願いいたします。', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (231, 65, '200,200', 4, '{1,2,10,0}', 20, 15, '初春改', 1338, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79,
                                                                                                                 49, 49,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 51, 1,
   'わらわが初春じゃ。<br>よろしく頼みますぞ。', 20, '0,0,0,0,0', 30, TRUE, 326);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (232, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '子日改', 1339, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 51, 1,
   '初めまして、ねのひ、だよぉ！<br>艦名、読みづらくなんか、ないよね？ね？', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (233, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '若葉改', 1340, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 51, 1,
   '駆逐艦、若葉だ。', 20, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (234, 70, '220,230', 4, '{1,2,10,0}', 20, 15, '初霜改', 1341, 2, 1, '{1,1,1,1}', 12, 12, 28, 13, 15, 0, 0, 0, 59, 49, 79,
                                                                                                                 49, 49,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 51, 1,
   '初春型四番艦、初霜です。<br>皆さん、よろしくお願いします！', 20, '0,0,0,0,0', 30, TRUE, 419);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (235, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '白露改', 1342, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 57, 1,
   '白露型駆逐艦一番艦、「白露」です！<br>はい、一番艦ですっ！', 22, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (236, 60, '180,200', 4, '{1,2,10,0}', 20, 15, '時雨改', 1343, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 15, 0, 0, 0, 59, 49, 79,
                                                                                                                 49, 49,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 57, 1,
   '僕は白露型駆逐艦、「時雨」。<br>これからよろしくね。', 22, '0,0,0,0,0', 30, TRUE, 145);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (237, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '村雨改', 1344, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 57, 1,
   'はいはーい！白露型駆逐艦「村雨」だよ。<br>みんな、よろしくね！', 22, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (238, 55, '180,200', 4, '{1,2,10,0}', 20, 15, '夕立改', 1345, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 15, 0, 0, 0, 59, 49, 79,
                                                                                                                 49, 49,
                                                                                                                 0, 3,
                                                                                                                 0, 0,
                                                                                                                 57, 1,
   'こんにちは、白露型駆逐艦「夕立」よ。<br>よろしくね！', 22, '0,0,0,0,0', 30, TRUE, 144);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (239, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '五月雨改', 1346, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                             49, 0, 3,
                                                                                                             0, 0, 57,
                                                                                                             1,
   '五月雨っていいます！よろしくお願いします。<br>護衛任務はお任せください！', 22, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (240, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '涼風改', 1347, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 57, 1,
   'ちわ！涼風だよ。<br>私が艦隊に加われば百人力さ！', 22, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (241, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '朝潮改', 1348, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 59, 1,
   '駆逐艦、朝潮です。<br>勝負ならいつでも受けて立つ覚悟です。', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (242, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '大潮改', 1349, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 59, 1,
   '駆逐艦、大潮です～！<br>小さな体に大きな魚雷！　お任せください。', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (243, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '満潮改', 1350, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 59, 1,
   '満潮よ。<br>私、なんでこんな部隊に配属されたのかしら。', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (244, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '荒潮改', 1351, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 59, 1,
   'あら。自己紹介まだでしたかー。<br>私、荒潮です。', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (245, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '霰改', 1352, 2, 1, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 59, 1,
   '霰です…<br>んちゃ…とかはいいません…よろしく…', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (246, 0, '0,0', 4, '{1,2,10,0}', 20, 15, '霞改', 1353, 2, 1, '{1,1,1,1}', 20, 12, 28, 14, 16, 0, 0, 0, 79, 49, 79, 49,
                                                                                                           49, 0, 3, 0,
                                                                                                           0, 59, 1,
   '霞よ。<br>ガンガンいくわよ。ついてらっしゃい。', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (247, 65, '170,100', 4, '{1,1,4,0}', 15, 15, '睦月改', 1354, 2, 1, '{1,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69,
                                                                                                               39, 39,
                                                                                                               0, 3, 0,
                                                                                                               0, 39, 1,
   '睦月です。<br>はりきって、まいりましょー！', 18, '0,0,0,0,0', 24, TRUE, 434);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (248, 65, '170,100', 4, '{1,1,4,0}', 15, 15, '如月改', 1355, 2, 1, '{0,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69,
                                                                                                               39, 39,
                                                                                                               0, 3, 0,
                                                                                                               0, 39, 1,
   '如月と申します。<br>おそばに置いてくださいね。', 18, '0,0,0,0,0', 24, TRUE, 435);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (249, 0, '0,0', 4, '{1,1,4,0}', 15, 15, '皐月改', 1356, 2, 1, '{0,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69, 39,
                                                                                                          39, 0, 3, 0,
                                                                                                          0, 39, 1,
   '皐月だよっ。<br>よろしくな！', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (250, 0, '0,0', 4, '{1,1,4,0}', 15, 15, '文月改', 1357, 2, 1, '{0,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69, 39,
                                                                                                          39, 0, 3, 0,
                                                                                                          0, 39, 1,
   'あたし、文月っていうの。<br>よろしくぅ～。', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (251, 0, '0,0', 4, '{1,1,4,0}', 15, 15, '長月改', 1358, 2, 1, '{0,1,0,0}', 20, 9, 18, 11, 12, 0, 0, 0, 79, 39, 69, 39,
                                                                                                          39, 0, 3, 0,
                                                                                                          0, 39, 1,
   '長月だ。<br>駆逐艦と侮るなよ。役に立つはずだ。', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (252, 0, '0,0', 4, '{1,1,4,0}', 15, 15, '菊月改', 1359, 2, 1, '{0,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69, 39,
                                                                                                          39, 0, 3, 0,
                                                                                                          0, 39, 1,
   '私が菊月だ、共にゆこう。', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (253, 0, '0,0', 4, '{1,1,4,0}', 15, 15, '三日月改', 1360, 2, 1, '{0,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69, 39,
                                                                                                           39, 0, 3, 0,
                                                                                                           0, 39, 1,
   'あなたが司令官ですね。三日月です。<br>どうぞお手柔らかにお願いします。', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (254, 0, '0,0', 4, '{1,1,4,0}', 15, 15, '望月改', 1361, 2, 1, '{0,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69, 39,
                                                                                                          39, 0, 3, 0,
                                                                                                          0, 39, 1,
   'ん？あぁ、望月でーす。', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (255, 65, '380,480', 4, '{3,6,15,1}', 55, 35, '古鷹改', 1362, 5, 1, '{2,1,1,2}', 10, 36, 18, 32, 18, 0, 0, 0, 59, 70, 59,
                                                                                                                 70, 59,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 65, 2,
   '古鷹と言います。<br>重巡洋艦のいいところ、たくさん知ってもらえると嬉しいです。', 60, '2,2,2,2,0', 48, TRUE, 416);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (256, 65, '380,480', 4, '{3,6,15,1}', 55, 35, '加古改', 1363, 5, 1, '{2,1,1,2}', 10, 36, 18, 32, 18, 0, 0, 0, 59, 70, 59,
                                                                                                                 70, 59,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 65, 2,
   '古鷹型重巡の2番艦、加古ってんだ、よっろしくぅー！', 60, '2,2,2,2,0', 48, TRUE, 417);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (257, 0, '0,0', 4, '{3,6,15,1}', 55, 35, '青葉改', 1364, 5, 0, '{2,1,1,2}', 30, 36, 18, 34, 18, 0, 0, 0, 79, 72, 59, 70,
                                                                                                            59, 0, 4, 0,
                                                                                                            0, 65, 2,
   'ども、恐縮です、青葉ですぅ！<br>一言お願いします！', 60, '2,2,2,2,0', 49, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (258, 70, '800,900', 5, '{4,7,20,2}', 70, 40, '妙高改', 1365, 5, 3, '{3,1,1,2}', 10, 48, 24, 42, 18, 0, 0, 0, 59, 76, 79,
                                                                                                                 73, 69,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 69, 2,
   '私、妙高型重巡洋艦、妙高と申します。<br>共に頑張りましょう。', 80, '2,2,2,2,0', 55, TRUE, 319);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (259, 65, '800,900', 4, '{4,7,20,2}', 70, 40, '那智改', 1366, 5, 1, '{3,1,1,2}', 10, 48, 24, 42, 18, 0, 0, 0, 59, 76, 69,
                                                                                                                 73, 69,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 69, 2,
   '貴様が司令官か。<br>私は那智。よろしくお願いする。', 80, '2,2,2,2,0', 55, TRUE, 192);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (260, 65, '800,900', 4, '{4,7,20,2}', 70, 40, '足柄改', 1367, 5, 3, '{3,1,1,2}', 10, 48, 24, 42, 18, 0, 0, 0, 59, 77, 69,
                                                                                                                 73, 69,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 69, 2,
   '足柄よ。砲雷撃戦が得意なの。<br>ふふ、よろしくね。', 80, '2,2,2,2,0', 55, TRUE, 193);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (261, 65, '800,900', 4, '{4,7,20,2}', 70, 40, '羽黒改', 1368, 5, 1, '{3,1,1,2}', 10, 48, 24, 42, 18, 0, 0, 0, 59, 77, 69,
                                                                                                                 73, 69,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 69, 2,
   '羽黒です。妙高型重巡洋艦姉妹の末っ娘です。<br>あ、あの…ごめんなさいっ！', 80, '2,2,2,2,0', 55, TRUE, 194);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (262, 0, '0,0', 5, '{4,7,20,2}', 70, 40, '高雄改', 1369, 5, 0, '{3,1,1,2}', 10, 48, 24, 45, 20, 0, 0, 0, 59, 77, 79, 75,
                                                                                                            69, 0, 4, 0,
                                                                                                            0, 69, 2,
   'こんにちは。高雄です。<br>貴方のような素敵な提督で良かったわ。', 85, '2,2,2,2,0', 57, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (263, 0, '0,0', 5, '{4,7,20,2}', 70, 40, '愛宕改', 1370, 5, 0, '{3,1,1,2}', 10, 48, 24, 45, 20, 0, 0, 0, 59, 77, 79, 75,
                                                                                                            69, 0, 4, 0,
                                                                                                            0, 69, 2,
   '私は愛宕、提督、覚えてくださいね。', 85, '2,2,2,2,0', 57, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (264, 75, '750,1150', 4, '{4,7,20,2}', 70, 40, '摩耶改', 1371, 5, 1, '{2,1,4,2}', 10, 43, 24, 45, 55, 0, 0, 0, 59, 78,
                                                                                                                  69,
                                                                                                                  75,
                                                                                                                  89, 0,
                                                                                                                  4, 0,
                                                                                                                  0, 69,
                                                                                                                  2,
   'よ！アタシ、摩耶ってんだ、よろしくな。', 85, '2,2,2,2,0', 55, TRUE, 428);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (265, 65, '650,1300', 4, '{4,7,20,2}', 70, 40, '鳥海改', 1372, 5, 1, '{3,1,1,2}', 10, 48, 24, 45, 20, 0, 0, 0, 59, 78,
                                                                                                                  69,
                                                                                                                  75,
                                                                                                                  69, 0,
                                                                                                                  4, 0,
                                                                                                                  0, 69,
                                                                                                                  2,
   '私が鳥海です。よろしくです。', 85, '2,2,2,2,0', 57, TRUE, 427);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (266, 70, '1000,700', 5, '{5,7,18,3}', 65, 45, '利根改', 1373, 5, 1, '{3,1,2,2}', 10, 42, 24, 46, 24, 0, 0, 0, 59, 76,
                                                                                                                  79,
                                                                                                                  77,
                                                                                                                  79, 0,
                                                                                                                  4, 0,
                                                                                                                  0, 69,
                                                                                                                  2,
   '吾輩が利根である！<br>吾輩が艦隊に加わる以上、もう、索敵の心配はないぞ！', 90, '4,4,4,4,0', 56, TRUE, 188);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (267, 70, '1000,700', 5, '{5,7,18,3}', 65, 45, '筑摩改', 1374, 5, 1, '{3,1,2,2}', 10, 42, 24, 46, 24, 0, 0, 0, 59, 76,
                                                                                                                  79,
                                                                                                                  77,
                                                                                                                  79, 0,
                                                                                                                  4, 0,
                                                                                                                  0, 69,
                                                                                                                  2,
   'はじめまして、利根型２番艦、筑摩と申します。', 90, '4,4,4,4,0', 56, TRUE, 189);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (268, 0, '0,0', 7, '{20,30,50,3}', 160, 100, '長門改', 1375, 9, 1, '{5,0,2,5}', 32, 90, 0, 85, 33, 0, 0, 0, 99, 99, 0,
                                                                                                               98, 99,
                                                                                                               0, 4, 0,
                                                                                                               0, 98, 3,
   '私が、戦艦長門だ。よろしく頼むぞ。<br>敵戦艦との殴り合いなら任せておけ。', 300, '3,3,3,3,0', 90, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (269, 0, '0,0', 7, '{20,30,50,3}', 160, 100, '陸奥改', 1376, 9, 1, '{5,0,2,5}', 6, 90, 0, 85, 33, 0, 0, 0, 59, 99, 0, 98,
                                                                                                              99, 0, 4,
                                                                                                              0, 0, 98,
                                                                                                              3,
   '長門型戦艦２番艦の陸奥よ。よろしくね。<br>あまり火遊びはしないでね…お願いよ。', 300, '3,3,3,3,0', 90, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (270, 0, '0,0', 7, '{10,15,35,12}', 75, 75, '赤城改', 1377, 11, 1, '{0,0,5,4}', 12, 0, 0, 40, 35, 0, 0, 0, 59, 49, 0, 79,
                                                                                                              79, 0, 4,
                                                                                                              0, 0, 92,
                                                                                                              1,
   '航空母艦、赤城です。<br>空母機動部隊を編制するなら、私にお任せくださいませ。', 270, '20,20,32,10,0', 77, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (271, 0, '0,0', 6, '{10,17,40,15}', 80, 80, '加賀改', 1378, 11, 3, '{0,0,5,4}', 12, 0, 0, 40, 30, 0, 0, 0, 59, 49, 0, 79,
                                                                                                              79, 0, 4,
                                                                                                              0, 0, 92,
                                                                                                              1,
   '航空母艦、加賀です。<br>貴方が私の提督なの？　それなりに期待はしているわ。', 260, '20,20,46,12,0', 79, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (272, 78, '1200,1700', 6, '{9,13,30,10}', 65, 65, '蒼龍改', 1379, 11, 0, '{0,0,4,4}', 12, 0, 0, 35, 30, 0, 0, 0, 59, 39,
                                                                                                                    0,
                                                                                                                    69,
                                                                                                                    79,
                                                                                                                    0,
                                                                                                                    4,
                                                                                                                    0,
                                                                                                                    0,
                                                                                                                    89,
                                                                                                                    1,
   '航空母艦、蒼龍です。<br>空母機動部隊を編制するなら、私もぜひ入れてね！', 250, '18,27,18,10,0', 65, TRUE, 197);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (273, 77, '1200,1700', 7, '{9,13,30,10}', 65, 65, '飛龍改', 1380, 11, 0, '{0,0,4,4}', 40, 0, 0, 35, 30, 0, 0, 0, 89, 39,
                                                                                                                    0,
                                                                                                                    69,
                                                                                                                    79,
                                                                                                                    0,
                                                                                                                    4,
                                                                                                                    0,
                                                                                                                    0,
                                                                                                                    89,
                                                                                                                    1,
   '航空母艦、飛龍です。<br>空母戦ならお任せ！どんな苦境でも戦えます！', 250, '18,27,18,10,0', 65, TRUE, 196);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (274, 75, '600,600', 5, '{4,6,20,6}', 40, 40, '龍驤改', 1381, 7, 1, '{0,0,3,2}', 12, 0, 0, 25, 20, 0, 0, 0, 59, 29, 0,
                                                                                                               59, 39,
                                                                                                               0, 4, 0,
                                                                                                               0, 69, 1,
   '軽空母、龍驤や。独特なシルエットでしょ？<br>でも、艦載機を次々繰り出す、ちゃーんとした空母なんや。期待してや！', 170, '9,24,5,5,0', 45, TRUE, 157);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (275, 0, '0,0', 5, '{4,6,20,6}', 40, 40, '祥鳳改', 1382, 7, 1, '{0,0,3,2}', 12, 0, 0, 25, 18, 0, 0, 0, 59, 29, 0, 59, 39,
                                                                                                          0, 4, 0, 0,
                                                                                                          69, 1,
   '軽空母、祥鳳です。<br>はい、ちょっと小柄ですけど、ぜひ提督の機動部隊に加えてくださいね！', 160, '18,12,12,6,0', 45, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (276, 0, '0,0', 5, '{6,10,25,8}', 45, 45, '飛鷹改', 1383, 7, 1, '{0,0,3,3}', 12, 0, 0, 30, 25, 0, 0, 0, 59, 29, 0, 59,
                                                                                                           69, 0, 4, 0,
                                                                                                           0, 79, 1,
   '名前は出雲ま…じゃなかった、飛鷹です。<br>航空母艦よ。よろしくね、提督！', 180, '18,18,18,12,0', 50, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (277, 80, '900,1400', 5, '{6,10,25,8}', 45, 45, '隼鷹改', 1384, 7, 1, '{0,0,3,3}', 30, 0, 0, 30, 25, 0, 0, 0, 79, 29, 0,
                                                                                                                 59, 69,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 79, 1,
   '商船改装空母、隼鷹でーすっ！<br>ひゃっはぁー！', 180, '18,18,18,12,0', 50, TRUE, 408);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (278, 0, '0,0', 4, '{3,4,15,4}', 30, 30, '鳳翔改', 1385, 7, 1, '{0,0,2,2}', 30, 0, 0, 25, 15, 0, 0, 0, 79, 29, 0, 49, 39,
                                                                                                          0, 3, 0, 0,
                                                                                                          59, 1,
   '航空母艦、鳳翔です。<br>ふつつか者ですが、よろしくお願い致します。', 120, '14,16,12,0,0', 40, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (279, 80, '3500,2400', 5, '{10,15,35,3}', 105, 95, '扶桑改', 1386, 10, 1, '{4,0,2,4}', 10, 63, 0, 72, 40, 0, 0, 0, 59,
    79, 0, 89, 89, 0, 4, 0, 0, 89, 3, '扶桑型超弩級戦艦、姉の扶桑です。<br>妹の山城ともども、よろしくお願い致します。', 260, '10,10,10,10,0', 75, TRUE, 411);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (280, 80, '3500,2400', 5, '{10,15,35,3}', 105, 95, '山城改', 1387, 10, 1, '{4,0,2,4}', 10, 63, 0, 72, 40, 0, 0, 0, 59,
    79, 0, 89, 89, 0, 4, 0, 0, 89, 3, '扶桑型戦艦姉妹、妹のほう、山城です。<br>あの、扶桑姉さま、見ませんでした？', 260, '10,10,10,10,0', 75, TRUE, 412);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (281, 0, '0,0', 6, '{7,10,30,10}', 70, 65, '翔鶴改', 1388, 11, 3, '{0,0,4,3}', 12, 0, 0, 42, 40, 0, 0, 0, 89, 39, 0, 72,
                                                                                                             79, 0, 4,
                                                                                                             0, 0, 90,
                                                                                                             1,
   '翔鶴型航空母艦１番艦、翔鶴です。<br>一航戦、二航戦の先輩方に、少しでも近づけるように<br>瑞鶴と一緒に頑張ります！', 360, '24,24,24,12,0', 75, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (282, 0, '0,0', 5, '{2,2,10,0}', 35, 25, '鬼怒改', 1389, 3, 3, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59, 79, 59,
                                                                                                            59, 0, 3, 0,
                                                                                                            0, 59, 2,
   'きたきたぁ！　鬼怒、いよいよ到着しましたよ！', 75, '1,1,1,0,0', 41, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (283, 75, '550,400', 6, '{2,2,10,0}', 35, 25, '阿武隈改', 1390, 3, 3, '{1,1,1,2}', 12, 20, 24, 29, 15, 0, 0, 0, 59, 59,
                                                                                                                  79,
                                                                                                                  59,
                                                                                                                  59, 0,
                                                                                                                  3, 0,
                                                                                                                  0, 59,
                                                                                                                  2,
   'こ、こんにちは、軽巡、阿武隈です。', 75, '1,1,1,0,0', 42, TRUE, 200);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (284, 50, '430,370', 5, '{5,10,24,7}', 40, 45, '千歳航改', 1391, 7, 3, '{0,0,3,3}', 12, 0, 0, 32, 27, 0, 0, 0, 59, 34, 0,
                                                                                                                 64, 69,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 79, 1,
   'はじめまして。どうぞ、よろしくお願いいたします！', 190, '24,16,8,8,0', 57, TRUE, 296);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (285, 50, '430,370', 5, '{5,10,24,7}', 40, 45, '千代田航改', 1392, 7, 3, '{0,0,3,3}', 12, 0, 0, 32, 27, 0, 0, 0, 59, 34, 0,
                                                                                                                  64,
                                                                                                                  69, 0,
                                                                                                                  4, 0,
                                                                                                                  0, 79,
                                                                                                                  1,
   'はじめまして。どうぞ、よろしくお願いいたします！', 190, '24,16,8,8,0', 57, TRUE, 297);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (286, 0, '0,0', 6, '{2,2,7,0}', 40, 25, '夕張改', 1393, 3, 3, '{1,1,2,1}', 17, 23, 24, 28, 20, 0, 0, 0, 69, 63, 79, 49,
                                                                                                           69, 0, 4, 0,
                                                                                                           0, 49, 2,
   'はーい、お待たせ？<br>兵装実験軽巡、夕張、到着いたしました！', 82, '0,0,0,0,0', 36, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (287, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '舞風改', 1394, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   'こんにちは！陽炎型駆逐艦、舞風です。<br>暗い雰囲気は苦手です！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (288, 55, '380,480', 5, '{3,6,15,1}', 60, 35, '衣笠改', 1395, 5, 3, '{2,1,1,2}', 10, 36, 18, 34, 18, 0, 0, 0, 59, 66, 59,
                                                                                                                 64, 59,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 65, 2,
   'はーいっ！衣笠さんの登場よ！<br>青葉ともども、よろしくね！', 60, '2,2,2,2,0', 49, TRUE, 142);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (289, 0, '0,0', 6, '{5,10,24,7}', 40, 45, '千歳航改二', 121, 7, 3, '{0,0,3,3}', 13, 0, 0, 32, 30, 0, 0, 0, 59, 34, 0, 65,
                                                                                                            72, 0, 4, 0,
                                                                                                            0, 79, 1,
   'ダイエットして空母になった千歳です！<br>足も速くなったの。本でも出そうかしら！', 190, '24,16,11,8,0', 58, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (290, 0, '0,0', 6, '{5,10,24,7}', 40, 45, '千代田航改二', 122, 7, 3, '{0,0,3,3}', 13, 0, 0, 32, 30, 0, 0, 0, 59, 34, 0, 65,
                                                                                                             72, 0, 4,
                                                                                                             0, 0, 79,
                                                                                                             1,
   '空母になった千代田です。<br>ぜひ、千歳お姉と一緒に機動部隊を編制してね！', 190, '24,16,11,8,0', 58, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (291, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '初風改', 1396, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   '初風です、よろしく。<br>提督さんにとって私は何人目の私かしら？', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (292, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '秋雲改', 1397, 2, 3, '{1,1,1,1}', 15, 8, 28, 14, 22, 0, 0, 0, 59, 44, 79, 49,
                                                                                                           59, 0, 3, 0,
                                                                                                           0, 49, 1,
   '秋雲、着任！<br>提督よろしくねっ！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (293, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '夕雲改', 1398, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 50, 80, 49,
                                                                                                            50, 0, 3, 0,
                                                                                                            0, 49, 1,
   '夕雲型一番艦、夕雲、着任しました。<br>提督、甘えてくれても、いいんですよ？', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (294, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '巻雲改', 1399, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 50, 80, 49,
                                                                                                            50, 0, 3, 0,
                                                                                                            0, 49, 1,
   '夕雲型駆逐艦、巻雲といいます。<br>夕雲姉さんを見習って、頑張ります！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (295, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '長波改', 1400, 2, 3, '{1,1,1,1}', 14, 12, 28, 14, 16, 0, 0, 0, 59, 50, 80, 49,
                                                                                                            50, 0, 3, 0,
                                                                                                            0, 49, 1,
   '夕雲型駆逐艦四番艦、長波サマだよ！<br>さーいくぜ、オーッ！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (296, 0, '0,0', 6, '{3,5,14,1}', 40, 30, '阿賀野改', 1401, 3, 3, '{2,1,1,2}', 10, 28, 24, 31, 20, 0, 0, 0, 59, 62, 79, 69,
                                                                                                             72, 0, 3,
                                                                                                             0, 0, 62,
                                                                                                             2,
   'こんにちはーっ！<br>最新鋭軽巡の阿賀野でーすっ。ふふ。', 60, '2,2,2,0,0', 45, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (297, 0, '0,0', 6, '{3,5,14,1}', 40, 30, '能代改', 1402, 3, 3, '{2,1,1,2}', 10, 28, 24, 31, 20, 0, 0, 0, 59, 62, 79, 69,
                                                                                                            72, 0, 3, 0,
                                                                                                            0, 62, 2,
   '阿賀野型軽巡二番艦、能代。<br>着任しました。よろしくどうぞ！', 60, '2,2,2,0,0', 45, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (298, 0, '0,0', 8, '{3,5,14,1}', 40, 30, '矢矧改', 1403, 3, 3, '{2,1,1,2}', 14, 28, 24, 32, 22, 0, 0, 0, 69, 64, 79, 69,
                                                                                                            74, 0, 3, 0,
                                                                                                            0, 63, 2,
   '軽巡矢矧、着任したわ。<br>提督、最後まで頑張っていきましょう！', 60, '2,2,2,0,0', 47, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (299, 0, '0,0', 5, '{1,1,4,0}', 15, 15, '弥生改', 1404, 2, 1, '{1,1,0,0}', 12, 9, 18, 11, 12, 0, 0, 0, 59, 39, 69, 39,
                                                                                                          39, 0, 3, 0,
                                                                                                          0, 39, 1,
   '初めまして、弥生、着任…。<br>あ、気を使わないでくれていい…です。', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (300, 0, '0,0', 5, '{1,1,4,0}', 15, 15, '卯月改', 1405, 2, 1, '{0,1,0,0}', 14, 7, 18, 12, 18, 0, 0, 0, 59, 34, 69, 39,
                                                                                                          49, 0, 3, 0,
                                                                                                          0, 39, 1,
   'やったぁ！ でたっぴょん！ 卯月でっす！ <br>うーちゃんって呼ばれてまっす！', 18, '0,0,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (301, 70, '350,300', 6, '{1,1,6,0}', 25, 20, 'Z1改', 1406, 2, 3, '{1,1,0,0}', 12, 11, 25, 15, 15, 0, 0, 0, 49, 45, 70,
                                                                                                                45, 45,
                                                                                                                0, 3, 0,
                                                                                                                0, 59,
                                                                                                                1,
   'Guten Morgen.<br>僕の名前はレーベレヒト・マース。<br>レーベでいいよ…うん。', 24, '0,0,0,0,0', 33, TRUE, 179);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (302, 70, '350,300', 6, '{1,1,6,0}', 25, 20, 'Z3改', 1407, 2, 3, '{1,1,0,0}', 12, 11, 25, 15, 15, 0, 0, 0, 49, 45, 70,
                                                                                                                45, 45,
                                                                                                                0, 3, 0,
                                                                                                                0, 59,
                                                                                                                1,
   'Guten Tag.<br>私は駆逐艦マックス・シュルツよ。<br>マックス…でもいいけれど。よろしく。', 24, '0,0,0,0,0', 33, TRUE, 180);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (303, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '浜風改', 1408, 2, 1, '{1,1,1,1}', 17, 12, 28, 14, 22, 0, 0, 0, 59, 48, 79, 49,
                                                                                                            60, 0, 3, 0,
                                                                                                            0, 49, 1,
   '駆逐艦、浜風です。<br>これより貴艦隊所属となります。', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (304, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '谷風改', 1409, 2, 1, '{1,1,1,1}', 16, 12, 28, 14, 16, 0, 0, 0, 59, 48, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   '提督、谷風だよ。<br>これからお世話になるね！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (305, 0, '0,0', 6, '{3,5,14,1}', 40, 30, '酒匂改', 1410, 3, 3, '{2,1,1,2}', 30, 27, 23, 31, 19, 0, 0, 0, 69, 61, 78, 69,
                                                                                                            73, 0, 3, 0,
                                                                                                            0, 62, 2,
   'ぴゃん♪　阿賀野型軽巡四番艦、酒匂です！<br>司令、よろしくね！', 60, '2,2,2,0,0', 46, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (306, 0, '0,0', 7, '{1,2,10,0}', 20, 20, '天津風改', 1411, 2, 3, '{1,1,1,1}', 17, 12, 32, 14, 23, 0, 0, 0, 69, 49, 84, 61,
                                                                                                             63, 0, 3,
                                                                                                             0, 0, 54,
                                                                                                             1,
   'いい風きてる？<br>次世代型駆逐艦のプロトタイプ、<br>あたし、天津風の出番ね。', 24, '0,0,0,0,0', 34, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (307, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '浦風改', 1412, 2, 1, '{1,1,1,1}', 13, 12, 28, 14, 16, 0, 0, 0, 59, 48, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   'うち、浦風じゃ、よろしくね！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (308, 0, '0,0', 6, '{4,8,24,5}', 40, 35, '龍鳳改', 190, 7, 3, '{0,0,2,2}', 24, 0, 0, 24, 28, 0, 0, 0, 79, 32, 0, 57, 62,
                                                                                                         0, 4, 0, 0, 70,
                                                                                                         1,
   '潜水母艦改装空母の龍鳳です。<br>航空母艦として、私、頑張ります！', 160, '21,9,9,6,0', 48, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (309, 0, '0,0', 6, '{4,7,20,2}', 75, 45, '妙高改二', 191, 5, 3, '{3,1,2,2}', 32, 50, 36, 47, 28, 0, 0, 0, 79, 80, 88, 78,
                                                                                                            80, 0, 4, 0,
                                                                                                            0, 71, 2,
   '私、妙高型重巡洋艦、妙高と申します。<br>共に頑張りましょう。', 80, '2,2,4,4,0', 56, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (310, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '磯風改', 1413, 2, 3, '{1,1,1,1}', 18, 12, 28, 14, 24, 0, 0, 0, 59, 48, 79, 49,
                                                                                                            64, 0, 3, 0,
                                                                                                            0, 49, 1,
   '陽炎型駆逐艦十二番艦、磯風。<br>司令、共に進もう…心配はいらない。', 24, '0,0,0,0,0', 33, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (311, 0, '0,0', 7, '{4,3,14,3}', 35, 35, '大淀改', 1414, 3, 3, '{2,0,2,2}', 30, 32, 0, 32, 22, 0, 0, 0, 79, 63, 49, 68,
                                                                                                           74, 0, 4, 0,
                                                                                                           0, 64, 2,
   '提督、旗艦大淀、お供いたします。<br>前線艦隊指揮はどうぞお任せください！', 80, '0,6,6,0,0', 47, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (312, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '時津風改', 1415, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 48, 79, 49,
                                                                                                             49, 0, 3,
                                                                                                             0, 0, 49,
                                                                                                             1,
   '陽炎型駆逐艦十番艦。<br>時津風……出るよ。', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (313, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '春雨改', 1416, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 15, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 57, 1,
   '白露型駆逐艦五番艦の春雨です、はい。<br>輸送作戦はお任せください……です。', 22, '0,0,0,0,0', 30, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (314, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '早霜改', 1417, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 50, 80, 49,
                                                                                                            50, 0, 3, 0,
                                                                                                            0, 49, 1,
   'また…来てしまったのね、この海に。<br>夕雲型駆逐艦、早霜…着任しました。', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (315, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '清霜改', 1418, 2, 3, '{1,1,1,1}', 13, 12, 28, 14, 16, 0, 0, 0, 59, 50, 80, 49,
                                                                                                            50, 0, 3, 0,
                                                                                                            0, 49, 1,
   'どうも！夕雲型の最終艦、清霜です。<br>到着遅れました、よろしくお願いです！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (316, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '初春改二', 204, 2, 1, '{1,2,1,1}', 16, 13, 32, 14, 23, 0, 0, 0, 59, 52, 88, 51,
                                                                                                            73, 0, 3, 0,
                                                                                                            0, 52, 1,
   'わらわが初春じゃ。<br>よろしく頼みますぞ。', 20, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (317, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '朝雲改', 1419, 2, 3, '{1,1,1,1}', 12, 12, 28, 14, 16, 0, 0, 0, 59, 49, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 59, 1,
   '朝潮型駆逐艦、朝雲、着任したわ！<br>貴方が司令…かあ。ふうーん。ま、いいわ。私がやったげる！', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (318, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '山雲改', 1420, 2, 3, '{1,1,1,1}', 11, 12, 28, 14, 16, 0, 0, 0, 58, 49, 79, 48,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 59, 1,
   'おはようございます～。<br>朝潮型駆逐艦六番艦、山雲、入ります～。', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (319, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '野分改', 1421, 2, 3, '{1,1,1,1}', 13, 12, 28, 14, 16, 0, 0, 0, 59, 48, 79, 49,
                                                                                                            49, 0, 3, 0,
                                                                                                            0, 49, 1,
   '陽炎型駆逐艦、野分。参上しました。<br>さあ、司令。いきましょう。', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (320, 0, '0,0', 7, '{1,2,6,1}', 25, 20, '秋月改', 1422, 2, 3, '{1,1,3,1}', 12, 24, 24, 16, 80, 0, 0, 0, 69, 57, 54, 53,
                                                                                                           116, 0, 3, 0,
                                                                                                           0, 57, 1,
   '秋月型防空駆逐艦、一番艦、秋月。<br>ここに推参致しました。お任せください！', 30, '0,0,0,0,0', 37, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (321, 50, '750,1000', 6, '{7,9,26,5}', 45, 50, '天城', 202, 11, 1, '{0,0,3,3}', 13, 0, 0, 26, 27, 0, 0, 0, 59, 25, 0,
                                                                                                               51, 72,
                                                                                                               0, 4, 0,
                                                                                                               0, 79, 1,
   '雲龍型航空母艦、天城と申します。<br>提督、どうぞよろしくお願い致します。<br>天城、精進致します！', 210, '18,24,3,6,0', 48, FALSE, 429);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (322, 50, '750,1000', 6, '{7,9,26,5}', 45, 50, '葛城', 203, 11, 1, '{0,0,3,3}', 20, 0, 0, 27, 27, 0, 0, 0, 69, 25, 0,
                                                                                                               52, 72,
                                                                                                               0, 4, 0,
                                                                                                               0, 79, 1,
   '雲龍型航空母艦、三番艦、葛城よ！<br>え？　水上防空砲台ですって？<br>ち、違うわよ！　提督、何いってんの！', 210, '18,24,3,6,0', 48, FALSE, 430);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (323, 55, '170,270', 6, '{1,2,2,1}', 20, 10, 'U-511改', 1504, 13, 1, '{1,2,0,0}', 34, 3, 27, 6, 0, 0, 0, 0, 67, 12, 64,
                                                                                                                 20, 0,
                                                                                                                 0, 2,
                                                                                                                 0, 0,
                                                                                                                 18, 1,
   'ドイツ海軍所属、潜水艦U-511です。<br>ユーとお呼びください。<br>少し遠出してきました。よろしくお願い致します……。', 22, '0,0,0,0,0', 13, TRUE, 436);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (324, 0, '0,0', 5, '{3,2,11,1}', 20, 35, '香取改', 1423, 21, 3, '{1,1,2,1}', 12, 16, 14, 15, 24, 0, 0, 0, 54, 36, 40, 39,
                                                                                                             48, 0, 4,
                                                                                                             0, 0, 54,
                                                                                                             2,
   '練習巡洋艦、香取です。<br>心配しないで…。色々と優しく、指導させて頂きますから。', 70, '2,2,2,2,0', 40, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (325, 0, '0,0', 5, '{1,3,10,1}', 20, 15, '朝霜改', 1424, 2, 1, '{0,1,1,1}', 18, 12, 28, 14, 22, 0, 0, 0, 68, 47, 78, 49,
                                                                                                            62, 0, 3, 0,
                                                                                                            0, 49, 1,
   'よお！　夕雲型駆逐艦、十六番艦の朝霜、いつでも出撃できんぜ。<br>まだまだ、暴れよう…な、司令！', 24, '0,0,0,0,0', 33, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (326, 0, '0,0', 5, '{1,2,10,0}', 20, 15, '高波改', 1425, 2, 3, '{1,1,1,1}', 10, 12, 28, 14, 16, 0, 0, 0, 57, 50, 80, 49,
                                                                                                            50, 0, 3, 0,
                                                                                                            0, 49, 1,
   '夕雲型駆逐艦、六番艦の高波です。<br>あ、あの…頑張ります！ホントかもです！', 24, '0,0,0,0,0', 32, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (327, 0, '0,0', 4, '{1,2,2,1}', 20, 10, '伊168改', 1498, 13, 3, '{0,2,0,0}', 10, 3, 30, 5, 0, 0, 0, 0, 49, 11, 69, 18,
                                                                                                           0, 0, 2, 0,
                                                                                                           0, 19, 1,
   '伊１６８よ。何よ、言いにくいの？<br>じゃ、イムヤでいいわ…よろしくねっ！', 22, '0,0,0,0,0', 15, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (328, 0, '0,0', 5, '{1,2,2,2}', 25, 10, '伊58改', 1499, 14, 3, '{0,2,1,0}', 50, 3, 36, 5, 0, 0, 0, 0, 79, 12, 84, 19, 0,
                                                                                                          0, 2, 0, 0,
                                                                                                          24, 1,
   'こんにちは！ 伊五十八です。<br>ゴーヤって呼んでもいいよ！苦くなんかないよぉ！', 22, '1,1,0,0,0', 18, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (329, 0, '0,0', 6, '{1,2,2,2}', 25, 10, '伊8改', 1500, 14, 3, '{0,2,1,0}', 25, 4, 36, 5, 0, 0, 0, 0, 69, 14, 84, 19, 0,
                                                                                                         0, 2, 0, 0, 25,
                                                                                                         1,
   'グーテンターク…あ、違った、ごめんなさいね…<br>「はち」と呼んでくださいね。', 22, '1,1,0,0,0', 19, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (330, 0, '0,0', 5, '{1,2,2,2}', 25, 10, '伊19改', 1501, 14, 3, '{0,2,1,0}', 13, 3, 42, 5, 0, 0, 0, 0, 59, 12, 89, 19, 0,
                                                                                                          0, 2, 0, 0,
                                                                                                          24, 1,
   '素敵な提督で嬉しいのね。<br>伊十九なの。そう、イクって呼んでもいいの！', 22, '1,1,0,0,0', 18, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (331, 0, '0,0', 6, '{1,0,1,0}', 10, 10, 'まるゆ改', 1502, 13, 3, '{0,1,0,1}', 7, 1, 0, 2, 0, 0, 0, 0, 77, 5, 19, 11, 0, 0,
                                                                                                        1, 0, 0, 13, 1,
   '隊長、もっとまるゆに頑張らせてくださいね。', 17, '0,0,0,0,0', 7, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (332, 0, '0,0', 7, '{1,2,4,3}', 30, 25, '伊401改', 1503, 14, 3, '{0,2,1,1}', 20, 6, 40, 7, 0, 0, 0, 0, 59, 19, 80, 24,
                                                                                                           0, 0, 2, 0,
                                                                                                           0, 39, 1,
   '提督、ごきげんよう。<br>潜特型二番艦伊401、改良型です！', 200, '3,3,0,0,0', 24, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (333, 50, '750,1000', 6, '{7,9,26,5}', 45, 50, '雲龍', 201, 11, 1, '{0,0,3,3}', 10, 0, 0, 26, 28, 0, 0, 0, 49, 27, 0,
                                                                                                               52, 72,
                                                                                                               0, 4, 0,
                                                                                                               0, 79, 1,
   '雲龍型航空母艦、雲龍、推参しました。<br>提督、よろしくお願いしますね。', 210, '18,24,3,6,0', 48, FALSE, 406);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (334, 30, '110,120', 4, '{1,1,5,0}', 20, 15, '春雨', 205, 2, 1, '{1,1,0,0}', 10, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 32, 1,
   '白露型駆逐艦五番艦の春雨です、はい。<br>輸送作戦はお任せください……です。', 22, '0,0,0,0,0', 16, FALSE, 323);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (335, 0, '0,0', 7, '{7,13,30,10}', 55, 50, '雲龍改', 206, 11, 3, '{0,0,4,3}', 12, 0, 0, 35, 32, 0, 0, 0, 59, 48, 0, 77,
                                                                                                            78, 0, 4, 0,
                                                                                                            0, 84, 1,
   '雲龍型航空母艦、雲龍、参ります。<br>提督、新生機動部隊はお任せください！', 210, '18,21,27,3,0', 60, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (336, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '潮改二', 207, 2, 1, '{1,2,2,1}', 32, 10, 25, 15, 24, 0, 0, 0, 80, 50, 80, 55,
                                                                                                           74, 0, 3, 0,
                                                                                                           0, 53, 1,
   '特型駆逐艦…綾波型の「潮」です。<br>もう下がってよろしいでしょうか…。', 20, '0,0,0,0,0', 33, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (337, 0, '0,0', 6, '{6,14,26,10}', 50, 45, '隼鷹改二', 208, 7, 1, '{0,0,4,3}', 41, 0, 0, 31, 36, 0, 0, 0, 84, 40, 0, 62,
                                                                                                            74, 0, 4, 0,
                                                                                                            0, 82, 1,
   '商船改装空母、隼鷹でーすっ！<br>ひゃっはぁー！', 180, '24,18,20,4,0', 55, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (338, 30, '110,140', 4, '{1,1,6,0}', 20, 15, '早霜', 209, 2, 1, '{0,1,0,1}', 11, 10, 24, 6, 9, 0, 0, 0, 49, 30, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   'また…来てしまったのね、この海に。<br>夕雲型駆逐艦、早霜…着任しました。', 24, '0,0,0,0,0', 16, FALSE, 324);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (339, 30, '110,140', 4, '{1,1,6,0}', 20, 15, '清霜', 210, 2, 1, '{0,1,0,1}', 12, 10, 24, 6, 9, 0, 0, 0, 49, 30, 69, 19,
                                                                                                            39, 0, 2, 0,
                                                                                                            0, 34, 1,
   'どうも！夕雲型の最終艦、清霜です。<br>到着遅れました、よろしくお願いです！', 24, '0,0,0,0,0', 16, FALSE, 325);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (340, 0, '0,0', 6, '{12,15,38,5}', 140, 105, '扶桑改二', 211, 10, 1, '{5,0,3,4}', 13, 80, 0, 72, 44, 0, 0, 0, 69, 99, 0,
                                                                                                                90, 88,
                                                                                                                0, 4, 0,
                                                                                                                0, 94,
                                                                                                                3,
   '扶桑型超弩級戦艦、姉の扶桑です。<br>妹の山城ともども、よろしくお願い致します。', 260, '4,4,9,23,0', 77, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (341, 0, '0,0', 6, '{12,15,38,5}', 140, 105, '山城改二', 212, 10, 1, '{5,0,3,4}', 14, 80, 0, 73, 43, 0, 0, 0, 70, 98, 0,
                                                                                                                91, 87,
                                                                                                                0, 4, 0,
                                                                                                                0, 94,
                                                                                                                3,
   '扶桑型戦艦姉妹、妹のほう、山城です。<br>あの、扶桑姉さま、見ませんでした？', 260, '4,4,9,23,0', 77, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (342, 35, '110,140', 4, '{1,1,5,0}', 20, 15, '朝雲', 213, 2, 1, '{0,1,0,1}', 8, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 33, 1,
   '朝潮型駆逐艦、朝雲、着任したわ！<br>貴方が司令…かあ。ふうーん。ま、いいわ。私がやったげる！', 22, '0,0,0,0,0', 16, FALSE, 327);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (343, 35, '110,140', 4, '{1,1,5,0}', 20, 15, '山雲', 214, 2, 1, '{0,1,0,1}', 7, 10, 24, 6, 9, 0, 0, 0, 49, 29, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 33, 1,
   'おはようございます～。<br>朝潮型駆逐艦六番艦、山雲です～。<br>よろしくお願い致します～。', 22, '0,0,0,0,0', 16, FALSE, 328);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (344, 35, '110,140', 5, '{1,1,6,0}', 20, 15, '野分', 215, 2, 1, '{0,1,0,1}', 14, 10, 24, 6, 12, 0, 0, 0, 49, 29, 69, 19,
                                                                                                             44, 0, 2,
                                                                                                             0, 0, 34,
                                                                                                             1,
   '陽炎型駆逐艦、野分。参上しました。<br>さあ、司令。いきましょう。', 24, '0,0,0,0,0', 16, FALSE, 329);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (345, 0, '0,0', 6, '{3,7,16,1}', 65, 35, '古鷹改二', 216, 5, 1, '{2,1,1,2}', 14, 39, 24, 34, 22, 0, 0, 0, 64, 77, 75, 72,
                                                                                                            64, 0, 4, 0,
                                                                                                            0, 65, 2,
   '古鷹と言います。<br>重巡洋艦のいいところ、たくさん知ってもらえると嬉しいです。', 60, '2,2,2,2,0', 53, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (346, 0, '0,0', 6, '{3,7,16,1}', 65, 35, '加古改二', 217, 5, 1, '{2,1,1,2}', 12, 40, 25, 33, 24, 0, 0, 0, 62, 78, 77, 72,
                                                                                                            65, 0, 4, 0,
                                                                                                            0, 64, 2,
   '古鷹型重巡の2番艦、加古ってんだ、よっろしくぅー！', 60, '2,2,2,2,0', 52, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (347, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '初霜改二', 219, 2, 1, '{2,2,1,1}', 53, 12, 28, 14, 34, 0, 0, 0, 100, 50, 84, 51,
                                                                                                             79, 0, 3,
                                                                                                             0, 0, 52,
                                                                                                             1,
   '初春型四番艦、初霜です。<br>皆さん、よろしくお願いします！', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (348, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '叢雲改二', 220, 2, 3, '{1,2,1,1}', 15, 14, 32, 14, 27, 0, 0, 0, 57, 55, 89, 50,
                                                                                                            74, 0, 3, 0,
                                                                                                            0, 49, 1,
   'あんたが司令官ね。<br>ま、せいぜい頑張りなさい！', 22, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (349, 40, '170,270', 6, '{1,2,6,1}', 25, 20, '秋月', 221, 2, 1, '{0,1,3,1}', 10, 16, 16, 9, 70, 0, 0, 0, 59, 48, 48, 27,
                                                                                                             104, 0, 3,
                                                                                                             0, 0, 40,
                                                                                                             1,
   '秋月型防空駆逐艦、一番艦、秋月。<br>ここに推参致しました。お任せください！', 30, '0,0,0,0,0', 20, FALSE, 330);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (350, 30, '110,130', 4, '{1,1,6,0}', 20, 15, '高波', 224, 2, 1, '{0,1,0,1}', 8, 10, 24, 6, 9, 0, 0, 0, 44, 30, 69, 19,
                                                                                                           39, 0, 2, 0,
                                                                                                           0, 34, 1,
   '夕雲型駆逐艦、六番艦の高波です。<br>あ、あの…頑張ります！ホントかもです！', 24, '0,0,0,0,0', 16, FALSE, 345);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (351, 45, '150,170', 4, '{1,1,6,0}', 20, 15, '朝霜', 225, 2, 1, '{0,1,0,1}', 16, 10, 24, 6, 9, 0, 0, 0, 59, 29, 68, 19,
                                                                                                            44, 0, 2, 0,
                                                                                                            0, 34, 1,
   'よお！　あたいは、夕雲型駆逐艦、十六番艦の朝霜さ。<br>覚えといてよ。忘れんなよ……なあ！', 24, '0,0,0,0,0', 16, FALSE, 344);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (352, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '吹雪改二', 226, 2, 3, '{2,2,1,1}', 17, 15, 30, 14, 35, 0, 0, 0, 77, 59, 88, 50,
                                                                                                            78, 0, 3, 0,
                                                                                                            0, 49, 1,
   'はじめまして吹雪です。<br>よろしくお願い致します。', 20, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (353, 0, '0,0', 6, '{4,7,21,3}', 80, 45, '鳥海改二', 227, 5, 1, '{4,1,2,2}', 19, 55, 35, 46, 24, 0, 0, 0, 68, 85, 86, 78,
                                                                                                            70, 0, 4, 0,
                                                                                                            0, 72, 2,
   '私が鳥海です。よろしくです。', 85, '3,3,3,3,0', 57, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (354, 0, '0,0', 6, '{4,6,21,4}', 80, 45, '摩耶改二', 228, 5, 1, '{2,1,5,2}', 14, 42, 34, 48, 72, 0, 0, 0, 64, 77, 84, 78,
                                                                                                            106, 0, 4,
                                                                                                            0, 0, 71, 2,
   'よ！アタシ、摩耶ってんだ、よろしくな。', 85, '3,3,3,3,0', 57, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (355, 0, '0,0', 7, '{7,13,30,10}', 55, 50, '天城改', 229, 11, 3, '{0,0,4,3}', 17, 0, 0, 35, 33, 0, 0, 0, 69, 45, 0, 76,
                                                                                                            79, 0, 4, 0,
                                                                                                            0, 84, 1,
   '雲龍型航空母艦、天城です。<br>提督、天城、今なら十分活躍できます！', 210, '18,21,27,3,0', 60, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (356, 0, '0,0', 7, '{7,13,30,10}', 55, 50, '葛城改', 230, 11, 3, '{0,0,4,3}', 30, 0, 0, 36, 32, 0, 0, 0, 79, 45, 0, 78,
                                                                                                            78, 0, 4, 0,
                                                                                                            0, 84, 1,
   '雲龍型航空母艦、三番艦、葛城よ！<br>え？　水上防空砲台ですって？<br>ち、違うわよ！　提督、何いってんの！', 210, '18,21,27,3,0', 60, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (357, 35, '170,270', 5, '{1,2,2,1}', 20, 10, 'U-511', 231, 13, 1, '{0,2,0,0}', 30, 2, 22, 4, 0, 0, 0, 0, 63, 8, 58,
                                                                                                               16, 0, 0,
                                                                                                               1, 0, 0,
                                                                                                               16, 1,
   'ドイツ海軍所属、潜水艦U-511です。<br>ユーとお呼びください。<br>少し遠出してきました。よろしくお願い致します……。', 22, '0,0,0,0,0', 8, FALSE, 334);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (358, 0, '0,0', 6, '{1,2,7,0}', 15, 15, '睦月改二', 234, 2, 1, '{1,2,1,0}', 14, 10, 28, 12, 16, 0, 0, 0, 64, 45, 79, 43,
                                                                                                           56, 0, 3, 0,
                                                                                                           0, 43, 1,
   '睦月です。<br>はりきって、まいりましょー！', 18, '0,0,0,0,0', 27, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (359, 0, '0,0', 6, '{1,2,7,0}', 15, 15, '如月改二', 235, 2, 1, '{1,2,1,0}', 13, 10, 28, 12, 18, 0, 0, 0, 60, 46, 80, 43,
                                                                                                           57, 0, 3, 0,
                                                                                                           0, 43, 1,
   '如月と申します。<br>おそばに置いてくださいね。', 18, '0,0,0,0,0', 27, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (360, 0, '0,0', 7, '{1,2,2,1}', 20, 10, '呂500', 236, 13, 3, '{1,2,0,0}', 44, 4, 30, 7, 0, 0, 0, 0, 77, 13, 69, 21, 0,
                                                                                                         0, 2, 0, 0, 19,
                                                                                                         1,
   'UボートU-511改め、呂号第500潜水艦です。<br>ユーちゃん改め、ローちゃんです。<br>テイトク、よろしくお願いしまーす！', 22, '0,0,0,0,0', 13, FALSE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (361, 0, '0,0', 6, '{1,2,10,0}', 20, 15, '暁改二', 237, 2, 3, '{1,2,1,1}', 15, 14, 32, 14, 19, 0, 0, 0, 67, 60, 90, 50,
                                                                                                           59, 0, 3, 0,
                                                                                                           0, 50, 1,
   '暁よ。<br>一人前のレディーとして扱ってよね！', 20, '0,0,0,0,0', 31, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (362, 35, '900,1500', 6, '{10,18,37,6}', 150, 130, 'Littorio', 241, 8, 1, '{3,0,1,3}', 20, 78, 0, 72, 40, 0, 0, 0, 69,
    97, 0, 86, 72, 0, 4, 0, 0, 94, 4, 'ヴィットリオ・ヴェネト級戦艦２番艦、リットリオです。<br>火力と速度には自信があるの。よろしくお願いしますね。', 300, '3,3,3,3,0', 88,
   FALSE, 446);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (363, 35, '900,1500', 6, '{10,18,37,6}', 150, 130, 'Roma', 242, 8, 1, '{3,0,1,3}', 6, 79, 0, 71, 44, 0, 0, 0, 39, 98,
                                                                                                                    0,
                                                                                                                    85,
                                                                                                                    74,
                                                                                                                    0,
                                                                                                                    4,
                                                                                                                    0,
                                                                                                                    0,
                                                                                                                    94,
                                                                                                                    4,
   'ヴィットリオ・ヴェネト級戦艦４番艦、ローマです、よろしく。<br>何？あまりジロジロ見ないでくださいね。', 300, '3,3,3,3,0', 88, FALSE, 447);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (364, 35, '350,700', 7, '{3,1,7,4}', 10, 50, '秋津洲', 245, 16, 1, '{0,0,1,1}', 12, 6, 0, 9, 12, 0, 0, 0, 59, 18, 0, 25,
                                                                                                             36, 0, 2,
                                                                                                             0, 0, 44,
                                                                                                             1,
   '水上機母艦、秋津洲よ！<br>この大艇ちゃんと一緒に覚えてよね！', 70, '1,1,0,0,0', 32, FALSE, 450);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (365, 0, '0,0', 7, '{18,28,39,7}', 170, 140, 'Italia', 246, 8, 3, '{5,0,2,3}', 30, 81, 0, 77, 44, 0, 0, 0, 79, 102, 0,
                                                                                                                 92, 90,
                                                                                                                 0, 4,
                                                                                                                 0, 0,
                                                                                                                 98, 4,
   'ヴィットリオ・ヴェネト級戦艦二番艦、リットリオ改め、イタリアです。<br>よろしくお願いしますね。', 300, '3,3,3,3,0', 92, FALSE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (366, 0, '0,0', 7, '{18,28,39,7}', 170, 140, 'Roma改', 247, 8, 3, '{5,0,2,3}', 8, 82, 0, 76, 46, 0, 0, 0, 57, 105, 0,
                                                                                                               90, 94,
                                                                                                               0, 4, 0,
                                                                                                               0, 98, 4,
   'ヴィットリオ・ヴェネト級戦艦４番艦、ローマです、よろしく。<br>何？あまりジロジロ見ないでくださいね。', 300, '3,3,3,3,0', 92, TRUE, 0);
INSERT INTO ship (id, afterlv, remodel_cost, rarity, broken, ammo_max, fuel_max, name, number, stype, voicef, modern_use, luck_base, firepower_base, torpedo_base, armour_base, antiair_base, antisub_base, los_base, evasion_base, luck_max, firepower_max, torpedo_max, armour_max, antiair_max, antisub_max, maxslots, maxlos, evasion_max, maxhp, srange, getmsg, buildtime, maxplanes, hp_base, kai, aftership_num)
VALUES
  (367, 0, '0,0', 8, '{3,1,7,6}', 15, 60, '秋津洲改', 250, 16, 3, '{0,0,2,1}', 14, 8, 0, 13, 16, 0, 0, 0, 72, 28, 0, 42, 44,
                                                                                                          0, 3, 0, 0,
                                                                                                          48, 1,
   '水上機母艦、秋津洲よ！<br>この大艇ちゃんと一緒に覚えてよね！', 70, '1,1,1,0,0', 36, TRUE, 0);


--
-- Name: ship_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('ship_id_seq', 367, TRUE);


--
-- PostgreSQL database dump complete
--

