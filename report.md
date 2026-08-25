# API Reliability Monitor — SLA Report

> Last updated: **2026-08-25 22:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.41% | 3190.5 | 10420.1 | 1000ms | 728/2380 |
| ❌ | `public_apis_list` | 0.0% | 99.45% | 139.6 | 5075.4 | 1500ms | 13/2380 |
| ❌ | `ipapi_check` | 50.34% | 99.96% | 144.4 | 4507.0 | 2500ms | 1/2380 |
| ❌ | `nasa_apod` | 80.25% | 58.03% | 2746.9 | 11152.5 | 2000ms | 999/2380 |
| ⚠️ | `dog_ceo_random` | 96.81% | 97.52% | 485.3 | 10244.1 | 2500ms | 59/2380 |
| ⚠️ | `open_meteo_weather` | 98.99% | 98.19% | 675.4 | 14877.1 | 2000ms | 43/2380 |
| ✅ | `rest_countries` | 99.37% | 99.12% | 266.8 | 10221.5 | 2500ms | 21/2380 |
| ✅ | `useless_fact` | 99.79% | 99.71% | 654.6 | 10229.6 | 2500ms | 7/2380 |
| ✅ | `catfact_random` | 99.79% | 99.45% | 261.4 | 10080.2 | 3000ms | 13/2380 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.92% | 96.3 | 4328.4 | 1500ms | 2/2380 |
| ✅ | `agify_name` | 99.92% | 99.5% | 403.1 | 16112.2 | 2000ms | 12/2380 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.8 | 3882.8 | 2000ms | 2/2380 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4832.5 | 48.0% |
| `numbers_trivia` | 10:00 | 3795.8 | 36.17% |
| `numbers_trivia` | 02:00 | 3664.7 | 34.78% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 14:00 | 3575.5 | 34.58% |
| `numbers_trivia` | 09:00 | 3491.9 | 33.66% |
| `nasa_apod` | 03:00 | 3414.9 | 50.0% |
| `nasa_apod` | 05:00 | 3413.5 | 48.48% |
| `numbers_trivia` | 17:00 | 3401.9 | 33.87% |
| `numbers_trivia` | 05:00 | 3396.0 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
