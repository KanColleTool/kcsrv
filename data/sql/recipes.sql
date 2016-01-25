BEGIN TRANSACTION;

/* 電 */
insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 1, 5, 33, 1, 2
  where not exists(
    select id from recipe where id = 1
  );

/* 雷 */

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 2, 5, 32, 1, 2
  where not exists(
    select id from recipe where id = 2
  );

/* 響 */

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 3, 5, 31, 1, 2
  where not exists(
    select id from recipe where id = 3
  );

/* 暁 */

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 4, 5, 30, 1, 2
  where not exists(
    select id from recipe where id = 4
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 5, 5, 1, 1, 2
  where not exists(
    select id from recipe where id = 5
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 6, 5, 2, 1, 2
  where not exists(
    select id from recipe where id = 6
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 7, 5, 50, 4, 5
  where not exists(
    select id from recipe where id = 7
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 8, 5, 51, 4, 5
  where not exists(
    select id from recipe where id = 8
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 9, 5, 52, 4, 5
  where not exists(
    select id from recipe where id = 9
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 10, 5, 52, 4, 5
  where not exists(
    select id from recipe where id = 10
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 11, 5, 97, 4, 5
  where not exists(
    select id from recipe where id = 11
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 12, 5, 96, 4, 5
  where not exists(
    select id from recipe where id = 12
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 13, 5, 97, 4, 5
  where not exists(
    select id from recipe where id = 13
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 14, 5, 17, 4, 5
  where not exists(
    select id from recipe where id = 14
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 15, 5, 95, 4, 5
  where not exists(
    select id from recipe where id = 15
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 16, 1, 20, 4, 5
  where not exists(
    select id from recipe where id = 16
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 17, 1, 21, 4, 5
  where not exists(
    select id from recipe where id = 17
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 18, 10, 55, 5, 6
  where not exists(
    select id from recipe where id = 18
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 19, 10, 56, 5, 6
  where not exists(
    select id from recipe where id = 19
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 20, 8, 62, 5, 6
  where not exists(
    select id from recipe where id = 20
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 21, 8, 63, 5, 6
  where not exists(
    select id from recipe where id = 21
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 22, 5, 120, 5, 6
  where not exists(
    select id from recipe where id = 22
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 23, 1, 74, 7, 8
  where not exists(
    select id from recipe where id = 23
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 24, 1, 120, 7, 8
  where not exists(
    select id from recipe where id = 24
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 25, 1, 82, 7, 8
  where not exists(
    select id from recipe where id = 25
  );

insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 26, 1, 81, 7, 8
  where not exists(
    select id from recipe where id = 26
  );




END TRANSACTION;