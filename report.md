# API Reliability Monitor — SLA Report

> Last updated: **2026-06-07 21:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.17% | 2774.3 | 10206.7 | 1000ms | 266/1030 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.7 | 4595.4 | 1500ms | 4/1030 |
| ❌ | `ipapi_check` | 76.02% | 99.9% | 156.7 | 4507.0 | 2500ms | 1/1030 |
| ❌ | `nasa_apod` | 76.89% | 55.73% | 3020.8 | 10565.8 | 2000ms | 456/1030 |
| ⚠️ | `rest_countries` | 98.54% | 98.25% | 351.9 | 10221.5 | 2500ms | 18/1030 |
| ⚠️ | `open_meteo_weather` | 98.93% | 96.99% | 701.6 | 14877.1 | 2000ms | 31/1030 |
| ✅ | `dog_ceo_random` | 99.51% | 95.92% | 575.0 | 10244.1 | 2500ms | 42/1030 |
| ✅ | `catfact_random` | 99.71% | 99.13% | 268.3 | 10080.2 | 3000ms | 9/1030 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.5 | 253.3 | 1500ms | 0/1030 |
| ✅ | `useless_fact` | 99.81% | 99.61% | 622.6 | 10229.6 | 2500ms | 4/1030 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.0 | 16112.2 | 2000ms | 3/1030 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 222.2 | 3882.8 | 2000ms | 2/1030 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4070.4 | 51.72% |
| `nasa_apod` | 11:00 | 3824.2 | 49.12% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 05:00 | 3766.2 | 62.96% |
| `numbers_trivia` | 05:00 | 3541.5 | 33.33% |
| `nasa_apod` | 12:00 | 3363.9 | 47.83% |
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
