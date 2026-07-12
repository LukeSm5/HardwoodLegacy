create table players (
  id uuid primary key default gen_random_uuid(),
  dynasty_id uuid references dynasties(id) on delete cascade,
  first_name text not null,
  last_name text not null,
  position text not null check (position in ('PG', 'SG', 'SF', 'PF', 'C')),
  archetype text not null,
  year int not null check (year between 1 and 5), -- 5 = redshirt
  is_redshirting boolean default false,
  height_inches int,
  weight_lbs int,

  -- Ratings (0-100)
  overall int not null,
  scoring int not null,
  defense int not null,
  athleticism int not null,
  basketball_iq int not null,
  rebounding int not null,
  passing int not null,
  three_point int not null,
  development_potential int not null, -- hidden ceiling
  development_focus text check (development_focus in ('shooting', 'strength', 'iq', null)),

  -- Status
  is_injured boolean default false,
  injury_games_remaining int default 0,
  fatigue int default 0 check (fatigue between 0 and 100),
  rotation_minutes int default 0,
  is_starter boolean default false,
  player_role text, -- 'ball_handler', 'defensive_stopper', 'stretch_big', etc.

  created_at timestamptz default now()
);

-- Career stats history per season
create table player_season_stats (
  id serial primary key,
  player_id uuid references players(id) on delete cascade,
  dynasty_id uuid references dynasties(id) on delete cascade,
  season int not null,
  games_played int default 0,
  points_per_game numeric(4,1) default 0,
  rebounds_per_game numeric(4,1) default 0,
  assists_per_game numeric(4,1) default 0,
  fg_pct numeric(4,3) default 0,
  three_pct numeric(4,3) default 0,
  true_shooting_pct numeric(4,3) default 0,
  turnovers_per_game numeric(4,1) default 0,
  steals_per_game numeric(4,1) default 0,
  blocks_per_game numeric(4,1) default 0
);