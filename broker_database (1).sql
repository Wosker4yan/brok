-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 26, 2017 at 06:33 PM
-- Server version: 5.7.17-0ubuntu0.16.04.2
-- PHP Version: 7.0.15-0ubuntu0.16.04.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `broker_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `Brok`
--

CREATE TABLE `Brok` (
  `Code` bigint(20) NOT NULL,
  `type` int(1) DEFAULT NULL,
  `purpose` int(1) DEFAULT NULL,
  `district` int(1) DEFAULT NULL,
  `street` int(1) DEFAULT NULL,
  `house_format` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `room` int(1) DEFAULT NULL,
  `floors_how_many` int(1) DEFAULT NULL,
  `the_floor` int(1) DEFAULT NULL,
  `square_meter` int(5) DEFAULT NULL,
  `comments` text CHARACTER SET utf8 COLLATE utf8_bin,
  `phone_number` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `price` int(4) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `name_worker` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `currency` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Brok`
--

INSERT INTO `Brok` (`Code`, `type`, `purpose`, `district`, `street`, `house_format`, `room`, `floors_how_many`, `the_floor`, `square_meter`, `comments`, `phone_number`, `price`, `date`, `name_worker`, `currency`) VALUES
(1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(2, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(3, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(4, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(5, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(6, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(7, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(8, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(9, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(10, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(11, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(12, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(13, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(14, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(15, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(16, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(17, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(18, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(19, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(20, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(21, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(22, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(23, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(24, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(25, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(26, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, '81234', 3, NULL, 'asdf', ''),
(27, 2, 3, 2, 2, NULL, 2, 6, 6, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(28, 1, 1, 2, 2, NULL, 2, 3, 4, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(29, 2, 3, 3, 3, NULL, 5, 14, 18, 12312, NULL, NULL, NULL, NULL, NULL, ''),
(30, 1, 1, 3, 2, NULL, 3, 12, 16, 123131, NULL, NULL, NULL, NULL, NULL, ''),
(31, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(32, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(33, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(34, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(35, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(36, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(37, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(38, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(39, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(40, 1, 1, 3, 2, NULL, 3, 12, 16, 123, NULL, NULL, NULL, NULL, NULL, ''),
(41, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(42, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(43, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(44, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(45, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(46, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(47, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(48, 1, 1, 3, 3, NULL, 4, 14, 7, 1231, NULL, NULL, NULL, NULL, NULL, ''),
(49, 1, 1, 3, 2, NULL, 3, 12, 14, 12313, NULL, NULL, NULL, NULL, NULL, ''),
(50, 1, 1, 3, 2, NULL, 3, 12, 14, 12313, NULL, NULL, NULL, NULL, NULL, ''),
(51, 1, 1, 3, 2, NULL, 3, 12, 14, 12313, NULL, NULL, NULL, NULL, NULL, ''),
(52, 1, 1, 3, 2, NULL, 3, 12, 14, 12313, NULL, NULL, NULL, NULL, NULL, ''),
(53, 3, 1, 2, 3, NULL, 3, 12, 4, 123123, NULL, NULL, NULL, NULL, NULL, ''),
(54, 3, 1, 2, 3, NULL, 3, 12, 4, 123123, NULL, NULL, NULL, NULL, NULL, ''),
(55, 3, 1, 2, 3, NULL, 3, 12, 4, 123123, NULL, NULL, NULL, NULL, NULL, ''),
(56, NULL, NULL, NULL, NULL, ' 12313asada', NULL, NULL, NULL, NULL, 'xsaf', 'qsada', 4545454, NULL, '1231', ''),
(57, 3, 1, 2, 3, NULL, 3, 12, 4, 123123, NULL, NULL, NULL, NULL, NULL, ''),
(58, NULL, NULL, NULL, NULL, ' 12313asada', NULL, NULL, NULL, NULL, 'xsaf', 'qsada', 4545454, NULL, '1231', ''),
(59, 3, 1, 2, 3, NULL, 3, 12, 4, 123123, NULL, NULL, NULL, NULL, NULL, ''),
(60, NULL, NULL, NULL, NULL, ' 12313asada', NULL, NULL, NULL, NULL, 'xsaf', 'qsada', 4545454, NULL, '1231', ''),
(61, 3, 1, 2, 3, NULL, 3, 12, 4, 123123, NULL, NULL, NULL, NULL, NULL, ''),
(62, NULL, NULL, NULL, NULL, ' 12313asada', NULL, NULL, NULL, NULL, 'xsaf', 'qsada', 4545454, NULL, '1231', ''),
(63, 3, 1, 2, 3, NULL, 3, 12, 4, 123123, NULL, NULL, NULL, NULL, NULL, ''),
(64, NULL, NULL, NULL, NULL, ' 12313asada', NULL, NULL, NULL, NULL, 'xsaf', 'qsada', 4545454, NULL, '1231', ''),
(744, 3, 1, 0, 0, NULL, 0, 0, 0, 1234, NULL, NULL, NULL, NULL, NULL, ''),
(745, 1, 1, 0, 0, NULL, 0, 0, 0, 12343, 'HRANt', NULL, NULL, NULL, NULL, ''),
(746, 2, 1, 0, 0, NULL, 0, 0, 0, 2342, 'HRANT JAN', NULL, NULL, NULL, NULL, ''),
(747, 2, 1, 0, 0, NULL, 0, 0, 0, 2342, '', NULL, NULL, NULL, NULL, ''),
(748, 1, 3, 3, 3, ' adn', 3, 5, 6, 123131, 'rabdababa123', '123131', 2222, NULL, '333333', ''),
(749, 4, 3, 3, 1, ' 123', 2, 3, 2, 12321, 'sadasdsadsa', 'sadada', 1231231, NULL, '31231313', ''),
(750, 1, 3, 2, 1, ' 2131', 3, 2, 5, 1313, 'qwewda', 'qweqe', 123123131, NULL, 'sdadsadasada', ''),
(751, 2, 3, 1, 1, ' 1/231', 0, 5, 0, 1231311231, 'asdadq123', 'eqweqeqweq', 211231313, NULL, 'wqeqeqe', ''),
(752, 3, 3, 2, 1, ' 123/113', 3, 4, 8, 12313131, 'ysgdaudgaudgau', '+374951515497', 123123131, NULL, 'vahahha', ''),
(753, 1, 3, 2, 1, ' 1/231', 2, 8, 10, 1231, '12321313213131', 'sdada', 12313, NULL, 'sadsadasds', 'AMD'),
(754, 4, 2, 2, 1, ' 2/312', 1, 3, 3, 12313, '132131', 'qwee', 21313, NULL, '1312312313', 'Euro'),
(755, 4, 2, 2, 1, ' 2/312', 1, 3, 3, 12313, '132131', 'qwee', 21313, NULL, '1312312313', 'Euro'),
(756, 3, 2, 3, 1, ' 3/123', 2, 4, 5, 2131, '31231', '3123', 131, NULL, '11', 'AMD'),
(757, 3, 2, 3, 1, ' 3/123', 2, 4, 5, 2131, '31231', '3123', 131, NULL, '11', 'AMD'),
(758, 3, 3, 1, 1, ' 2/31', 2, 8, 9, 2131, '123123', '13123', 13123, '2025-04-17', '123131', 'Euro'),
(759, 2, 1, 2, 1, ' 1/231', 2, 7, 8, 313, '131313', '13123', 131231, '2017-04-25', '12313', 'AMD');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Brok`
--
ALTER TABLE `Brok`
  ADD PRIMARY KEY (`Code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Brok`
--
ALTER TABLE `Brok`
  MODIFY `Code` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=760;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
