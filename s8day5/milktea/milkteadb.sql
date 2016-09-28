/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : milkteadb

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2015-01-08 20:37:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for chatrecord
-- ----------------------------
DROP TABLE IF EXISTS `chatrecord`;
CREATE TABLE `chatrecord` (
  `Nid` int(11) NOT NULL AUTO_INCREMENT,
  `Message` varchar(256) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  `UserId` int(11) DEFAULT NULL,
  PRIMARY KEY (`Nid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of chatrecord
-- ----------------------------
INSERT INTO `chatrecord` VALUES ('1', 'y', '2015-01-08 20:21:31', '1');
INSERT INTO `chatrecord` VALUES ('2', 'gb.', '2015-01-08 20:21:31', '1');
INSERT INTO `chatrecord` VALUES ('3', 'kk', '2015-01-08 20:21:33', '1');
INSERT INTO `chatrecord` VALUES ('4', 'gb.', '2015-01-08 20:21:33', '1');
INSERT INTO `chatrecord` VALUES ('5', 'll', '2015-01-08 20:21:58', '1');
INSERT INTO `chatrecord` VALUES ('6', 'gb.', '2015-01-08 20:21:58', '1');
INSERT INTO `chatrecord` VALUES ('7', 'hh', '2015-01-08 20:21:59', '1');
INSERT INTO `chatrecord` VALUES ('8', 'gb.', '2015-01-08 20:21:59', '1');
INSERT INTO `chatrecord` VALUES ('9', 'wocao', '2015-01-08 20:22:00', '1');
INSERT INTO `chatrecord` VALUES ('10', 'gb.', '2015-01-08 20:22:00', '1');
INSERT INTO `chatrecord` VALUES ('11', 'll', '2015-01-08 20:24:11', '1');
INSERT INTO `chatrecord` VALUES ('12', 'gb.', '2015-01-08 20:24:11', '1');
INSERT INTO `chatrecord` VALUES ('13', '1', '2015-01-08 20:27:24', '1');
INSERT INTO `chatrecord` VALUES ('14', 'gb.', '2015-01-08 20:27:24', '1');
INSERT INTO `chatrecord` VALUES ('15', '11', '2015-01-08 20:27:29', '1');
INSERT INTO `chatrecord` VALUES ('16', 'gb.', '2015-01-08 20:27:29', '1');
INSERT INTO `chatrecord` VALUES ('17', 'haha', '2015-01-08 20:27:30', '1');
INSERT INTO `chatrecord` VALUES ('18', 'gb.', '2015-01-08 20:27:30', '1');

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `Nid` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Nid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('1', 'wupeiqi', '123');
