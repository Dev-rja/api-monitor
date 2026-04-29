# API Reliability Monitor — SLA Report

> Last updated: **2026-04-29 23:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.06% | 4886.2 | 10206.7 | 1000ms | 261/556 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 124.1 | 4088.9 | 1500ms | 2/556 |
| ❌ | `nasa_apod` | 66.91% | 43.35% | 3932.4 | 10549.1 | 2000ms | 315/556 |
| ❌ | `ipapi_check` | 87.41% | 100.0% | 156.3 | 353.0 | 2500ms | 0/556 |
| ⚠️ | `rest_countries` | 98.38% | 98.2% | 353.0 | 10221.5 | 2500ms | 10/556 |
| ⚠️ | `open_meteo_weather` | 98.56% | 97.12% | 725.2 | 14877.1 | 2000ms | 16/556 |
| ⚠️ | `dog_ceo_random` | 99.46% | 92.45% | 752.1 | 10244.1 | 2500ms | 42/556 |
| ✅ | `catfact_random` | 99.46% | 99.46% | 253.6 | 10080.2 | 3000ms | 3/556 |
| ✅ | `useless_fact` | 99.64% | 99.28% | 583.4 | 10229.6 | 2500ms | 4/556 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 98.9 | 252.0 | 1500ms | 0/556 |
| ✅ | `agify_name` | 100.0% | 99.82% | 370.0 | 3237.1 | 2000ms | 1/556 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 240.2 | 3882.8 | 2000ms | 2/556 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 01:00 | 6379.1 | 62.5% |
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 07:00 | 5753.1 | 55.56% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 12:00 | 5601.9 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5367.0 | 66.67% |
| `numbers_trivia` | 05:00 | 5217.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
