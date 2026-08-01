# API Reliability Monitor — SLA Report

> Last updated: **2026-08-01 11:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.07% | 2246.5 | 10420.1 | 1000ms | 350/1672 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 129.0 | 5052.3 | 1500ms | 5/1672 |
| ❌ | `ipapi_check` | 68.9% | 99.94% | 150.1 | 4507.0 | 2500ms | 1/1672 |
| ❌ | `nasa_apod` | 78.17% | 55.08% | 2946.8 | 11152.5 | 2000ms | 751/1672 |
| ⚠️ | `dog_ceo_random` | 95.45% | 96.59% | 544.6 | 10244.1 | 2500ms | 57/1672 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.55% | 701.0 | 14877.1 | 2000ms | 41/1672 |
| ✅ | `rest_countries` | 99.1% | 98.74% | 296.3 | 10221.5 | 2500ms | 21/1672 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.8 | 10229.6 | 2500ms | 5/1672 |
| ✅ | `catfact_random` | 99.82% | 99.46% | 257.9 | 10080.2 | 3000ms | 9/1672 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.8 | 4328.4 | 1500ms | 1/1672 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.8 | 16112.2 | 2000ms | 4/1672 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 199.9 | 3882.8 | 2000ms | 2/1672 |

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
| `nasa_apod` | 12:00 | 3293.3 | 50.7% |
| `nasa_apod` | 01:00 | 3257.3 | 46.15% |
| `nasa_apod` | 11:00 | 3243.2 | 47.83% |
| `nasa_apod` | 18:00 | 3106.4 | 45.65% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
