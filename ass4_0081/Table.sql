CREATE TABLE Towns (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    lat NUMERIC(10, 8),
    lng NUMERIC(11, 8),
    country VARCHAR(255),
    iso2 VARCHAR(2),
    admin_name VARCHAR(255),
    capital VARCHAR(20),
    population INTEGER,
    population_proper INTEGER
);

COPY Towns (city, lat, lng,country,iso2,admin_name,capital, population, population_proper)
FROM 'C:/SCHOOL/2024/5.1/webmapping/kenya cities.csv'
DELIMITER ',' CSV HEADER;