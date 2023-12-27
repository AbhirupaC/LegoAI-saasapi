create table Users (
    id serial primary key,
    email varchar(255) unique,
    password varchar(255),
    company varchar(255),
    full_name varchar(255),
    created_at timestamp default CURRENT_TIMESTAMP,
    last_logged_in timestamp,
    user_authentication_type varchar(255) default 'legoai'
);
