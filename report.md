# API Reliability Monitor — SLA Report

> Last updated: **2026-06-03 17:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.99% | 2890.7 | 10206.7 | 1000ms | 266/985 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.0 | 4595.4 | 1500ms | 4/985 |
| ❌ | `ipapi_check` | 76.04% | 99.9% | 157.0 | 4507.0 | 2500ms | 1/985 |
| ❌ | `nasa_apod` | 78.07% | 57.36% | 2896.2 | 10565.8 | 2000ms | 420/985 |
| ⚠️ | `rest_countries` | 98.48% | 98.17% | 359.5 | 10221.5 | 2500ms | 18/985 |
| ⚠️ | `open_meteo_weather` | 98.98% | 96.95% | 703.5 | 14877.1 | 2000ms | 30/985 |
| ✅ | `dog_ceo_random` | 99.49% | 95.74% | 584.3 | 10244.1 | 2500ms | 42/985 |
| ✅ | `catfact_random` | 99.7% | 99.19% | 266.4 | 10080.2 | 3000ms | 8/985 |
| ✅ | `coingecko_bitcoin` | 99.7% | 100.0% | 97.0 | 253.3 | 1500ms | 0/985 |
| ✅ | `useless_fact` | 99.8% | 99.59% | 621.6 | 10229.6 | 2500ms | 4/985 |
| ✅ | `agify_name` | 99.9% | 99.7% | 381.9 | 16112.2 | 2000ms | 3/985 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 224.0 | 3882.8 | 2000ms | 2/985 |

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
