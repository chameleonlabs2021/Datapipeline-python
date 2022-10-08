truncate table customers;

insert into customers(id, status, identifiers_identifier_type_email, identifiers_identifier_email, identifiers_identifier_type_username, identifiers_identifier_username, identifiers_identifier_type_phone, identifiers_identifier_phone,
customer_details_title, customer_details_first_name, customer_details_middle_name, customer_details_last_name,
customer_details_dob, customer_details_gender, customer_details_nationality, customer_details_email_address,
customer_details_mobile_phone_number, customer_details_home_phone_number, customer_details_business_phone_number,
customer_details_contact_method, customer_details_country_of_residence, customer_details_country_of_taxation,
customer_details_accessibility, customer_details_external_customer_id, additional_details_key, additional_details_value, tm_load_timestamp, load_tm_status) select cd.customercid ,pd.account_status , 'IDENTIFIER_TYPE_EMAIL', cd.email, 'IDENTIFIER_TYPE_USERNAME', cd.customername, 'IDENTIFIER_TYPE_PHONE', cd.mobilenumber,
'title', 'abc', 'abc', 'xyz',
'10/10/1996', 'female', 'Singaporean', 'abc@gmail.com',
pd.phone_number,'78676676', pd.phone_number,
'email', 'Singapore', 'Singapore', 'Sg', 'France', 'key1', 'value1', '12/09/2022', 'loading' from customer_details  cd inner join product_details  pd on cd.customercid = pd.national_id
where cd.customercid is not null;
commit;