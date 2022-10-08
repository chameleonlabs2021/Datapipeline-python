select
	concat('{
  "payment_device_links": [
    {
	  "id":"', id, 
	'" ,' , '"token": "', token, 
	'",' , '"payment_device_id": "', payment_device_id ,'",
"account_id": "' , account_id ,'",
"status": "' , status  ,'",
"start_timestamp": "' , start_timestamp  ,'",
"end_timestamp": "' , end_timestamp  ,'"'
		'
'	}'
'  ] '
'}') as payment_device_link_json_output from payment_device_link where load_tm_status <>'Success' limit 10;