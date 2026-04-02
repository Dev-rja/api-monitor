{{
    config(
        materialized='view'
    )
}}

with source as (

    select * from raw_pings

),

cleaned as (

    select
        id                                          as ping_id,
        api_name,
        url,

        datetime(checked_at)                        as checked_at,
        cast(strftime('%H', checked_at) as integer) as hour_of_day,
        strftime('%Y-%m-%d', checked_at)            as check_date,

        status_code,
        cast(response_ms as real)                   as response_ms,
        cast(sla_ms as real)                        as sla_ms,

        case when cast(is_success as text) in ('1','true','True') then 1 else 0 end  as is_success,
        case when cast(is_success as text) in ('1','true','True') then 0 else 1 end  as is_failure,
        case when response_ms > sla_ms then 1 else 0 end                             as breached_sla,

        round(response_ms - sla_ms, 2)             as sla_delta_ms,

        error_message,
        case
            when error_message = 'timeout'             then 'timeout'
            when error_message like 'request_error:%'  then 'network_error'
            when cast(is_success as text) not in ('1','true','True')
             and error_message is null               then 'wrong_status'
            else null
        end                                         as failure_reason

    from source

)
select * from cleaned