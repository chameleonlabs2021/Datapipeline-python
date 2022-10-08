select concat('{ "flags":[ { "id" : "',id,
'", "flag_definition_id" : "', flag_definition_id,
'", "description": "', description,
'", "creation_timestamp": "', creation_timestamp,
'", "effective_timestamp": "', effective_timestamp,
'", "expiry_timestamp": "',expiry_timestamp,
'", "is_active": "', is_active,
'", "customer_id": "', customer_id, '"} ] }'
)
from flags where load_tm_status <>'Success' order by sequence_id