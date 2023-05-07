--SELECT * FROM stack.accounts
CREATE FUNCTION stack.select_last_pok_by_acc(num int) RETURNS TABLE(acc int, serv int, date date, tarif int, value int) AS $$
	SELECT number, service, date, meter_pok.tarif, value
	FROM stack.accounts JOIN stack.counters ON accounts.row_id = counters.acc_id
	JOIN stack.meter_pok ON accounts.row_id = meter_pok.acc_id AND counters.row_id = meter_pok.counter_id
	WHERE accounts.number = num
	ORDER BY service, date DESC 
$$ LANGUAGE SQL;

select * from stack.select_last_pok_by_acc(266)