# API Reliability Monitor — SLA Report

> Last updated: **2026-06-07 10:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.0% | 2791.9 | 10206.7 | 1000ms | 266/1023 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.7 | 4595.4 | 1500ms | 4/1023 |
| ❌ | `ipapi_check` | 75.86% | 99.9% | 156.6 | 4507.0 | 2500ms | 1/1023 |
| ❌ | `nasa_apod` | 77.22% | 56.01% | 2987.1 | 10565.8 | 2000ms | 450/1023 |
| ⚠️ | `rest_countries` | 98.53% | 98.24% | 353.2 | 10221.5 | 2500ms | 18/1023 |
| ⚠️ | `open_meteo_weather` | 98.92% | 96.97% | 702.6 | 14877.1 | 2000ms | 31/1023 |
| ✅ | `dog_ceo_random` | 99.51% | 95.89% | 576.6 | 10244.1 | 2500ms | 42/1023 |
| ✅ | `catfact_random` | 99.71% | 99.12% | 268.8 | 10080.2 | 3000ms | 9/1023 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1023 |
| ✅ | `useless_fact` | 99.8% | 99.61% | 622.8 | 10229.6 | 2500ms | 4/1023 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.4 | 16112.2 | 2000ms | 3/1023 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 222.3 | 3882.8 | 2000ms | 2/1023 |

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
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |
| `numbers_trivia` | 10:00 | 3288.5 | 30.77% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
