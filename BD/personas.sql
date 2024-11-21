-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2024 a las 20:27:50
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `personas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `fecha` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id`, `nombre`, `correo`, `fecha`) VALUES
(1, 'jon', 'ini', '2024-09-06'),
(2, 'John Doe', 'empleado@atlas.com', ' 2024-11-19 11:00'),
(3, 'John Doe', 'empleado@atlas.com', '    2024-11-19 11:02'),
(4, 'admin@', 'admin@admin.com', '2024-11-19'),
(5, 'admin@', 'admin@admin.com', '  2024-11-19'),
(8, 'admin@', 'admin@admin.com', '2024-11-19'),
(10, 'admin@', 'admin@admin.com', ' 2024-11-19 12:30:41.293375'),
(14, 'docu', 'ggjhh@ghhj.com', '  2024-11-20 17:30:57.934722'),
(15, 'John Doe', 'empleado@atlas.com', ' 2024-11-20 17:36:15.563396'),
(16, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 10:29:40.401117'),
(17, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 10:31:09.898270'),
(18, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 10:50:08.911694'),
(19, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 10:50:36.204934'),
(20, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 11:14:22.218928'),
(21, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 11:17:50.669656'),
(22, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 11:17:55.694837'),
(23, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 11:21:04.329433'),
(24, 'John Doe', 'empleado@atlas.com', ' 2024-11-21 11:21:12.942701');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
