truncate table accounts;
insert into accounts(id,name, product_id,product_version_id, permitted_denominations_0, status, opening_timestamp, closing_timestamp,
stakeholder_ids_0, instance_param_vals_key, derived_instance_param_vals_key, details_key, accounting_tside, tm_load_timestamp, load_tm_status)
select Account_Number, Account_Name, GL_Code, Account_Status, Account_Opening_Date, 'values', 'values_denominations', '12/09/2022',
'stakeholder_values', 'instance_values', 'derived_instance_values', 'key_values', 'accounting_values', '12/09/2022', 'Inserted' from product_details;
commit;