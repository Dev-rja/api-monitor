# API Reliability Monitor — SLA Report

> Last updated: **2026-08-22 12:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.57% | 3373.2 | 10420.1 | 1000ms | 728/2245 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 137.5 | 5075.4 | 1500ms | 11/2245 |
| ❌ | `ipapi_check` | 52.96% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2245 |
| ❌ | `nasa_apod` | 79.55% | 56.79% | 2820.3 | 11152.5 | 2000ms | 970/2245 |
| ⚠️ | `dog_ceo_random` | 96.61% | 97.42% | 490.2 | 10244.1 | 2500ms | 58/2245 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.08% | 680.9 | 14877.1 | 2000ms | 43/2245 |
| ✅ | `rest_countries` | 99.33% | 99.06% | 271.5 | 10221.5 | 2500ms | 21/2245 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.5 | 10229.6 | 2500ms | 7/2245 |
| ✅ | `catfact_random` | 99.78% | 99.42% | 262.7 | 10080.2 | 3000ms | 13/2245 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.5 | 4328.4 | 1500ms | 2/2245 |
| ✅ | `agify_name` | 99.91% | 99.69% | 396.1 | 16112.2 | 2000ms | 7/2245 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.8 | 3882.8 | 2000ms | 2/2245 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5024.8 | 50.0% |
| `numbers_trivia` | 02:00 | 4199.6 | 40.0% |
| `numbers_trivia` | 10:00 | 4043.1 | 38.64% |
| `numbers_trivia` | 14:00 | 3852.3 | 37.37% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 09:00 | 3667.1 | 35.42% |
| `numbers_trivia` | 17:00 | 3655.0 | 36.52% |
| `nasa_apod` | 05:00 | 3561.5 | 50.79% |
| `numbers_trivia` | 05:00 | 3550.7 | 34.92% |
| `nasa_apod` | 09:00 | 3483.5 | 48.42% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
