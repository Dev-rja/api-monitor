# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 17:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.92% | 4808.9 | 10206.7 | 1000ms | 235/510 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 126.2 | 4088.9 | 1500ms | 2/510 |
| ❌ | `nasa_apod` | 64.12% | 39.61% | 4202.3 | 10549.1 | 2000ms | 308/510 |
| ❌ | `ipapi_check` | 88.82% | 100.0% | 157.3 | 353.0 | 2500ms | 0/510 |
| ⚠️ | `open_meteo_weather` | 98.43% | 97.06% | 730.9 | 14877.1 | 2000ms | 15/510 |
| ⚠️ | `rest_countries` | 98.63% | 98.24% | 345.9 | 10221.5 | 2500ms | 9/510 |
| ⚠️ | `dog_ceo_random` | 99.41% | 91.76% | 786.0 | 10244.1 | 2500ms | 42/510 |
| ✅ | `catfact_random` | 99.41% | 99.41% | 260.2 | 10080.2 | 3000ms | 3/510 |
| ✅ | `useless_fact` | 99.61% | 99.22% | 579.8 | 10229.6 | 2500ms | 4/510 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 100.0 | 252.0 | 1500ms | 0/510 |
| ✅ | `agify_name` | 100.0% | 99.8% | 370.8 | 3237.1 | 2000ms | 1/510 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 240.9 | 3882.8 | 2000ms | 2/510 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5645.9 | 54.55% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 18:00 | 5530.3 | 81.82% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 16:00 | 5394.5 | 52.17% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |
| `nasa_apod` | 11:00 | 5354.0 | 63.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
