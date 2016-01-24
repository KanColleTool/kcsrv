BEGIN TRANSACTION;

/* 電 */
insert into recipe (id, chance, ship_id, min_resources_id, max_resources_id)
    select 1, 5, 33, 1, 2
  where not exists(
    select id from recipe where id = 1
  );


END TRANSACTION;