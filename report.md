# API Reliability Monitor — SLA Report

> Last updated: **2026-08-23 04:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.01% | 3329.5 | 10420.1 | 1000ms | 728/2276 |
| ❌ | `public_apis_list` | 0.0% | 99.47% | 138.7 | 5075.4 | 1500ms | 12/2276 |
| ❌ | `ipapi_check` | 52.33% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2276 |
| ❌ | `nasa_apod` | 79.7% | 57.07% | 2804.2 | 11152.5 | 2000ms | 977/2276 |
| ⚠️ | `dog_ceo_random` | 96.66% | 97.45% | 488.6 | 10244.1 | 2500ms | 58/2276 |
| ⚠️ | `open_meteo_weather` | 98.99% | 98.11% | 679.8 | 14877.1 | 2000ms | 43/2276 |
| ✅ | `rest_countries` | 99.34% | 99.08% | 270.5 | 10221.5 | 2500ms | 21/2276 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.9 | 10229.6 | 2500ms | 7/2276 |
| ✅ | `catfact_random` | 99.78% | 99.43% | 262.0 | 10080.2 | 3000ms | 13/2276 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.9 | 4328.4 | 1500ms | 2/2276 |
| ✅ | `agify_name` | 99.91% | 99.6% | 398.9 | 16112.2 | 2000ms | 9/2276 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.6 | 3882.8 | 2000ms | 2/2276 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4927.1 | 48.98% |
| `numbers_trivia` | 10:00 | 4043.1 | 38.64% |
| `numbers_trivia` | 02:00 | 4003.5 | 38.1% |
| `numbers_trivia` | 14:00 | 3780.0 | 36.63% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 09:00 | 3667.1 | 35.42% |
| `numbers_trivia` | 17:00 | 3595.1 | 35.9% |
| `nasa_apod` | 05:00 | 3561.5 | 50.79% |
| `numbers_trivia` | 05:00 | 3550.7 | 34.92% |
| `nasa_apod` | 09:00 | 3483.5 | 48.42% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
