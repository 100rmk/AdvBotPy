CREATE TABLE "users"
("user_id"	INTEGER NOT NULL UNIQUE,
"first_name" TEXT,
"second_name" TEXT,
"phone" TEXT NOT NULL UNIQUE,
PRIMARY KEY("user_id"));
