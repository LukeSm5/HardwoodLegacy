create table programs (
  id serial primary key,
  name text not null,
  abbreviation text not null,
  conference text not null,
  prestige_tier int not null check (prestige_tier between 1 and 5),
  location text,
  arena_capacity int default 10000,
  practice_facility_level int default 1,
  locker_room_level int default 1,
  recruiting_budget int default 500000,
  nil_budget int default 250000,
  fan_support int default 50 check (fan_support between 0 and 100),
  created_at timestamptz default now()
);