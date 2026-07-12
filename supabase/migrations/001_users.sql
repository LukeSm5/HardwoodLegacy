create table users (
  id uuid primary key references auth.users(id) on delete cascade,
  dark_mode boolean default false,
  created_at timestamptz default now()
);