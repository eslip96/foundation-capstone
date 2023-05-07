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

CREATE TABLE IF NOT EXISTS Assessment_Scores (
    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    date_taken TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users (rowid),
    FOREIGN KEY (assessment_id) REFERENCES Assessments (score_id),
    FOREIGN KEY (manager_id) REFERENCES Users (rowid)
);

CREATE TABLE IF NOT EXISTS Assessments (
assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
assessment_name TEXT NOT NULL,
date_created TEXT NOT NULL
);