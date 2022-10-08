select
	concat('{ "posting_instruction_batches": [ {"id":"', id, '" ,' , '"create_request_id": "', create_request_id, ' ",' , '"client_id": "', client_id , '",' , '"posting_instructions": [
        {
          "posting_instructions_0_id": "' , posting_instructions_0_id , '" ,' ,
          '"client_transaction_id": "' , posting_instructions_0_client_transaction_id , '" ,' ,
          '"pics": ["' , posting_instructions_0_pics_0 , '"] ,' 
          '"instruction_details": {'
          '  "KEY": "' , posting_instructions_0_instruction_details_KEY , '"},
          
          
          "committed_postings": [
            {
              "credit": "' , posting_instructions_0_committed_postings_0_credit , '" ,' 
          '"amount":"' , posting_instructions_0_committed_postings_0_amount , '" ,' 
           '"denomination":"', posting_instructions_0_committed_postings_0_denomination , '" ,' 
              '"account_id":"' , posting_instructions_0_account_violations_0_account_id , '" ,' 
              '"account_address":"' , posting_instructions_0_committed_postings_0_account_address , '" ,' 
             '"asset":"' , posting_instructions_0_committed_postings_0_asset , '" ,' 
            '"phase":"' , posting_instructions_0_committed_postings_0_phase , '"  
         }
       ] ,
          "posting_violations": [
            {
              "type":"' , posting_instructions_0_posting_violations_0_type , '"
              
              }
          ],
          "account_violations": [
            {
              "account_id":"' , posting_instructions_0_account_violations_0_account_id , '" ,'
           '"payment_device_token":"' , posting_instructions_0_account_violations_0_payment_device_token, '" ,'
            '"type": "' , posting_instructions_0_account_violations_0_type , '"
}          ],
          "restriction_violations": [
            {
              "restriction_set_id": "' , posting_instructions_0_restriction_violations_0_restriction_set_id, '" ,'
            '  "account_id":"' , posting_instructions_0_restriction_violations_0_account_id, '" ,'
           '   "payment_device_id":"' , posting_instructions_0_restriction_violations_0_payment_device_id, '" ,'
            '  "customer_id":"' , posting_instructions_0_restriction_violations_0_customer_id, '" ,'
             ' "requires_review":"' , posting_instructions_0_restriction_violations_0_requires_review , '"
}
          ],
          "contract_violations": [
            {
              "account_id": "', posting_instructions_0_contract_violations_0_account_id, '" ,'
             ' "type": "', posting_instructions_0_contract_violations_0_type, '" ,'
             ' "reason": "' , posting_instructions_0_contract_violations_0_reason, '"
           }
          ],
          "override": {
            "restrictions": {
              "all": "' , posting_instructions_0_override_restrictions_all , '" ,'
              '  "restriction_set_ids": ["' ,
               posting_instructions_0_override_restrictions_restriction_set_id , '"

]
            }
          },
          "transaction_code": {
            "domain":"' , posting_instructions_0_transaction_code_domain , '" ,'
            '"family": "' , posting_instructions_0_transaction_code_family, '" ,'
            '"subfamily":"' , posting_instructions_0_transaction_code_subfamily , '"
},
       "outbound_authorisation": {
       "amount": "' , posting_instructions_0_outbound_authorisation_amount , '",'
           '"denomination": "' , posting_instructions_0_outbound_authorisation_denomination, '",
	"target_account": {
	"payment_device_token": "' , posting_instructions_0_outbound_authorisation_denomination , '"
},
      "internal_account_id":"' , posting_instructions_0_outbound_authorisation_internal_account_ , '",'
       '"advice": "' , posting_instructions_0_outbound_authorisation_advice, '",'
       '"target_account_id": "' , posting_instructions_0_outbound_authorisation_target_account_id , '"
}
      }
      ],
      "batch_details": {
        "KEY": "' , batch_details_key , '"
},
    "value_timestamp":"' , value_timestamp, '",'
    '"status":"' , status , '",
      "error": {
        "type": "' , error_type , '",'
        ' "message": "' , error_message , '"
 },
     "insertion_timestamp":"' , insertion_timestamp , '",'
     '"dry_run": "' , dry_run , '"}
  ]
}'
       )
from
	posting_instruction_batch p where load_tm_status <>'Success' limit 10;