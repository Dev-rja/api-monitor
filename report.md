# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 17:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.4 | 524.7 | 1000ms | 0/116 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.4 | 234.1 | 1500ms | 0/116 |
| ❌ | `nasa_apod` | 93.1% | 68.1% | 1667.2 | 10538.0 | 2000ms | 37/116 |
| ❌ | `ipapi_check` | 94.83% | 100.0% | 156.3 | 248.6 | 2500ms | 0/116 |
| ⚠️ | `open_meteo_weather` | 97.41% | 99.14% | 575.7 | 2550.7 | 2000ms | 1/116 |
| ❌ | `dog_ceo_random` | 98.28% | 66.38% | 1946.3 | 5586.8 | 2500ms | 39/116 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 569.4 | 2439.0 | 2500ms | 0/116 |
| ✅ | `agify_name` | 100.0% | 99.14% | 415.9 | 3237.1 | 2000ms | 1/116 |
| ✅ | `rest_countries` | 100.0% | 98.28% | 325.2 | 7269.1 | 2500ms | 2/116 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.14% | 257.1 | 2314.9 | 2000ms | 1/116 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 243.7 | 1218.5 | 3000ms | 0/116 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.4 | 252.0 | 1500ms | 0/116 |

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
