truncate table flags;
insert into flags (id ,
                  flag_definition_id ,
                  description ,
                  creation_timestamp ,
                  effective_timestamp ,
                  expiry_timestamp  ,
                  is_active ,
                  customer_id ,
                  load_TM_status )

                  select national_id,customer_number,'description','01/01/2999','01/01/2999','01/01/2999',account_status,customer_number,'Inserted'
                  from product_details;

                  commit;