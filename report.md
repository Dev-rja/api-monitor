# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 20:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 86.48% | 1625.0 | 10206.7 | 1000ms | 43/318 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 126.7 | 3806.8 | 1500ms | 1/318 |
| ❌ | `nasa_apod` | 66.35% | 44.65% | 3775.4 | 10538.0 | 2000ms | 176/318 |
| ❌ | `ipapi_check` | 93.08% | 100.0% | 159.7 | 353.0 | 2500ms | 0/318 |
| ⚠️ | `open_meteo_weather` | 97.48% | 96.23% | 801.4 | 14877.1 | 2000ms | 12/318 |
| ⚠️ | `dog_ceo_random` | 99.37% | 87.11% | 1002.9 | 5586.8 | 2500ms | 41/318 |
| ✅ | `useless_fact` | 99.37% | 99.69% | 568.6 | 10229.6 | 2500ms | 1/318 |
| ✅ | `catfact_random` | 99.37% | 99.69% | 255.3 | 10070.5 | 3000ms | 1/318 |
| ✅ | `agify_name` | 100.0% | 99.69% | 381.4 | 3237.1 | 2000ms | 1/318 |
| ✅ | `rest_countries` | 100.0% | 98.74% | 276.6 | 7269.1 | 2500ms | 4/318 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 240.2 | 2314.9 | 2000ms | 1/318 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.3 | 252.0 | 1500ms | 0/318 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 10:00 | 4445.3 | 57.14% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 21:00 | 3704.5 | 38.89% |
| `nasa_apod` | 15:00 | 3689.4 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
