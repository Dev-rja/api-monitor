# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 20:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.4 | 524.7 | 1000ms | 0/139 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.2 | 234.1 | 1500ms | 0/139 |
| ❌ | `nasa_apod` | 91.37% | 69.06% | 1749.7 | 10538.0 | 2000ms | 43/139 |
| ❌ | `ipapi_check` | 92.81% | 100.0% | 156.3 | 252.2 | 2500ms | 0/139 |
| ❌ | `open_meteo_weather` | 94.24% | 94.96% | 1024.2 | 14877.1 | 2000ms | 7/139 |
| ❌ | `dog_ceo_random` | 98.56% | 71.22% | 1787.6 | 5586.8 | 2500ms | 40/139 |
| ⚠️ | `useless_fact` | 98.56% | 99.28% | 630.2 | 10229.6 | 2500ms | 1/139 |
| ✅ | `catfact_random` | 99.28% | 100.0% | 238.2 | 1218.5 | 3000ms | 0/139 |
| ✅ | `agify_name` | 100.0% | 99.28% | 406.5 | 3237.1 | 2000ms | 1/139 |
| ✅ | `rest_countries` | 100.0% | 98.56% | 305.4 | 7269.1 | 2500ms | 2/139 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.28% | 253.2 | 2314.9 | 2000ms | 1/139 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.4 | 252.0 | 1500ms | 0/139 |

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
