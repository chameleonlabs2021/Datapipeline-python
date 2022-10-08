truncate table Payment_Device_Link;
insert into Payment_Device_Link (id ,
                                   token ,
                                     payment_device_id ,
                                    account_id ,
                                    status ,
                                    start_timestamp ,
                                    end_timestamp ,
                                    load_TM_status )
                                    select "id" ,
                                            "token" ,
                                             "payment_device_id" ,
                                              "account_id" ,
                                               "status" ,
                                                "start_timestamp" ,
                                                "end_timestamp" ,
                                                  "load_TM_status"
                                                  from product_details;
commit;