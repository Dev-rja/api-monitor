
    select
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
  
    
    



select hour_of_day
from main."mart_hourly_trends"
where hour_of_day is null



  
  
      
    ) dbt_internal_test