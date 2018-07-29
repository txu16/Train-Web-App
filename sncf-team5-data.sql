use sncf_team5;


-- table USER
-- admins
insert into user (email, password, first_name, last_name) values(
"kelvin.xing@yahoo.com", "kxing3", "Kelvin", "Xing");
insert into user (email, password, first_name, last_name) values(
"rshid@gmail.com", "rshid3", "Raj", "Shiddapur");
insert into user (email, password, first_name, last_name) values(
"ylim@gatech.edu", "ylim3", "Youngjoon", "Lim");
insert into user (email, password, first_name, last_name) values(
"txu3@gatech.edu", "txus3", "Tiffany", "Xu");
insert into user (email, password, first_name, last_name) values(
"jcruz3@gatech.edu", "jcruz3", "Jorge", "Cruz");
insert into user (email, password, first_name, last_name) values(
"echen3@gatech.edu", "echen3", "Eileen", "Chen");

-- customers
insert into user (email, password, first_name, last_name) values(
"johndoe@gmail.com", "jdoe3", "John", "Doe");
insert into user (email, password, first_name, last_name) values(
"csimpkins@gatech.edu", "csimpkins3", "Christopher", "Simpkins");


-- table ADDRESS
insert into address (line1, city, state, post_code, country) values (
"405 Willow Oak Terrace", "Johns Creek", "GA", "30005", "USA");
insert into address (line1, city, state, post_code, country) values (
"120 North Ave NW", "Atlanta", "GA", "30332", "USA");
insert into address (line1, city, state, post_code, country) values (
"123 6th St.", "Melbourne", "FL", "32904", "USA");
insert into address (line1, city, state, post_code, country) values (
"1072 Snyder Street", "Atlanta", "GA", "30318", "USA");
insert into address (line1, city, state, post_code, country) values (
"2 Rue Marconi", "Metz", NULL, "57070", "FR");
insert into address (line1, city, state, post_code, country) values (
"12345 My Lane",  "Dallas", "TX", "75001", "USA");
insert into address (line1, city, state, post_code, country) values (
"266 4th Street NW", "Atlanta", "GA", "30313", "USA");
insert into address (line1, city, state, post_code, country) values (
"8913 Carastan Dr", "Charlotte", "NC", "28216", "USA");

-- METZ VILLE
insert into address (line1, city, state, post_code, country) values (
"1 Place du Général de Gaulle", "Metz", NULL, "57000", "FR");
-- NICE VILLE
insert into address (line1, line2, city, state, post_code, country) values (
"Gare de Nice Ville", "Avenue Thiers", "Nice", NULL, "06008", "FR");
-- THIONVILLE
insert into address (line1, city, state, post_code, country) values (
"Route Départementale 9", "Aix-en-Provence", NULL, "13290", "FR" );
-- STRASBOURG
insert into address (line1, city, state, post_code, country) values (
"20 Place de la Gare", "Strasbourg", NULL, "67000", "FR");
-- PARIS EST
insert into address (line1, city, state, post_code, country) values (
"Place du 11 Novembre 1918", "Paris", NULL, "75010", "FR");
-- Mulhouse
insert into address (line1, city, state, post_code, country) values (
"10 Avenue du Général Leclerc", "Mulhouse", NULL, "68100", "FR");
-- Montpellier
insert into address (line1, city, state, post_code, country) values (
"Place Auguste Gilbert", "Montpellier", NULL, "34000", "FR");
-- Nantes
insert into address (line1, city, state, post_code, country) values (
"27 Boulevard de Stalingrad", "Nantes", NULL, "44041", "FR");
-- Lyon Part Dieu
insert into address (line1, city, state, post_code, country) values (
"5 Place Charles Béraudier", "Lyon", NULL, "69003", "FR");
-- Nancy
insert into address (line1, city, state, post_code, country) values (
"3 Place Thiers", "Nancy", NULL, "5400", "FR");


-- table CUSTOMER
insert into customer (user_id, address_id, birthdate, credit_card_no, credit_card_expiry) values (
7, 7, 19950808, "1111111111111111", 20260824);
insert into customer (user_id, address_id, birthdate, credit_card_no, credit_card_expiry) values (
8, 8, 19920212, "1234567890000000", 20211130);


-- table STATION
insert into station (name, address_id) values (
"Metz Ville", 9);
insert into station (name, address_id) values (
"Nice Ville", 10);
insert into station (name, address_id) values (
"Aix", 11);
insert into station (name, address_id) values (
"Strasbourg", 12);
insert into station (name, address_id) values (
"Paris Est", 13);
insert into station (name, address_id) values (
"Mulhouse", 14);
insert into station (name, address_id) values (
"Montpellier", 15);
insert into station (name, address_id) values (
"Nantes", 16);
insert into station (name, address_id) values (
"Lyon Part Dieu", 17);
insert into station (name, address_id) values (
"Nancy", 18);


-- table TRAIN
insert into train (capacity, price_per_km) values (
225, .10);
insert into train (capacity, price_per_km) values (
350, .10);
insert into train (capacity, price_per_km) values (
525, .10);
insert into train (capacity, price_per_km) values (
110, .10);
insert into train (capacity, price_per_km) values (
480, .10);
insert into train (capacity, price_per_km) values (
225, .10);
insert into train (capacity, price_per_km) values (
110, .10);
insert into train (capacity, price_per_km) values (
525, .10);
insert into train (capacity, price_per_km) values (
300, .10);
insert into train (capacity, price_per_km) values (
350, .10); 
insert into train (capacity, price_per_km) values (
110, .10);
insert into train (capacity, price_per_km) values (
525, .10);
insert into train (capacity, price_per_km) values (
300, .10);
insert into train (capacity, price_per_km) values (
350, .10); 
insert into train (capacity, price_per_km) values (
225, .10);
insert into train (capacity, price_per_km) values (
350, .10);

-- table STOP 

-- METZ <-> AIX
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
1, 1, NULL, 070000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
3, 1, 120000, NULL, 750);

insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
3, 2, NULL, 123000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
1, 2, 173000, NULL, 750);

-- METZ --> STRASBOURG --> AIX

insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
1, 3, NULL, 050000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
4, 3, 063000, 064500, 150);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
3, 3, 121500, NULL, 700);

-- METZ --> LYON
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
1, 4, NULL, 050000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
9, 4, 090000, NULL, 450);

-- LYON --> AIX
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
9, 5, NULL, 093000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
3, 5, 103000, NULL, 300);

-- NANTES <-> PARIS <-> METZ
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
8, 7, NULL, 100000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
5, 7, 120000, 121500, 400);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
1, 7, 134500, NULL, 750);

insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
1, 8, NULL, 140000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
5, 8, 153000, 154500, 350);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
8, 8, 174500, NULL, 750);

-- NANTES <-> PARIS <-> MULHOUSE
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
8, 9, NULL, 093000 , 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
5, 9, 113000, 114500, 400);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
6, 9, 145000, NULL, 900);

insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
6, 10, NULL, 150000 , 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
5, 10, 180000, 181500, 500);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
8, 10, 194500 , NULL, 900);

-- PARIS <-> LYON <-> NICE
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
5, 11, NULL, 080000 , 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
9,11, 100000, 101500, 450 );
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
2,11, 144500 , NULL, 850);

insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
2, 12, NULL, 150000 , 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
9, 12, 193000, 194500, 400);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
5, 12, 214500 , NULL, 850);

-- STRASBOURG <-> MULHOUSE <-> NICE
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
4, 13, NULL, 053000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
6, 13, 063000, 064500, 100);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
2, 13, 134500, NULL, 600);

insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
2, 14, NULL, 140000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
6, 14, 210000, 211500, 500);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
4, 14, 224500, NULL, 600);

-- MONTPELLIER <-> LYON <-> NANCY
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
7, 15, NULL, 070000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
9, 15, 090000, 091500, 300);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
10, 15, 151500, NULL, 700);

insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
10, 16, NULL, 153000, 0);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
9, 16, 213000, 214500, 400);
insert into stop (station_id, train_id, arrival_time, departure_time, distance) values (
7, 16, 234500, NULL, 700);