# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 21:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 91.06% | 1175.8 | 10176.4 | 1000ms | 27/302 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 125.9 | 3806.8 | 1500ms | 1/302 |
| ❌ | `nasa_apod` | 67.22% | 46.03% | 3650.7 | 10538.0 | 2000ms | 163/302 |
| ❌ | `ipapi_check` | 93.71% | 100.0% | 159.4 | 353.0 | 2500ms | 0/302 |
| ⚠️ | `open_meteo_weather` | 97.35% | 96.36% | 808.5 | 14877.1 | 2000ms | 11/302 |
| ⚠️ | `dog_ceo_random` | 99.34% | 86.42% | 1037.4 | 5586.8 | 2500ms | 41/302 |
| ✅ | `useless_fact` | 99.34% | 99.67% | 568.8 | 10229.6 | 2500ms | 1/302 |
| ✅ | `catfact_random` | 99.34% | 99.67% | 256.9 | 10070.5 | 3000ms | 1/302 |
| ✅ | `agify_name` | 100.0% | 99.67% | 384.5 | 3237.1 | 2000ms | 1/302 |
| ✅ | `rest_countries` | 100.0% | 98.68% | 280.6 | 7269.1 | 2500ms | 4/302 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 240.6 | 2314.9 | 2000ms | 1/302 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/302 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4550.4 | 66.67% |
| `nasa_apod` | 17:00 | 4370.4 | 58.82% |
| `nasa_apod` | 14:00 | 4321.9 | 52.94% |
| `nasa_apod` | 11:00 | 4098.4 | 57.89% |
| `nasa_apod` | 10:00 | 3989.3 | 53.85% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 21:00 | 3704.5 | 38.89% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
