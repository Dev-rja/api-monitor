
    
    

select
    api_name as unique_field,
    count(*) as n_records

from main."mart_api_sla_summary"
where api_name is not null
group by api_name
having count(*) > 1


