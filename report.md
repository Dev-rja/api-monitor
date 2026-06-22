# API Reliability Monitor — SLA Report

> Last updated: **2026-06-22 05:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.01% | 2492.9 | 10206.7 | 1000ms | 266/1157 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.1 | 4595.4 | 1500ms | 4/1157 |
| ❌ | `nasa_apod` | 74.5% | 51.6% | 3281.9 | 11152.5 | 2000ms | 560/1157 |
| ❌ | `ipapi_check` | 76.32% | 99.91% | 155.9 | 4507.0 | 2500ms | 1/1157 |
| ⚠️ | `rest_countries` | 98.7% | 98.36% | 338.7 | 10221.5 | 2500ms | 19/1157 |
| ⚠️ | `open_meteo_weather` | 98.96% | 96.89% | 713.8 | 14877.1 | 2000ms | 36/1157 |
| ✅ | `useless_fact` | 99.57% | 99.65% | 630.1 | 10229.6 | 2500ms | 4/1157 |
| ✅ | `dog_ceo_random` | 99.57% | 96.37% | 551.5 | 10244.1 | 2500ms | 42/1157 |
| ✅ | `catfact_random` | 99.74% | 99.22% | 261.8 | 10080.2 | 3000ms | 9/1157 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 96.1 | 253.3 | 1500ms | 0/1157 |
| ✅ | `agify_name` | 99.91% | 99.74% | 376.9 | 16112.2 | 2000ms | 3/1157 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 218.0 | 3882.8 | 2000ms | 2/1157 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4606.9 | 67.74% |
| `nasa_apod` | 17:00 | 4293.2 | 56.25% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 01:00 | 3945.6 | 57.14% |
| `nasa_apod` | 11:00 | 3815.6 | 51.61% |
| `nasa_apod` | 18:00 | 3660.2 | 53.45% |
| `nasa_apod` | 14:00 | 3413.5 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
