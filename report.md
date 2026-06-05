# API Reliability Monitor — SLA Report

> Last updated: **2026-06-05 20:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.48% | 2843.4 | 10206.7 | 1000ms | 266/1003 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 125.7 | 4595.4 | 1500ms | 4/1003 |
| ❌ | `ipapi_check` | 75.77% | 99.9% | 156.8 | 4507.0 | 2500ms | 1/1003 |
| ❌ | `nasa_apod` | 77.67% | 56.73% | 2943.2 | 10565.8 | 2000ms | 434/1003 |
| ⚠️ | `rest_countries` | 98.5% | 98.21% | 356.9 | 10221.5 | 2500ms | 18/1003 |
| ⚠️ | `open_meteo_weather` | 98.9% | 97.01% | 700.8 | 14877.1 | 2000ms | 30/1003 |
| ✅ | `dog_ceo_random` | 99.5% | 95.81% | 580.5 | 10244.1 | 2500ms | 42/1003 |
| ✅ | `catfact_random` | 99.7% | 99.2% | 264.8 | 10080.2 | 3000ms | 8/1003 |
| ✅ | `coingecko_bitcoin` | 99.7% | 100.0% | 96.9 | 253.3 | 1500ms | 0/1003 |
| ✅ | `useless_fact` | 99.8% | 99.6% | 622.7 | 10229.6 | 2500ms | 4/1003 |
| ✅ | `agify_name` | 99.9% | 99.7% | 381.6 | 16112.2 | 2000ms | 3/1003 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 223.3 | 3882.8 | 2000ms | 2/1003 |

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
| `numbers_trivia` | 07:00 | 3442.2 | 32.26% |
| `numbers_trivia` | 10:00 | 3366.7 | 31.58% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
