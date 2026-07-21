# API Reliability Monitor — SLA Report

> Last updated: **2026-07-21 16:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.44% | 1957.3 | 10206.7 | 1000ms | 268/1526 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 122.9 | 4595.4 | 1500ms | 4/1526 |
| ❌ | `ipapi_check` | 72.02% | 99.93% | 152.3 | 4507.0 | 2500ms | 1/1526 |
| ❌ | `nasa_apod` | 76.8% | 52.95% | 3102.9 | 11152.5 | 2000ms | 718/1526 |
| ⚠️ | `dog_ceo_random` | 95.09% | 96.26% | 562.7 | 10244.1 | 2500ms | 57/1526 |
| ⚠️ | `open_meteo_weather` | 98.75% | 97.31% | 712.3 | 14877.1 | 2000ms | 41/1526 |
| ✅ | `rest_countries` | 99.02% | 98.69% | 304.1 | 10221.5 | 2500ms | 20/1526 |
| ✅ | `useless_fact` | 99.67% | 99.74% | 636.5 | 10229.6 | 2500ms | 4/1526 |
| ✅ | `catfact_random` | 99.8% | 99.41% | 255.8 | 10080.2 | 3000ms | 9/1526 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 97.1 | 4328.4 | 1500ms | 1/1526 |
| ✅ | `agify_name` | 99.93% | 99.74% | 385.0 | 16112.2 | 2000ms | 4/1526 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 204.3 | 3882.8 | 2000ms | 2/1526 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 17:00 | 3842.7 | 52.56% |
| `nasa_apod` | 09:00 | 3838.2 | 50.0% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 01:00 | 3487.7 | 50.0% |
| `nasa_apod` | 12:00 | 3477.2 | 53.03% |
| `nasa_apod` | 11:00 | 3458.1 | 50.59% |
| `nasa_apod` | 18:00 | 3369.2 | 47.56% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
