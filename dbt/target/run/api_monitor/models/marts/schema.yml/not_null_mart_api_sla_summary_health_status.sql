
    select
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
  
    
    



select health_status
from main."mart_api_sla_summary"
where health_status is null



  
  
      
    ) dbt_internal_test