/* Default resources values. */
insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 1, 0, 0, 0, 0
  where not exists(
      select id from recipe__resources where id = 1
  );

insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 2, 2147483647, 2147483647, 2147483647, 2147483647
  where not exists(
      select id from recipe__resources where id = 2
  );

/* Lower class destroyers, subs, and CL. */

insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 3, 30, 30, 30, 30
  where not exists(
      select id from recipe__resources where id = 3
  );

insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 4, 100, 100, 100, 30
  where not exists(
      select id from recipe__resources where id = 4
  );

/* CL/CA */

insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 5, 250, 130, 250, 30
  where not exists(
      select id from recipe__resources where id = 5
  );

/* CA */

insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 6, 270, 30, 330, 130
  where not exists(
    select id from recipe__resources where id = 6
  );

/* BB */
insert into recipe__resources (id, fuel, ammo, steel, baux)
    select 7, 400, 100, 600, 30
  where not exists(
    select id from recipe__resources where id = 7
  );

insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 8, 500, 100, 600, 30
  where not exists(
    select id from recipe__resources where id = 8
  );

/* CV */

insert into recipe__resources (id, fuel, ammo, steel, baux)
  select 9, 300, 100, 400, 300
  where not exists(
    select id from recipe__resources where id = 9
  );

insert into recipe__resources (id, fuel, ammo, steel, baux)
    select 10, 300, 100, 400, 330
  where not exists(
    select id from recipe__resources where id = 10
  );

/* SS */
insert into recipe__resources (id, fuel, ammo, steel, baux)
    select 11, 250, 30, 200, 30
    where not exists(
      select id from recipe__resources where id = 11
    );