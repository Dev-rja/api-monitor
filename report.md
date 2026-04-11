# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 19:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.9 | 588.9 | 1000ms | 0/222 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 129.0 | 3806.8 | 1500ms | 1/222 |
| ❌ | `nasa_apod` | 77.93% | 59.46% | 2374.2 | 10538.0 | 2000ms | 90/222 |
| ❌ | `ipapi_check` | 94.14% | 100.0% | 156.0 | 252.2 | 2500ms | 0/222 |
| ⚠️ | `open_meteo_weather` | 96.4% | 95.95% | 884.6 | 14877.1 | 2000ms | 9/222 |
| ⚠️ | `dog_ceo_random` | 99.1% | 81.53% | 1275.5 | 5586.8 | 2500ms | 41/222 |
| ✅ | `useless_fact` | 99.1% | 99.55% | 589.9 | 10229.6 | 2500ms | 1/222 |
| ✅ | `catfact_random` | 99.1% | 99.55% | 272.2 | 10070.5 | 3000ms | 1/222 |
| ✅ | `agify_name` | 100.0% | 99.55% | 399.5 | 3237.1 | 2000ms | 1/222 |
| ✅ | `rest_countries` | 100.0% | 98.65% | 296.2 | 7269.1 | 2500ms | 3/222 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.55% | 240.9 | 2314.9 | 2000ms | 1/222 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/222 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2793.9 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
