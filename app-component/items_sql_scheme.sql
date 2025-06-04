-- table scheme
create table items (
 Name varchar(255) not null,
 Type varchar(255),
 Color varchar(255),
 Address_of_origin varchar(255),
 Owner_name varchar(255),
 Owner_phone varchar(255),
 Value int,
 Checked_out boolean,
 primary key (Name));


-- first entry into table
insert into items (Name, Type, Color, Address_of_origin, Owner_name, Value, Checked_out)
values ('Root', 'Board Game', 'Light Blue', 'Warehouse', 'Luke Lundell', 50, False);