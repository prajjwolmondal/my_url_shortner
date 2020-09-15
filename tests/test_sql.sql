DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `urllist`;

CREATE TABLE `users` (
  `username` varchar(40) NOT NULL,
  `user_id` varchar(32) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` blob NOT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `users_UNIQUE` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `urllist` (
  `short_code` varchar(6) NOT NULL,
  `full_url` varchar(120) NOT NULL,
  `created_at` datetime NOT NULL,
  `created_by` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO heroku_14ff47fb4752f4e.urllist (short_code, full_url, created_at, created_by) VALUES
('ILAMMO', 'https://www.linkedin.com/in/prajjwolmondal/', '2020-08-07 03:46:12.0', 'c6565937-4948-436b-a95b-b0fa7435'),
('ULOTIG', 'https://github.com/prajjwolmondal/', '2020-07-28 03:50:14.0', null),
('NSSTOR', 'https://docs.pylonsproject.org/projects/webtest/en/latest/api.html', '2020-09-15 16:25:20.0', NULL)
;

