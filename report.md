# API Reliability Monitor — SLA Report

> Last updated: **2026-06-06 20:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.84% | 2806.6 | 10206.7 | 1000ms | 266/1017 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.8 | 4595.4 | 1500ms | 4/1017 |
| ❌ | `ipapi_check` | 75.81% | 99.9% | 156.7 | 4507.0 | 2500ms | 1/1017 |
| ❌ | `nasa_apod` | 77.29% | 56.24% | 2978.5 | 10565.8 | 2000ms | 445/1017 |
| ⚠️ | `rest_countries` | 98.53% | 98.23% | 354.0 | 10221.5 | 2500ms | 18/1017 |
| ⚠️ | `open_meteo_weather` | 98.92% | 96.95% | 702.1 | 14877.1 | 2000ms | 31/1017 |
| ✅ | `dog_ceo_random` | 99.51% | 95.87% | 577.6 | 10244.1 | 2500ms | 42/1017 |
| ✅ | `catfact_random` | 99.71% | 99.21% | 263.8 | 10080.2 | 3000ms | 8/1017 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1017 |
| ✅ | `useless_fact` | 99.8% | 99.61% | 622.3 | 10229.6 | 2500ms | 4/1017 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.3 | 16112.2 | 2000ms | 3/1017 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 222.6 | 3882.8 | 2000ms | 2/1017 |

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
| `numbers_trivia` | 10:00 | 3366.7 | 31.58% |
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
