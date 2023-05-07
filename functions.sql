CREATE FUNCTION stack.select_count_pok_by_service(ser int, mon date) 
RETURNS TABLE(number int, service int, count int) AS $$
	SELECT number, service, COUNT(*) AS count 
	FROM stack.accounts
	JOIN stack.counters ON accounts.row_id = counters.acc_id
	JOIN stack.meter_pok ON accounts.row_id = meter_pok.acc_id AND counters.row_id = meter_pok.counter_id
	WHERE service = ser AND month = mon
	GROUP BY number, service
$$ LANGUAGE SQL;

select * from stack.select_count_pok_by_service('300','20230201')