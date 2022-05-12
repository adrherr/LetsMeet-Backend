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
    `userid` int(10) NOT NULL,
    `tag` varchar(30) NOT NULL,
    PRIMARY KEY (`userid`, `tag`),
    FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
INSERT INTO `tags` VALUES   (1,"Movies"),
                            (1,"Animals"),
                            (1,"Horses"),
                            (1,"Dogs"),
                            (1,"Books"),
                            (2,"Books"),
                            (2,"Technology"),
                            (2,"Politics"),
                            (2,"Debates"),
                            (4,"Fishing"),
                            (4,"Beach"),
                            (4,"Basketball"),
                            (4,"Hiking"),
                            (6,"Space"),
                            (6,"Mars"),
                            (6,"Twitter"),
                            (6,"SpaceX"),
                            (6,"Tesla"),
                            (6,"Cars"),
                            (6,"Batteries"),
                            (6,"Memes"),
                            (6,"Entrepreneurship"),
                            (8,"Beach"),
                            (8,"Tanning"),
                            (8,"Malibu"),
                            (8,"Parties"),
                            (8,"Raves");
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;

CREATE TABLE `events` (
    `eventid` int(10) NOT NULL AUTO_INCREMENT,
    `title` varchar(500) CHARACTER SET utf8mb4 NOT NULL,
    `edate` date NOT NULL,
    `description` varchar(2000) CHARACTER SET utf8mb4 NOT NULL,
    `location` varchar(500) CHARACTER SET utf8mb4 NOT NULL,
    `image` varchar(1000) CHARACTER SET utf8mb4,
    `hostid` int(10) NOT NULL,
    PRIMARY KEY (`eventid`),
    FOREIGN KEY (`hostid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
INSERT INTO `events` VALUES (1,'Music Concert','2022-05-17','Come join us for another big concert','The Greek Theatre','https://www.digitalmusicnews.com/wp-content/uploads/2018/03/audience_concert.jpg',8),
                            (2,'Camping','2022-05-20','Have fun at our annual camping trip!','Castaic Lake','https://vegoutmag.com/wp-content/uploads/2021/08/camping.jpg',7),
                            (3,'Movies','2022-05-24','Join everyone to go see the The Batman!','AMC Porter Ranch','https://studybreaks.com/wp-content/uploads/2017/06/41-majesticbrookfield-exteriorjpg.jpg',7),
                            (4,'Hiking','2022-06-01','Hiking through beautiful Malibu trails','Malibu','https://images.theconversation.com/files/405661/original/file-20210610-18-imwshy.jpg?ixlib=rb-1.1.0&rect=6%2C0%2C4486%2C2997&q=45&auto=format&w=926&fit=clip',6),
                            (5,'Natural History Museum','2022-06-07','If you like dinosaurs come join!','900 W Exposition Blvd','https://www.ioes.ucla.edu/wp-content/uploads/nhmla_pic.jpg',5),
                            (6,'Golfing','2022-06-10','Grab your shiniest golf clubs for this years annual golfing meet','Porter Ranch Country Club','https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Golfer_swing.jpg/800px-Golfer_swing.jpg',4),
                            (7,'Yoga Classes','2022-06-13','If you are new to yoga this is the perfect opportunity to learn more!','Santa Monica Beach','https://images.everydayhealth.com/images/healthy-living/fitness/yoga-poses-for-beginners-07-722x406.jpg?w=720',3);
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
INSERT INTO `participants` VALUES   (1,1,8),
                                    (2,1,2),
                                    (3,1,3),
                                    (4,1,4),
                                    (5,1,1),
                                    (6,2,7),
                                    (7,2,6),
                                    (8,3,7),
                                    (9,3,4),
                                    (10,3,3),
                                    (11,4,6),
                                    (12,4,5),
                                    (13,4,7),
                                    (14,5,5),
                                    (15,5,4),
                                    (16,6,4),
                                    (17,6,2),
                                    (18,6,1),
                                    (19,7,3),
                                    (20,7,1),
                                    (21,7,5);
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
                                (4,777,"Hey we should totally hang out","2022-04-20T18:24:00.000Z",8),
                                (5,999,"Hi","2022-04-03T18:20:00.000Z",3),
                                (6,999,"Hello!","2022-04-03T18:27:00.000Z",4),
                                (7,222,"Are you hungry?","2022-04-08T18:20:00.000Z",5),
                                (8,222,"Yes where do you want to go?","2022-04-08T18:27:00.000Z",6),
                                (9,333,"Do you want to go shopping?","2022-03-10T18:20:00.000Z",7),
                                (10,333,"Yes, I need more clothes!","2022-03-10T18:27:00.000Z",8);
UNLOCK TABLES;