create table transfer_portal (
  id uuid primary key default gen_random_uuid(),
  player_id uuid references players(id) on delete cascade,
  dynasty_id uuid references dynasties(id) on delete cascade,
  season int not null,
  reason text check (reason in ('playing_time', 'program_performance', 'personal', 'nil')),
  status text default 'available' check (status in ('available', 'committed', 'withdrawn')),
  nil_offer_amount int default 0,
  committed_to_program_id int references programs(id),
  entered_at timestamptz default now()
);