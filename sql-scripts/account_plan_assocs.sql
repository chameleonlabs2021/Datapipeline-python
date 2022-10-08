select concat('{ "account_plan_assocs":[ { "id" : "',id,
'", "account_id" : "', account_id,
'", "plan_id": "', plan_id,
'", "create_timestamp": "', create_timestamp,
'", "start_timestamp": "', start_timestamp,
'", "end_timestamp": "', end_timestamp,
'", "status": "', status, '"
}
]
}'
)
from account_plan_assocs where load_tm_status <>'Success' limit 10;