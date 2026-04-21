# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 10:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.75% | 3555.8 | 10206.7 | 1000ms | 137/412 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 130.2 | 4088.9 | 1500ms | 2/412 |
| ❌ | `nasa_apod` | 62.14% | 38.11% | 4300.3 | 10549.1 | 2000ms | 255/412 |
| ❌ | `ipapi_check` | 93.93% | 100.0% | 159.3 | 353.0 | 2500ms | 0/412 |
| ⚠️ | `open_meteo_weather` | 98.06% | 96.84% | 748.5 | 14877.1 | 2000ms | 13/412 |
| ⚠️ | `dog_ceo_random` | 99.27% | 89.81% | 881.4 | 10244.1 | 2500ms | 42/412 |
| ✅ | `catfact_random` | 99.27% | 99.27% | 277.0 | 10080.2 | 3000ms | 3/412 |
| ✅ | `useless_fact` | 99.51% | 99.03% | 586.7 | 10229.6 | 2500ms | 4/412 |
| ✅ | `agify_name` | 100.0% | 99.76% | 372.7 | 3237.1 | 2000ms | 1/412 |
| ✅ | `rest_countries` | 100.0% | 99.03% | 259.9 | 7269.1 | 2500ms | 4/412 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 233.2 | 2314.9 | 2000ms | 1/412 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/412 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5778.8 | 70.83% |
| `nasa_apod` | 18:00 | 5606.7 | 82.35% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4978.5 | 62.5% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |
| `nasa_apod` | 23:00 | 4535.5 | 55.17% |
| `numbers_trivia` | 07:00 | 4515.1 | 42.86% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
