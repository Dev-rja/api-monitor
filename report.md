# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 03:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.15% | 3223.0 | 10206.7 | 1000ms | 117/392 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 121.4 | 3806.8 | 1500ms | 1/392 |
| ❌ | `nasa_apod` | 62.76% | 39.29% | 4210.7 | 10538.0 | 2000ms | 238/392 |
| ❌ | `ipapi_check` | 93.88% | 100.0% | 159.4 | 353.0 | 2500ms | 0/392 |
| ⚠️ | `open_meteo_weather` | 97.96% | 96.94% | 750.6 | 14877.1 | 2000ms | 12/392 |
| ⚠️ | `dog_ceo_random` | 99.23% | 89.29% | 906.1 | 10244.1 | 2500ms | 42/392 |
| ✅ | `useless_fact` | 99.49% | 98.98% | 588.6 | 10229.6 | 2500ms | 4/392 |
| ✅ | `catfact_random` | 99.49% | 99.74% | 245.9 | 10070.5 | 3000ms | 1/392 |
| ✅ | `agify_name` | 100.0% | 99.74% | 373.1 | 3237.1 | 2000ms | 1/392 |
| ✅ | `rest_countries` | 100.0% | 98.98% | 261.6 | 7269.1 | 2500ms | 4/392 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 233.9 | 2314.9 | 2000ms | 1/392 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/392 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5952.4 | 90.91% |
| `numbers_trivia` | 00:00 | 5880.9 | 57.14% |
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 00:00 | 4679.5 | 71.43% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 20:00 | 4536.6 | 66.67% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
