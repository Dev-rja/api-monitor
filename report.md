# API Reliability Monitor — SLA Report

> Last updated: **2026-04-29 22:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 52.97% | 4894.8 | 10206.7 | 1000ms | 261/555 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 124.3 | 4088.9 | 1500ms | 2/555 |
| ❌ | `nasa_apod` | 66.85% | 43.24% | 3939.1 | 10549.1 | 2000ms | 315/555 |
| ❌ | `ipapi_check` | 87.39% | 100.0% | 156.4 | 353.0 | 2500ms | 0/555 |
| ⚠️ | `rest_countries` | 98.38% | 98.2% | 353.1 | 10221.5 | 2500ms | 10/555 |
| ⚠️ | `open_meteo_weather` | 98.56% | 97.12% | 725.3 | 14877.1 | 2000ms | 16/555 |
| ⚠️ | `dog_ceo_random` | 99.46% | 92.43% | 752.7 | 10244.1 | 2500ms | 42/555 |
| ✅ | `catfact_random` | 99.46% | 99.46% | 253.9 | 10080.2 | 3000ms | 3/555 |
| ✅ | `useless_fact` | 99.64% | 99.28% | 582.9 | 10229.6 | 2500ms | 4/555 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 99.0 | 252.0 | 1500ms | 0/555 |
| ✅ | `agify_name` | 100.0% | 99.82% | 369.8 | 3237.1 | 2000ms | 1/555 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 240.3 | 3882.8 | 2000ms | 2/555 |

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
