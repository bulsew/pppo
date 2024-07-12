-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: rm-cn-k963tjcl90001ako.rwlb.rds.aliyuncs.com    Database: abc
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'eb7f550f-3dd5-11ef-bc51-00163e124cfe:1-10165';

--
-- Table structure for table `aboutusers_emailverification`
--

DROP TABLE IF EXISTS `aboutusers_emailverification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aboutusers_emailverification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `code` varchar(4) NOT NULL,
  `expire_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aboutusers_emailverification`
--

LOCK TABLES `aboutusers_emailverification` WRITE;
/*!40000 ALTER TABLE `aboutusers_emailverification` DISABLE KEYS */;
/*!40000 ALTER TABLE `aboutusers_emailverification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 道路信息',6,'add_road'),(22,'Can change 道路信息',6,'change_road'),(23,'Can delete 道路信息',6,'delete_road'),(24,'Can view 道路信息',6,'view_road'),(25,'Can add 历史预测记录',7,'add_historicalprediction'),(26,'Can change 历史预测记录',7,'change_historicalprediction'),(27,'Can delete 历史预测记录',7,'delete_historicalprediction'),(28,'Can view 历史预测记录',7,'view_historicalprediction'),(29,'Can add 反馈信息',8,'add_feedback'),(30,'Can change 反馈信息',8,'change_feedback'),(31,'Can delete 反馈信息',8,'delete_feedback'),(32,'Can view 反馈信息',8,'view_feedback'),(33,'Can add 预测结果信息',9,'add_trafficpredictionresult'),(34,'Can change 预测结果信息',9,'change_trafficpredictionresult'),(35,'Can delete 预测结果信息',9,'delete_trafficpredictionresult'),(36,'Can view 预测结果信息',9,'view_trafficpredictionresult'),(37,'Can add 用户表',10,'add_users'),(38,'Can change 用户表',10,'change_users'),(39,'Can delete 用户表',10,'delete_users'),(40,'Can view 用户表',10,'view_users'),(41,'Can add email verification',11,'add_emailverification'),(42,'Can change email verification',11,'change_emailverification'),(43,'Can delete email verification',11,'delete_emailverification'),(44,'Can view email verification',11,'view_emailverification'),(45,'Can add 交叉口信息',12,'add_intersection'),(46,'Can change 交叉口信息',12,'change_intersection'),(47,'Can delete 交叉口信息',12,'delete_intersection'),(48,'Can view 交叉口信息',12,'view_intersection'),(49,'Can add 道路交叉口关系信息',13,'add_roadintersectionrelation'),(50,'Can change 道路交叉口关系信息',13,'change_roadintersectionrelation'),(51,'Can delete 道路交叉口关系信息',13,'delete_roadintersectionrelation'),(52,'Can view 道路交叉口关系信息',13,'view_roadintersectionrelation'),(53,'Can add 车流量预测图表',14,'add_trafficprediction'),(54,'Can change 车流量预测图表',14,'change_trafficprediction'),(55,'Can delete 车流量预测图表',14,'delete_trafficprediction'),(56,'Can view 车流量预测图表',14,'view_trafficprediction');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_intersection`
--

DROP TABLE IF EXISTS `car_intersection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_intersection` (
  `id` int NOT NULL,
  `type` varchar(10) NOT NULL,
  `current_red_time` int NOT NULL,
  `current_green_time` int NOT NULL,
  `longitude` double NOT NULL,
  `latitude` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_intersection`
--

LOCK TABLES `car_intersection` WRITE;
/*!40000 ALTER TABLE `car_intersection` DISABLE KEYS */;
INSERT INTO `car_intersection` VALUES (1,'十字',60,60,1,1),(2,'丁字',60,60,1,1),(3,'十字',60,60,1,1),(4,'十字',60,60,1,1),(5,'十字',60,60,1,1);
/*!40000 ALTER TABLE `car_intersection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_road`
--

DROP TABLE IF EXISTS `car_road`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_road` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `information` longtext NOT NULL,
  `dataset_link` varchar(200) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `main_road` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_road`
--

LOCK TABLES `car_road` WRITE;
/*!40000 ALTER TABLE `car_road` DISABLE KEYS */;
INSERT INTO `car_road` VALUES (1,'黄山路西向1段','','',31.845954274333142,117.20151091228072,1),(2,'黄山路东向1段','','',31.84578635000493,117.2013163624033,1),(4,'黄山路西向2段','','',31.846121794646486,117.20678022372822,1),(5,'科学大道南向1段','','',31.85508856509952,117.22435838149262,2),(6,'黄山路东向3段','','',31.846305511470085,117.21647637561742,1),(7,'黄山路西向3段','','',31.846376477044064,117.21174238867744,1),(8,'科学大道北向1段','','',31.84599373358729,117.21141964501574,2),(9,'黄山路东向2段','','',31.84613239811703,117.21063227330038,1);
/*!40000 ALTER TABLE `car_road` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_roadintersectionrelation`
--

DROP TABLE IF EXISTS `car_roadintersectionrelation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_roadintersectionrelation` (
  `id` int NOT NULL,
  `intersection_id` int NOT NULL,
  `road_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `car_roadintersection_intersection_id_fae969cf_fk_car_inter` (`intersection_id`),
  KEY `car_roadintersectionrelation_road_id_91002200_fk_car_road_id` (`road_id`),
  CONSTRAINT `car_roadintersection_intersection_id_fae969cf_fk_car_inter` FOREIGN KEY (`intersection_id`) REFERENCES `car_intersection` (`id`),
  CONSTRAINT `car_roadintersectionrelation_road_id_91002200_fk_car_road_id` FOREIGN KEY (`road_id`) REFERENCES `car_road` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_roadintersectionrelation`
--

LOCK TABLES `car_roadintersectionrelation` WRITE;
/*!40000 ALTER TABLE `car_roadintersectionrelation` DISABLE KEYS */;
INSERT INTO `car_roadintersectionrelation` VALUES (1,1,1),(2,1,2),(3,2,4),(4,3,7),(5,3,8),(6,3,9),(7,4,6),(8,5,5);
/*!40000 ALTER TABLE `car_roadintersectionrelation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_trafficprediction`
--

DROP TABLE IF EXISTS `car_trafficprediction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_trafficprediction` (
  `id` int NOT NULL,
  `data1` double NOT NULL,
  `data2` double NOT NULL,
  `data3` double NOT NULL,
  `data4` double NOT NULL,
  `data5` double NOT NULL,
  `data6` double NOT NULL,
  `data7` double NOT NULL,
  `data8` double NOT NULL,
  `road_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `car_trafficprediction_road_id_4189c658_fk_car_road_id` (`road_id`),
  CONSTRAINT `car_trafficprediction_road_id_4189c658_fk_car_road_id` FOREIGN KEY (`road_id`) REFERENCES `car_road` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_trafficprediction`
--

LOCK TABLES `car_trafficprediction` WRITE;
/*!40000 ALTER TABLE `car_trafficprediction` DISABLE KEYS */;
/*!40000 ALTER TABLE `car_trafficprediction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_system_users_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_system_users_id` FOREIGN KEY (`user_id`) REFERENCES `system_users` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'aboutUsers','emailverification'),(10,'aboutUsers','users'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(8,'car','feedback'),(7,'car','historicalprediction'),(12,'car','intersection'),(6,'car','road'),(13,'car','roadintersectionrelation'),(14,'car','trafficprediction'),(9,'car','trafficpredictionresult'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-09 18:15:19.898999'),(2,'contenttypes','0002_remove_content_type_name','2024-07-09 18:15:19.956065'),(3,'auth','0001_initial','2024-07-09 18:15:20.115515'),(4,'auth','0002_alter_permission_name_max_length','2024-07-09 18:15:20.154426'),(5,'auth','0003_alter_user_email_max_length','2024-07-09 18:15:20.165420'),(6,'auth','0004_alter_user_username_opts','2024-07-09 18:15:20.176601'),(7,'auth','0005_alter_user_last_login_null','2024-07-09 18:15:20.187182'),(8,'auth','0006_require_contenttypes_0002','2024-07-09 18:15:20.196277'),(9,'auth','0007_alter_validators_add_error_messages','2024-07-09 18:15:20.207663'),(10,'auth','0008_alter_user_username_max_length','2024-07-09 18:15:20.219066'),(11,'auth','0009_alter_user_last_name_max_length','2024-07-09 18:15:20.231136'),(12,'auth','0010_alter_group_name_max_length','2024-07-09 18:15:20.261272'),(13,'auth','0011_update_proxy_permissions','2024-07-09 18:15:20.290012'),(14,'auth','0012_alter_user_first_name_max_length','2024-07-09 18:15:20.301853'),(15,'aboutUsers','0001_initial','2024-07-09 18:15:20.487128'),(16,'admin','0001_initial','2024-07-09 18:15:20.570950'),(17,'admin','0002_logentry_remove_auto_add','2024-07-09 18:15:20.585377'),(18,'admin','0003_logentry_add_action_flag_choices','2024-07-09 18:15:20.598861'),(19,'car','0001_initial','2024-07-09 18:15:20.878007'),(20,'car','0002_remove_trafficpredictionresult_image_link_and_more','2024-07-09 18:15:20.933184'),(21,'car','0003_remove_road_length_and_more','2024-07-09 18:15:21.177163'),(22,'car','0004_remove_road_connected_to','2024-07-09 18:15:21.270102'),(23,'car','0005_remove_road_prediction_image_road_prediction_image1_and_more','2024-07-09 18:15:21.332402'),(24,'car','0006_alter_road_prediction_image1','2024-07-09 18:15:21.353915'),(25,'car','0007_alter_historicalprediction_id','2024-07-09 18:15:21.403995'),(26,'car','0008_remove_historicalprediction_user','2024-07-09 18:15:21.490504'),(27,'car','0009_remove_road_latitude_remove_road_longitude_and_more','2024-07-09 18:15:21.603624'),(28,'sessions','0001_initial','2024-07-09 18:15:21.646626'),(29,'aboutUsers','0002_remove_users_first_name_remove_users_last_name_and_more','2024-07-09 21:23:30.602739'),(30,'aboutUsers','0003_users_name','2024-07-09 21:36:50.337831'),(31,'aboutUsers','0004_emailverification','2024-07-09 22:29:22.172339'),(32,'car','0010_intersection_remove_historicalprediction_road_and_more','2024-07-10 14:57:05.434227');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_users`
--

DROP TABLE IF EXISTS `system_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `email` varchar(40) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `gender` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_users`
--

LOCK TABLES `system_users` WRITE;
/*!40000 ALTER TABLE `system_users` DISABLE KEYS */;
INSERT INTO `system_users` VALUES (1,'pbkdf2_sha256$720000$D5lxQCjqTnTsos825I9eHR$jtlKcvOc4S+PfmWfPd5C06Z196zalWMopCQA1PhzX6g=',NULL,0,'wjb','2863374302@qq.com',0,1,'2024-07-09 21:24:21.894727',1,NULL),(2,'pbkdf2_sha256$720000$9n1Nqpu3KScT8z2GRYoT85$C/M8csC6N18UmuJ5YGEHR8VD+Ssj79nAik+60Htnks0=',NULL,0,'wwb','981518587@qq.com',0,1,'2024-07-10 10:42:02.774694',0,NULL);
/*!40000 ALTER TABLE `system_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_users_groups`
--

DROP TABLE IF EXISTS `system_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_users_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `users_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_users_groups_users_id_group_id_7483be9d_uniq` (`users_id`,`group_id`),
  KEY `system_users_groups_group_id_13685d93_fk_auth_group_id` (`group_id`),
  CONSTRAINT `system_users_groups_group_id_13685d93_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `system_users_groups_users_id_3c266c8f_fk_system_users_id` FOREIGN KEY (`users_id`) REFERENCES `system_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_users_groups`
--

LOCK TABLES `system_users_groups` WRITE;
/*!40000 ALTER TABLE `system_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_users_user_permissions`
--

DROP TABLE IF EXISTS `system_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_users_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `users_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_users_user_permis_users_id_permission_id_84c282cb_uniq` (`users_id`,`permission_id`),
  KEY `system_users_user_pe_permission_id_691fa57c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `system_users_user_pe_permission_id_691fa57c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `system_users_user_pe_users_id_1cfa57c2_fk_system_us` FOREIGN KEY (`users_id`) REFERENCES `system_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_users_user_permissions`
--

LOCK TABLES `system_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `system_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'abc'
--

--
-- Dumping routines for database 'abc'
--
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-11 10:30:32
