
    select
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
  select *
from main."stg_pings"
where is_success not in (0, 1)
   or is_failure not in (0, 1)
   or breached_sla not in (0, 1)
  
  
      
    ) dbt_internal_test