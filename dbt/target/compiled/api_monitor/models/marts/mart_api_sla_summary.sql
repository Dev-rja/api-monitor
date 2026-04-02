

with pings as (

    select * from main."stg_pings"

),

aggregated as (

    select
        api_name,
        url,

        -- volume
        count(*)                                        as total_pings,
        sum(is_success)                                 as successful_pings,
        sum(is_failure)                                 as failed_pings,
        sum(breached_sla)                               as sla_breaches,

        -- uptime %
        round(
            100.0 * sum(is_success) / count(*), 2
        )                                               as uptime_pct,

        -- SLA compliance %
        round(
            100.0 * (count(*) - sum(breached_sla)) / count(*), 2
        )                                               as sla_compliance_pct,

        -- response time stats
        round(avg(response_ms), 1)                      as avg_response_ms,
        round(min(response_ms), 1)                      as min_response_ms,
        round(max(response_ms), 1)                      as max_response_ms,

        -- p95 approximation (SQLite has no native percentile)
        round(avg(response_ms) + (2.0 * (
            select avg((p.response_ms - sub.mean) * (p.response_ms - sub.mean))
            from pings p,
            (select api_name as an, avg(response_ms) as mean from pings group by api_name) sub
            where p.api_name = pings.api_name and sub.an = pings.api_name
        )), 1)                                          as p95_response_ms_approx,

        -- SLA threshold (same for all rows per api)
        max(sla_ms)                                     as sla_threshold_ms,

        -- failure breakdown
        sum(case when failure_reason = 'timeout'       then 1 else 0 end) as timeout_count,
        sum(case when failure_reason = 'network_error' then 1 else 0 end) as network_error_count,
        sum(case when failure_reason = 'wrong_status'  then 1 else 0 end) as wrong_status_count,

        -- window
        min(checked_at)                                 as first_seen,
        max(checked_at)                                 as last_seen

    from pings
    group by api_name, url

),

final as (

    select
        *,

        -- health label for the README report card
        case
            when uptime_pct >= 99 and sla_compliance_pct >= 95 then 'healthy'
            when uptime_pct >= 95 and sla_compliance_pct >= 80 then 'degraded'
            else 'unhealthy'
        end                                             as health_status

    from aggregated

)

select * from final
order by uptime_pct asc, avg_response_ms desc