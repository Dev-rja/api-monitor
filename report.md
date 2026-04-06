# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 23:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **81.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.8 | 524.7 | 1000ms | 0/124 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.5 | 234.1 | 1500ms | 0/124 |
| ❌ | `nasa_apod` | 90.32% | 66.94% | 1875.1 | 10538.0 | 2000ms | 41/124 |
| ❌ | `ipapi_check` | 94.35% | 100.0% | 155.7 | 251.4 | 2500ms | 0/124 |
| ⚠️ | `open_meteo_weather` | 97.58% | 99.19% | 570.4 | 2550.7 | 2000ms | 1/124 |
| ❌ | `dog_ceo_random` | 98.39% | 68.55% | 1864.0 | 5586.8 | 2500ms | 39/124 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 563.4 | 2439.0 | 2500ms | 0/124 |
| ✅ | `agify_name` | 100.0% | 99.19% | 410.3 | 3237.1 | 2000ms | 1/124 |
| ✅ | `rest_countries` | 100.0% | 98.39% | 315.0 | 7269.1 | 2500ms | 2/124 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.19% | 254.4 | 2314.9 | 2000ms | 1/124 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 239.2 | 1218.5 | 3000ms | 0/124 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.8 | 252.0 | 1500ms | 0/124 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `dog_ceo_random` | 14:00 | 2625.3 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
