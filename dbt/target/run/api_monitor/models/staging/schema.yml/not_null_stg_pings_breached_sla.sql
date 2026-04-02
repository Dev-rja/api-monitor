
    select
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
  
    
    



select breached_sla
from main."stg_pings"
where breached_sla is null



  
  
      
    ) dbt_internal_test