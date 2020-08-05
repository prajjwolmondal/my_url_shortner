DROP TABLE IF EXISTS `urllist`;

CREATE TABLE urllist (
    short_code varchar(6),
    full_url varchar(80),
    created_at datetime
);

INSERT INTO urllist
VALUES (
    'ULOTIG',
    'https://github.com/prajjwolmondal/',
    '2020-07-28 03:50:14.0'
);