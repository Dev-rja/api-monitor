# API Reliability Monitor — SLA Report

> Last updated: **2026-06-07 23:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.22% | 2769.6 | 10206.7 | 1000ms | 266/1032 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.7 | 4595.4 | 1500ms | 4/1032 |
| ❌ | `ipapi_check` | 76.07% | 99.9% | 156.6 | 4507.0 | 2500ms | 1/1032 |
| ❌ | `nasa_apod` | 76.84% | 55.72% | 3025.1 | 10565.8 | 2000ms | 457/1032 |
| ⚠️ | `rest_countries` | 98.55% | 98.26% | 351.8 | 10221.5 | 2500ms | 18/1032 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.0% | 701.5 | 14877.1 | 2000ms | 31/1032 |
| ✅ | `dog_ceo_random` | 99.52% | 95.93% | 574.7 | 10244.1 | 2500ms | 42/1032 |
| ✅ | `catfact_random` | 99.71% | 99.13% | 268.1 | 10080.2 | 3000ms | 9/1032 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.5 | 253.3 | 1500ms | 0/1032 |
| ✅ | `useless_fact` | 99.81% | 99.61% | 622.9 | 10229.6 | 2500ms | 4/1032 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.1 | 16112.2 | 2000ms | 3/1032 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 222.0 | 3882.8 | 2000ms | 2/1032 |

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
