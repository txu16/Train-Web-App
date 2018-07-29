use sncf_team5;

-- List the emails and names of all the admin users.
SELECT '';
select 'List the emails and names of all the admin users.';
SELECT '';

	select 
		email, 
		first_name, 
		last_name 
	from 
	user left join customer using (user_id)
	where customer_id is NULL;

-- List the emails and names of all the customers.
SELECT '';
SELECT 'List the emails and names of all the customers.';
SELECT '';

	select 
		email, 
		first_name, 
		last_name 
	from 
	user join customer using (user_id);

-- List the direct trips (single trains) from Metz to Aix.
SELECT '';
SELECT 'List the direct trips (single trains) from Metz to Aix.';
SELECT '';

	select 
		start.name, 
		start.departure_time, 
		ending.name, 
		ending.arrival_time 
	from 

		(
			select 
				name, 
				train_id, 
				arrival_time, 
				departure_time 
			from 
			stop join station using (station_id)
		) 

		as start

	join 

		(
			select 
				name, 
				train_id, 
				arrival_time, 
				departure_time 
			from 
			stop join station using (station_id)
		)

		as ending

	using (train_id)
	where (
		start.name = "Metz Ville" 
		and ending.name = "Aix" 
		and start.arrival_time is NULL 
		and ending.departure_time is NULL
		);

-- List the one-change trips (two trains) from Metz to Aix. 
-- Layovers should not be less than 10 minutes.
SELECT '';
SELECT 'List the one-change trips (two trains) from Metz to Aix. Layovers should not be less than 10 minutes.';
SELECT '';

	select 
		starting_station,
		leg1_depart as train1_depart,
		leg1_arrive as train1_arrive,
		middle_station as changing_station,
		leg2_departagain as train2_depart,
		leg2_arrive as train2_arrive,
		ending_station
	from

		-- trains leaving Metz and their destinations
		(
			select 
				train_id as leg1_id, 
				leavemetz.departure_time as leg1_depart, 
				moremetz.arrival_time as leg1_arrive, 
				moremetz.departure_time as leg2_depart, 
				leavemetz.name as starting_station,
				moremetz.name as middle_station, 
				leavemetz.distance as leg1_startdist, 
				moremetz.distance as leg1_enddist 
			from 

			(
				select 
					departure_time, 
					name, 
					train_id, 
					distance 
				from 
				stop join station 
				using (station_id) 
				where (
					name = "Metz Ville" 
					and arrival_time is NULL
					)
			) 
			as leavemetz 

		join 

			(
				select 
					arrival_time, 
					departure_time, 
					name, 
					train_id, 
					distance 
				from 
				stop join station using (station_id)
			) 
			as moremetz 

		using (train_id)
		where (leavemetz.name != moremetz.name)
		)

	as metz 

	join 

		-- trains coming to Aix and their origins
		(
		select 
			train_id as leg2_id, 
			moreaix.departure_time as leg2_departagain, 
			moreaix.name as middle_station, 
			comeaix.name as ending_station,
			moreaix.distance as leg2_startdist, 
			comeaix.arrival_time as leg2_arrive, 
			comeaix.distance as leg2_enddist 
		from 

			(
				select 
					arrival_time, 
					departure_time, 
					name, 
					train_id, 
					distance 
				from 
				stop join station using (station_id)
			) 
			as moreaix 

		join

			(
				select 
					arrival_time, 
					name, 
					train_id, 
					distance 
				from 
				stop join station using (station_id) 
				where (
					name = "Aix" 
					and departure_time is NULL)
			) 
			as comeaix 

		using (train_id)

		where (comeaix.name != moreaix.name) 
		)

	as aix

	using (middle_station)
	where (
		leg1_id != leg2_id
		and leg2_departagain - leg1_arrive >= 10
		);

-- Book a trip from Metz to Aix on 8 August 2017 for two passengers 
-- (including the customer booking the trip).
SELECT '';
SELECT 'Book a trip from Metz to Aix on 8 August 2017 for two passengers (including the customer booking the trip).';
SELECT '';

	-- table TRIP
	insert into trip(customer_id, price) values (
	2, 70.00);

	-- table PASSENGER
	insert into passenger (first_name, last_name, birthdate, trip_id) values (
	"John", "Cena", 19770423, 1 );
	insert into passenger (first_name, last_name, birthdate, trip_id) values (
	"Paul", "Voss", 16200808, 1);

	-- table TRIP_TRAIN
	insert into trip_train values (
	1, 5, 6);

-- Show the passenger manifest (passenger first names and last names) 
-- for the leg Metz to Strasbourg for the train that originates in Metz and terminates in Aix.
SELECT '';
SELECT 'Show the passenger manifest (passenger first names and last names) for the leg Metz to Strasbourg for the train that originates in Metz and terminates in Aix.';
SELECT '';

	select 
		concat(custfirst, ' ', custlast) as customer_name,
		concat(first_name, ' ', last_name) as passenger_name
	from 
	(
		select trip_id, first_name, last_name, custfirst, custlast
			from passenger join (

				select 
					trip_id, 
					first_name as custfirst, 
					last_name as custlast 

				from trip join (

					select 
						customer_id, 
						first_name, 
						last_name 

					from customer join user using (user_id)

					) as custuser

			using (customer_id)

			) as passtrip
			using (trip_id)
	) 
	as totalmanifest
	join 
	trip_train using (trip_id)

	where (
		embark_stop_id = (

		select stop_id from stop join 

		(
			select 
				leg1_id as train_id,
				leg1_depart as metz_depart,
				leg1_arrive as strasbourg_arrive,
				leg2_depart as strasbourg_depart
			from

			-- trains leaving Metz and their destinations
			(
				select 
				train_id as leg1_id, 
					leavemetz.departure_time as leg1_depart, 
					moremetz.arrival_time as leg1_arrive, 
					moremetz.departure_time as leg2_depart, 
					leavemetz.name as starting_station,
					moremetz.name as middle_station, 
					leavemetz.distance as leg1_startdist, 
					moremetz.distance as leg1_enddist 
				from 

					(
						select 
							departure_time, 
							name, 
							train_id, 
							distance 
						from stop join station using (station_id) 
						where (
							name = "Metz Ville" 
							and arrival_time is NULL
							)
					) 
					as leavemetz 

				join 

					(
						select 
							arrival_time, 
							departure_time, 
							name, 
							train_id, 
							distance 
						from stop join station using (station_id)
					)
					as moremetz 

				using (train_id)

				where (leavemetz.name != moremetz.name)
			)

			as metz join 

			-- trains coming to Aix and their origins
			(
				select 
					train_id as leg2_id, 
					moreaix.departure_time as leg2_departagain, 
					moreaix.name as middle_station, 
					comeaix.name as ending_station,
					moreaix.distance as leg2_startdist, 
					comeaix.arrival_time as leg2_arrive, 
					comeaix.distance as leg2_enddist 
				from 

					(
						select 
							arrival_time, 
							departure_time, 
							name, 
							train_id, 
							distance 
						from stop join station using (station_id)
					) 
					as moreaix 

				join

					(
						select 
							arrival_time, 
							name, 
							train_id, 
							distance 
						from stop join station using (station_id) 
						where (
							name = "Aix" 
							and departure_time is NULL
							)
					) 
					as comeaix 

				using (train_id)

				where (comeaix.name != moreaix.name) 
			)

			as aix

			using (middle_station)
			where (
				leg1_id = leg2_id
				)
		)


		as stras


		using (train_id)
		where (
			stop.departure_time = stras.metz_depart 
			-- or stop.arrival_time = stras.strasbourg_arrive
			)
		)
		and disembark_stop_id = (
			select stop_id from stop join 

			(
				select 
					leg1_id as train_id,
					leg1_depart as metz_depart,
					leg1_arrive as strasbourg_arrive,
					leg2_depart as strasbourg_depart
				from

				-- trains leaving Metz and their destinations
				(
					select 
					train_id as leg1_id, 
						leavemetz.departure_time as leg1_depart, 
						moremetz.arrival_time as leg1_arrive, 
						moremetz.departure_time as leg2_depart, 
						leavemetz.name as starting_station,
						moremetz.name as middle_station, 
						leavemetz.distance as leg1_startdist, 
						moremetz.distance as leg1_enddist 
					from 

						(
							select 
								departure_time, 
								name, 
								train_id, 
								distance 
							from stop join station using (station_id) 
							where (
								name = "Metz Ville" 
								and arrival_time is NULL
								)
						) 
						as leavemetz 

					join 

						(
							select 
								arrival_time, 
								departure_time, 
								name, 
								train_id, 
								distance 
							from stop join station using (station_id)
						)
						as moremetz 

					using (train_id)

					where (leavemetz.name != moremetz.name)
				)

				as metz join 

				-- trains coming to Aix and their origins
				(
					select 
						train_id as leg2_id, 
						moreaix.departure_time as leg2_departagain, 
						moreaix.name as middle_station, 
						comeaix.name as ending_station,
						moreaix.distance as leg2_startdist, 
						comeaix.arrival_time as leg2_arrive, 
						comeaix.distance as leg2_enddist 
					from 

						(
							select 
								arrival_time, 
								departure_time, 
								name, 
								train_id, 
								distance 
							from stop join station using (station_id)
						) 
						as moreaix 

					join

						(
							select 
								arrival_time, 
								name, 
								train_id, 
								distance 
							from stop join station using (station_id) 
							where (
								name = "Aix" 
								and departure_time is NULL
								)
						) 
						as comeaix 

					using (train_id)

					where (comeaix.name != moreaix.name) 
				)

			as aix

			using (middle_station)
			where (
				leg1_id = leg2_id
				)
		)


		as stras


		using (train_id)
		where (
			stop.arrival_time = stras.strasbourg_arrive
			)
		)
	);