# API Reliability Monitor — SLA Report

> Last updated: **2026-08-01 16:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.88% | 2265.3 | 10420.1 | 1000ms | 354/1676 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 129.1 | 5052.3 | 1500ms | 5/1676 |
| ❌ | `ipapi_check` | 68.79% | 99.94% | 150.0 | 4507.0 | 2500ms | 1/1676 |
| ❌ | `nasa_apod` | 78.16% | 55.13% | 2946.7 | 11152.5 | 2000ms | 752/1676 |
| ⚠️ | `dog_ceo_random` | 95.47% | 96.6% | 543.9 | 10244.1 | 2500ms | 57/1676 |
| ⚠️ | `open_meteo_weather` | 98.87% | 97.55% | 700.8 | 14877.1 | 2000ms | 41/1676 |
| ✅ | `rest_countries` | 99.11% | 98.75% | 296.2 | 10221.5 | 2500ms | 21/1676 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.7 | 10229.6 | 2500ms | 5/1676 |
| ✅ | `catfact_random` | 99.82% | 99.46% | 258.0 | 10080.2 | 3000ms | 9/1676 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.8 | 4328.4 | 1500ms | 1/1676 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.9 | 16112.2 | 2000ms | 4/1676 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 199.8 | 3882.8 | 2000ms | 2/1676 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 4217.1 | 40.0% |
| `nasa_apod` | 03:00 | 3899.0 | 63.33% |
| `nasa_apod` | 09:00 | 3718.2 | 48.57% |
| `nasa_apod` | 17:00 | 3560.0 | 48.24% |
| `nasa_apod` | 12:00 | 3389.4 | 51.39% |
| `nasa_apod` | 01:00 | 3257.3 | 46.15% |
| `nasa_apod` | 11:00 | 3243.2 | 47.83% |
| `nasa_apod` | 18:00 | 3106.4 | 45.65% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
