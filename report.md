# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 19:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.61% | 3080.0 | 10206.7 | 1000ms | 109/384 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 122.0 | 3806.8 | 1500ms | 1/384 |
| ❌ | `nasa_apod` | 63.54% | 40.1% | 4122.9 | 10538.0 | 2000ms | 230/384 |
| ❌ | `ipapi_check` | 93.75% | 100.0% | 159.8 | 353.0 | 2500ms | 0/384 |
| ⚠️ | `open_meteo_weather` | 97.92% | 96.88% | 754.3 | 14877.1 | 2000ms | 12/384 |
| ⚠️ | `dog_ceo_random` | 99.22% | 89.06% | 916.3 | 10244.1 | 2500ms | 42/384 |
| ✅ | `useless_fact` | 99.48% | 98.96% | 588.9 | 10229.6 | 2500ms | 4/384 |
| ✅ | `catfact_random` | 99.48% | 99.74% | 245.6 | 10070.5 | 3000ms | 1/384 |
| ✅ | `agify_name` | 100.0% | 99.74% | 372.4 | 3237.1 | 2000ms | 1/384 |
| ✅ | `rest_countries` | 100.0% | 98.96% | 262.1 | 7269.1 | 2500ms | 4/384 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.5 | 2314.9 | 2000ms | 1/384 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/384 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |
| `nasa_apod` | 13:00 | 4333.9 | 66.67% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
