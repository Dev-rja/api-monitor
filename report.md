# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 06:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.0 | 524.7 | 1000ms | 0/128 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.6 | 234.1 | 1500ms | 0/128 |
| ❌ | `nasa_apod` | 90.63% | 67.19% | 1846.2 | 10538.0 | 2000ms | 42/128 |
| ❌ | `ipapi_check` | 94.53% | 100.0% | 156.9 | 252.2 | 2500ms | 0/128 |
| ⚠️ | `open_meteo_weather` | 96.09% | 97.66% | 783.0 | 14877.1 | 2000ms | 3/128 |
| ❌ | `dog_ceo_random` | 98.44% | 69.53% | 1825.4 | 5586.8 | 2500ms | 39/128 |
| ⚠️ | `useless_fact` | 98.44% | 99.22% | 638.0 | 10229.6 | 2500ms | 1/128 |
| ✅ | `catfact_random` | 99.22% | 100.0% | 237.9 | 1218.5 | 3000ms | 0/128 |
| ✅ | `agify_name` | 100.0% | 99.22% | 409.6 | 3237.1 | 2000ms | 1/128 |
| ✅ | `rest_countries` | 100.0% | 98.44% | 312.2 | 7269.1 | 2500ms | 2/128 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.22% | 256.0 | 2314.9 | 2000ms | 1/128 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.9 | 252.0 | 1500ms | 0/128 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `useless_fact` | 03:00 | 5454.5 | 50.0% |
| `open_meteo_weather` | 05:00 | 4216.1 | 25.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
