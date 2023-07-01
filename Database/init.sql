CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    ip_address VARCHAR(255),
    user_agent VARCHAR(255),
    accept_languages VARCHAR(255),
    resolution VARCHAR(255),
    ppi VARCHAR(255),
    server_time TIMESTAMP,
    local_time TIMESTAMP,
    cookie VARCHAR(255)
);
