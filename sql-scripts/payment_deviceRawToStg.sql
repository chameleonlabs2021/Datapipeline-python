truncate table payment_device;
insert into payment_device(id ,
                              token  ,
                              payment_device_id ,
                              account_id ,
                              status ,
                              start_timestamp ,
                              end_timestamp ,
                              TM_load_timestamp ,
                              load_TM_status )
                              select "id" ,
                                 "token"  ,
                                 "payment_device_id" ,
                                  account_number ,
                                  account_status ,
                                  "01/01/2999" ,
                                  "01/01/2999",
                                  "Inserted"
                                  from product_details;
                                  commit;
                                                                                                                                      load_TM_statusfrom