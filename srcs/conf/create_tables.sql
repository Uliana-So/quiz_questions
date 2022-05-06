CREATE SEQUENCE IF NOT EXISTS quiz_questions_id_seq;

CREATE TABLE IF NOT EXISTS quiz_questions (
    id SERIAL PRIMARY KEY,
    id_question INT NOT NULL,
    question CHAR(1500),
    answer CHAR(250),
    date_time CHAR(50)
);
