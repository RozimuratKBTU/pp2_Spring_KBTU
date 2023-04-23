create table PhoneBoook(
	id int  primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	phone_number varchar(15) not null
	
);

insert into Phoneboook (id,first_name, last_name, phone_number)
values 
(1,'John','Doe','1234567890'),
(2,'Rozi','Mirpulatov','87023454947'),
(3,'Dueyn','Jhonson','87771343254');

select * from Phoneboook

update Phoneboook set first_name = 'Jane', phone_number ='111222333'
where id = 1;

select * from PhoneBoook where first_name = 'Rozi' or  phone_number like '%111%';

delete from PhoneBoook where first_name = 'Dueyn' 

select * from PhoneBoook