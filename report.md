# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 18:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.07% | 3915.3 | 10206.7 | 1000ms | 161/436 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 130.0 | 4088.9 | 1500ms | 2/436 |
| ❌ | `nasa_apod` | 61.24% | 36.93% | 4408.3 | 10549.1 | 2000ms | 275/436 |
| ❌ | `ipapi_check` | 93.58% | 100.0% | 158.3 | 353.0 | 2500ms | 0/436 |
| ⚠️ | `open_meteo_weather` | 98.17% | 96.79% | 747.1 | 14877.1 | 2000ms | 14/436 |
| ⚠️ | `dog_ceo_random` | 99.31% | 90.37% | 854.7 | 10244.1 | 2500ms | 42/436 |
| ✅ | `catfact_random` | 99.31% | 99.31% | 271.8 | 10080.2 | 3000ms | 3/436 |
| ✅ | `useless_fact` | 99.54% | 99.08% | 584.9 | 10229.6 | 2500ms | 4/436 |
| ✅ | `rest_countries` | 99.54% | 98.85% | 280.0 | 10052.7 | 2500ms | 5/436 |
| ✅ | `agify_name` | 100.0% | 99.77% | 373.6 | 3237.1 | 2000ms | 1/436 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.9 | 2314.9 | 2000ms | 1/436 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/436 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 6132.0 | 73.08% |
| `nasa_apod` | 18:00 | 5700.0 | 84.21% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4979.2 | 61.54% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
