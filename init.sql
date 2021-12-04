-- Initial Database for Let's Meet

--
-- Create new database `meet`
--

DROP DATABASE IF EXISTS `meet`;
CREATE DATABASE `meet`;
USE `meet`;

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
    `hostid` int(10) NOT NULL,
    PRIMARY KEY (`eventid`),
    FOREIGN KEY (`hostid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
INSERT INTO `events` VALUES (1,'Music Concert','2020-03-17','Come join us for another big concert',7),
                            (2,'Camping','2020-06-22','Have fun at our annual comping trip!',8);
UNLOCK TABLES;

--
-- Table structure for table `participants`
--

DROP TABLE IF EXISTS `participants`;

CREATE TABLE `participants` (
    `pid` int(10) NOT NULL AUTO_INCREMENT,
    `eventid` int(10) NOT NULL,
    `userid` int(10) NOT NULL,
    PRIMARY KEY (`pid`),
    FOREIGN KEY (`eventid`) REFERENCES `events` (`eventid`),
    FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `participants`
--

LOCK TABLES `participants` WRITE;
INSERT INTO `participants` VALUES   (1,2,3),
                                    (2,2,4),
                                    (3,2,2),
                                    (4,2,5),
                                    (5,1,1),
                                    (6,1,5);
UNLOCK TABLES;