# API Reliability Monitor — SLA Report

> Last updated: **2026-08-02 16:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.25% | 2323.3 | 10420.1 | 1000ms | 368/1692 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 129.3 | 5052.3 | 1500ms | 5/1692 |
| ❌ | `ipapi_check` | 68.2% | 99.94% | 149.6 | 4507.0 | 2500ms | 1/1692 |
| ❌ | `nasa_apod` | 78.19% | 55.2% | 2943.8 | 11152.5 | 2000ms | 758/1692 |
| ⚠️ | `dog_ceo_random` | 95.51% | 96.63% | 542.3 | 10244.1 | 2500ms | 57/1692 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.58% | 699.8 | 14877.1 | 2000ms | 41/1692 |
| ✅ | `rest_countries` | 99.11% | 98.76% | 295.0 | 10221.5 | 2500ms | 21/1692 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.9 | 10229.6 | 2500ms | 5/1692 |
| ✅ | `catfact_random` | 99.82% | 99.47% | 258.1 | 10080.2 | 3000ms | 9/1692 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1692 |
| ✅ | `agify_name` | 99.88% | 99.76% | 389.4 | 16112.2 | 2000ms | 4/1692 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 199.1 | 3882.8 | 2000ms | 2/1692 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 4181.7 | 41.94% |
| `nasa_apod` | 03:00 | 3796.4 | 61.29% |
| `nasa_apod` | 09:00 | 3718.2 | 48.57% |
| `nasa_apod` | 17:00 | 3549.1 | 48.84% |
| `nasa_apod` | 12:00 | 3346.7 | 50.68% |
| `nasa_apod` | 01:00 | 3257.3 | 46.15% |
| `nasa_apod` | 11:00 | 3213.9 | 47.31% |
| `nasa_apod` | 18:00 | 3183.4 | 46.24% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
