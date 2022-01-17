DROP DATABASE IF EXISTS bmstu_web_f1;
CREATE DATABASE bmstu_web_f1;
\c bmstu_web_f1


-- DROP TABLE users CASCADE;
CREATE TABLE IF NOT EXISTS users(
    id INT GENERATED ALWAYS AS IDENTITY,
    username VARCHAR,
    pswrd VARCHAR,  -- YES, I KNOW! I'm just lazy 
    user_role VARCHAR,

    PRIMARY KEY (id)
);

-- DROP TABLE gps CASCADE;
CREATE TABLE IF NOT EXISTS gps(
    id INT GENERATED ALWAYS AS IDENTITY,
    title VARCHAR,
    gp_date DATE,
    vendor_id INT,

    PRIMARY KEY (id),
    FOREIGN KEY(vendor_id) REFERENCES users(id)
);

-- DROP TABLE tickets CASCADE;
CREATE TABLE IF NOT EXISTS tickets(
    id INT GENERATED ALWAYS AS IDENTITY,
    price VARCHAR,
    gp_session INT,  -- bit-wise (e.g. 3 day = 111(7), only quali = 010(2), only gp = 001(1))
    gp_id INT,
    in_stock BOOLEAN DEFAULT TRUE,

    PRIMARY KEY (id),
    FOREIGN KEY(gp_id) REFERENCES gps(id)
);


INSERT INTO users(username, pswrd, user_role)
VALUES
    ('Dmitriy Kovalev', 'maxmaxsupermax', 'vendor'),
    ('Artem Sarkisov', '12345', 'client'),
    ('Vlad Krivozubov', 'qwerty', 'client');

INSERT INTO gps(title, gp_date, vendor_id)
VALUES
    ('FORMULA 1 GRAND PRIX DE MONACO 2022', '2022-05-27', 1),
    ('FORMULA 1 BELGIAN GRAND PRIX 2022', '2022-08-28', 1),
    ('FORMULA 1 JAPANESE GRAND PRIX 2022', '2022-10-09', 1),
    ('FORMULA 1 GRAN PREMIO D’ITALIA 2022', '2022-09-11', 1),
    ('FORMULA 1 GRANDE PREMIO DE SAO PAULO 2022', '2022-11-13', 1);

INSERT INTO tickets(price, gp_session, gp_id)
VALUES
    (100000, 7, 1),
    (500, 2, 2),
    (500, 2, 3),
    (200, 1, 4),
    (500, 4, 5),
    (7000, 7, 3);
