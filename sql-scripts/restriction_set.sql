select
	concat('{ "restriction_sets": [ {"id":"', id, 
	'" ,' , '"restriction_set_definition_id": "', restriction_set_definition_id, 
	'",' , '"restriction_set_definition_version_id": "', restriction_set_definition_version_id ,
	'",	"name": "' , name , '",
'"restrictions": [        {'
          '"restriction_type": "' , restriction_type ,
          '",          "parameters": {
          '  "KEY": "' , restriction_parameters_KEY,
          '" },          "customer_id": "' , restrictions_customer_id ,
          '",          "account_id": "' , restrictions_account_id ,
          '",          "payment_device_id": "' , restrictions_payment_device_id ,
          '",          "effective_timestamp": "' , restrictions_effective_timestamp ,
          '",          "expiry_timestamp": "' , restrictions_expiry_timestamp ,
          '",          "id": "' , restrictions_id ,
          '"}       ],       "description": "' , restriction_desc ,
          '",       "restriction_set_parameters": {         "KEY": "' , restriction_set_parameters_key ,
          '" },      "customer_id": "' , customer_id ,
          '",      "account_id": "' , account_id ,
          '",	"payment_device_id": "' , payment_device_id ,
          '",     "effective_timestamp": "' , effective_timestamp ,
          '",       "expiry_timestamp": "' , expiry_timestamp ,
          '","is_active":' , case when is_active = TRUE then 'true' else 'false' end , ''
	
	'} ] }') as restriction_set_json_output from restriction_set where load_tm_status <>'Success' order by sequence_id