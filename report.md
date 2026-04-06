# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 07:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.2 | 524.7 | 1000ms | 0/107 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.8 | 234.1 | 1500ms | 0/107 |
| ⚠️ | `ipapi_check` | 95.33% | 100.0% | 156.9 | 248.6 | 2500ms | 0/107 |
| ⚠️ | `open_meteo_weather` | 97.2% | 99.07% | 575.9 | 2550.7 | 2000ms | 1/107 |
| ❌ | `dog_ceo_random` | 98.13% | 67.29% | 1882.5 | 5142.0 | 2500ms | 35/107 |
| ❌ | `nasa_apod` | 98.13% | 71.03% | 1219.5 | 10538.0 | 2000ms | 31/107 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 573.5 | 2439.0 | 2500ms | 0/107 |
| ✅ | `agify_name` | 100.0% | 99.07% | 408.1 | 3237.1 | 2000ms | 1/107 |
| ✅ | `rest_countries` | 100.0% | 98.13% | 332.0 | 7269.1 | 2500ms | 2/107 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 247.8 | 1218.5 | 3000ms | 0/107 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 241.9 | 1556.1 | 2000ms | 0/107 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.0 | 252.0 | 1500ms | 0/107 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `dog_ceo_random` | 17:00 | 3338.8 | 83.33% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `dog_ceo_random` | 14:00 | 2501.6 | 66.67% |
| `nasa_apod` | 22:00 | 2253.1 | 28.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
