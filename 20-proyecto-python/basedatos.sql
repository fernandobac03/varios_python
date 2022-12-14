CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuario(
    id          int(25) auto_increment NOT NULL,
    nombre      varchar(100),
    apellido    varchar(255),
    email       varchar(255) NOT NULL,
    password    varchar(255) NOT NULL,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE (email)
) ENGINE=InnoDb;

CREATE TABLE notas(
 id         int(25) auto_increment not null,
 usuario_id int(25) not null,
 titulo     varchar(255) not null,
 descripcion MEDIUMTEXT,
 fecha      date not null ,
 CONSTRAINT pk_notas PRIMARY KEY (id),
 CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuario(id)
)ENGINE=InnoDb;