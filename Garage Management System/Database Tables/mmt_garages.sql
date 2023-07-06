-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2021 at 07:04 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mmt_garages`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Customer_Code` int(255) NOT NULL,
  `Customer_Name` varchar(80) NOT NULL,
  `CNIC_Number` varchar(80) NOT NULL,
  `Date_of_Birth` varchar(10) NOT NULL,
  `Gender` varchar(80) NOT NULL,
  `Phone_Number` varchar(80) NOT NULL,
  `Email_Address` varchar(80) NOT NULL,
  `Car_Name` varchar(80) NOT NULL,
  `Car_Model` varchar(80) NOT NULL,
  `Car_Registration_Number` varchar(80) NOT NULL,
  `Address` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Customer_Code`, `Customer_Name`, `CNIC_Number`, `Date_of_Birth`, `Gender`, `Phone_Number`, `Email_Address`, `Car_Name`, `Car_Model`, `Car_Registration_Number`, `Address`) VALUES
(11, 'Chinmay Beldar', '567', '2002-03-10', 'male', '9370183965', 'chimaybeldar@gmail.com', ' Tata Nano', 'XE', 'MH12RS1256', 'chalisgaov Vidharbh'),
(12, 'Prasad Labade', '789', '2002-11-06', 'male', '9370183695', 'digitalchamp2016@gmail.com', ' Maruti Aulto', 'XZ', 'MH12TR16786', 'Panvel Mumbai'),
(13, 'Atharv Natu', '980', '2002-12-07', 'male', '9370813695', 'atharvnatu@gmail.com', ' Maruti Celerio', 'XT', 'MH12SD1458', 'Suncity Pune'),
(15, 'Manasi Tambe', '989', '1997-08-03', 'Female', '9833456778', 'mmt0897@gmail.com', 'Tata Tiago', 'XZ', 'MH12NJ9870', '512,Shaniwar Peth,Pune-411030'),
(18, 'Piyush Patil', '89', '2002-06-12', 'male', '9370876695', 'piyushpatil@gmail.com', ' Maruti Brizza', 'XE', 'MH12TR4185', 'Ambegaov Pune');

-- --------------------------------------------------------

--
-- Table structure for table `detail`
--

CREATE TABLE `detail` (
  `Car_Code` int(255) NOT NULL,
  `Car_Name` varchar(50) NOT NULL,
  `Car_Model` varchar(50) NOT NULL,
  `Registration_Number` varchar(50) NOT NULL,
  `Date_of_Entry` varchar(50) NOT NULL,
  `Time_of_Entry` time NOT NULL,
  `Owner_Name` varchar(50) NOT NULL,
  `Owner_CNIC_Number` varchar(50) NOT NULL,
  `Car_Color` varchar(50) NOT NULL,
  `Extra_Details` varchar(50) NOT NULL,
  `Exiting_Time` time DEFAULT NULL,
  `Exiting_Date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `detail`
--

INSERT INTO `detail` (`Car_Code`, `Car_Name`, `Car_Model`, `Registration_Number`, `Date_of_Entry`, `Time_of_Entry`, `Owner_Name`, `Owner_CNIC_Number`, `Car_Color`, `Extra_Details`, `Exiting_Time`, `Exiting_Date`) VALUES
(1, 'Hundai i20', 'Asta', 'MH12NH8901', '2020-07-06', '12:40:06', 'Abhiraj Londhe', '1243', 'Silver', '', '01:59:38', '2021-04-22'),
(2, 'Tata Tiago', 'XM', 'MH12NE7680', '2020-07-06', '12:49:55', 'Manish Tambe', '1234', 'Silver', '', '01:42:27', '2020-07-09'),
(3, 'Maruti Aulto', 'LS', 'MH47JH1234', '2020-07-06', '13:08:00', 'Prasad Labade', '5671', 'Silver', '', '18:00:13', '2021-04-20');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `Employee_Code` int(255) NOT NULL,
  `Employee_Name` varchar(50) NOT NULL,
  `CNIC_Number` varchar(50) NOT NULL,
  `Designation` varchar(50) NOT NULL,
  `Date_of_Birth` date NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `Phone_Number` varchar(50) NOT NULL,
  `Email_Address` varchar(50) NOT NULL,
  `Date_of_Joining` date NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Extra_Detail` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`Employee_Code`, `Employee_Name`, `CNIC_Number`, `Designation`, `Date_of_Birth`, `Gender`, `Phone_Number`, `Email_Address`, `Date_of_Joining`, `Address`, `Extra_Detail`) VALUES
(8, 'Manish Tambe', '123', 'Manager', '2003-01-01', 'Male', '9822060894', 'tambemanish1@gmail.com', '2013-01-01', 'Pune-411030', '');

-- --------------------------------------------------------

--
-- Table structure for table `logindb`
--

CREATE TABLE `logindb` (
  `id` int(11) NOT NULL,
  `Fname` varchar(20) NOT NULL,
  `Lname` varchar(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Username` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `Password` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logindb`
--

INSERT INTO `logindb` (`id`, `Fname`, `Lname`, `Email`, `Username`, `Password`) VALUES
(7, 'Manish', 'Tambe', 'tambemanish1@gmail.com', 'Admin', '00000');

-- --------------------------------------------------------

--
-- Table structure for table `recept`
--

CREATE TABLE `recept` (
  `Car_Code` int(255) NOT NULL,
  `Sr_No` int(255) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Price` int(255) NOT NULL,
  `Machine_Fee` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `Item_Code` int(11) NOT NULL,
  `Item_Name` varchar(50) NOT NULL,
  `Category` varchar(50) NOT NULL,
  `Quantity` int(255) NOT NULL,
  `Buying_Price` int(255) NOT NULL,
  `Selling_Price` int(255) NOT NULL,
  `Car_Name` varchar(50) NOT NULL,
  `Time_Of_Entry` time NOT NULL,
  `Date_Of_Entry` varchar(50) NOT NULL,
  `Warranty` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`Item_Code`, `Item_Name`, `Category`, `Quantity`, `Buying_Price`, `Selling_Price`, `Car_Name`, `Time_Of_Entry`, `Date_Of_Entry`, `Warranty`) VALUES
(1, 'AC', 'Air Conditioning System', 16, 6000, 7000, 'Tata', '14:31:37', '2020-07-05', ''),
(2, '6 Mirrors Pack', 'Body Parts', 29, 18000, 20000, 'Tata', '14:32:27', '2020-07-05', ''),
(3, 'Side Mirror', 'Body Parts', 9, 1200, 1300, 'Hundai', '14:33:08', '2020-07-05', ''),
(4, 'Spoiler', 'Door and Windows', 17, 1000, 2000, 'Hundai', '14:34:22', '2020-07-05', ''),
(5, 'Grills', 'Body Parts', 27, 6000, 7000, 'Maruti Suzuki', '14:35:36', '2020-07-05', ''),
(6, 'Speaker', 'Door and Windows', 24, 7000, 8000, 'Fiat', '14:36:14', '2020-07-05', ''),
(7, 'NOS', 'Engine Parts', 18, 89000, 90000, 'BMW', '14:37:08', '2020-07-05', ''),
(17, 'Side Mirrors', 'Door and Windows', 4, 2000, 4000, 'Tata Tiago', '20:30:42', '2021-04-18', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`Customer_Code`),
  ADD UNIQUE KEY `CNIC_Number` (`CNIC_Number`),
  ADD UNIQUE KEY `Phone_Number` (`Phone_Number`),
  ADD UNIQUE KEY `Email_Address` (`Email_Address`),
  ADD UNIQUE KEY `Car_Registration_Number` (`Car_Registration_Number`);

--
-- Indexes for table `detail`
--
ALTER TABLE `detail`
  ADD PRIMARY KEY (`Car_Code`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`Employee_Code`),
  ADD UNIQUE KEY `CNIC_Number` (`CNIC_Number`,`Phone_Number`,`Email_Address`);

--
-- Indexes for table `logindb`
--
ALTER TABLE `logindb`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Email_2` (`Email`),
  ADD UNIQUE KEY `Email_3` (`Email`),
  ADD UNIQUE KEY `Password` (`Password`),
  ADD UNIQUE KEY `Username` (`Username`),
  ADD UNIQUE KEY `Username_2` (`Username`),
  ADD KEY `Email` (`Email`);

--
-- Indexes for table `recept`
--
ALTER TABLE `recept`
  ADD PRIMARY KEY (`Sr_No`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`Item_Code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `Customer_Code` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `detail`
--
ALTER TABLE `detail`
  MODIFY `Car_Code` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `Employee_Code` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `logindb`
--
ALTER TABLE `logindb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `recept`
--
ALTER TABLE `recept`
  MODIFY `Sr_No` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `Item_Code` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
