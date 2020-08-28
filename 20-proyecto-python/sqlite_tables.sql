CREATE TABLE IF NOT EXISTS usuarios(
	id 			integer	 PRIMARY KEY,
	nombre 		varchar(100),
	apellidos 	varchar(255),
	email 		varchar(255) NOT NULL,
	password	varchar(255) NOT NULL,
	fecha		date NOT NULL,
	CONSTRAINT  uq_email UNIQUE(email)
);

CREATE TABLE IF NOT EXISTS notas(
	id 			integer PRIMARY KEY,
	usr_id		integer NOT NULL,
	titulo		varchar(255) NOT NULL,
	descripcion MEDIUMTEXT,
	fecha		date NOT NULL,
	CONSTRAINT fk_nota_usr FOREIGN KEY(usr_id) REFERENCES usuarios(id)
);