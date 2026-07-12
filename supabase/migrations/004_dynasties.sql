create table dynasties (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade,
  program_id int references programs(id),
  coaching_background text not null check (coaching_background in ('offense_specialist', 'recruiter', 'developer')),
  current_season int default 1,
  coach_xp int default 0,
  coach_level int default 1,
  job_security int default 75 check (job_security between 0 and 100),
  created_at timestamptz default now()
);

-- Coaching skill tree
create table coaching_skills (
  id serial primary key,
  dynasty_id uuid references dynasties(id) on delete cascade,
  skill_name text not null,
  skill_category text not null check (skill_category in ('recruiting', 'development', 'strategy', 'program_management')),
  level int default 0,
  unlocked_at timestamptz
);