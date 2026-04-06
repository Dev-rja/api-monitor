# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 14:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.2 | 524.7 | 1000ms | 0/113 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.4 | 234.1 | 1500ms | 0/113 |
| ❌ | `nasa_apod` | 94.69% | 69.03% | 1527.2 | 10538.0 | 2000ms | 35/113 |
| ❌ | `ipapi_check` | 94.69% | 100.0% | 157.1 | 248.6 | 2500ms | 0/113 |
| ⚠️ | `open_meteo_weather` | 97.35% | 99.12% | 574.2 | 2550.7 | 2000ms | 1/113 |
| ❌ | `dog_ceo_random` | 98.23% | 65.49% | 1968.4 | 5586.8 | 2500ms | 39/113 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 570.4 | 2439.0 | 2500ms | 0/113 |
| ✅ | `agify_name` | 100.0% | 99.12% | 412.3 | 3237.1 | 2000ms | 1/113 |
| ✅ | `rest_countries` | 100.0% | 98.23% | 326.6 | 7269.1 | 2500ms | 2/113 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 245.5 | 1218.5 | 3000ms | 0/113 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 237.6 | 1556.1 | 2000ms | 0/113 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.2 | 252.0 | 1500ms | 0/113 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `dog_ceo_random` | 17:00 | 3338.8 | 83.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `dog_ceo_random` | 14:00 | 2625.3 | 71.43% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 22:00 | 2253.1 | 28.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
