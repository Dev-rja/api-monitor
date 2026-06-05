# API Reliability Monitor — SLA Report

> Last updated: **2026-06-05 22:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.53% | 2838.2 | 10206.7 | 1000ms | 266/1005 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 125.7 | 4595.4 | 1500ms | 4/1005 |
| ❌ | `ipapi_check` | 75.72% | 99.9% | 156.8 | 4507.0 | 2500ms | 1/1005 |
| ❌ | `nasa_apod` | 77.61% | 56.62% | 2949.9 | 10565.8 | 2000ms | 436/1005 |
| ⚠️ | `rest_countries` | 98.51% | 98.21% | 356.6 | 10221.5 | 2500ms | 18/1005 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.92% | 704.5 | 14877.1 | 2000ms | 31/1005 |
| ✅ | `dog_ceo_random` | 99.5% | 95.82% | 580.3 | 10244.1 | 2500ms | 42/1005 |
| ✅ | `catfact_random` | 99.7% | 99.2% | 264.8 | 10080.2 | 3000ms | 8/1005 |
| ✅ | `coingecko_bitcoin` | 99.7% | 100.0% | 96.9 | 253.3 | 1500ms | 0/1005 |
| ✅ | `useless_fact` | 99.8% | 99.6% | 622.9 | 10229.6 | 2500ms | 4/1005 |
| ✅ | `agify_name` | 99.9% | 99.7% | 381.7 | 16112.2 | 2000ms | 3/1005 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 223.3 | 3882.8 | 2000ms | 2/1005 |

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
