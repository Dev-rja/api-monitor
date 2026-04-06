# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 22:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **81.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.5 | 524.7 | 1000ms | 0/122 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.3 | 234.1 | 1500ms | 0/122 |
| ❌ | `nasa_apod` | 90.16% | 66.39% | 1896.4 | 10538.0 | 2000ms | 41/122 |
| ⚠️ | `ipapi_check` | 95.08% | 100.0% | 156.5 | 251.4 | 2500ms | 0/122 |
| ⚠️ | `open_meteo_weather` | 97.54% | 99.18% | 572.9 | 2550.7 | 2000ms | 1/122 |
| ❌ | `dog_ceo_random` | 98.36% | 68.03% | 1886.3 | 5586.8 | 2500ms | 39/122 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 566.9 | 2439.0 | 2500ms | 0/122 |
| ✅ | `agify_name` | 100.0% | 99.18% | 414.3 | 3237.1 | 2000ms | 1/122 |
| ✅ | `rest_countries` | 100.0% | 98.36% | 318.9 | 7269.1 | 2500ms | 2/122 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.18% | 255.3 | 2314.9 | 2000ms | 1/122 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 241.8 | 1218.5 | 3000ms | 0/122 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.2 | 252.0 | 1500ms | 0/122 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 22:00 | 3240.1 | 37.5% |
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `dog_ceo_random` | 14:00 | 2625.3 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
