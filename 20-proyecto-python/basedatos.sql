CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE IF NOT EXISTS usuarios(
	id 			int	auto_increment NOT NULL,
	nombre 		varchar(100),
	apellidos 	varchar(255),
	email 		varchar(255) NOT NULL,
	password	varchar(255) NOT NULL,
	fecha		date NOT NULL,
	CONSTRAINT 	pk_usuarios PRIMARY KEY(id),
	CONSTRAINT  uq_email UNIQUE(email)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS notas(
	id 			int auto_increment NOT NULL,
	usr_id		int NOT NULL,
	titulo		varchar(255) NOT NULL,
	descripcion MEDIUMTEXT,
	fecha		date NOT NULL,
	CONSTRAINT pk_notas PRIMARY KEY(id),
	CONSTRAINT fk_nota_usr FOREIGN KEY(usr_id) REFERENCES usuarios(id)
)ENGINE=InnoDB;