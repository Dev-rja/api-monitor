# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 20:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.61% | 4839.5 | 10206.7 | 1000ms | 238/513 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.9 | 4088.9 | 1500ms | 2/513 |
| ❌ | `nasa_apod` | 64.33% | 39.96% | 4179.5 | 10549.1 | 2000ms | 308/513 |
| ❌ | `ipapi_check` | 88.89% | 100.0% | 156.9 | 353.0 | 2500ms | 0/513 |
| ⚠️ | `open_meteo_weather` | 98.44% | 97.08% | 730.1 | 14877.1 | 2000ms | 15/513 |
| ⚠️ | `rest_countries` | 98.64% | 98.25% | 345.4 | 10221.5 | 2500ms | 9/513 |
| ⚠️ | `dog_ceo_random` | 99.42% | 91.81% | 783.9 | 10244.1 | 2500ms | 42/513 |
| ✅ | `catfact_random` | 99.42% | 99.42% | 259.4 | 10080.2 | 3000ms | 3/513 |
| ✅ | `useless_fact` | 99.61% | 99.22% | 579.5 | 10229.6 | 2500ms | 4/513 |
| ✅ | `coingecko_bitcoin` | 99.81% | 100.0% | 99.7 | 252.0 | 1500ms | 0/513 |
| ✅ | `agify_name` | 100.0% | 99.81% | 371.1 | 3237.1 | 2000ms | 1/513 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 240.7 | 3882.8 | 2000ms | 2/513 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5645.9 | 54.55% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 18:00 | 5428.6 | 52.17% |
| `numbers_trivia` | 16:00 | 5394.5 | 52.17% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |
| `nasa_apod` | 11:00 | 5354.0 | 63.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
