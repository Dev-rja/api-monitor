# API Reliability Monitor — SLA Report

> Last updated: **2026-05-01 11:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.69% | 4720.5 | 10206.7 | 1000ms | 261/576 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 122.9 | 4088.9 | 1500ms | 2/576 |
| ❌ | `nasa_apod` | 68.06% | 45.14% | 3816.3 | 10549.1 | 2000ms | 316/576 |
| ❌ | `ipapi_check` | 87.5% | 100.0% | 156.2 | 353.0 | 2500ms | 0/576 |
| ⚠️ | `rest_countries` | 98.44% | 98.26% | 348.4 | 10221.5 | 2500ms | 10/576 |
| ⚠️ | `open_meteo_weather` | 98.61% | 97.22% | 719.7 | 14877.1 | 2000ms | 16/576 |
| ⚠️ | `dog_ceo_random` | 99.48% | 92.71% | 740.1 | 10244.1 | 2500ms | 42/576 |
| ✅ | `catfact_random` | 99.48% | 99.48% | 251.0 | 10080.2 | 3000ms | 3/576 |
| ✅ | `useless_fact` | 99.65% | 99.31% | 585.2 | 10229.6 | 2500ms | 4/576 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 99.0 | 252.0 | 1500ms | 0/576 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.9 | 3237.1 | 2000ms | 1/576 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 238.4 | 3882.8 | 2000ms | 2/576 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 18:00 | 5398.4 | 52.0% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5367.0 | 66.67% |
| `numbers_trivia` | 07:00 | 5197.7 | 50.0% |
| `numbers_trivia` | 10:00 | 5173.5 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `numbers_trivia` | 14:00 | 5027.1 | 48.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
