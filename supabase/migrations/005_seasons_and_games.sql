create table seasons (
  id serial primary key,
  dynasty_id uuid references dynasties(id) on delete cascade,
  season_number int not null,
  is_complete boolean default false,
  conference_champion boolean default false,
  national_champion boolean default false,
  final_record_wins int default 0,
  final_record_losses int default 0,
  offensive_efficiency numeric(5,2),
  defensive_efficiency numeric(5,2),
  pace numeric(5,2),
  strength_of_schedule numeric(5,2)
);

create table games (
  id uuid primary key default gen_random_uuid(),
  dynasty_id uuid references dynasties(id) on delete cascade,
  season_id int references seasons(id) on delete cascade,
  opponent_program_id int references programs(id),
  is_home boolean default true,
  is_conference boolean default false,
  is_postseason boolean default false,
  game_type text default 'regular' check (game_type in ('regular', 'conference_tournament', 'ncaa_tournament')),
  scheduled_date date,
  is_simulated boolean default false,
  user_score int,
  opponent_score int,
  home_court_factor numeric(3,2) default 1.0
);

-- Per-game box score for each player
create table game_player_stats (
  id serial primary key,
  game_id uuid references games(id) on delete cascade,
  player_id uuid references players(id) on delete cascade,
  minutes int default 0,
  points int default 0,
  rebounds int default 0,
  assists int default 0,
  steals int default 0,
  blocks int default 0,
  turnovers int default 0,
  fg_made int default 0,
  fg_attempted int default 0,
  three_made int default 0,
  three_attempted int default 0,
  ft_made int default 0,
  ft_attempted int default 0
);

-- Play by play events for WebSocket replay/storage
create table game_play_by_play (
  id serial primary key,
  game_id uuid references games(id) on delete cascade,
  sequence_number int not null,
  clock_minutes int,
  clock_seconds int,
  half int check (half in (1, 2)),
  event_type text not null,
  description text not null,
  player_id uuid references players(id),
  score_user int,
  score_opponent int
);