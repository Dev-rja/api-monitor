# API Reliability Monitor — SLA Report

> Last updated: **2026-06-07 12:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.02% | 2789.3 | 10206.7 | 1000ms | 266/1024 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.7 | 4595.4 | 1500ms | 4/1024 |
| ❌ | `ipapi_check` | 75.88% | 99.9% | 156.7 | 4507.0 | 2500ms | 1/1024 |
| ❌ | `nasa_apod` | 77.15% | 55.96% | 2994.4 | 10565.8 | 2000ms | 451/1024 |
| ⚠️ | `rest_countries` | 98.54% | 98.24% | 353.0 | 10221.5 | 2500ms | 18/1024 |
| ⚠️ | `open_meteo_weather` | 98.93% | 96.97% | 702.3 | 14877.1 | 2000ms | 31/1024 |
| ✅ | `dog_ceo_random` | 99.51% | 95.9% | 576.3 | 10244.1 | 2500ms | 42/1024 |
| ✅ | `catfact_random` | 99.71% | 99.12% | 268.6 | 10080.2 | 3000ms | 9/1024 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1024 |
| ✅ | `useless_fact` | 99.8% | 99.61% | 622.8 | 10229.6 | 2500ms | 4/1024 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.3 | 16112.2 | 2000ms | 3/1024 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 222.2 | 3882.8 | 2000ms | 2/1024 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3959.8 | 50.88% |
| `nasa_apod` | 11:00 | 3824.2 | 49.12% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 05:00 | 3766.2 | 62.96% |
| `numbers_trivia` | 05:00 | 3541.5 | 33.33% |
| `nasa_apod` | 12:00 | 3363.9 | 47.83% |
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
