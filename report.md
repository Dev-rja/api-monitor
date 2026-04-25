# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 21:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.78% | 4627.6 | 10206.7 | 1000ms | 218/493 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 127.5 | 4088.9 | 1500ms | 2/493 |
| ❌ | `nasa_apod` | 63.29% | 38.74% | 4273.9 | 10549.1 | 2000ms | 302/493 |
| ❌ | `ipapi_check` | 90.87% | 100.0% | 157.9 | 353.0 | 2500ms | 0/493 |
| ⚠️ | `open_meteo_weather` | 98.38% | 97.16% | 724.7 | 14877.1 | 2000ms | 14/493 |
| ⚠️ | `rest_countries` | 98.58% | 98.17% | 350.2 | 10221.5 | 2500ms | 9/493 |
| ⚠️ | `dog_ceo_random` | 99.39% | 91.48% | 800.6 | 10244.1 | 2500ms | 42/493 |
| ✅ | `catfact_random` | 99.39% | 99.39% | 261.5 | 10080.2 | 3000ms | 3/493 |
| ✅ | `useless_fact` | 99.59% | 99.19% | 581.2 | 10229.6 | 2500ms | 4/493 |
| ✅ | `agify_name` | 100.0% | 99.8% | 371.3 | 3237.1 | 2000ms | 1/493 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.59% | 241.4 | 3882.8 | 2000ms | 2/493 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/493 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 01:00 | 5838.7 | 66.67% |
| `nasa_apod` | 17:00 | 5623.1 | 68.97% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 18:00 | 5530.3 | 81.82% |
| `numbers_trivia` | 12:00 | 5436.1 | 52.38% |
| `numbers_trivia` | 18:00 | 5218.5 | 50.0% |
| `numbers_trivia` | 07:00 | 5211.4 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
