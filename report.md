# API Reliability Monitor — SLA Report

> Last updated: **2026-06-03 22:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.05% | 2885.3 | 10206.7 | 1000ms | 266/987 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.0 | 4595.4 | 1500ms | 4/987 |
| ❌ | `ipapi_check` | 76.09% | 99.9% | 156.9 | 4507.0 | 2500ms | 1/987 |
| ❌ | `nasa_apod` | 77.91% | 57.24% | 2911.1 | 10565.8 | 2000ms | 422/987 |
| ⚠️ | `rest_countries` | 98.48% | 98.18% | 359.3 | 10221.5 | 2500ms | 18/987 |
| ⚠️ | `open_meteo_weather` | 98.99% | 96.96% | 703.2 | 14877.1 | 2000ms | 30/987 |
| ✅ | `dog_ceo_random` | 99.49% | 95.74% | 583.8 | 10244.1 | 2500ms | 42/987 |
| ✅ | `catfact_random` | 99.7% | 99.19% | 266.1 | 10080.2 | 3000ms | 8/987 |
| ✅ | `coingecko_bitcoin` | 99.7% | 100.0% | 96.9 | 253.3 | 1500ms | 0/987 |
| ✅ | `useless_fact` | 99.8% | 99.59% | 621.8 | 10229.6 | 2500ms | 4/987 |
| ✅ | `agify_name` | 99.9% | 99.7% | 382.0 | 16112.2 | 2000ms | 3/987 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 223.9 | 3882.8 | 2000ms | 2/987 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3959.8 | 50.88% |
| `nasa_apod` | 11:00 | 3843.9 | 48.21% |
| `numbers_trivia` | 05:00 | 3674.1 | 34.62% |
| `nasa_apod` | 09:00 | 3526.1 | 47.73% |
| `nasa_apod` | 05:00 | 3511.6 | 61.54% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |
| `numbers_trivia` | 07:00 | 3442.2 | 32.26% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
