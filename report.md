# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 16:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.37% | 3006.0 | 10206.7 | 1000ms | 105/380 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 122.8 | 3806.8 | 1500ms | 1/380 |
| ❌ | `nasa_apod` | 64.21% | 40.53% | 4057.0 | 10538.0 | 2000ms | 226/380 |
| ❌ | `ipapi_check` | 93.68% | 100.0% | 159.8 | 353.0 | 2500ms | 0/380 |
| ⚠️ | `open_meteo_weather` | 97.89% | 96.84% | 757.4 | 14877.1 | 2000ms | 12/380 |
| ⚠️ | `dog_ceo_random` | 99.21% | 88.95% | 923.0 | 10244.1 | 2500ms | 42/380 |
| ✅ | `useless_fact` | 99.47% | 98.95% | 590.8 | 10229.6 | 2500ms | 4/380 |
| ✅ | `catfact_random` | 99.47% | 99.74% | 245.8 | 10070.5 | 3000ms | 1/380 |
| ✅ | `agify_name` | 100.0% | 99.74% | 373.7 | 3237.1 | 2000ms | 1/380 |
| ✅ | `rest_countries` | 100.0% | 98.95% | 263.4 | 7269.1 | 2500ms | 4/380 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 235.2 | 2314.9 | 2000ms | 1/380 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/380 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |
| `nasa_apod` | 13:00 | 4333.9 | 66.67% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
