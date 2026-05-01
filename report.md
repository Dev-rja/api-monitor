# API Reliability Monitor — SLA Report

> Last updated: **2026-05-01 17:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.08% | 4682.0 | 10206.7 | 1000ms | 261/581 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 122.8 | 4088.9 | 1500ms | 2/581 |
| ❌ | `nasa_apod` | 68.33% | 45.61% | 3786.8 | 10549.1 | 2000ms | 316/581 |
| ❌ | `ipapi_check` | 87.44% | 100.0% | 156.1 | 353.0 | 2500ms | 0/581 |
| ⚠️ | `rest_countries` | 98.45% | 98.28% | 347.5 | 10221.5 | 2500ms | 10/581 |
| ⚠️ | `open_meteo_weather` | 98.62% | 97.25% | 718.6 | 14877.1 | 2000ms | 16/581 |
| ⚠️ | `dog_ceo_random` | 99.48% | 92.77% | 737.5 | 10244.1 | 2500ms | 42/581 |
| ✅ | `catfact_random` | 99.48% | 99.48% | 250.4 | 10080.2 | 3000ms | 3/581 |
| ✅ | `useless_fact` | 99.66% | 99.31% | 585.2 | 10229.6 | 2500ms | 4/581 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 99.0 | 252.0 | 1500ms | 0/581 |
| ✅ | `agify_name` | 100.0% | 99.83% | 370.0 | 3237.1 | 2000ms | 1/581 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 237.8 | 3882.8 | 2000ms | 2/581 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 18:00 | 5398.4 | 52.0% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5222.7 | 64.71% |
| `numbers_trivia` | 07:00 | 5197.7 | 50.0% |
| `numbers_trivia` | 10:00 | 5173.5 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `numbers_trivia` | 05:00 | 4949.4 | 47.37% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
