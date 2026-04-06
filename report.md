# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 11:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.4 | 524.7 | 1000ms | 0/110 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.4 | 234.1 | 1500ms | 0/110 |
| ⚠️ | `ipapi_check` | 95.45% | 100.0% | 156.9 | 248.6 | 2500ms | 0/110 |
| ❌ | `nasa_apod` | 97.27% | 70.91% | 1288.3 | 10538.0 | 2000ms | 32/110 |
| ⚠️ | `open_meteo_weather` | 97.27% | 99.09% | 574.5 | 2550.7 | 2000ms | 1/110 |
| ❌ | `dog_ceo_random` | 98.18% | 67.27% | 1909.1 | 5142.0 | 2500ms | 36/110 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 570.0 | 2439.0 | 2500ms | 0/110 |
| ✅ | `agify_name` | 100.0% | 99.09% | 410.7 | 3237.1 | 2000ms | 1/110 |
| ✅ | `rest_countries` | 100.0% | 98.18% | 328.5 | 7269.1 | 2500ms | 2/110 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 246.6 | 1218.5 | 3000ms | 0/110 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 239.5 | 1556.1 | 2000ms | 0/110 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.7 | 252.0 | 1500ms | 0/110 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `dog_ceo_random` | 17:00 | 3338.8 | 83.33% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 11:00 | 2638.9 | 50.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `dog_ceo_random` | 11:00 | 2519.7 | 62.5% |
| `dog_ceo_random` | 14:00 | 2501.6 | 66.67% |
| `nasa_apod` | 22:00 | 2253.1 | 28.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
