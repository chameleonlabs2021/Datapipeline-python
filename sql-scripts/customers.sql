select concat('{     "customers": [       {         "sequence_id": "',sequence_id,
'", "id": "',id,
'", "status": "',status,
'", "identifiers":[  {'
            '"identifier_type": "',identifiers_identifier_type_email,
            '","identifier": "',identifiers_identifier_type_email,
            '"}, {" identifier_type": "',identifiers_identifier_type_username,
            '"," identifier":"', identifiers_identifier_type_username,
            '"}, {" identifier_type": "',identifiers_identifier_type_phone,
             '",    " identifier": "', identifiers_identifier_type_phone,
            '"}
			 ],
            "customer_details": { '
             '"title": "', customer_details_title,
             '", "first_name": "', customer_details_first_name,
             '", "middle_name": "', customer_details_middle_name,
             '", "last_name": "', customer_details_last_name,
             '", "dob": "', customer_details_dob,
             '", "gender": "', customer_details_gender,
             '", "nationality":"', customer_details_nationality,
             '", "email_address":"', customer_details_email_address,
             '", "mobile_phone_number":"', customer_details_mobile_phone_number,
             '", "home_phone_number":"', customer_details_home_phone_number,
             '", "business_phone_number":"', customer_details_business_phone_number,
             '", "contact_method":"', customer_details_contact_method,
             '", "country_of_residence":"', customer_details_country_of_residence,
             '", "country_of_taxation":"', customer_details_country_of_taxation,
             '", "accessibility":"', customer_details_accessibility,
             '", "external_customer_id":"', customer_details_external_customer_id,
             '" },
			 "additional_details":{ '
             '"key1":"', additional_details_value,
             '"}',
             ', "TM_load_timestamp": "', TM_load_timestamp,
             '", "load_TM_status":"', load_TM_status,
			  '"}
			]
}
			'
            )
 from customers where load_TM_status <>'insert' order by sequence_id

