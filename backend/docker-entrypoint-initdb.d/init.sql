CREATE DATABASE backend;
CREATE ROLE backend WITH ENCRYPTED PASSWORD '123456';
ALTER ROLE backend WITH LOGIN;
ALTER DATABASE backend OWNER TO backend;
\connect backend;
GRANT CREATE ON SCHEMA public TO backend;