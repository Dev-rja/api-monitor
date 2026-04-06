# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 11:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 300.1 | 524.7 | 1000ms | 0/111 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.7 | 234.1 | 1500ms | 0/111 |
| ⚠️ | `ipapi_check` | 95.5% | 100.0% | 157.1 | 248.6 | 2500ms | 0/111 |
| ❌ | `nasa_apod` | 96.4% | 70.27% | 1370.3 | 10538.0 | 2000ms | 33/111 |
| ⚠️ | `open_meteo_weather` | 97.3% | 99.1% | 573.1 | 2550.7 | 2000ms | 1/111 |
| ❌ | `dog_ceo_random` | 98.2% | 66.67% | 1923.2 | 5142.0 | 2500ms | 37/111 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 568.8 | 2439.0 | 2500ms | 0/111 |
| ✅ | `agify_name` | 100.0% | 99.1% | 409.9 | 3237.1 | 2000ms | 1/111 |
| ✅ | `rest_countries` | 100.0% | 98.2% | 326.2 | 7269.1 | 2500ms | 2/111 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 245.9 | 1218.5 | 3000ms | 0/111 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.4 | 1556.1 | 2000ms | 0/111 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.2 | 252.0 | 1500ms | 0/111 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `dog_ceo_random` | 17:00 | 3338.8 | 83.33% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `dog_ceo_random` | 14:00 | 2501.6 | 66.67% |
| `nasa_apod` | 22:00 | 2253.1 | 28.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
