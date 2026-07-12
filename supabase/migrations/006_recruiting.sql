create table recruits (
  id uuid primary key default gen_random_uuid(),
  dynasty_id uuid references dynasties(id) on delete cascade,
  season int not null,
  first_name text not null,
  last_name text not null,
  position text not null check (position in ('PG', 'SG', 'SF', 'PF', 'C')),
  archetype text not null,
  star_rating int check (star_rating between 1 and 5),
  national_ranking int,
  overall_rating int not null,
  scoring int not null,
  defense int not null,
  athleticism int not null,
  basketball_iq int not null,
  development_potential int not null,
  is_hidden_gem boolean default false,

  -- Recruit preferences (0-100 weight)
  values_playing_time int default 50,
  values_academics int default 50,
  values_location int default 50,
  values_facilities int default 50,
  values_nil int default 50,

  -- Status
  status text default 'available' check (status in ('available', 'offered', 'visited', 'committed', 'signed', 'lost')),
  committed_to_program_id int references programs(id),
  interest_level int default 0 check (interest_level between 0 and 100),
  nil_offer_amount int default 0,
  has_visited boolean default false,
  created_at timestamptz default now()
);

create table scholarship_offers (
  id serial primary key,
  dynasty_id uuid references dynasties(id) on delete cascade,
  recruit_id uuid references recruits(id) on delete cascade,
  offered_at timestamptz default now(),
  nil_amount int default 0,
  status text default 'pending' check (status in ('pending', 'accepted', 'declined'))
);