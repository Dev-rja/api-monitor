# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 07:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 89.29% | 1350.0 | 10206.7 | 1000ms | 33/308 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 126.7 | 3806.8 | 1500ms | 1/308 |
| ❌ | `nasa_apod` | 66.88% | 45.45% | 3702.5 | 10538.0 | 2000ms | 168/308 |
| ❌ | `ipapi_check` | 93.83% | 100.0% | 159.8 | 353.0 | 2500ms | 0/308 |
| ⚠️ | `open_meteo_weather` | 97.4% | 96.43% | 802.6 | 14877.1 | 2000ms | 11/308 |
| ⚠️ | `dog_ceo_random` | 99.35% | 86.69% | 1022.8 | 5586.8 | 2500ms | 41/308 |
| ✅ | `useless_fact` | 99.35% | 99.68% | 567.1 | 10229.6 | 2500ms | 1/308 |
| ✅ | `catfact_random` | 99.35% | 99.68% | 255.0 | 10070.5 | 3000ms | 1/308 |
| ✅ | `agify_name` | 100.0% | 99.68% | 384.2 | 3237.1 | 2000ms | 1/308 |
| ✅ | `rest_countries` | 100.0% | 98.7% | 279.3 | 7269.1 | 2500ms | 4/308 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.68% | 240.7 | 2314.9 | 2000ms | 1/308 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/308 |

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
