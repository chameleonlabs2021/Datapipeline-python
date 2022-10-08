truncate table account_plan_assocs;
insert into account_plan_assocs(id, account_id, plan_id,create_timestamp,start_timestamp,end_timestamp,status,load_tm_status)
select national_id,account_Number ,product_type,account_opening_date,account_opening_date,date_of_expiry,account_status ,'Inserted' from
product_details ;
commit;