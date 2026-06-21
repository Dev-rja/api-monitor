# API Reliability Monitor — SLA Report

> Last updated: **2026-06-21 22:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.97% | 2497.0 | 10206.7 | 1000ms | 266/1155 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.2 | 4595.4 | 1500ms | 4/1155 |
| ❌ | `nasa_apod` | 74.63% | 51.69% | 3271.8 | 11152.5 | 2000ms | 558/1155 |
| ❌ | `ipapi_check` | 76.36% | 99.91% | 155.9 | 4507.0 | 2500ms | 1/1155 |
| ⚠️ | `rest_countries` | 98.7% | 98.35% | 338.9 | 10221.5 | 2500ms | 19/1155 |
| ⚠️ | `open_meteo_weather` | 98.96% | 96.88% | 714.3 | 14877.1 | 2000ms | 36/1155 |
| ✅ | `useless_fact` | 99.57% | 99.65% | 630.2 | 10229.6 | 2500ms | 4/1155 |
| ✅ | `dog_ceo_random` | 99.57% | 96.36% | 551.7 | 10244.1 | 2500ms | 42/1155 |
| ✅ | `catfact_random` | 99.74% | 99.22% | 262.1 | 10080.2 | 3000ms | 9/1155 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 96.2 | 253.3 | 1500ms | 0/1155 |
| ✅ | `agify_name` | 99.91% | 99.74% | 377.1 | 16112.2 | 2000ms | 3/1155 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 218.0 | 3882.8 | 2000ms | 2/1155 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4415.7 | 66.67% |
| `nasa_apod` | 17:00 | 4293.2 | 56.25% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 01:00 | 3945.6 | 57.14% |
| `nasa_apod` | 11:00 | 3815.6 | 51.61% |
| `nasa_apod` | 18:00 | 3660.2 | 53.45% |
| `nasa_apod` | 14:00 | 3413.5 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
