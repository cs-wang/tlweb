-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: tldb
-- ------------------------------------------------------
-- Server version	5.6.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add advice',7,'add_advice'),(20,'Can change advice',7,'change_advice'),(21,'Can delete advice',7,'delete_advice'),(22,'Can add commission detail',8,'add_commissiondetail'),(23,'Can change commission detail',8,'change_commissiondetail'),(24,'Can delete commission detail',8,'delete_commissiondetail'),(25,'Can add commission order',9,'add_commissionorder'),(26,'Can change commission order',9,'change_commissionorder'),(27,'Can delete commission order',9,'delete_commissionorder'),(28,'Can add member status',10,'add_memberstatus'),(29,'Can change member status',10,'change_memberstatus'),(30,'Can delete member status',10,'delete_memberstatus'),(31,'Can add member',11,'add_member'),(32,'Can change member',11,'change_member'),(33,'Can delete member',11,'delete_member'),(34,'Can add message',12,'add_message'),(35,'Can change message',12,'change_message'),(36,'Can delete message',12,'delete_message'),(37,'Can add order form',13,'add_orderform'),(38,'Can change order form',13,'change_orderform'),(39,'Can delete order form',13,'delete_orderform'),(40,'Can add product',14,'add_product'),(41,'Can change product',14,'change_product'),(42,'Can delete product',14,'delete_product'),(43,'Can add service',15,'add_service'),(44,'Can change service',15,'change_service'),(45,'Can delete service',15,'delete_service'),(46,'Can add service account',16,'add_serviceaccount'),(47,'Can change service account',16,'change_serviceaccount'),(48,'Can delete service account',16,'delete_serviceaccount'),(49,'Can add short message',17,'add_shortmessage'),(50,'Can change short message',17,'change_shortmessage'),(51,'Can delete short message',17,'delete_shortmessage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$MTF0u2x9kFUP$+lninOjsOdU+svKaubWZIFI6kpM0MMyr84H3Mak0ngQ=','2016-04-09 12:08:12.523528',1,'zhejiangxiaomai','','','358088534@qq.com',1,1,'2016-03-31 14:08:14.010178');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_advice`
--

LOCK TABLES `db_advice` WRITE;
/*!40000 ALTER TABLE `db_advice` DISABLE KEYS */;
INSERT INTO `db_advice` VALUES (5,'内容内容','2016-03-02 08:17:04.771930',NULL,1,'0',NULL,1,'没阅读啊哈哈'),(6,'内容内容','2016-04-02 08:17:21.479637','2016-04-02 08:18:43.497258',1,'1','回复回复',1,'阅读了');
/*!40000 ALTER TABLE `db_advice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_commissiondetail`
--

LOCK TABLES `db_commissiondetail` WRITE;
/*!40000 ALTER TABLE `db_commissiondetail` DISABLE KEYS */;
INSERT INTO `db_commissiondetail` VALUES ('0','推荐奖'),('1','优秀推荐奖'),('2','超级推荐奖'),('3','广告费'),('4','网络推荐奖'),('5','优秀人才奖');
/*!40000 ALTER TABLE `db_commissiondetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_commissionorder`
--

LOCK TABLES `db_commissionorder` WRITE;
/*!40000 ALTER TABLE `db_commissionorder` DISABLE KEYS */;
INSERT INTO `db_commissionorder` VALUES (1,900,'备注 哈哈','2016-03-31 14:17:53.752614','2016-03-31 14:17:53.752614','1','1',1),(4,800,'哈哈悲剧恩','2016-03-03 14:17:53.752614','2016-03-31 14:17:53.752614','1','2',1),(9,1231,'额尔','2016-04-01 14:17:53.752614','2016-03-31 14:17:53.752614','2','3',1);
/*!40000 ALTER TABLE `db_commissionorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_member`
--

LOCK TABLES `db_member` WRITE;
/*!40000 ALTER TABLE `db_member` DISABLE KEYS */;
INSERT INTO `db_member` VALUES (1,'lzf','改密码咯','李志芳',1,0,'19930312',NULL,'新手机号码','新微信号码','新开户银行','新账户啊','新持卡人啊','新收货人啊','新收货电话啊','新收获地址啊','2016-03-31 14:17:53.752614','2016-03-31 14:17:53.752614',2),(3,'su','pwd','nickname_',1,1,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-03-29 14:17:53.752614','2016-03-29 14:17:53.752614',2),(4,'su123123','pwd','nickname_',1,1,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-03-31 14:22:55.790164','2016-03-31 14:17:53.752614',1),(5,'zzh','pwd','nickname_',1,1,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-03-31 14:23:55.827537','2016-03-31 14:17:53.752614',1),(6,'wcs','pwd','nickname_',1,1,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-03-31 14:25:02.001543','2016-03-31 14:17:53.752614',1),(7,'wcs123','pwd','nickname_',1,3,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-03 05:33:22.610103','2016-03-31 14:17:53.752614',1),(8,'wcs12','pwd','nickname_',1,3,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-03 05:34:34.447805','2016-03-31 14:17:53.752614',1),(9,'zzh12','pwd','赵镇辉啊',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-03 05:37:07.361007','2016-03-31 14:17:53.752614',1),(10,'zzhasda','pwd','赵镇辉啊',1,9,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-03 05:39:27.197043','2016-03-31 14:17:53.752614',1),(11,'zdg','pwd','赵镇辉啊',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-03 05:44:32.545562','2016-03-31 14:17:53.752614',1),(12,'zdgg','pwd','赵镇辉啊',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-03 05:47:15.685986','2016-03-31 14:17:53.752614',1),(13,'newUser','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-03 08:17:43.013382','2016-03-31 14:17:53.752614',1),(14,'new','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:42:30.511879','2016-03-31 14:17:53.752614',1),(15,'new1','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:02.490695','2016-03-31 14:17:53.752614',1),(16,'new2','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:12.112406','2016-03-31 14:17:53.752614',1),(17,'new3','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:17.712882','2016-03-31 14:17:53.752614',1),(18,'new4','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:23.741996','2016-03-31 14:17:53.752614',1),(19,'new5','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:29.111348','2016-03-31 14:17:53.752614',1),(20,'new6','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:34.584210','2016-03-31 14:17:53.752614',1),(21,'new7','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:39.079521','2016-03-31 14:17:53.752614',1),(22,'new8','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:43.671880','2016-03-31 14:17:53.752614',1),(23,'new9','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:48.438878','2016-03-31 14:17:53.752614',1),(24,'new10','pwd','hahah',1,0,'delegation_phone_','delegation_info_','bind_phone_','weixinId','bank_','account_','cardHolder','receiver_','reciever_phone_','receiver_addr_','2016-04-05 11:43:53.723756','2016-03-31 14:17:53.752614',1);
/*!40000 ALTER TABLE `db_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_memberstatus`
--

LOCK TABLES `db_memberstatus` WRITE;
/*!40000 ALTER TABLE `db_memberstatus` DISABLE KEYS */;
INSERT INTO `db_memberstatus` VALUES (1,'1','未审核'),(2,'2','已审核'),(3,'3','已激活'),(4,'4','已出局'),(5,'5','服务中心锁定'),(6,'6','管理员锁定'),(7,'7','申请加单');
/*!40000 ALTER TABLE `db_memberstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_message`
--

LOCK TABLES `db_message` WRITE;
/*!40000 ALTER TABLE `db_message` DISABLE KEYS */;
INSERT INTO `db_message` VALUES (14,'您的订单已经发货','您的商品A+B都是货物啊已经发货，快递号为1232131231232131231','2016-04-03 12:32:32.907371','0',NULL,1),(15,'您的订单已经发货','您的商品A+B都是货物啊已经发货，快递号为1232131231232131231','2016-04-03 12:35:35.862729','0',NULL,1),(16,'您的订单已经发货','您的商品order_Memo已经发货，快递号为1232131231232131231','2016-04-03 12:39:41.366025','0',NULL,6),(17,'lzf申请加单，请审核','lzf已经申请加单，请至订单列表进行审核。','2016-04-03 13:24:31.766115','0',1,NULL),(18,'lzf申请加单，请审核','lzf已经申请加单，请至订单列表进行审核。','2016-04-03 13:29:25.798395','0',1,NULL),(19,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-05 01:31:06.046922','0',NULL,3),(20,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:42:30.511879','0',1,14),(21,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:02.490695','0',1,15),(22,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:12.112406','0',1,16),(23,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:17.712882','0',1,17),(24,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:23.741996','0',1,18),(25,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:29.111348','0',1,19),(26,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:34.584210','0',1,20),(27,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:39.079521','0',1,21),(28,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:43.671880','0',1,22),(29,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:48.438878','0',1,23),(30,'hahah首次加单，请审核订单并激活会员','会员hahah已申请加单,请至会员列表进行审核。','2016-04-05 11:43:53.723756','0',1,24),(31,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-05 12:02:49.563496','0',NULL,3),(32,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-05 12:31:16.654333','0',NULL,3),(33,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-05 13:23:52.423969','0',NULL,3),(34,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-05 13:26:41.380764','0',NULL,3),(35,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-08 06:14:19.585200','0',NULL,3),(36,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-08 06:14:40.452729','0',NULL,3),(37,'您的帐号已激活','su您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持','2016-04-08 06:17:42.064785','0',NULL,3);
/*!40000 ALTER TABLE `db_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_orderform`
--

LOCK TABLES `db_orderform` WRITE;
/*!40000 ALTER TABLE `db_orderform` DISABLE KEYS */;
INSERT INTO `db_orderform` VALUES (1,1,1000,'0','2016-03-31 14:25:02.001543','2016-04-03 12:39:41.363561','order_Memo','已发货','五环快递','1232131231232131231',1,NULL),(2,1,1000,'0','2016-04-03 05:33:22.610103',NULL,'order_Memo','未发货',NULL,NULL,1,NULL),(3,1,1000,'0','2016-04-03 05:34:34.447805',NULL,'order_Memo','已发货',NULL,NULL,1,NULL),(4,1,1000,'0','2016-04-03 05:37:07.361007',NULL,'order_Memo','已发货',NULL,NULL,1,NULL),(5,1,1000,'0','2016-04-03 05:39:27.197043',NULL,'order_Memo','已发货',NULL,NULL,10,NULL),(6,1,1000,'0','2016-04-03 05:44:32.545562',NULL,'order_Memo','已发货',NULL,NULL,11,NULL),(7,1,1000,'0','2016-04-03 05:47:15.685986',NULL,'order_Memo','已发货',NULL,NULL,12,NULL),(8,1,1000,'0','2016-04-03 08:17:43.013382',NULL,'order_Memo','未发货',NULL,NULL,13,NULL),(9,1,1000,'1','2016-04-03 11:37:53.683899',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(10,1,1000,'1','2016-04-03 11:47:09.418466',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(11,1,1000,'1','2016-03-03 11:48:30.310045',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(12,1,1000,'1','2016-04-03 11:49:18.078465',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(13,1,1000,'1','2016-04-03 11:57:20.589319',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(14,1,1000,'1','2016-04-03 12:00:07.823771',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(15,1,1000,'1','2016-04-03 12:00:11.218818','2016-04-03 12:38:50.733661','A+B都是货物啊','已发货','申通快递','1232131231232131231',1,NULL),(16,1,1000,'1','2016-04-03 13:24:31.762164',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(17,1,1000,'1','2016-03-03 13:29:25.794811',NULL,'A+B都是货物啊','未发货',NULL,NULL,1,NULL),(18,1,1000,'0','2016-04-05 11:42:30.511879',NULL,'order_Memo','未发货',NULL,NULL,14,NULL),(19,1,1000,'0','2016-04-05 11:43:02.490695',NULL,'order_Memo','未发货',NULL,NULL,1,NULL),(20,1,1000,'0','2016-04-05 11:43:12.112406',NULL,'order_Memo','未发货',NULL,NULL,16,NULL),(21,1,1000,'0','2016-04-05 11:43:17.712882',NULL,'order_Memo','未发货',NULL,NULL,17,NULL),(22,1,1000,'0','2016-04-05 11:43:23.741996',NULL,'order_Memo','未发货',NULL,NULL,1,NULL),(23,1,1000,'0','2016-04-05 11:43:29.111348',NULL,'order_Memo','未发货',NULL,NULL,19,NULL),(24,1,1000,'0','2016-04-05 11:43:34.584210',NULL,'order_Memo','未发货',NULL,NULL,20,NULL),(25,1,1000,'0','2016-04-05 11:43:39.079521',NULL,'order_Memo','未发货',NULL,NULL,21,NULL),(26,1,1000,'0','2016-04-05 11:43:43.671880',NULL,'order_Memo','未发货',NULL,NULL,22,NULL),(27,1,1000,'0','2016-04-05 11:43:48.438878',NULL,'order_Memo','未发货',NULL,NULL,23,NULL),(28,1,1000,'0','2016-04-05 11:43:53.723756',NULL,'order_Memo','未发货',NULL,NULL,24,NULL);
/*!40000 ALTER TABLE `db_orderform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_product`
--

LOCK TABLES `db_product` WRITE;
/*!40000 ALTER TABLE `db_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `db_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_service`
--

LOCK TABLES `db_service` WRITE;
/*!40000 ALTER TABLE `db_service` DISABLE KEYS */;
INSERT INTO `db_service` VALUES (1,'zj001','zj001','诸暨','1',NULL,NULL,NULL),(2,'sh001','sh001','上海','1',NULL,NULL,NULL),(3,'service_name_','service_pwd_','service_area_','2','老李','老李备忘录','1'),(4,'hello','hello','service_area_','3','老zhuji','老李备忘录','2');
/*!40000 ALTER TABLE `db_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_serviceaccount`
--

LOCK TABLES `db_serviceaccount` WRITE;
/*!40000 ALTER TABLE `db_serviceaccount` DISABLE KEYS */;
INSERT INTO `db_serviceaccount` VALUES ('上海银行','21312321213','李伯伯','122131231',1),('工商银行','213213123123123123123','赵镇辉','15757116149',1);
/*!40000 ALTER TABLE `db_serviceaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `db_shortmessage`
--

LOCK TABLES `db_shortmessage` WRITE;
/*!40000 ALTER TABLE `db_shortmessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `db_shortmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'db','advice'),(8,'db','commissiondetail'),(9,'db','commissionorder'),(11,'db','member'),(10,'db','memberstatus'),(12,'db','message'),(13,'db','orderform'),(14,'db','product'),(15,'db','service'),(16,'db','serviceaccount'),(17,'db','shortmessage'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-03-31 13:58:46.839250'),(2,'auth','0001_initial','2016-03-31 13:58:47.135674'),(3,'admin','0001_initial','2016-03-31 13:58:47.206192'),(4,'admin','0002_logentry_remove_auto_add','2016-03-31 13:58:47.241996'),(5,'contenttypes','0002_remove_content_type_name','2016-03-31 13:58:47.314424'),(6,'auth','0002_alter_permission_name_max_length','2016-03-31 13:58:47.343959'),(7,'auth','0003_alter_user_email_max_length','2016-03-31 13:58:47.383287'),(8,'auth','0004_alter_user_username_opts','2016-03-31 13:58:47.394944'),(9,'auth','0005_alter_user_last_login_null','2016-03-31 13:58:47.427030'),(10,'auth','0006_require_contenttypes_0002','2016-03-31 13:58:47.428924'),(11,'auth','0007_alter_validators_add_error_messages','2016-03-31 13:58:47.440296'),(12,'db','0001_initial','2016-03-31 13:58:48.007124'),(13,'sessions','0001_initial','2016-03-31 13:58:48.040900'),(14,'db','0002_advice_advice_status','2016-04-02 07:01:34.288496'),(15,'db','0003_advice_reply_content','2016-04-02 07:05:36.360929'),(16,'db','0004_auto_20160402_0714','2016-04-02 07:14:15.350524'),(17,'db','0005_auto_20160402_0750','2016-04-02 07:50:11.762028'),(18,'db','0006_advice_advice_title','2016-04-02 08:12:24.930098'),(19,'db','0007_message_id','2016-04-03 04:58:46.782630'),(20,'db','0008_auto_20160403_0501','2016-04-03 05:01:20.633942'),(21,'db','0009_auto_20160403_0735','2016-04-03 07:35:55.514366'),(22,'db','0010_auto_20160403_1322','2016-04-03 13:23:09.943611'),(23,'db','0011_auto_20160403_1329','2016-04-03 13:29:20.916107'),(24,'db','0002_service_service_response','2016-04-09 13:38:37.178317'),(25,'db','0003_auto_20160409_1351','2016-04-09 13:51:20.388516');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1k7bcbfniqyh4kv5fjl2pvi38vkxvpx9','MGQwNTFjY2M4ZDQ2ZjY2ZDM1ZDJlYjIyMGMyZmNhNTA2NjY4ZmY3NDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijg3ODhmZGJiMGI2OTcwNjVjODk1ZjVkZDdiZmE3NjYyZTkzZTAyMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-04-14 14:08:37.575525'),('vbulaa84pa2rhk1qoer3xf6uscnijcjq','ODNkMjk3OTdiZmI1MjBjZjI5MGU2Mjg5YmI4MjA1NWU1YjUxYmExNDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijg3ODhmZGJiMGI2OTcwNjVjODk1ZjVkZDdiZmE3NjYyZTkzZTAyMDMiLCJyb2xlIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2016-04-23 14:41:09.625763');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-09 23:24:23
