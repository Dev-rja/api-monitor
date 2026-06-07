# API Reliability Monitor — SLA Report

> Last updated: **2026-06-07 14:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.05% | 2786.7 | 10206.7 | 1000ms | 266/1025 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.8 | 4595.4 | 1500ms | 4/1025 |
| ❌ | `ipapi_check` | 75.9% | 99.9% | 156.7 | 4507.0 | 2500ms | 1/1025 |
| ❌ | `nasa_apod` | 77.07% | 55.9% | 3001.6 | 10565.8 | 2000ms | 452/1025 |
| ⚠️ | `rest_countries` | 98.54% | 98.24% | 352.8 | 10221.5 | 2500ms | 18/1025 |
| ⚠️ | `open_meteo_weather` | 98.93% | 96.98% | 702.1 | 14877.1 | 2000ms | 31/1025 |
| ✅ | `dog_ceo_random` | 99.51% | 95.9% | 576.1 | 10244.1 | 2500ms | 42/1025 |
| ✅ | `catfact_random` | 99.71% | 99.12% | 268.5 | 10080.2 | 3000ms | 9/1025 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.5 | 253.3 | 1500ms | 0/1025 |
| ✅ | `useless_fact` | 99.8% | 99.61% | 622.7 | 10229.6 | 2500ms | 4/1025 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.1 | 16112.2 | 2000ms | 3/1025 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 222.2 | 3882.8 | 2000ms | 2/1025 |

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
