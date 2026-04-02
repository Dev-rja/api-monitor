

with pings as (

    select * from main."stg_pings"

),

hourly as (

    select
        api_name,
        hour_of_day,

        count(*)                                        as total_pings,
        sum(is_success)                                 as successful_pings,
        sum(breached_sla)                               as sla_breaches,

        round(avg(response_ms), 1)                      as avg_response_ms,
        round(min(response_ms), 1)                      as min_response_ms,
        round(max(response_ms), 1)                      as max_response_ms,

        round(
            100.0 * sum(is_success) / count(*), 2
        )                                               as uptime_pct,

        round(
            100.0 * sum(breached_sla) / count(*), 2
        )                                               as sla_breach_pct,

        max(sla_ms)                                     as sla_threshold_ms

    from pings
    group by api_name, hour_of_day

),

final as (

    select
        *,

        -- readable hour label e.g. "02:00", "14:00"
        case
            when hour_of_day < 10 then '0' || hour_of_day || ':00'
            else hour_of_day || ':00'
        end                                             as hour_label,

        -- flag hours where this API is consistently slow
        case
            when avg_response_ms > sla_threshold_ms then 1
            else 0
        end                                             as is_slow_hour

    from hourly

)

select * from final
order by api_name, hour_of_day