select concat('{     "accounts": [ '
'     {       '
' "id": "',id,
'", "name": "',name,
'", "product_id": "', product_id,
'", "product_version_id": "', product_version_id,
'", "permitted_denominations":[  "',
           permitted_denominations_0,
            '" ], '
'  "status": "',status,
'", "opening_timestamp": "',opening_timestamp,
'", "closing_timestamp": "',closing_timestamp,
'", "stakeholder_ids":["',
			stakeholder_ids_0,
			'"],'
' "instance_param_vals":{'
			'"key1":"', instance_param_vals_KEY,
			'"}, '
' "derived_instance_param_vals":{'
			'"key1":"', derived_instance_param_vals_KEY,
			'"}, '
' "details":{'
			'"key1":"', details_KEY,
			'"}, '
' "accounting":{'
			'"tside":"', accounting_tside,
			'"}'
			  '}
			],
"previous_page_token": "NiFDMjU",
  "next_page_token": "NiFDMjU"

}			'
)
from accounts where load_tm_status <>'Success' order by sequence_id
