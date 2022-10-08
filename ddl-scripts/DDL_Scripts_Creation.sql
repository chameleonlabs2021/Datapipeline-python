-- // 1) Table creation for plan

create table Plan (
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
supervisor_contract_version_id varchar(200),
create_timestamp varchar(200),
status varchar(200),
opening_timestamp varchar(200),
activation_completed_timestamp varchar(200),
closing_timestamp  varchar(200),
closure_completed_timestamp varchar(200),
details_key varchar(200),
details_value varchar(200),
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200)
);

-- // 2) Table creation for flag
create table flags (
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
flag_definition_id varchar(200),
description varchar(200),
creation_timestamp varchar(200),
effective_timestamp varchar(200),
expiry_timestamp  varchar(200),
is_active varchar(200),
customer_id varchar(200),
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200)
);

-- // 3) Table creation for Customers

CREATE TABLE customers (
   sequence_id SERIAL PRIMARY KEY,
   id varchar(200),
   status varchar(200),
   identifiers_identifier_type_email varchar(200),
   identifiers_identifier_email varchar(200),
   identifiers_identifier_type_username varchar(200),
   identifiers_identifier_username varchar(200),
   identifiers_identifier_type_phone varchar(200),
   identifiers_identifier_phone varchar(200),
   customer_details_title varchar(200),
   customer_details_first_name varchar(200),
   customer_details_middle_name varchar(200),
   customer_details_last_name varchar(200),
   customer_details_dob varchar(200),
   customer_details_gender varchar(200),
   customer_details_nationality varchar(200),
   customer_details_email_address varchar(256),
   customer_details_mobile_phone_number varchar(100),
   customer_details_home_phone_number varchar(100),
   customer_details_business_phone_number varchar(100),
   customer_details_contact_method varchar(200),
   customer_details_country_of_residence varchar(200),
   customer_details_country_of_taxation varchar(200),
   customer_details_accessibility varchar(200),
   customer_details_external_customer_id varchar(200),
   additional_details_key varchar(200),
   additional_details_value varchar(200),
   TM_load_timestamp timestamp default current_timestamp,
   load_TM_status varchar(200)
);

-- // 4) Table creation for Accounts

create table accounts(
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
name varchar(200),
product_id varchar(200),
product_version_id varchar(200),
permitted_denominations_0 varchar(200),
status varchar(200),
opening_timestamp varchar(200),
closing_timestamp varchar(200),
stakeholder_ids_0 varchar(100),
instance_param_vals_key varchar(100),
derived_instance_param_vals_key varchar(200),
details_key varchar(200),
accounting_tside varchar(200),
tm_load_timestamp varchar(200),
load_tm_status varchar(200)
);

-- // 5) Table creation for account_plan_assocs

create table account_plan_assocs (
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
account_id varchar(200),
plan_id varchar(200),
create_timestamp varchar(200),
start_timestamp varchar(200),
end_timestamp varchar(200),
status varchar(200),
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200)
);

-- // 6) Table creation for Payment_Device

CREATE TABLE Payment_Device(
  sequence_id SERIAL PRIMARY KEY,
   id varchar(200),
   token varchar(200) NOT NULL,
   payment_device_id int,
   account_id int,
   status int,
   start_timestamp TIMESTAMP,
   end_timestamp TIMESTAMP,
   TM_load_timestamp timestamp default current_timestamp,
   load_TM_status varchar(200)
);


-- // 7) Table creation for Payment_Device_Link
 
create TABLE Payment_Device_Link(
  sequence_id SERIAL PRIMARY KEY,
  id varchar(200),
  token varchar(200) NOT NULL,
    payment_device_id varchar(200),
   account_id varchar(200),
   status varchar(200),
   start_timestamp TIMESTAMP,
   end_timestamp TIMESTAMP,
   TM_load_timestamp timestamp default current_timestamp,
   load_TM_status varchar(200));

--------  Table creation for reconciliation files---------------

-- // 1) Table creation for plan

create table Plan_recon (
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
supervisor_contract_version_id varchar(200),
create_timestamp varchar(200),
status varchar(200),
opening_timestamp varchar(200),
activation_completed_timestamp varchar(200),
closing_timestamp  varchar(200),
closure_completed_timestamp varchar(200),
details_key varchar(200),
details_value varchar(200),
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200)
);

-- // 2) Table creation for flag
create table flags_recon (
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
flag_definition_id varchar(200),
description varchar(200),
creation_timestamp varchar(200),
effective_timestamp varchar(200),
expiry_timestamp  varchar(200),
is_active varchar(200),
customer_id varchar(200),
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200)
);

-- // 3) Table creation for Customers

CREATE TABLE customers_recon (
   sequence_id SERIAL PRIMARY KEY,
   id varchar(200),
   status varchar(200),
   identifiers_identifier_type_email varchar(200),
   identifiers_identifier_email varchar(200),
   identifiers_identifier_type_username varchar(200),
   identifiers_identifier_username varchar(200),
   identifiers_identifier_type_phone varchar(200),
   identifiers_identifier_phone varchar(200),
   customer_details_title varchar(200),
   customer_details_first_name varchar(200),
   customer_details_middle_name varchar(200),
   customer_details_last_name varchar(200),
   customer_details_dob varchar(200),
   customer_details_gender varchar(200),
   customer_details_nationality varchar(200),
   customer_details_email_address varchar(256),
   customer_details_mobile_phone_number varchar(100),
   customer_details_home_phone_number varchar(100),
   customer_details_business_phone_number varchar(100),
   customer_details_contact_method varchar(200),
   customer_details_country_of_residence varchar(200),
   customer_details_country_of_taxation varchar(200),
   customer_details_accessibility varchar(200),
   customer_details_external_customer_id varchar(200),
   additional_details_key varchar(200),
   additional_details_value varchar(200),
   TM_load_timestamp timestamp default current_timestamp,
   load_TM_status varchar(200)
);

-- // 4) Table creation for Accounts

create table accounts_recon(
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
name varchar(30),
product_id varchar(30),
product_version_id varchar(30),
permitted_denominations_0 varchar(200),
status varchar(200),
opening_timestamp varchar(200),
closing_timestamp varchar(200),
stakeholder_ids_0 varchar(200),
instance_param_vals_key varchar(200),
derived_instance_param_vals_key varchar(200),
details_key varchar(200),
accounting_tside varchar(200),
tm_load_timestamp varchar(200),
load_tm_status varchar(200)
);

-- // 5) Table creation for account_plan_assocs

create table account_plan_assocs_recon (
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
account_id varchar(200),
plan_id varchar(200),
create_timestamp varchar(200),
start_timestamp varchar(200),
end_timestamp varchar(200),
status varchar(200),
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200)
);

-- // 6) Table creation for Payment_Device

CREATE TABLE Payment_Device_Recon(
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
token varchar(200) NOT NULL,
payment_device_id int,
account_id int,
status int,
start_timestamp TIMESTAMP,
end_timestamp TIMESTAMP,
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200)
);

-- // 7) Table creation for Payment_Device_Link
  
create TABLE Payment_Device_Link_Recon(
sequence_id SERIAL PRIMARY KEY,
id varchar(200),
token varchar(200) NOT NULL,
payment_device_id varchar(200),
account_id varchar(200),
status varchar(200),
start_timestamp TIMESTAMP,
end_timestamp TIMESTAMP,
TM_load_timestamp timestamp default current_timestamp,
load_TM_status varchar(200));



------------ Table creation for Raw Data Excel Files-----------------

Creating tables for "product_details", "customer_transactions", "customer_payment_details", "customer_details"

-- a)GL040 ->Is named as Product_Details

create table Product_details(
Institution varchar(200),
Product_Type varchar(200),
GL_Code varchar(200),
GL_Desc varchar(200),
Currency varchar(200),
Account_Number varchar(200),
Account_Name varchar(200),
Customer_Number varchar(200),
Customer_Name varchar(200),
Phone_Number varchar(200),
Customer_Type varchar(200),
Balance_Direction varchar(200),
Whether_To_Pay_Interest varchar(200),
Whether_To_Allow_Overdraft varchar(200),
Balance_Update_Type varchar(200),
Account_Status varchar(200),
Opponent_Account varchar(200),
Account_Opening_Date varchar(200),
Date_Of_Expiry varchar(200),
Value_Date varchar(200),
Account_Balance varchar(200),
Write_off varchar(200),
Term_of_Suspense varchar(200),
Write_off_Mode varchar(200),
National_ID varchar(30),
Business_License varchar(30)
);

-- b) PY001 --> Is named as Customer Transaction
create table Customer_Transactions(
transaction_date varchar(200),
transaction_time varchar(200),
core_reference_number varchar(200),
partner_reference_number varchar(200),
channel_reference_number varchar(200),
transaction_type varchar(200),
transaction_type_description varchar(200),
transaction_result varchar(200),
account_name varchar(200),
account_number varchar(200),
currency varchar(200),
debit_credit varchar(200),
commission varchar(200),
transaction_amount varchar(200),
counterparty_account_name varchar(200),
counterparty_account_number varchar(200),
debit_account_number varchar(200),
credit_account_number varchar(200),
counterparty_currency varchar(200),
transaction_purpose varchar(200),
essential_service_sub_category varchar(200),
bill_reference_number varchar(200),
transaction_id varchar(200),
partner_response varchar(200),
remarks varchar(200),
fail_reason varchar(200)
);

--c) PY002 --> Is named as Customer Payment Details

create table customer_Payment_details(
Recurring_Payment_ID varchar(200),
Serial_No varchar(200),
Account_Number varchar(200),
Account_Name varchar(200),
Schedule_Date varchar(200),
Counterparty_Account_Number varchar(200),
Counterparty_Account_Name varchar(200),
Recurring_Payment_Amount varchar(200),
Transfer_Purpose varchar(200),
Frequency varchar(200),
Repeat_Freq varchar(200),
Status varchar(200),
Payment_Date varchar(200),
Payment_Result varchar(200),
Payment_Failed_Reason varchar(200),
Channel_Reference_Number varchar(200),
Core_Reference_Number varchar(200),
Partner_Reference_Number varchar(200)
);

--D) CL001 --> Is named as Customer Details

create table customer_details(
CustomerCID varchar(200),
CustomerName varchar(200),
MobileNumber varchar(200),
Email varchar(200),
LoanAccountNumber varchar(200),
LoanApprovedAmount varchar(200),
LoanOpenDate varchar(200)
);
