-- Inital Database for Let's Meet

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
    `userid` int(10) NOT NULL AUTO_INCREMENT,
    `email` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
    `password` varchar(45) CHARACTER SET utf8mb4 NOT NULL,
    `name` varchar(45) CHARACTER SET utf8mb4 NOT NULL,
    PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES  (1,'bob@g.com','1234','Bob'),
                            (2,'tom@g.com','1234','Tom'),
                            (3,'sally@g.com','1234','Sally'),
                            (4,'jack@g.com','1234','Jack'),
                            (5,'jerry@g.com','1234','Jerry'),
                            (6,'elon@g.com','1234','Elon'),
                            (7,'bill@g.com','1234','Bill'),
                            (8,'niki@g.com','1234','Niki');
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;

CREATE TABLE `events` (
    `eventid` int(10) NOT NULL AUTO_INCREMENT,
    `title` varchar(100) CHARACTER SET utf8mb4 NOT NULL,
    `edate` date NOT NULL,
    `description` varchar(300) CHARACTER SET utf8mb4 NOT NULL,
    `host` int(10) NOT NULL,
    PRIMARY KEY (`eventid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
INSERT INTO `events` VALUES (1,'Music Concert','2020-03-17','Come join us for another big concert',7),
                            (2,'Camping','2020-06-22','Have fun at our annual comping trip!',8);
UNLOCK TABLES;