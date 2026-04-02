
    
    

select
    ping_id as unique_field,
    count(*) as n_records

from main."stg_pings"
where ping_id is not null
group by ping_id
having count(*) > 1


