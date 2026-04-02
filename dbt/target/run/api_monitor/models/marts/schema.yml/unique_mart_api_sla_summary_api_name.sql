
    select
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
  
    
    

select
    api_name as unique_field,
    count(*) as n_records

from main."mart_api_sla_summary"
where api_name is not null
group by api_name
having count(*) > 1



  
  
      
    ) dbt_internal_test