# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 18:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **81.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.6 | 524.7 | 1000ms | 0/117 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.7 | 234.1 | 1500ms | 0/117 |
| ❌ | `nasa_apod` | 92.31% | 67.52% | 1704.6 | 10538.0 | 2000ms | 38/117 |
| ❌ | `ipapi_check` | 94.87% | 100.0% | 156.2 | 248.6 | 2500ms | 0/117 |
| ⚠️ | `open_meteo_weather` | 97.44% | 99.15% | 574.7 | 2550.7 | 2000ms | 1/117 |
| ❌ | `dog_ceo_random` | 98.29% | 66.67% | 1947.2 | 5586.8 | 2500ms | 39/117 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 568.4 | 2439.0 | 2500ms | 0/117 |
| ✅ | `agify_name` | 100.0% | 99.15% | 416.0 | 3237.1 | 2000ms | 1/117 |
| ✅ | `rest_countries` | 100.0% | 98.29% | 323.1 | 7269.1 | 2500ms | 2/117 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.15% | 256.6 | 2314.9 | 2000ms | 1/117 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 242.5 | 1218.5 | 3000ms | 0/117 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.0 | 252.0 | 1500ms | 0/117 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `dog_ceo_random` | 14:00 | 2625.3 | 71.43% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 15:00 | 2469.6 | 42.86% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
