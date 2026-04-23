# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 19:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.84% | 4133.9 | 10206.7 | 1000ms | 177/452 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 129.1 | 4088.9 | 1500ms | 2/452 |
| ❌ | `nasa_apod` | 61.5% | 36.73% | 4412.1 | 10549.1 | 2000ms | 286/452 |
| ❌ | `ipapi_check` | 93.58% | 100.0% | 158.3 | 353.0 | 2500ms | 0/452 |
| ⚠️ | `open_meteo_weather` | 98.23% | 96.9% | 740.7 | 14877.1 | 2000ms | 14/452 |
| ⚠️ | `rest_countries` | 98.45% | 98.01% | 362.8 | 10221.5 | 2500ms | 9/452 |
| ⚠️ | `dog_ceo_random` | 99.34% | 90.71% | 838.9 | 10244.1 | 2500ms | 42/452 |
| ✅ | `catfact_random` | 99.34% | 99.34% | 268.1 | 10080.2 | 3000ms | 3/452 |
| ✅ | `useless_fact` | 99.56% | 99.12% | 584.0 | 10229.6 | 2500ms | 4/452 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.0 | 3237.1 | 2000ms | 1/452 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 233.3 | 2314.9 | 2000ms | 1/452 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/452 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6006.5 | 74.07% |
| `nasa_apod` | 18:00 | 5937.8 | 85.0% |
| `nasa_apod` | 03:00 | 5851.5 | 84.62% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5177.6 | 62.96% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 10:00 | 4947.7 | 47.62% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 21:00 | 4923.2 | 56.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
