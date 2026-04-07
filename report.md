# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 16:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.2 | 524.7 | 1000ms | 0/136 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.6 | 234.1 | 1500ms | 0/136 |
| ❌ | `nasa_apod` | 91.18% | 68.38% | 1778.1 | 10538.0 | 2000ms | 43/136 |
| ❌ | `ipapi_check` | 92.65% | 100.0% | 156.4 | 252.2 | 2500ms | 0/136 |
| ❌ | `open_meteo_weather` | 94.12% | 94.85% | 1035.7 | 14877.1 | 2000ms | 7/136 |
| ❌ | `dog_ceo_random` | 98.53% | 70.59% | 1821.5 | 5586.8 | 2500ms | 40/136 |
| ⚠️ | `useless_fact` | 98.53% | 99.26% | 632.6 | 10229.6 | 2500ms | 1/136 |
| ✅ | `catfact_random` | 99.26% | 100.0% | 239.7 | 1218.5 | 3000ms | 0/136 |
| ✅ | `agify_name` | 100.0% | 99.26% | 408.9 | 3237.1 | 2000ms | 1/136 |
| ✅ | `rest_countries` | 100.0% | 98.53% | 307.7 | 7269.1 | 2500ms | 2/136 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.26% | 251.9 | 2314.9 | 2000ms | 1/136 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.1 | 252.0 | 1500ms | 0/136 |

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
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
