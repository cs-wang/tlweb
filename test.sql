
/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50629
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50629
File Encoding         : 65001

Date: 2016-03-28 21:01:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for advice
-- ----------------------------
DROP TABLE IF EXISTS `advice`;
CREATE TABLE `advice` (
  `advice_id` bigint(20) NOT NULL COMMENT '意见ID',
  `user_name` varchar(20) DEFAULT NULL COMMENT '用户名',
  `advice_content` varchar(255) DEFAULT NULL COMMENT '意见内容',
  `advice_created` datetime DEFAULT NULL,
  `reply_time` datetime DEFAULT NULL,
  `service_id` bigint(20) NOT NULL COMMENT '服务点id',
  PRIMARY KEY (`advice_id`),
  KEY `advice_username_fk` (`user_name`),
  KEY `advice_service` (`service_id`),
  CONSTRAINT `advice_service` FOREIGN KEY (`service_id`) REFERENCES `service` (`service_id`),
  CONSTRAINT `advice_username_fk` FOREIGN KEY (`user_name`) REFERENCES `member` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of advice
-- ----------------------------
INSERT INTO `advice` VALUES ('1', 'user1', 'assad', '2016-03-08 20:25:55', '2016-04-01 20:25:58', '1');
INSERT INTO `advice` VALUES ('2', 'user2', 'asdsadasd', '2016-03-27 20:46:07', '2016-04-07 20:46:13', '2');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add member_status', '7', 'add_member_status');
INSERT INTO `auth_permission` VALUES ('20', 'Can change member_status', '7', 'change_member_status');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete member_status', '7', 'delete_member_status');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$24000$v7PzzfeUt0wS$FOo6hxvVA9EuDB1PZaGxsTJTKgjYOCRDdAL2jbhT+3o=', '2016-03-28 07:34:07.548391', '1', 'zhejiangxiaomai', '', '', '358088534@qq.com', '1', '1', '2016-03-28 07:32:32.749746');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for commission_detail
-- ----------------------------
DROP TABLE IF EXISTS `commission_detail`;
CREATE TABLE `commission_detail` (
  `commission_type` char(1) CHARACTER SET utf8 NOT NULL,
  `commission_desc` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`commission_type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of commission_detail
-- ----------------------------
INSERT INTO `commission_detail` VALUES ('1', '推荐奖');
INSERT INTO `commission_detail` VALUES ('2', '广告费');
INSERT INTO `commission_detail` VALUES ('3', '优秀推荐奖');
INSERT INTO `commission_detail` VALUES ('4', '超级推荐奖');

-- ----------------------------
-- Table structure for commission_order
-- ----------------------------
DROP TABLE IF EXISTS `commission_order`;
CREATE TABLE `commission_order` (
  `commission_id` bigint(20) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `commission_price` double(10,2) DEFAULT NULL,
  `commission_type` char(1) NOT NULL,
  `commission_memo` varchar(255) DEFAULT NULL,
  `commission_created` datetime DEFAULT NULL,
  `commission_sent` datetime DEFAULT NULL,
  `commission_status` char(1) DEFAULT NULL COMMENT '1为未发放，2为已发放',
  PRIMARY KEY (`commission_id`,`user_name`),
  KEY `commision_type` (`commission_type`),
  KEY `username_commision_fk` (`user_name`),
  CONSTRAINT `commission_type_fk` FOREIGN KEY (`commission_type`) REFERENCES `commission_detail` (`commission_type`),
  CONSTRAINT `username_commision_fk` FOREIGN KEY (`user_name`) REFERENCES `member` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of commission_order
-- ----------------------------
INSERT INTO `commission_order` VALUES ('1', 'user1', '1000.00', '1', 'sadsadsa', '2016-03-31 20:26:22', '2016-03-23 20:26:25', '1');

-- ----------------------------
-- Table structure for db_member_status
-- ----------------------------
DROP TABLE IF EXISTS `db_member_status`;
CREATE TABLE `db_member_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status_id` varchar(1) NOT NULL,
  `status_desc` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of db_member_status
-- ----------------------------
INSERT INTO `db_member_status` VALUES ('1', '8', '丢你老母');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'db', 'advice');
INSERT INTO `django_content_type` VALUES ('10', 'db', 'member');
INSERT INTO `django_content_type` VALUES ('7', 'db', 'member_status');
INSERT INTO `django_content_type` VALUES ('8', 'db', 'message');
INSERT INTO `django_content_type` VALUES ('13', 'db', 'service');
INSERT INTO `django_content_type` VALUES ('12', 'db', 'serviceaccount');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-03-28 02:10:22.267908');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-03-28 02:10:36.479166');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-03-28 02:10:40.011627');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2016-03-28 02:10:40.480252');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2016-03-28 02:10:41.615548');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2016-03-28 02:10:42.611677');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2016-03-28 02:10:43.551343');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2016-03-28 02:10:43.608756');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2016-03-28 02:10:44.503896');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2016-03-28 02:10:44.560479');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2016-03-28 02:10:44.623147');
INSERT INTO `django_migrations` VALUES ('12', 'sessions', '0001_initial', '2016-03-28 02:10:45.499575');
INSERT INTO `django_migrations` VALUES ('13', 'db', '0001_initial', '2016-03-28 03:19:41.851345');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('19nzcgbfcnczwi0uczwypqy0dz8cvqdn', 'ODYzM2E5YTE2ZGVmYmJjNTEyYWIzMmU4NDU0ZGVmNDhkOTU3YWY1ODp7Il9hdXRoX3VzZXJfaGFzaCI6IjlmNTdhMGYzMWNjMjkxZDA2ZmQ5OGJhOGUxYzg3NjMzZjM5YTU3MDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-04-11 07:34:07.659380');

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member` (
  `user_name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `password` varchar(500) CHARACTER SET utf8 NOT NULL,
  `nickname` varchar(10) CHARACTER SET utf8 NOT NULL,
  `status_id` char(1) CHARACTER SET utf8 NOT NULL,
  `service_id` bigint(20) DEFAULT NULL,
  `reference_id` bigint(20) DEFAULT NULL COMMENT '推荐人ID,1表示推荐人为服务点 2,3..等为用户',
  `user_id` bigint(20) DEFAULT NULL COMMENT '所在服务点的绝对id',
  `delegation_phone` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `delegation_info` varchar(500) CHARACTER SET utf8 DEFAULT NULL,
  `bind_phone` varchar(20) CHARACTER SET utf8 NOT NULL,
  `weixin_id` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `bank` varchar(255) CHARACTER SET utf8 NOT NULL COMMENT '开户银行',
  `account` varchar(50) CHARACTER SET utf8 NOT NULL COMMENT '银行卡号',
  `card_holder` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '持卡人',
  `receiver` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `receiver_phone` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `receiver_addr` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `register_time` datetime DEFAULT NULL COMMENT '会员注册时间',
  `confirm_time` datetime DEFAULT NULL COMMENT '确认收到钱的时间',
  PRIMARY KEY (`user_name`),
  KEY `member_status_fk` (`status_id`),
  CONSTRAINT `member_status_fk` FOREIGN KEY (`status_id`) REFERENCES `member_status` (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of member
-- ----------------------------
INSERT INTO `member` VALUES ('user1', '123', '浙江1', '2', '1', '0', '1', '119', '中国人民代付', '123123123', 'weixin1', '中国人民银行人民分行', '6228480402564890018', '李小方', '李大方', '15757116789', '331', '2016-03-09 16:47:23', '2016-03-26 16:47:27');
INSERT INTO `member` VALUES ('user10', '123', 'yyy', '2', '1', '9', '10', '13906857911', '中国人民代付', '123123123', 'weixin10', '中国农业银行xxx支行', '62284804025648213123312313', 'cs', 'cs', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user11', '123', 'gaox', '2', '1', '10', '11', '13906857911', '中国人民代付', '123123123', 'weixin11', '中国农业银行xxx支行', '62284804025648213123312313', 'plpl', 'plpl', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user12', '123', 'hashiqi', '2', '1', '11', '12', '13906857911', '中国人民代付', '123123123', 'weixin12', '中国农业银行xxx支行', '62284804025648213123312313', 'wewe', 'wewe', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user13', '123', 'zxq', '2', '1', '12', '13', '13906857911', '中国人民代付', '123123123', 'weixin13', '中国农业银行xxx支行', '62284804025648213123312313', 'rtrt', 'rtrt', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user14', '123', 'ymb', '2', '1', '13', '14', '13906857911', '中国人民代付', '123123123', 'weixin14', '中国农业银行xxx支行', '62284804025648213123312313', 'njnj', 'njnj', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user15', '123', 'yyyyyy', '2', '1', '14', '15', '13906857911', '中国人民代付', '123123123', '中国哈哈哈', '中国农业银行xxx支行', '62284804025648213123312313', 'uiui', 'uiui', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user16', '123', '已下单没进排位', '3', '1', '15', null, '13906857911', '中国人民代付', '123123123', '中国哈哈哈', '中国农业银行xxx支行', '62284804025648213123312313', '没进啊', '买东西了', '15757116789', '331', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user17', '123', '没汇款的人', '1', '1', '15', null, '13906857911', '中国人民代付', '123123123', 'hahah', '中国农业银行xxx支行', '62284804025648213123312313', '没进啊', '买东西了给给钱', '15757118198', '阿萨德撒的撒打算', '2016-03-09 16:47:23', null);
INSERT INTO `member` VALUES ('user18', '123', '已下单已汇款', '2', '1', '1', '16', '110', '中国人民代付', '1898989891', '中国人民代付', '中国农业银行xxx支行', '62284804025648213123312313', '没进啊', '被1推荐的', '13907878787', '萨达四大四大四大', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user19', '123', '上海地区', '2', '2', '0', '1', '120', '上海银行', '8989898921', '上海微信', '中国人民银行人民分行', '2312312321321321323131', '上海人', '上海人第一个', '14798989898', '都扣扣扣', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user2', '123', 'zzh', '2', '1', '1', '2', '15757116149', '中国人民代付', '15757116149', 'weixin2', '中国工商银行xxx支行', '62284804025648921312313', '赵大会', '赵大大', '15757118198', '乱七八糟', '2016-03-01 16:49:33', '2016-03-02 16:49:36');
INSERT INTO `member` VALUES ('user20', '123', '上海地区', '1', '2', '1', '2', '13487123123', '上海大学', '213213123213', '微信上海', '中国人民银行人民分行', '62284804025648213123312313', '上海人', '上海第二个', '1232133322321', '复大复旦复旦', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user3', '123', 'wcs', '2', '1', '2', '3', '13906857911', '中国人民代付', '123123123', 'weixin3', '中国农业银行xxx支行', '62284804025648213123312313', '王大锤', '挖大锤', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-01 16:49:33', '2016-03-01 16:49:33');
INSERT INTO `member` VALUES ('user4', '123', 'hcs', '2', '1', '3', '4', '13906857911', '中国人民代付', '123123123', 'weixin4', '中国农业银行xxx支行', '62284804025648213123312313', '王x锤', '王小锤', '13906857910', '乱七八糟', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user5', '123', 'fzh', '2', '1', '4', '5', '13906857911', '中国人民代付', '123123123', 'weixin5', '中国农业银行xxx支行', '62284804025648213123312313', '王x锤', '王小锤', '13906857910', '乱七八糟', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user7', '123', '浙江小麦', '2', '1', '6', '7', '13906857911', '中国人民代付', '123123123', 'weixin7', '中国农业银行xxx支行', '62284804025648213123312313', 'wacis', 'wacis', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user8', '123', '萌萌哒', '2', '1', '7', '8', '13906857911', '中国人民代付', '123123123', 'weixin8', '中国农业银行xxx支行', '62284804025648213123312313', 'xixixi', 'xixixi', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');
INSERT INTO `member` VALUES ('user9', '123', 'hhh', '2', '1', '8', '9', '13906857911', '中国人民代付', '123123123', 'weixin9', '中国农业银行xxx支行', '62284804025648213123312313', 'koko', 'koko', '13906857910', '华东师范大学华东师范大学华东师范大学华东师范大学华东师范大学', '2016-03-09 16:47:23', '2016-03-26 16:47:08');

-- ----------------------------
-- Table structure for member_status
-- ----------------------------
DROP TABLE IF EXISTS `member_status`;
CREATE TABLE `member_status` (
  `status_id` char(1) CHARACTER SET utf8 NOT NULL,
  `status_desc` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '目前只有',
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of member_status
-- ----------------------------
INSERT INTO `member_status` VALUES ('1', '未审核');
INSERT INTO `member_status` VALUES ('2', '已激活');
INSERT INTO `member_status` VALUES ('3', '已审核');
INSERT INTO `member_status` VALUES ('4', '已出局');
INSERT INTO `member_status` VALUES ('5', '服务中心锁定');
INSERT INTO `member_status` VALUES ('6', '管理员锁定');
INSERT INTO `member_status` VALUES ('7', '申请加单');

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `message_id` bigint(20) NOT NULL,
  `message_title` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `message_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `sent_time` datetime DEFAULT NULL,
  `message_status` char(1) CHARACTER SET utf8 DEFAULT NULL COMMENT '0为未读，1为已读',
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('1', '哈哈', '我冷你嘛', '2016-03-27 20:26:51', '1');

-- ----------------------------
-- Table structure for order_form
-- ----------------------------
DROP TABLE IF EXISTS `order_form`;
CREATE TABLE `order_form` (
  `order_id` bigint(20) NOT NULL,
  `order_rank` bigint(20) DEFAULT NULL,
  `user_name` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `order_price` double(10,2) DEFAULT NULL,
  `order_type` char(1) CHARACTER SET utf8 DEFAULT NULL COMMENT '0为报单，1为复销',
  `order_created` datetime DEFAULT NULL,
  `order_finished` datetime DEFAULT NULL,
  `order_memo` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '备忘录信息',
  `order_status` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `express_name` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `express_number` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `username_fk` (`user_name`),
  CONSTRAINT `username_fk` FOREIGN KEY (`user_name`) REFERENCES `member` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of order_form
-- ----------------------------
INSERT INTO `order_form` VALUES ('1', '1', 'user1', '1000.00', '1', '2016-03-24 10:43:42', '2016-03-24 10:43:42', '1+1', '未发货', '顺丰', '123456789090909021312312321');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `product_id` bigint(20) NOT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_price` double(10,2) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES ('1', '亚麻营养膳食粉', '500.00');
INSERT INTO `product` VALUES ('2', '亚麻籽有机冷榨油大礼盒', '500.00');
INSERT INTO `product` VALUES ('3', '亚麻籽益生菌水溶粉', '500.00');
INSERT INTO `product` VALUES ('4', '亚麻全营养代餐棒', '500.00');
INSERT INTO `product` VALUES ('5', '亚麻籽有机冷榨油小礼盒', '200.00');

-- ----------------------------
-- Table structure for service
-- ----------------------------
DROP TABLE IF EXISTS `service`;
CREATE TABLE `service` (
  `service_id` bigint(20) NOT NULL,
  `service_name` varchar(20) CHARACTER SET utf8 NOT NULL COMMENT '服务点用户名',
  `service_pwd` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '服务点密码',
  `service_area` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '服务点区域',
  `role` char(1) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of service
-- ----------------------------
INSERT INTO `service` VALUES ('1', 'zj001', 'zj001', '浙江', '1');
INSERT INTO `service` VALUES ('2', 'sh001', 'sh001', '上海', '1');
INSERT INTO `service` VALUES ('3', 'zj007', 'zh007', '浙江副中心', '2');

-- ----------------------------
-- Table structure for service_account
-- ----------------------------
DROP TABLE IF EXISTS `service_account`;
CREATE TABLE `service_account` (
  `service_id` bigint(20) NOT NULL,
  `bank` varchar(255) CHARACTER SET utf8 NOT NULL,
  `bank_account` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `card_holder` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`bank`),
  KEY `service_id_fk` (`service_id`),
  CONSTRAINT `service_id_fk` FOREIGN KEY (`service_id`) REFERENCES `service` (`service_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of service_account
-- ----------------------------
INSERT INTO `service_account` VALUES ('2', '中信银行', '老汪', '汪帅', '11011011001');
INSERT INTO `service_account` VALUES ('2', '微信支付(上海区域)', 'zhejiangxiaomai12', '李博', '110');
INSERT INTO `service_account` VALUES ('1', '微信支付(浙江区域)', 'zhejiangxiaomai', '赵镇辉', '15757116149');
INSERT INTO `service_account` VALUES ('1', '招商银行绍兴诸暨支行(浙江区域)', '6214855751739091', '赵岩忠', '18368583552');

-- ----------------------------
-- Table structure for short_message
-- ----------------------------
DROP TABLE IF EXISTS `short_message`;
CREATE TABLE `short_message` (
  `message_id` int(2) NOT NULL,
  `message_content` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of short_message
-- ----------------------------
INSERT INTO `short_message` VALUES ('1', '恭喜您已审核通过成为天龙健康会员，你的注册号：00000000000，推荐会员可以获得公司推广奖励，详见奖励模式请登录www.tljk518.com.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('2', 'xx会员您好：你已经成为vip会员，将自动进入公司系统公排模式，同时获得推荐奖200元，自动扣税5%，推荐奖不限，推荐越多奖金越多。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('3', 'XX会员您好：您的VIP编号：00000000000即将获得第1层第1次广告奖励400元，自动扣税5%，请关心绑定卡号或微信，继续推广可获得更多广告奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('4', 'XX会员您好：您的VIP编号：00000000000即将获得第1层第2次广告奖励400元，自动扣税5%，请关心绑定卡号或微信，继续推广可获得更多推荐奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('5', 'XX会员您好：您的VIP编号：00000000000即将获得第2层第1次广告奖励200元，自动扣税5%，请关心绑定卡号或微信，继续推广可获得更多推荐奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('6', 'XX会员您好：您的VIP编号：00000000000即将获得第2层第2次广告奖励200元，自动扣税5%，请关心绑定卡号或微信，继续推广可获得更多推荐奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('7', 'XX会员您好：您的VIP编号：00000000000即将获得第2层第3次广告奖励200元，自动扣税5%，请关心绑定卡号或微信，继续推广可获得更多推荐奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('8', 'XX会员您好：您的VIP编号：00000000000已成为公司高级会员，享受公司特别优惠政策，只需继续加单800元，就可以再次直接生成VIP会员，重新获取产品又可获得自动公排广告奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('9', 'XX会员您好:由您推荐的会员编号：00000000000即将奖励完毕，并已成公司高级会员，获得公司优惠待遇，只要重复消费800元，直接进入公司系统，再次获得自动公排广告奖励。继续推广可获得更多推荐奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】');
INSERT INTO `short_message` VALUES ('10', 'xx（推荐会员）会员您好：由你推荐的XXX会员已经成为vip会员，将自动进入公司系统公排模式，你再次获得推荐奖200元，自动扣税5%，推荐奖不限，推荐越多奖金越多。咨询电话：0575-87755511.回复TD退订【天龙健康】');
