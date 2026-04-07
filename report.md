# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 21:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.4 | 588.9 | 1000ms | 0/140 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.8 | 234.1 | 1500ms | 0/140 |
| ❌ | `nasa_apod` | 91.43% | 69.29% | 1739.3 | 10538.0 | 2000ms | 43/140 |
| ❌ | `ipapi_check` | 92.86% | 100.0% | 156.0 | 252.2 | 2500ms | 0/140 |
| ❌ | `open_meteo_weather` | 94.29% | 95.0% | 1022.0 | 14877.1 | 2000ms | 7/140 |
| ❌ | `dog_ceo_random` | 98.57% | 71.43% | 1778.0 | 5586.8 | 2500ms | 40/140 |
| ⚠️ | `useless_fact` | 98.57% | 99.29% | 630.6 | 10229.6 | 2500ms | 1/140 |
| ✅ | `catfact_random` | 99.29% | 100.0% | 239.0 | 1218.5 | 3000ms | 0/140 |
| ✅ | `agify_name` | 100.0% | 99.29% | 409.5 | 3237.1 | 2000ms | 1/140 |
| ✅ | `rest_countries` | 100.0% | 98.57% | 305.8 | 7269.1 | 2500ms | 2/140 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.29% | 252.3 | 2314.9 | 2000ms | 1/140 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.2 | 252.0 | 1500ms | 0/140 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `useless_fact` | 03:00 | 5454.5 | 50.0% |
| `open_meteo_weather` | 05:00 | 4216.1 | 25.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 3203.4 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `dog_ceo_random` | 17:00 | 2591.7 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
