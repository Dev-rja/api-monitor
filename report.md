# API Reliability Monitor — SLA Report

> Last updated: **2026-06-05 01:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.32% | 2859.1 | 10206.7 | 1000ms | 266/997 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 125.8 | 4595.4 | 1500ms | 4/997 |
| ❌ | `ipapi_check` | 75.83% | 99.9% | 156.9 | 4507.0 | 2500ms | 1/997 |
| ❌ | `nasa_apod` | 77.63% | 56.87% | 2942.0 | 10565.8 | 2000ms | 430/997 |
| ⚠️ | `rest_countries` | 98.5% | 98.19% | 358.0 | 10221.5 | 2500ms | 18/997 |
| ⚠️ | `open_meteo_weather` | 98.9% | 96.99% | 701.8 | 14877.1 | 2000ms | 30/997 |
| ✅ | `dog_ceo_random` | 99.5% | 95.79% | 582.3 | 10244.1 | 2500ms | 42/997 |
| ✅ | `catfact_random` | 99.7% | 99.2% | 265.5 | 10080.2 | 3000ms | 8/997 |
| ✅ | `coingecko_bitcoin` | 99.7% | 100.0% | 96.8 | 253.3 | 1500ms | 0/997 |
| ✅ | `useless_fact` | 99.8% | 99.6% | 622.2 | 10229.6 | 2500ms | 4/997 |
| ✅ | `agify_name` | 99.9% | 99.7% | 382.1 | 16112.2 | 2000ms | 3/997 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 223.4 | 3882.8 | 2000ms | 2/997 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3959.8 | 50.88% |
| `nasa_apod` | 11:00 | 3843.9 | 48.21% |
| `nasa_apod` | 05:00 | 3766.2 | 62.96% |
| `nasa_apod` | 09:00 | 3678.0 | 48.89% |
| `numbers_trivia` | 05:00 | 3541.5 | 33.33% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |
| `numbers_trivia` | 07:00 | 3442.2 | 32.26% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
