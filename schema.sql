create table piles (
  id integer primary key autoincrement,
  title text not null,
  balance integer not null
);

create table transactions (
    id integer primary key autoincrement,
    pile_id integer not null,
    name text not null,
    amount integer not null
);
