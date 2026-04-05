# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 23:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 297.9 | 524.7 | 1000ms | 0/103 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.8 | 234.1 | 1500ms | 0/103 |
| ⚠️ | `ipapi_check` | 96.12% | 100.0% | 156.5 | 248.6 | 2500ms | 0/103 |
| ⚠️ | `open_meteo_weather` | 97.09% | 99.03% | 572.9 | 2550.7 | 2000ms | 1/103 |
| ❌ | `dog_ceo_random` | 98.06% | 67.96% | 1853.2 | 5142.0 | 2500ms | 33/103 |
| ❌ | `nasa_apod` | 98.06% | 70.87% | 1229.2 | 10538.0 | 2000ms | 30/103 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 576.1 | 2439.0 | 2500ms | 0/103 |
| ✅ | `agify_name` | 100.0% | 99.03% | 404.8 | 3237.1 | 2000ms | 1/103 |
| ✅ | `rest_countries` | 100.0% | 98.06% | 333.8 | 7269.1 | 2500ms | 2/103 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 246.7 | 1218.5 | 3000ms | 0/103 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 235.3 | 1556.1 | 2000ms | 0/103 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.2 | 252.0 | 1500ms | 0/103 |

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
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
