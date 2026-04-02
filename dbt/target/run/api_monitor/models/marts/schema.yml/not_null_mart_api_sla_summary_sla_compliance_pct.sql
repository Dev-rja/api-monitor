
    select
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
  
    
    



select sla_compliance_pct
from main."mart_api_sla_summary"
where sla_compliance_pct is null



  
  
      
    ) dbt_internal_test