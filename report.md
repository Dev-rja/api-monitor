# API Reliability Monitor — SLA Report

> Last updated: **2026-04-27 00:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.09% | 4890.0 | 10206.7 | 1000ms | 243/518 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.8 | 4088.9 | 1500ms | 2/518 |
| ❌ | `nasa_apod` | 64.67% | 40.54% | 4143.6 | 10549.1 | 2000ms | 308/518 |
| ❌ | `ipapi_check` | 89.0% | 100.0% | 156.7 | 353.0 | 2500ms | 0/518 |
| ⚠️ | `open_meteo_weather` | 98.46% | 97.1% | 728.9 | 14877.1 | 2000ms | 15/518 |
| ⚠️ | `rest_countries` | 98.65% | 98.26% | 343.9 | 10221.5 | 2500ms | 9/518 |
| ⚠️ | `dog_ceo_random` | 99.42% | 91.89% | 780.0 | 10244.1 | 2500ms | 42/518 |
| ✅ | `catfact_random` | 99.42% | 99.42% | 258.2 | 10080.2 | 3000ms | 3/518 |
| ✅ | `useless_fact` | 99.61% | 99.23% | 578.3 | 10229.6 | 2500ms | 4/518 |
| ✅ | `coingecko_bitcoin` | 99.81% | 100.0% | 99.4 | 252.0 | 1500ms | 0/518 |
| ✅ | `agify_name` | 100.0% | 99.81% | 370.5 | 3237.1 | 2000ms | 1/518 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 240.3 | 3882.8 | 2000ms | 2/518 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6811.3 | 66.67% |
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
