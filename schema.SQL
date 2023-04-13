CREATE TABLE IF NOT EXISTS Users(
  customer_email TEXT NOT NULL,
  pass_word TEXT NOT NULL,
  first_name TEXT,
  last_name TEXT,
  phone TEXT,
  hire_date TEXT,
  user_type TEXT,
  active TEXT,
  date_created TEXT,
  UNIQUE(customer_email)

);