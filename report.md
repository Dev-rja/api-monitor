# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 05:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 89.58% | 1321.6 | 10206.7 | 1000ms | 32/307 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 126.8 | 3806.8 | 1500ms | 1/307 |
| ❌ | `nasa_apod` | 67.1% | 45.6% | 3680.9 | 10538.0 | 2000ms | 167/307 |
| ❌ | `ipapi_check` | 93.81% | 100.0% | 159.5 | 353.0 | 2500ms | 0/307 |
| ⚠️ | `open_meteo_weather` | 97.39% | 96.42% | 803.4 | 14877.1 | 2000ms | 11/307 |
| ⚠️ | `dog_ceo_random` | 99.35% | 86.64% | 1024.8 | 5586.8 | 2500ms | 41/307 |
| ✅ | `useless_fact` | 99.35% | 99.67% | 566.8 | 10229.6 | 2500ms | 1/307 |
| ✅ | `catfact_random` | 99.35% | 99.67% | 255.2 | 10070.5 | 3000ms | 1/307 |
| ✅ | `agify_name` | 100.0% | 99.67% | 383.5 | 3237.1 | 2000ms | 1/307 |
| ✅ | `rest_countries` | 100.0% | 98.7% | 279.3 | 7269.1 | 2500ms | 4/307 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 240.8 | 2314.9 | 2000ms | 1/307 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/307 |

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
