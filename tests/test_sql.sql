DROP TABLE IF EXISTS `urllist`;

CREATE TABLE urllist (
    short_code varchar(6),
    full_url varchar(80),
    created_at datetime
);

INSERT INTO url_shortcodes.urllist
(short_code, full_url, created_at)
VALUES('ILAMMO', 'https://www.linkedin.com/in/prajjwolmondal/', '2020-08-07 03:46:12.0');

INSERT INTO url_shortcodes.urllist
(short_code, full_url, created_at)
VALUES('ULOTIG', 'https://github.com/prajjwolmondal/', '2020-07-28 03:50:14.0');
