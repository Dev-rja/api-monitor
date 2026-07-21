# API Reliability Monitor — SLA Report

> Last updated: **2026-07-21 22:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.48% | 1953.3 | 10206.7 | 1000ms | 268/1530 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 122.8 | 4595.4 | 1500ms | 4/1530 |
| ❌ | `ipapi_check` | 71.83% | 99.93% | 152.1 | 4507.0 | 2500ms | 1/1530 |
| ❌ | `nasa_apod` | 76.86% | 53.07% | 3096.2 | 11152.5 | 2000ms | 718/1530 |
| ⚠️ | `dog_ceo_random` | 95.1% | 96.27% | 562.2 | 10244.1 | 2500ms | 57/1530 |
| ⚠️ | `open_meteo_weather` | 98.76% | 97.32% | 712.2 | 14877.1 | 2000ms | 41/1530 |
| ✅ | `rest_countries` | 99.02% | 98.69% | 303.6 | 10221.5 | 2500ms | 20/1530 |
| ✅ | `useless_fact` | 99.67% | 99.74% | 636.7 | 10229.6 | 2500ms | 4/1530 |
| ✅ | `catfact_random` | 99.8% | 99.41% | 255.8 | 10080.2 | 3000ms | 9/1530 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 97.0 | 4328.4 | 1500ms | 1/1530 |
| ✅ | `agify_name` | 99.93% | 99.74% | 385.3 | 16112.2 | 2000ms | 4/1530 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 204.0 | 3882.8 | 2000ms | 2/1530 |

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
| `nasa_apod` | 18:00 | 3331.3 | 46.99% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
