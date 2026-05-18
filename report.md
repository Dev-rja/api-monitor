# API Reliability Monitor — SLA Report

> Last updated: **2026-05-18 23:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.84% | 3396.5 | 10206.7 | 1000ms | 266/827 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.6 | 4595.4 | 1500ms | 4/827 |
| ❌ | `nasa_apod` | 76.9% | 57.68% | 2956.1 | 10549.1 | 2000ms | 350/827 |
| ❌ | `ipapi_check` | 82.83% | 100.0% | 154.8 | 431.8 | 2500ms | 0/827 |
| ⚠️ | `rest_countries` | 98.79% | 98.31% | 341.3 | 10221.5 | 2500ms | 14/827 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.1% | 699.4 | 14877.1 | 2000ms | 24/827 |
| ⚠️ | `dog_ceo_random` | 99.4% | 94.92% | 631.9 | 10244.1 | 2500ms | 42/827 |
| ✅ | `catfact_random` | 99.64% | 99.15% | 269.0 | 10080.2 | 3000ms | 7/827 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.8 | 253.3 | 1500ms | 0/827 |
| ✅ | `useless_fact` | 99.76% | 99.52% | 609.5 | 10229.6 | 2500ms | 4/827 |
| ✅ | `agify_name` | 99.88% | 99.64% | 391.5 | 16112.2 | 2000ms | 3/827 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 231.4 | 3882.8 | 2000ms | 2/827 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 12:00 | 4054.7 | 38.24% |
| `numbers_trivia` | 07:00 | 4051.7 | 38.46% |
| `nasa_apod` | 17:00 | 3990.5 | 51.06% |
| `numbers_trivia` | 10:00 | 3848.7 | 36.36% |
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `nasa_apod` | 05:00 | 3716.4 | 60.87% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
