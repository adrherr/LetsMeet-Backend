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
    `email` varchar(200) CHARACTER SET utf8mb4 NOT NULL,
    `password` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
    `name` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
    `bio` varchar(2000) CHARACTER SET utf8mb4,
    PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES  (1,'bob@g.com','1234','Bob','Hi I like dogs'),
                            (2,'tom@g.com','1234','Tom',NULL),
                            (3,'sally@g.com','1234','Sally','Hello, I am a student in college and I am studying math'),
                            (4,'jack@g.com','1234','Jack','I really enjoy fishing at the beach'),
                            (5,'jerry@g.com','1234','Jerry',NULL),
                            (6,'elon@g.com','1234','Elon','I am going to buy out twitter 😏'),
                            (7,'bill@g.com','1234','Bill',NULL),
                            (8,'niki@g.com','1234','Niki','You usually will find me at the beach getting a tan');
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;

CREATE TABLE `tags` (
    `pid` int(10) NOT NULL AUTO_INCREMENT,
    `userid` int(10) NOT NULL,
    `tag` varchar(30) NOT NULL,
    PRIMARY KEY (`pid`),
    FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
INSERT INTO `tags` VALUES   (1,1,"Movies"),
                            (2,1,"Animals"),
                            (3,1,"Horses"),
                            (4,1,"Dogs"),
                            (5,1,"Anti-Cats"),
                            (6,2,"Books"),
                            (7,2,"Technology"),
                            (8,2,"Politics"),
                            (9,2,"Debates"),
                            (10,4,"Fishing"),
                            (11,4,"Beach"),
                            (12,4,"Basketball"),
                            (13,4,"Hiking"),
                            (14,6,"Space"),
                            (15,6,"Mars"),
                            (16,6,"Twitter"),
                            (17,6,"SpaceX"),
                            (18,6,"Tesla"),
                            (19,6,"Cars"),
                            (20,6,"Batteries"),
                            (21,6,"Memes"),
                            (22,6,"Entrepreneurship"),
                            (23,8,"Beach"),
                            (24,8,"Tanning"),
                            (25,8,"Malibu"),
                            (26,8,"Parties"),
                            (27,8,"Raves");
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;

CREATE TABLE `events` (
    `eventid` int(10) NOT NULL AUTO_INCREMENT,
    `title` varchar(200) CHARACTER SET utf8mb4 NOT NULL,
    `edate` date NOT NULL,
    `description` varchar(2000) CHARACTER SET utf8mb4 NOT NULL,
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

--
-- Table structure for table `conversations`
--

DROP TABLE IF EXISTS `conversations`;

CREATE TABLE `conversations` (
    `convoid` int(10) NOT NULL,
    `userid` int(10) NOT NULL,
    FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `conversations`
--

LOCK TABLES `conversations` WRITE;
INSERT INTO `conversations` VALUES  (666,1),
                                    (666,2),
                                    (777,1),
                                    (777,8),
                                    (999,3),
                                    (999,4),
                                    (222,5),
                                    (222,6),
                                    (333,7),
                                    (333,8);
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;

CREATE TABLE `messages` (
    `pid` int(10) NOT NULL AUTO_INCREMENT,
    `convoid` int(10) NOT NULL,
    `text` varchar(2000) NOT NULL,
    `createdat` varchar(40) NOT NULL,
    `userid` int(10) NOT NULL,
    PRIMARY KEY (`pid`),
    FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
INSERT INTO `messages` VALUES   (1,666,"Hey what's up","2022-04-20T18:20:00.000Z",1),
                                (2,666,"Not doing anything today wbu?","2022-04-20T18:27:00.000Z",2),
                                (3,777,"Hey","2022-04-20T18:22:00.000Z",1),
                                (4,777,"Sorry don't talk to me","2022-04-20T18:24:00.000Z",8),
                                (5,999,"Hi","2022-04-03T18:20:00.000Z",3),
                                (6,999,"Hello!","2022-04-03T18:27:00.000Z",4),
                                (7,222,"Are you hungry?","2022-04-08T18:20:00.000Z",5),
                                (8,222,"Yes where do you want to go?","2022-04-08T18:27:00.000Z",6),
                                (9,333,"Do you want to go shopping?","2022-03-10T18:20:00.000Z",7),
                                (10,333,"Yes, I need more clothes!","2022-03-10T18:27:00.000Z",8);
UNLOCK TABLES;