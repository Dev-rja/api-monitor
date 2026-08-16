# API Reliability Monitor — SLA Report

> Last updated: **2026-08-16 09:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.75% | 3460.0 | 10420.1 | 1000ms | 665/2000 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 136.2 | 5075.4 | 1500ms | 9/2000 |
| ❌ | `ipapi_check` | 59.1% | 99.95% | 146.0 | 4507.0 | 2500ms | 1/2000 |
| ❌ | `nasa_apod` | 77.8% | 53.8% | 3019.9 | 11152.5 | 2000ms | 924/2000 |
| ⚠️ | `dog_ceo_random` | 96.2% | 97.1% | 511.3 | 10244.1 | 2500ms | 58/2000 |
| ⚠️ | `open_meteo_weather` | 98.9% | 97.85% | 692.6 | 14877.1 | 2000ms | 43/2000 |
| ✅ | `rest_countries` | 99.25% | 98.95% | 280.6 | 10221.5 | 2500ms | 21/2000 |
| ✅ | `useless_fact` | 99.75% | 99.65% | 650.7 | 10229.6 | 2500ms | 7/2000 |
| ✅ | `catfact_random` | 99.75% | 99.4% | 263.5 | 10080.2 | 3000ms | 12/2000 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.0 | 4328.4 | 1500ms | 1/2000 |
| ✅ | `agify_name` | 99.9% | 99.75% | 391.8 | 16112.2 | 2000ms | 5/2000 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 192.1 | 3882.8 | 2000ms | 2/2000 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5258.2 | 52.5% |
| `numbers_trivia` | 02:00 | 4528.0 | 42.86% |
| `numbers_trivia` | 10:00 | 4323.2 | 41.33% |
| `nasa_apod` | 05:00 | 4196.2 | 58.82% |
| `numbers_trivia` | 05:00 | 4102.4 | 39.22% |
| `numbers_trivia` | 14:00 | 4043.7 | 39.33% |
| `nasa_apod` | 02:00 | 3934.2 | 57.14% |
| `numbers_trivia` | 09:00 | 3846.3 | 37.21% |
| `nasa_apod` | 03:00 | 3832.5 | 57.5% |
| `numbers_trivia` | 07:00 | 3703.5 | 35.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
