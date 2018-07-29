-- Schema for Summer 2017 GTL project

drop database if exists sncf_team5;
create database sncf_team5;
use sncf_team5;

-- any user_id not in customer table is an admin
-- admins are only added by DBA, not by the train reservation application
create table user (
  user_id int primary key auto_increment,
  email varchar(32) unique not null,
  password varchar(64) not null,
  first_name varchar(32),
  last_name varchar(64)
);

create table address (
  address_id int primary key auto_increment,
  line1 varchar(32),
  line2 varchar(32),
  city varchar(32),
  state char(2),
  post_code char(5),
  country varchar(4)
);

create table customer (
  customer_id int primary key auto_increment,
  user_id int not null,
  address_id int not null,
  birthdate date,
  credit_card_no char(16) not null,
  credit_card_expiry date,

  foreign key (user_id) references user(user_id)
    on update cascade
    on delete cascade,
  foreign key (address_id) references address(address_id)
    on update cascade
    on delete restrict
);

create table trip (
  trip_id int primary key auto_increment,
  customer_id int,
  price decimal(5,2),

  foreign key (customer_id) references customer(customer_id)
    on update cascade
    on delete restrict
);

create table passenger (
  passenger_id int primary key auto_increment,
  first_name varchar(32),
  last_name varchar(64),
  birthdate date,
  trip_id int not null,

  foreign key (trip_id) references trip(trip_id)
    on update cascade
    on delete restrict
);

create table station (
  station_id int primary key auto_increment,
  name varchar(32) unique not null,
  address_id int,

  foreign key (address_id) references address(address_id)
    on update cascade
    on delete restrict
);

create table train (
  train_id int primary key auto_increment,
  capacity int not null,
  price_per_km double not null
);

create table stop (
  stop_id int primary key auto_increment,
  station_id int not null,
  train_id int not null,
  arrival_time time,
  departure_time time,
  distance int, -- distance from origin

  foreign key (station_id) references station(station_id)
    on update cascade
    on delete restrict,
  foreign key (train_id) references train(train_id)
    on update cascade
    on delete cascade
);


-- Error with trip_train: schema does not allow for booking two separate trains as legs
create table trip_train (
  trip_id int primary key,
  embark_stop_id int not null,
  disembark_stop_id int not null,

  foreign key (embark_stop_id) references stop(stop_id)
    on update cascade
    on delete restrict,
  foreign key (disembark_stop_id) references stop(stop_id)
    on update cascade
    on delete restrict,
  foreign key (trip_id) references trip(trip_id)
    on update cascade
    on delete restrict
);
