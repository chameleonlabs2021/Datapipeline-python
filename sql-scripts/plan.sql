select concat ('{ "id" : "', id,
'", "supervisor_contract_version_id" : "', supervisor_contract_version_id,
'", "create_timestamp" : "', create_timestamp, 
'", "status" : "', status,
'", "opening_timestamp" :"', opening_timestamp,
'", "activation_completed_timestamp" :"', activation_completed_timestamp,
'", "closing_timestamp" : "', closing_timestamp, 
'", "closure_completed_timestamp" : "', closure_completed_timestamp,
 '", "details":{'
		'"key1":"', details_KEY,
		'"} }'
)
from plan where load_tm_status <>'Success' order by sequence_id