select *
from main."stg_pings"
where is_success not in (0, 1)
   or is_failure not in (0, 1)
   or breached_sla not in (0, 1)