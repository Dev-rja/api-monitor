
    select
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
  
    
    



select api_name
from main."mart_api_sla_summary"
where api_name is null



  
  
      
    ) dbt_internal_test