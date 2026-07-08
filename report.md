# API Reliability Monitor — SLA Report

> Last updated: **2026-07-08 11:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.0% | 2196.5 | 10206.7 | 1000ms | 267/1335 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.5 | 4595.4 | 1500ms | 4/1335 |
| ❌ | `nasa_apod` | 74.46% | 49.96% | 3347.6 | 11152.5 | 2000ms | 668/1335 |
| ❌ | `ipapi_check` | 76.25% | 99.93% | 154.9 | 4507.0 | 2500ms | 1/1335 |
| ❌ | `dog_ceo_random` | 94.76% | 96.85% | 529.5 | 10244.1 | 2500ms | 42/1335 |
| ⚠️ | `open_meteo_weather` | 98.58% | 96.93% | 732.8 | 14877.1 | 2000ms | 41/1335 |
| ⚠️ | `rest_countries` | 98.88% | 98.58% | 317.9 | 10221.5 | 2500ms | 19/1335 |
| ✅ | `useless_fact` | 99.63% | 99.7% | 633.1 | 10229.6 | 2500ms | 4/1335 |
| ✅ | `catfact_random` | 99.78% | 99.33% | 255.7 | 10080.2 | 3000ms | 9/1335 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 98.0 | 4328.4 | 1500ms | 1/1335 |
| ✅ | `agify_name` | 99.93% | 99.7% | 383.9 | 16112.2 | 2000ms | 4/1335 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 212.4 | 3882.8 | 2000ms | 2/1335 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4792.7 | 80.95% |
| `nasa_apod` | 05:00 | 4266.1 | 62.16% |
| `nasa_apod` | 09:00 | 4153.2 | 53.45% |
| `nasa_apod` | 01:00 | 4125.5 | 58.97% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `numbers_trivia` | 03:00 | 4003.6 | 38.1% |
| `nasa_apod` | 18:00 | 3843.5 | 54.29% |
| `nasa_apod` | 11:00 | 3627.0 | 53.42% |
| `nasa_apod` | 20:00 | 3574.9 | 50.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
