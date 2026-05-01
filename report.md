# API Reliability Monitor — SLA Report

> Last updated: **2026-05-01 18:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.15% | 4674.2 | 10206.7 | 1000ms | 261/582 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 123.0 | 4088.9 | 1500ms | 2/582 |
| ❌ | `nasa_apod` | 68.38% | 45.7% | 3781.1 | 10549.1 | 2000ms | 316/582 |
| ❌ | `ipapi_check` | 87.46% | 100.0% | 156.1 | 353.0 | 2500ms | 0/582 |
| ⚠️ | `rest_countries` | 98.45% | 98.28% | 347.0 | 10221.5 | 2500ms | 10/582 |
| ⚠️ | `open_meteo_weather` | 98.63% | 97.25% | 718.1 | 14877.1 | 2000ms | 16/582 |
| ⚠️ | `dog_ceo_random` | 99.48% | 92.78% | 736.5 | 10244.1 | 2500ms | 42/582 |
| ✅ | `catfact_random` | 99.48% | 99.48% | 250.1 | 10080.2 | 3000ms | 3/582 |
| ✅ | `useless_fact` | 99.66% | 99.31% | 585.1 | 10229.6 | 2500ms | 4/582 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 98.9 | 252.0 | 1500ms | 0/582 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.6 | 3237.1 | 2000ms | 1/582 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 237.8 | 3882.8 | 2000ms | 2/582 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5222.7 | 64.71% |
| `numbers_trivia` | 07:00 | 5197.7 | 50.0% |
| `numbers_trivia` | 18:00 | 5196.2 | 50.0% |
| `numbers_trivia` | 10:00 | 5173.5 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `numbers_trivia` | 05:00 | 4949.4 | 47.37% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
