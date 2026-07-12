create table season_awards (
  id serial primary key,
  dynasty_id uuid references dynasties(id) on delete cascade,
  season int not null,
  award_type text not null, -- 'player_of_year', 'coach_of_year', 'all_conference', etc.
  player_id uuid references players(id),
  conference text,
  created_at timestamptz default now()
);